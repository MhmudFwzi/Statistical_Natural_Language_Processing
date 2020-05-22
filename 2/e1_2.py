import e1_1
import matplotlib.pyplot as plt


threshold = 57749 #number of words in the smallest corpus (Turkish)

def plot_corpus(corpus,language):
    x_values = []
    y_values = []
    for i in range(len(corpus)):
        x_values.append(i)
        y_values.append(corpus[i][1])
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Rank")
    plt.ylabel("Frequency")
    plt.plot(x_values,y_values,label = language)
    plt.legend()

de_corpus = e1_1.process_language("de",True,threshold)
en_corpus = e1_1.process_language("en",True,threshold)
es_corpus = e1_1.process_language("es",True,threshold)
hu_corpus = e1_1.process_language("hu",True,threshold)
tr_corpus = e1_1.process_language("tr",True,threshold)

plot_corpus(de_corpus,"de")
plot_corpus(en_corpus,"en")
plot_corpus(es_corpus,"es")
plot_corpus(hu_corpus,"hu")
plot_corpus(tr_corpus,"tr")
plt.savefig("e1_2.png")

print("check e1_2.png generated, the variation in the curves is due to")


