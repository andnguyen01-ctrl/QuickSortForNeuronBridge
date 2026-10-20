# Some General Notes
#   1) Upset plot is terribly outdated so you will need a dedicated conda environement for it to run with an older version of pandas
    # conda create -n upsetplot python=3.11 pandas=1.5 upsetplot matplotlib



# from pyvis.network import Network
import matplotlib.pyplot as plt
import os
import pandas as pd
from supervenn import supervenn


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




    
    return()

if __name__ == '__main__':
    main()

