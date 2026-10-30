import os
import pandas as pd
from supervenn import supervenn

def main(): 

    test_csv = pd.read_csv('AN04B003_T1L_BANC.csv')

    return()

def generate_neuron_driver_information():

    # points script towards which files to extract data from, then extracts data from them to generate [neuron: {driver set}] libraries

    neuron_driver_libraries = {}

    # for each csv in the script's directory, generate a corresponding neuron-driverset dictionary
    for neuron_file in os.listdir():                                                                # how csvs are found -- these are fed to the function read_neuron_csvs
        if neuron_file.endswith('.csv'):
            # neuron_driver_libraries[neuron_file] = read_neuron_csv(neuron_file)                    # read_neuron_csvs is used to parse driver data from each neuron-associated file 
            neuron_driver_libraries[neuron_file] = pd.read_csv(neuron_file) # read_neuron_csvs is used to parse driver data from each neuron-associated file 

    return(neuron_driver_libraries)




if __name__== '__main__':
    main()