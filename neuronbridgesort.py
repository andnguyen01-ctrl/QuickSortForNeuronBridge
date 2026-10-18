# from pyvis.network import Network
# import matplotlib.pyplot as plt
import os
import pandas as pd
from upsetplot import UpSet, from_contents
import matplotlib.pyplot as plt

def main():
   
    neurons = extract_data()

    drivers_sorted = sort_data(neurons)

    return()

def read_drivers(results_csv):

    drivers = set()
    
    read_drivers = pd.read_csv(results_csv, usecols=["Line Name"])

    for driver in read_drivers["Line Name"]:
        drivers.add(driver)
        # print(driver)

    return(drivers)

def extract_data():

    neurons = {}

    for file in os.listdir():
        if file.endswith('.csv'):
            candidate_drivers = read_drivers(file)
            neurons[file] = candidate_drivers
            
    return(neurons)



def sort_data(neurons_and_drivers):

    # This Function Was Written Using Claude Code - Andrew 
    
    # Strip .csv from keys for cleaner labels
    labeled = {k.replace('.csv', ''): v for k, v in neurons_and_drivers.items()}

    # Build the UpSet-compatible data structure
    data = from_contents(labeled)

    # Plot
    upset = UpSet(data, subset_size='count', show_counts=True, sort_by='cardinality')
    upset.plot()
    plt.suptitle("Shared and Unique Drivers Across Neuron CSVs")
    plt.show()

    return()
        
        


if __name__ == '__main__':
    main()

