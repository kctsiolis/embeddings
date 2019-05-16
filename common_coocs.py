#This is code which analyzes cooccurrence data from a text corpus
#and for each word outputs the five words that cooccur with it
#the most frequently.

#Reading coocurrence data (in this case a file called "merged.cooc")
with open("coocs/merged.cooc", "r") as f1:
    coocs = f1.readlines()

#Reading unigram data (in this case a file called "merged.unigram")
with open("unigrams/merged.unigram", "r") as f2:
    unigram = f2.readlines()

common_coocs = open("extended_coocs_left.txt", "w+")
vocab_size = 50000
num_coocs = 5
cooc_dict = dict([(key,[]) for key in range(vocab_size)])

#Function to find the word with the highest weighted coocurrence
#frequency for a given word
def find_max(dict,key):
    max_index = 0
    max_word_index = int(dict[key][0][0])
    max = float(dict[key][0][1])
    for i in range(len(dict[key])):
        if float(dict[key][i][1]) > max:
            max_word_index = int(dict[key][i][0])
            max = float(dict[key][i][1])
            max_index = i
    max_word = unigram[max_word_index].split()[1]
    del dict[key][max_index]
    return max_word

#Mapping each word to a list containing all words it cooccurs
#with along with their frequencies
for line in range(len(coocs)):    
    values = coocs[line].split()
    cooc_dict[int(values[0])].append((values[1],values[2]))

#Extracting the five most common cooccurring words
index = 0
for line in range(len(unigram)):
    if index > 0:
        values = unigram[line].split()
        word = values[1]
        common = [""] * num_coocs
        common_coocs.write("%d %s: { " %(index,word))
        for i in range(num_coocs):
            try:
                common[i] = find_max(cooc_dict,int(values[0]))
            except IndexError:
                common[i] = ""
            if i != num_coocs - 1:
                common_coocs.write("%s ; " %(common[i]))
            else:
                common_coocs.write("%s }\n" %(common[i]))
    index+=1
