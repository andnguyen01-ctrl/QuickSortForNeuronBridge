# Some General Notes
#   1) Upset plot is terribly outdated so you will need a dedicated conda environement for it to run with an older version of pandas
    # conda create -n upsetplot python=3.11 pandas=1.5 upsetplot matplotlib



# from pyvis.network import Network
import matplotlib.pyplot as plt
import os
import pandas as pd
from supervenn import supervenn
# god help me

def main():
    # os.remove('output.csv') ## SAVE YOUR DATA SET SOMEWHERE ELSE BEFORE RUNNING THIS SCRIPT EACH TIME

    neurons_and_drivers = generate_neuron_driver_libraries()

    generate_upset_plot(neurons_and_drivers)

    return()

def read_drivers(results_csv):

    drivers = set()
    
    read_drivers = pd.read_csv(neuron_file, usecols=["Line Name"])

    for driver in read_drivers["Line Name"]:
        neuron_driver_set.add(driver)

    return(neuron_driver_set)

def extract_data():

    # neurons = {}

    for file in os.listdir():
        if file.endswith('.csv'):
            candidate_drivers = read_drivers(file)
            neurons[file] = candidate_drivers
            
    return(neurons)

def sort_data(neurons): 
    
        
        
if __name__ == '__main__':
    main()

