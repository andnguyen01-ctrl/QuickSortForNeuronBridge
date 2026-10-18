# from pyvis.network import Network
# import matplotlib.pyplot as plt
import os
import pandas as pd

def main():
    

    return()

def read_drivers(results_csv):

    drivers = set()
    
    read_drivers = pd.read_csv(results_csv, usecols=["Line Name"])

    for driver in read_drivers["Line Name"]:
        drivers.add(driver)
        # print(driver)

    return(drivers)

def sort_data(data):



if __name__ == '__main__':
    main()

