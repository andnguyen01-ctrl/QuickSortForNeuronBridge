import os
import pandas as pd
from supervenn import supervenn

def main(): 

    test_csv = pd.read_csv('AN04B003_T1L_BANC.csv')

    test_extraction = extract_LSM(test_csv)

    filtered_test = LSM_Filter(test_extraction)
    
    return

def extract_LSM(neuron_file):
    # LSM stands for LineName, Score, MatchedPixels

    Neuron_LSM = neuron_file[["Line Name", "Score", "Matched Pixels"]]

    return(Neuron_LSM)

def LSM_Filter(Neuron_LSM):

   #filters the data set and returns the drivers lines that fit the filter parameters 
   Neuron_LSM_Filtered = Neuron_LSM[ (Neuron_LSM["Score"] >= 500) & (Neuron_LSM["Matched Pixels"] >= 200) ]

   print(Neuron_LSM_Filtered.shape)
   print(Neuron_LSM_Filtered.head)
    
   return(Neuron_LSM_Filtered["Line Name"])

def gen_Neuron_Driver_Libraries(DriverLines):
    NDL = {}
    for neuron_file in os.listdir():
        if neuron_file.endswith(".csv"):
            NDL[neuron_file.split('.')[0]] = 


if __name__== '__main__':
    main()