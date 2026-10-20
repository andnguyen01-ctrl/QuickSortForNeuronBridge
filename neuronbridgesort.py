# Some General Notes
#   1) Upset plot is terribly outdated so you will need a dedicated conda environement for it to run with an older version of pandas
    # conda create -n upsetplot python=3.11 pandas=1.5 upsetplot matplotlib
#   2) upset plot is terrible in general and i have decided to go forward with supervenn 

# from pyvis.network import Network
import matplotlib.pyplot as plt
import os
import pandas as pd
from supervenn import supervenn


def main():

    neurons_and_drivers = generate_neuron_driver_libraries()
    print('neurons and drivers from main has type', type(neurons_and_drivers), 'and a total number of ', len(neurons_and_drivers), 'keys')

    neuronlist, drivers_per_neuron = generate_supervenn_plot(neurons_and_drivers)

    paired_neurons_and_drivers = list(zip(neuronlist, drivers_per_neuron))
    
    juice = claude_find_unifying_or_mutually_exclusive_drivers(paired_neurons_and_drivers)

    claude_dict_to_csv(juice)

    # Uncomment here if you want figure to be created
    # supervenn(drivers_per_neuron, set_annotations=neuronlist, side_plots=False)
    # plt.savefig("output.png", dpi=900, bbox_inches="tight")
    # plt.close()

    return()

def generate_neuron_driver_libraries():

    # points script towards which files to extract data from, then extracts data from them to generate [neuron: {driver set}] libraries

    neuron_driver_libraries = {}

    # for each csv in the script's directory, generate a corresponding neuron-driverset dictionary
    for neuron_file in os.listdir():                                                                # how csvs are found -- these are fed to the function read_neuron_csvs
        if neuron_file.endswith('.csv'):
            neuron_driver_libraries[neuron_file] = read_neuron_csvs(neuron_file)                    # read_neuron_csvs is used to parse driver data from each neuron-associated file 

    return(neuron_driver_libraries)

def read_neuron_csvs(neuron_file):

    # each time a neuron-csv is encountered, generate_neuron_driver_libraries comes here to generate a library for the given csv file
    neuron_driver_set = set() 
    
    read_drivers = pd.read_csv(neuron_file, usecols=["Line Name"])

    for driver in read_drivers["Line Name"]:
        neuron_driver_set.add(driver)

    return(neuron_driver_set)

def generate_supervenn_plot(neurons_and_drivers):
    # started this on my own for the sake of learning how supervenn works after using claude to check its usability

    drivers_per_neuron = list()   # supervenn takes lists of sets as inputs
    neuronlist = list() # this is important to have around in order to make the plot interpretable

    for neuron in neurons_and_drivers.keys():
        drivers_per_neuron.append(neurons_and_drivers[neuron])
        neuronlist.append(neuron)

    return(neuronlist, drivers_per_neuron)

# def find_unifying_or_mutually_exclusive_drivers(paired_neuron_drivers_typelist):
#     # the input of this function should be a list of the form [str(neuron-name), set(str(driver)...)
    
#     # general question - is it more helpful to present this case as the neurons or drivers being the keys? 
    
#     # going to go by the neuron-as-key approach since I ancipiate it will make the data less clunky
    
#     neurons_and_exclusive_drivers = {}
    
#     for index, pair in enumerate(paired_neuron_drivers_typelist):
#         neurons_and_exclusive_drivers[pair[0]] = {}

        
#     print(neurons_and_exclusive_drivers)
#     return()

def claude_find_unifying_or_mutually_exclusive_drivers(paired_neuron_drivers_typelist):
    # Build the lookup dict first (your existing loop, slightly simplified)
    neurons_and_exclusive_drivers = {}
    
    for index, pair in enumerate(paired_neuron_drivers_typelist):
        neurons_and_exclusive_drivers[pair[0]] = {
            "drivers": pair[1],          # store the original set
            "intersections": {},          # neuron_name -> shared drivers
            "exclusive_to_me": {},        # neuron_name -> drivers only I have
        }

    # Now do pairwise comparisons using the dict you just built
    neuron_names = list(neurons_and_exclusive_drivers.keys())
    
    for i in range(len(neuron_names)):
        for j in range(i + 1, len(neuron_names)):  # i+1 avoids self-compare and repeats
            n1, n2 = neuron_names[i], neuron_names[j]
            s1 = neurons_and_exclusive_drivers[n1]["drivers"]
            s2 = neurons_and_exclusive_drivers[n2]["drivers"]

            intersection = s1 & s2
            
            if intersection:
                neurons_and_exclusive_drivers[n1]["intersections"][n2] = intersection
                neurons_and_exclusive_drivers[n2]["intersections"][n1] = intersection
            else:
                # mutually exclusive — record what each has that the other doesn't
                neurons_and_exclusive_drivers[n1]["exclusive_to_me"][n2] = s1 - s2
                neurons_and_exclusive_drivers[n2]["exclusive_to_me"][n1] = s2 - s1

    print("exclusive", neurons_and_exclusive_drivers)
    return neurons_and_exclusive_drivers  # return the dict, not ()

import pandas as pd

def claude_dict_to_csv(neurons_and_exclusive_drivers, output_path="claude_neuron_drivers.csv"):
    rows = []
    
    for neuron, data in neurons_and_exclusive_drivers.items():
        row = {
            "neuron": neuron,
            "drivers": ", ".join(sorted(data["drivers"])),  # set -> readable string
        }
        
        # Flatten intersections: {"B": {d1, d2}, "C": {d3}} -> "B: d1,d2 | C: d3"
        row["intersections"] = " | ".join(
            f"{other}: {', '.join(sorted(shared))}"
            for other, shared in data["intersections"].items()
        ) or "none"
        
        row["exclusive_to_me"] = " | ".join(
            f"{other}: {', '.join(sorted(excl))}"
            for other, excl in data["exclusive_to_me"].items()
        ) or "none"
        
        rows.append(row)
    
    df = pd.DataFrame(rows)
    df.to_csv(output_path, index=False)
    print(df)
    return df


if __name__ == '__main__':
    main()


# def generate_supervenn_plot_claude(neurons_and_drivers):

#     # Claude prompt shows this package works great! Code is also super readable and easy to follow 
    
#     test_sets = []
#     test_labels = []

#     for key in neurons_and_drivers.keys():
#         test_sets.append(neurons_and_drivers[key])  # append the whole set
#         test_labels.append(key)                     # optional but useful for plot labels

#     print(f"{len(test_sets)} sets found, sizes: {[len(s) for s in test_sets]}")

#     supervenn(test_sets, set_annotations=test_labels, side_plots=False)

#     plt.savefig("output.png", dpi=300, bbox_inches="tight")
#     plt.close()
    
# return()

# return(zip(drivers_per_neuron, neuronlist))


