# Some General Notes
#   1) Upset plot is terribly outdated so you will need a dedicated conda environement for it to run with an older version of pandas
    # conda create -n upsetplot python=3.11 pandas=1.5 upsetplot matplotlib



# from pyvis.network import Network
import matplotlib.pyplot as plt
from upsetplot import from_contents, plot, UpSet
# from matplotlib_venn import venn2 -- venn2 can't do more than 3 circles 
import os
import pandas as pd

def main():
    # os.remove('output.csv') ## SAVE YOUR DATA SET SOMEWHERE ELSE BEFORE RUNNING THIS SCRIPT EACH TIME

    neurons_and_drivers = generate_neuron_driver_libraries()

    generate_upset_plot(neurons_and_drivers)

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

def generate_upset_plot(neurons_and_drivers):

    # i tried to one-shot this section previously with claude in some commits, and it totally doesn't work because Upsetplot's format demands are somewhat esoteric. The code below was written by me in contrast to previous commits where it was prompted 
    
    # see data format guide for upsetplot at this URL: https://upsetplot.readthedocs.io/en/stable/formats.html The key step here is that now we must reverse the library structure such that each driver is a key and the readouts are the neurons, since these neurons are the categorical layer by which these drivers will be organized
    driver_library = {}

    for neuron in neurons_and_drivers.keys():
        for driver in neurons_and_drivers[neuron]:
            if driver not in driver_library:
                driver_library[driver] = set()
            driver_library[driver].add(neuron)

    drivers = from_contents(driver_library)
    
    graph = UpSet(drivers).plot()
    
    return()

if __name__ == '__main__':
    main()

