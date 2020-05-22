# import e1_1

p_letter = (1-0.05)/26
p_hello = p_letter**5
print("Probability of hello regardless of what's next = ((1-0.05)/26)**5 = " + str(p_hello) + 
"   (approximately = 0 which is the case for the given texts)")
print("Probability of hello + space (to avoid words like helloing) = 0.05((1-0.05)/26)**5 = " + str(0.05*p_hello) + 
"   (approximately = 0 which is the case for the given texts)")


# language = "en"
# en_corpus = e1_1.process_language(language,True,-1)
#                                 #___________________export corpus for testing if needed__________________
# corpus = open(language+"_corpus.txt","w+")
# for key in en_corpus:
#     corpus.write(key[0] + "\t" + str(key[1]) + "\n")
# corpus.close()