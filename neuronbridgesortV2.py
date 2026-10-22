import os
import pandas as pd
from supervenn import supervenn

def main(): 

    read_neuron_csvs('AN04B003_T1L_BANC.csv')

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

    # the shape of this initial read will 100% reflect the original csv
    read_drivers = pd.read_csv(neuron_file)



    # Here, you can select which columns you want to focus on, and potentially apply certain filters. 
        # filters that may be of interest: percentile in score, pixels matched, 
    print(read_drivers.shape)



    for driver in read_drivers["Line Name"]:
        neuron_driver_set.add(driver)

    return(neuron_driver_set)




if __name__== '__main__':
    main()