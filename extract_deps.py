'''
Code to extract an edge list of dependency relations in a corpus
based on data provided in CoNLL-U format and a matrix of 
dependency co-occurrences, called Nxx.

Outputs a txt file with lines of the following form:

[DEPENDENT] [HEAD] [RELATION]

Also outputs a npz file of a matrix where row corresponds to 
dependent, column corresponds to head, and the values 
correspond to the number of times in the corpus the dependent 
appears with that head.

One can also output an edgelist form of the above matrix.
'''

import numpy as np
from scipy import sparse

#Storing the dictionary of embedded words
def store_dict(dict_file):
    with open(dict_file, "r") as d:
        dict = {}
        j = 0
        for line in d:
            tmp = line.split()
            dict[tmp[1]] = tmp[0]
            j+=1
        dict["ROOT"] = str(j)

    return dict


#Iterating over lines and extracting dependencies
def write_edgelist(in_file,out_file,dict):
    edgelist = open(out_file, "w+")

    with open(in_file, "r") as f:
        sentence = []
        add = False

        for line in f:
            if line[0] == "\n" and add == True:
                add = False
                for i in range(len(sentence)):
                    cur = sentence[i]
                    rel = cur[7]
                    dependent = cur[1]
                    head_idx = cur[6]
                    if head_idx != "_": #if the dependent actually has a head
                        edgelist.write(dict[dependent] + " ")
                        if rel != "root":
                            head = sentence[int(head_idx)-1][1]
                            edgelist.write(dict[head] + " ")
                        else:
                            head = "ROOT"
                            edgelist.write(dict[head] + " ")
                        
                        edgelist.write(rel + "\n")

                sentence = []

            elif line[0] == "1" or add == True:
                add = True
                tmp = line.split("\t")
                sentence.append(tmp)

def write_nxx(dict,edgelist,nxx_file):
    with open(edgelist, "r") as f:
        nxx_np = np.zeros((len(dict),len(dict)))
        for line in f:
            tmp = line.split()
            row = int(tmp[0])
            col = int(tmp[1])
            nxx_np[row][col]+=1

        nxx_sparse = sparse.csr_matrix(nxx_np)
        sparse.save_npz(nxx_file, nxx_sparse)

    return nxx_np

def write_countlist(nxx,countlist):
    with open(countlist, "w+") as f:
        for i in range(len(dict)):
            for j in range(len(dict)):
                if nxx_np[i][j] != 0:
                    f2.write(str(i) + " ")
                    f2.write(str(j) + " ")
                    f2.write(str(nxx_np[i][j]) + "\n")

dictionary_file = "../EWT/unigrams/dictionary"
annotations = "../EWT/en_ewt-ud-train-lowered.conllu"
edgelist = "../EWT/edgelist.txt"
store_nxx = "../EWT/Nxx.npz"
countlist = "../EWT/countlist.txt"

dict = store_dict(dictionary_file)
write_edgelist(annotations,edgelist,dict)
nxx = write_nxx(dict,edgelist,store_nxx) 
#write_countlist(nxx,countlist)
