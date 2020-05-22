#!/usr/bin/env python
# coding: utf-8

# ## Task 1.1 : Data Preprocessing

# In[ ]:


import os,shutil,glob,re
import string
from collections import Counter
rootdir = './dataset'
prevdir = '../../'
for dirs in os.listdir(rootdir):
    os.chdir(rootdir+"/"+dirs)
    outfilename =  str(dirs)+".txt"
    with open(prevdir+outfilename, 'wb') as outfile:
        for filename in glob.glob('*.txt'):
            if filename == outfilename:
                continue
            with open(filename, 'rb') as readfile:
                shutil.copyfileobj(readfile, outfile)
    os.chdir(prevdir)


# In[53]:


def find_average_length(words,length):
    total_character = 0
    for word,value in words:
        total_character += len(word)
     
    return "{:.2f}".format(total_character/length)


# In[161]:


def find_average_length_set(words,length):
    total_character = 0
    for word in words:
        total_character += len(word)
     
    return "{:.2f}".format(total_character/length)


# In[162]:


def data_cleaning(file_name):
    file = open(file_name,"r",encoding='utf-8')
    text= file.read()
    file.close()
    words_list = text.split()
    removal_dict = str.maketrans("","",string.punctuation)
    tokenized_words = [w.translate(removal_dict) for w in words_list]
    clean_words_list = [word.lower() for word in tokenized_words]
    clean_words_list1 = [x for x in clean_words_list if x]
    
    return clean_words_list1
    


# In[166]:


import re
corpus_list = ['de.txt','en.txt','es.txt','hu.txt','tr.txt']
corpus_list_name = ['German','English','Spanish','Hungarian','Turkish']
for index,corpus in enumerate(corpus_list):
    print(corpus_list_name[index])
    print("")
    clean_words = data_cleaning(corpus)
    counts = Counter(clean_words)
    print("Top 10 most frequent words")
    top_words = counts.most_common(10)
    print(top_words)
    print("-----")
    print("Top 10 least frequent words")
    bottom_words = counts.most_common()[:-11:-1]
    print(bottom_words)
    print("-----")
    least_frequent = set(k for k,v in counts.items() if v==1)
    #print(least_frequent)
    top_words_avg_length =  find_average_length(top_words,10)
    bottom_words_avg_length = find_average_length_set(least_frequent,len(least_frequent))
    print("\n Average Length of top 10 most frequent Words : " + str(top_words_avg_length))
    print("\n Average Length of Lowest rank Words : " + str(bottom_words_avg_length))
    
    print("--------------------------\n")
    


# ## Task 1.2 :  Plotting Rank vs Frequency

# ### Create new corpora of same size

# In[101]:


corpus_list_new = ['de_new.txt','en_new.txt','es_new.txt','hu_new.txt','tr_new.txt']

for index,corpus in enumerate(corpus_list):
    with open(corpus, 'rb') as f:
        file_data = f.read(508928)
        f.close()
        f_write = open(corpus_list_new[index], "wb")
        f_write.write(file_data)
        f_write.close()


# In[127]:


import matplotlib.pyplot as plt

language_name =['German','English','Spanish','Hungarian','Turkish']
for index,corpus in enumerate(corpus_list_new):
    constant_value_list=[]
    print(corpus)
    print("")
    clean_words = data_cleaning(corpus)
    counts = Counter(clean_words)
    top_words = counts.most_common()
    i=1
    freq_rank_dict = {}
    for word,count in top_words:
        freq_rank_dict[i] = count
        i=i+1
    print(len(top_words))
    x = list(freq_rank_dict.keys())
    y = list(freq_rank_dict.values())
    print(len(x))
    plt.plot(y, x,label=language_name[index])
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.yscale('log')
    plt.xscale('log')

    plt.title(language_name[index])
    plt.show()
    
#plt.legend(loc="upper right")
#plt.show()


# ## Question 2

# In[13]:


import re,numpy as np
from collections import Counter


# In[23]:


def generate_random_character(character_list,prob_list):
    return np.random.choice(character_list,p=prob_list)


# In[42]:


def get_random_text(text_length):
    file = open('en.txt',"r",encoding='utf-8')
    text= file.read()
    file.close()
    regex = re.compile('[^a-zA-Z]')
    text_updated = regex.sub('',text.lower())
    counter_obj = Counter(text_updated)
    word_frequencies = dict(counter_obj)
    print('Frequency Distribution in English corpus\n')
    print(word_frequencies)
    print("------------\n")
    normalized_word_frequencies = {k: v / total for total in (sum(word_frequencies.values()),) for k, v in word_frequencies.items()}
    generated_text = ''
    print("Probabilty distribution according to English corpus\n\n")
    print(normalized_word_frequencies)
    print('-------------\n')
    #for w in sorted(normalized_word_frequencies, key=normalized_word_frequencies.get, reverse=True):
        #print(w, normalized_word_frequencies[w])
    for i in range(text_length):
        generated_text += generate_random_character(list(normalized_word_frequencies.keys()),list(normalized_word_frequencies.values())) 
    return generated_text


# In[45]:


random_text = get_random_text(90)
print('Generated Text : \n')
print(random_text)
print('-----------------\n')
counter_obj = Counter(random_text)
word_frequencies = dict(counter_obj)
print("Frequency Distribution in randonly generated text")
print(word_frequencies)
print('-------------')


# In[ ]:




