import numpy as np
import os,string
from random import choices

def removePunctuation(line):
    table = str.maketrans(dict.fromkeys(string.punctuation))
    return line.translate(table)

def ENwordValid(word):
    for i in word:
        if i not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            return False
    return True

def get_data_corpus(language):
    dir = "dataset/" +language+"/"
    dictionary = {" ":0}
    count = 0
    for filename in os.listdir(dir):
        if filename.endswith(".txt"): 
            with open(dir + filename,'r') as file:     
                for line in file:
                    dictionary[" "] = dictionary[" "] - 1
                    count = count - 1
                    new_line = removePunctuation(line)
                    for word in new_line.split():
                        dictionary[" "] = dictionary[" "] + 1
                        count = count + 1
                        if ENwordValid(word):
                            for i in word:
                                l = i.lower()
                                count = count + 1
                                if(l in dictionary):
                                    dictionary[l] = dictionary[l] + 1
                                else: dictionary[l] = 1                                                
    for i in dictionary:
        dictionary[i] = dictionary[i]/count
    return(dictionary)

en_dic = sorted(get_data_corpus("en").items(), key=lambda x: x[1], reverse=True)

def generate_text(length,normalized_dic):
    n = 0
    text = ""
    letters = []
    probabilities = []
    for i in normalized_dic:
        letters.append(i[0])
        probabilities.append(i[1])
    while n < length:
        r = choices(letters, probabilities)
        text = text + r[0]
        n = n + 1
    return text

t = generate_text(50,en_dic)
print(t)

en_dic = get_data_corpus("en")
pHello = en_dic["h"]*en_dic["e"]*en_dic["l"]*en_dic["l"]*en_dic["o"]
print("Probability of Hello =  " + str(pHello))
print("Probability of Hello with space (to avoid words like halloing) =  " + str(pHello*en_dic[" "]))