import os,string

def removePunctuation(line):
    table = str.maketrans(dict.fromkeys(string.punctuation))
    return line.translate(table)

def numberSpecialFree(word):
    if word == "–":
        return False
    return not any(word.isdigit() for char in word)

def process_language(language):
    dir = "dataset/" +language+"/"
    num = 0
    for filename in os.listdir(dir):
        if filename.endswith(".txt"): 
            with open(dir + filename,'r') as file:     
                for line in file:
                    new_line = removePunctuation(line)
                    for word in new_line.split():
                        if(numberSpecialFree(word)):
                            num = num + 1                   
    print(language + "\t" + str(num))

process_language("de")
process_language("en")
process_language("es")
process_language("hu")
process_language("tr")