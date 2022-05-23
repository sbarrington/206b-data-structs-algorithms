import os
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
 
def print_dictionary(doc_dict):
    for key in doc_dict:
        print("Word: " + str(key[0]) + ", % count: " + str(key[1]))

def build_dictionary(prefixes, percent = True):
    
    # Get files
    files = list()
    
    for prefix in prefixes: 
        for file in os.listdir():
            if prefix in file:
                files.append(file)
    
    # For each file, add to the dict
    N = 0
    word_dict = {}
    
    for file in files:
        f = open(file, "r")
        lines = f.readlines()

        for line in lines:
            words = line.split()

            for i in range(0, len(words)):
                words[i] = strip_word(words[i])

                if len(words[i]) == 0:
                    continue

                elif words[i] in word_dict:
                    word_dict[words[i]] = word_dict[words[i]] + 1
                    N = N + 1

                else: 
                    word_dict[words[i]] = 1
                    N = N + 1
        
    if percent:
        # Convert counts to percentages
        for key in word_dict.keys():
            word_dict[key] = word_dict[key] * (100/N)
    
    return(word_dict)
          
def create_matrix(dim1=9, dim2=25):

    # Construct placeholder matrices
    F1 = np.zeros((dim1,dim2)) # pk

    # Create PK file loop
    pk_files = list()
        
    for file in os.listdir():
        if "pk" in file:
            pk_files.append(file)
        
    # For each file, add to the dict
    i = 0
    for file in pk_files:
        # Build the dictionary of ALL mentioned words 
        temp_dict = build_dictionary([str(file)])
        # Create a copy of the top_25 dictionary 
        temp_top_25 = top_25.copy()
        
        # Loop through each of the top 25 copys
        j = 0
        for key in temp_top_25:
            # Find the key in the dictionary of all words for the document
            if key in temp_dict: # If present, overwrite
                temp_top_25[key] = temp_dict[key]
            else: # If not present, set to 0
                temp_top_25[key] = 0
                
            # Populate the matrix
            F1[i, j] = F1[i, j] + temp_top_25[key]
            j = j + 1
            
        i = i + 1
                
    print(F1)

    return F1

def dim_reduction(F1, F2):
    F   = np.concatenate((F1,F2),axis=0)
    pca = PCA(n_components=2)
    Fp  = pca.fit(F).transform(F)
    plt.scatter( Fp[0:9,0], Fp[0:9,1], color='b')
    plt.scatter( Fp[9:18,0], Fp[9:18,1], color='r' )

    return None

