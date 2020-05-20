import os,string

# def ENwordValid(word):
#     if(word.isalpha() and (word[0].islower() or word.istitle())):
#         return True
#     return False

def removePunctuation(line):
    table = str.maketrans(dict.fromkeys(string.punctuation))
    return line.translate(table)

def numberSpecialFree(word):
    if word == "–":
        return False
    return not any(word.isdigit() for char in word)

def process_language(language):
    dir = "dataset/" +language+"/"
    dictionary = {}
    for filename in os.listdir(dir):
        if filename.endswith(".txt"): 
            with open(dir + filename,'r') as file:     
                for line in file:
                    new_line = removePunctuation(line)
                    for word in new_line.split():
                        if(numberSpecialFree(word)):
                            word = word.lower()
                            if(word in dictionary):
                                dictionary[word] = dictionary[word] + 1
                            else: dictionary[word] = 1                       
    dic_final = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
                                #___________________export corpus for testing if needed__________________
    #corpus = open(language+"_corpus.txt","w+")
    # for key in dic_final:
    #     corpus.write(key[0] + "\t" + str(key[1]) + "\n")
    # corpus.close()
    print(language + " ~~~~ Top 10 ~~~~")
    avg_length = 0
    for i in range(10):
        avg_length = avg_length + len(dic_final[i][0])
        print(dic_final[i])
    print("~~~~ Average Length of Top 10 is " + str(avg_length/10) + " ~~~~")
    i = len(dic_final) - 1 #last index in dic_final
    j = i
    avg_length = 0
    while dic_final[i][1] == 1:
        avg_length = avg_length + len(dic_final[i][0])
        i = i-1
    print("~~~~ Average Length of Words with Lowest Rank is " + str(avg_length/(j-i)) + " ~~~~")

process_language("de")
process_language("en")
process_language("es")
process_language("hu")
process_language("tr")

print("The difference between the two averages in all languages complies with the fact that language behaves in compliance")
print("with Statistics. Words with higher average length are less probable to be said or used statistically")