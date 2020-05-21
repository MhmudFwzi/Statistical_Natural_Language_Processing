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

def process_language(language,with_limit = False,limit = 0):
    dir = "dataset/" +language+"/"
    dictionary = {}
    token_count = 0
    for filename in os.listdir(dir):
        if filename.endswith(".txt"): 
            with open(dir + filename,'r') as file:     
                for line in file:
                    new_line = removePunctuation(line)
                    for word in new_line.split():
                        if(with_limit and token_count == limit):
                            dic_final = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
                            return dic_final
                        if(numberSpecialFree(word)):
                            word = word.lower()
                            token_count = token_count + 1
                            if(word in dictionary):
                                dictionary[word] = dictionary[word] + 1
                            else: dictionary[word] = 1                    
    dic_final = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    if(with_limit):
        return dic_final
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