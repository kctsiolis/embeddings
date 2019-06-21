'''
Python script to analyze Hilbert embeddings. Given a particular word,
it considers its covector (context vector) and word vector. It finds
the word vectors with which its word vector has the highest inner 
product, as well as the context vectors for which it has the highest
inner product.
'''

import numpy as np
import math

w = np.load("emb_29/2200/W.npy")

v = np.load("emb_29/2200/V.npy")

with open("symmetric_data/dictionary", "r") as f:
    vocabulary = f.read()

output = open("emb_29/vector_similarities_right_29.txt", "w+")

vocabulary = vocabulary.split("\n")
dict = {}
n = 10 #Number of similar vectors to output

for i in range(len(vocabulary)):
    dict[vocabulary[i]] = i

def covector_similarity_ij(word):
    index = dict[word]
    j = v[index,:] #Vector for word
    dot = np.zeros(len(vocabulary))

    for k in range(len(vocabulary)):
        i = w[k,:] #Covector for a given word in the vocabulary
        dot[k] = np.dot(i,j)

    find_max(index,word,dot)

def covector_similarity_ji(word):
    index = dict[word]
    j = w[index,:]
    dot = np.zeros(len(vocabulary))

    for k in range(len(vocabulary)):
        i = v[k,:]
        dot[k] = np.dot(i,j)

    find_max(index,word,dot)

def find_max(index,word,dot):
    max_words = [None] * n
    output.write("%d %s: { " %(index,word))

    for m in range(n):
        max_index = np.argmax(dot)
        dot[max_index] = -math.inf
        max_words[m] = vocabulary[max_index]
        if m != n - 1:
            output.write("%s ; " %(max_words[m]))
        else:
            output.write("%s }\n" %(max_words[m]))

def vector_similarity(word):
    index = dict[word]
    j = v[index,:]
    dot = np.zeros(len(vocabulary))

    for k in range(len(vocabulary)):
        i = v[k,:] #Another word vector in the vocabulary
        dot[k] = np.dot(i,j)

    find_max(index,word,dot)

output.write("===========Covectors(i,j)============\n\n")

output.write("-----Nouns-----\n\n")
covector_similarity_ij("man")
covector_similarity_ij("woman")
covector_similarity_ij("person")
covector_similarity_ij("company")
covector_similarity_ij("president")
covector_similarity_ij("cat")
covector_similarity_ij("dog")

output.write("\n-----Pronouns-----\n\n")
covector_similarity_ij("he")
covector_similarity_ij("she")
covector_similarity_ij("they")

output.write("\n-----Adjectives------\n\n")
covector_similarity_ij("big")
covector_similarity_ij("small")
covector_similarity_ij("blue")

output.write("\n-----Transitive Verbs-----\n\n")
covector_similarity_ij("eat")
covector_similarity_ij("run")
covector_similarity_ij("gave")
covector_similarity_ij("offered")

output.write("\n-----Intransitive Verbs-----\n\n")
covector_similarity_ij("arrived")
covector_similarity_ij("lied")
covector_similarity_ij("went")
covector_similarity_ij("worked")

output.write("\n----Prepositions-----\n\n")
covector_similarity_ij("for")
covector_similarity_ij("in")
covector_similarity_ij("above")

output.write("\n-----Determiners-----\n\n")
covector_similarity_ij("the")
covector_similarity_ij("a")
covector_similarity_ij("their")

output.write("\n===========Covectors(j,i)============\n\n")

output.write("-----Nouns-----\n\n")
covector_similarity_ji("man")
covector_similarity_ji("woman")
covector_similarity_ji("person")
covector_similarity_ji("company")
covector_similarity_ji("president")
covector_similarity_ji("cat")
covector_similarity_ji("dog")

output.write("\n-----Pronouns-----\n\n")
covector_similarity_ji("he")
covector_similarity_ji("she")
covector_similarity_ji("they")

output.write("\n-----Adjectives------\n\n")
covector_similarity_ji("big")
covector_similarity_ji("small")
covector_similarity_ji("blue")

output.write("\n-----Transitive Verbs-----\n\n")
covector_similarity_ji("eat")
covector_similarity_ji("run")
covector_similarity_ji("gave")
covector_similarity_ji("offered")

output.write("\n-----Intransitive Verbs-----\n\n")
covector_similarity_ji("arrived")
covector_similarity_ji("lied")
covector_similarity_ji("went")
covector_similarity_ji("worked")

output.write("\n----Prepositions-----\n\n")
covector_similarity_ji("for")
covector_similarity_ji("in")
covector_similarity_ji("above")

output.write("\n-----Determiners-----\n\n")
covector_similarity_ji("the")
covector_similarity_ji("a")
covector_similarity_ji("their")



output.write("\n===========Vectors=============\n\n")
output.write("-----Nouns-----\n\n")
vector_similarity("man")
vector_similarity("woman")
vector_similarity("person")
vector_similarity("company")
vector_similarity("president")
vector_similarity("cat")
vector_similarity("dog")

output.write("\n-----Pronouns-----\n\n")
vector_similarity("he")
vector_similarity("she")
vector_similarity("they")

output.write("\n-----Adjectives------\n\n")
vector_similarity("big")
vector_similarity("small")
vector_similarity("blue")

output.write("\n-----Transitive Verbs-----\n\n")
vector_similarity("eat")
vector_similarity("run")
vector_similarity("gave")
vector_similarity("offered")

output.write("\n-----Intransitive Verbs-----\n\n")
vector_similarity("arrived")
vector_similarity("lied")
vector_similarity("went")
vector_similarity("worked")

output.write("\n----Prepositions-----\n\n")
vector_similarity("for")
vector_similarity("in")
vector_similarity("above")

output.write("\n-----Determiners-----\n\n")
vector_similarity("the")
vector_similarity("a")
vector_similarity("their")
