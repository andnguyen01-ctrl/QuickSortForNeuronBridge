import os
import pandas as pd
from supervenn import supervenn
import matplotlib.pyplot as plt
from itertools import combinations
def main(): 

    NDL = gen_Neuron_Driver_Libraries()
    
    driversets, labels = superVennSetsAndLabels(NDL)

    # plotSuperVenn = supervenn(sets, labels)

    # plt.savefig("output.png", dpi=300, bbox_inches="tight")

    intersection_of_all = intersections(driversets, labels)

    intersections_of_4 = quartet_intersections(NDL)

    print("common drivers amongst all neurons:", intersection_of_all)
    print()
    print("common drivers amongst quartets:")
    for key in intersections_of_4.keys():
        print(key, intersections_of_4[key])
    

    return

def gen_Neuron_Driver_Libraries():
    NDL = {} # NDL stands for neuronDriverLibrary
    for neuron_file in os.listdir():
        
        if neuron_file.endswith(".csv") and "VNC" in neuron_file:
            LSM = extract_LSM(neuron_file)
            Filtered_Drivers = LSM_Filter_Drivers(LSM)
            NDL[neuron_file.split('_')[0] + neuron_file.split('_')[1] + "_VNC"] = Filtered_Drivers 

        if neuron_file.endswith(".csv") and "Brain" in neuron_file:
                    LSM = extract_LSM(neuron_file)
                    Filtered_Drivers = LSM_Filter_Drivers(LSM)
                    NDL[neuron_file.split('_')[0] + neuron_file.split('_')[1] + "_Brain"] = Filtered_Drivers 
    
    return(NDL)

def extract_LSM(neuron_file):
    # LSM stands for LineName, Score, MatchedPixels
    Neuron_read = pd.read_csv(neuron_file)

    Neuron_LSM = Neuron_read[["Line Name", "Score", "Matched Pixels"]]

    return(Neuron_LSM)

def LSM_Filter_Drivers(Neuron_LSM):

   #filters the data set and returns the drivers lines that fit the filter parameters 
   Neuron_LSM_Filtered = Neuron_LSM[ (Neuron_LSM["Score"] >= 4) & (Neuron_LSM["Matched Pixels"] >= 4) ]
    
   return(Neuron_LSM_Filtered["Line Name"])

def superVennSetsAndLabels(NDL):

    driversets = list()
    labels = list()

    for key in NDL.keys():
        labels.append(key)
        set_to_add = set()
        for driver in NDL[key]:
            set_to_add.add(driver)
        driversets.append(set_to_add)

    return(driversets, labels)

def quartet_intersections(NDL):
    Neuron_quartet_intersections = {}

    for combo in combinations(NDL.keys(), 4):
        sets = [set(NDL[neuron]) for neuron in combo]
        Neuron_quartet_intersections[combo] = set.intersection(*sets)

    return Neuron_quartet_intersections
        
def intersections(driversets, labels):
    intersections = set.intersection(*driversets)

    return (intersections)


if __name__== '__main__':
    main()