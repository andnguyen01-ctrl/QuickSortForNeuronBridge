import os
import pandas as pd
from supervenn import supervenn
import matplotlib.pyplot as plt

def main(): 

    NDL = gen_Neuron_Driver_Libraries()
    
    sets, labels = superVennSetsAndLabels(NDL)
        
    plotSuperVenn = supervenn(sets, labels)
    plt.savefig("output.png", dpi=300, bbox_inches="tight")
    return

def gen_Neuron_Driver_Libraries():
    NDL = {} # NDL stands for neuronDriverLibrarie
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
   Neuron_LSM_Filtered = Neuron_LSM[ (Neuron_LSM["Score"] >= 500) & (Neuron_LSM["Matched Pixels"] >= 200) ]
    
   return(Neuron_LSM_Filtered["Line Name"])

def superVennSetsAndLabels(NDL):

    sets = list()
    labels = list()

    for key in NDL.keys():
        labels.append(key)
        set_to_add = set()
        for driver in NDL[key]:
            set_to_add.add(driver)
        sets.append(set_to_add)

    return(sets, labels)

if __name__== '__main__':
    main()