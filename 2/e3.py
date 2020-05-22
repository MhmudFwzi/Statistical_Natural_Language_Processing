import os,string

def removePunctuation(line):
    table = str.maketrans(dict.fromkeys(string.punctuation))
    return line.translate(table)

def ENwordValid(word):
    for i in word:
        if i not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            return False
    return True

def ENletterValid(word):
        if i not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ":
            return False
        return True

def get_data_corpus(dir):
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

en_distribution = sorted(get_data_corpus("dataset/en/").items(), key=lambda x: x[1], reverse=True)
cipher_distribution = sorted(get_data_corpus("ct/").items(), key=lambda x: x[1], reverse=True)

en_map = {}
cipher_map = {}

for i in range(27):
    en_map[i] = en_distribution[i][0]
    cipher_map[cipher_distribution[i][0]] = i

decrypted = ""

print(en_map)
print(cipher_map)

with open("ct/Cipher.txt",'r') as file:
    for line in file:
        for i in line:
            if(ENletterValid(i)):
                l = i.lower()
                decrypted = decrypted + en_map[cipher_map[l]]

print(decrypted)