# Some General Notes
#   1) Upset plot is terribly outdated so you will need a dedicated conda environement for it to run with an older version of pandas
    # conda create -n upsetplot python=3.11 pandas=1.5 upsetplot matplotlib



# from pyvis.network import Network
import matplotlib.pyplot as plt
import os
import pandas as pd
from supervenn import supervenn


def main():

    neurons_and_drivers = generate_neuron_driver_libraries()
    print('neurons and drivers from main has type', type(neurons_and_drivers), 'and a total number of ', len(neurons_and_drivers), 'keys')

    generate_supervenn_plot(neurons_and_drivers)

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

    list_of_sets = list()   # supervenn takes lists of sets as inputs
    set_labels = list() # this is important to have around in order to make the plot interpretable

    for neuron in neurons_and_drivers.keys():
        list_of_sets.append(neurons_and_drivers[neuron])
        set_labels.append(neuron)
    
    supervenn(list_of_sets, set_annotations=set_labels, side_plots=True)

    plt.savefig("output.png", dpi=900, bbox_inches="tight")
    plt.close()


    return()

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
    
    return()


if __name__ == '__main__':
    main()

