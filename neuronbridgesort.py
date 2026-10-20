# from pyvis.network import Network
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import os
import pandas as pd
import matplotlib.pyplot as plt

def main():
   
    neurons = extract_data()

    drivers_sorted = sort_data(neurons)

    return()

def read_drivers(results_csv):
    # reads the csv file and returns a set of drivers

    drivers = set()
    
    read_drivers = pd.read_csv(results_csv, usecols=["Line Name"])

    for driver in read_drivers["Line Name"]:
        drivers.add(driver)
        # print(driver)

    return(drivers)

def extract_data():
    # takes the output of read drivers and converts it into a dictionary of {file_name: set_of_drivers}

    neurons = {}

    for file in os.listdir():
        if file.endswith('.csv'):
            candidate_drivers = read_drivers(file)
            neurons[file] = candidate_drivers
            
    return(neurons)

def sort_data(neurons):

    return ()
        
        
if __name__ == '__main__':
    main()

