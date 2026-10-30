import os
import pandas as pd
from supervenn import supervenn

def main(): 

    test_csv = pd.read_csv('AN04B003_T1L_BANC.csv')

    test_extraction = extract_LSM(test_csv)

    filtered_test = LSM_Filter(test_extraction)
    return

# def generate_neuron_LSM_libraries():

#     # points script towards which files to extract data from, then extracts data from them to generate [neuron: {driver set}] libraries

#     neuron_LSM_libraries = {}

#     # for each csv in the script's directory, generate a corresponding neuron-LSM dictionary
#     for neuron_file in os.listdir():                                     
#          if neuron_file.endswith('.csv'):
#             neuron_LSM_libraries[neuron_file] = extract_LSM(neuron_file)  # replace extract_LSM after testing phase is over 
#             # strucutre is determined here, we can say that if 
#     return(neuron_LSM_libraries)

def extract_LSM(neuron_file):
    # LSM stands for LineName, Score, MatchedPixels

    Neuron_LSM = neuron_file[["Line Name", "Score", "Matched Pixels"]]

    return(Neuron_LSM)

def LSM_Filter(Neuron_LSM):
    
   Neuron_LSM_Filtered = Neuron_LSM.loc[Neuron_LSM["Score"] > 1, "Line Name"]

   print 
   
   return(Neuron_LSM_Filtered)

if __name__== '__main__':
    main()