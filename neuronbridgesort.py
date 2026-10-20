# from pyvis.network import Network
import matplotlib.pyplot as plt
from upsetplot import from_memberships, plot
# from matplotlib_venn import venn2 -- venn2 can't do more than 3 circles 
import os
import pandas as pd

def main():
    
    neurons_and_drivers = generate_neuron_driver_libraries()
    print(neurons_and_drivers)

    return()


def generate_neuron_driver_libraries():

    # points script towards which files to extract data from, then extracts data from them to generate [neuron: {driver set}] libraries

    neuron_driver_libraries = {}

    # for each csv in the script's directory, generate a corresponding neuron-driverset dictionary
    for neuron_file in os.listdir():                                                                # how csvs are found
        if neuron_file.endswith('.csv'):
            neuron_driver_libraries[neuron_file] = read_neuron_csvs(neuron_file)                    # a function called read_neuron_csvs is used to parse driver data from each neuron-associated file 
    
    return(neuron_driver_libraries)

def read_neuron_csvs(neuron_file):

    # each time a neuron-csv is encountered, generate_neuron_driver_libraries comes here to generate a library for the given csv file
    neuron_driver_library = set() 
    
    read_drivers = pd.read_csv(neuron_file, usecols=["Line Name"])

    for driver in read_drivers["Line Name"]:
        neuron_driver_library.add(driver)

    return(neuron_driver_library)

if __name__ == '__main__':
    main()

