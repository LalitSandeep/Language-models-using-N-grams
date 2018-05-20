
# coding: utf-8

# In[16]:


import nltk 
import string

from nltk.util import ngrams


from nltk.corpus import udhr  


english = udhr.raw('English-Latin1') 
french = udhr.raw('French_Francais-Latin1') 
italian = udhr.raw('Italian_Italiano-Latin1') 
spanish = udhr.raw('Spanish_Espanol-Latin1')  

english_train, english_dev = english[0:1000], english[1000:1100]
french_train, french_dev = french[0:1000], french[1000:1100]
italian_train, italian_dev = italian[0:1000], italian[1000:1100] 
spanish_train, spanish_dev = spanish[0:1000], spanish[1000:1100] 
english_test = udhr.words('English-Latin1')[0:1000] 
french_test = udhr.words('French_Francais-Latin1')[0:1000]
italian_test = udhr.words('Italian_Italiano-Latin1')[0:1000] 
spanish_test = udhr.words('Spanish_Espanol-Latin1')[0:1000]



# Creating training dataset
eng_train=list(english_train)

#Removing punctuation, special characters, capitalization 

eng_train = [''.join(c for c in s if c not in string.punctuation) for s in eng_train]


eng_train = [s.rstrip() for s in eng_train]

eng_train=[item.lower() for item in eng_train]


# Creating N grams models

unigrams=eng_train


bigrams = list(ngrams(eng_train,2))
trigrams = list(ngrams(eng_train,3))




french_training=list(french_train)


french_training = [''.join(c for c in s if c not in string.punctuation) for s in french_training]



french_training = [s.rstrip() for s in french_training]

french_training=[item.lower() for item in french_training]

unigrams_french=french_training



trigrams_french = list(ngrams(french_training,3))





# Creating Frequency Distribution
fdist1=nltk.FreqDist(trigrams)
fdist2=nltk.FreqDist(trigrams_french)


eng_test=list(english_test)


eng_test = [''.join(c for c in s if c not in string.punctuation) for s in eng_test]


eng_test = [s.rstrip() for s in eng_test]

eng_test=[item.lower() for item in eng_test]

eng_test=[item for item in eng_test if not item.isdigit()]

#Calculating Accuracy

eng_count = 0
french_count = 0

def Trigram_model(english_test):
    global eng_count
    global french_count
    for word in english_test:
        
        eng_tri_prob =1
        french_tri_prob=1
        word = word.lower()
        test_word= list(ngrams(word, 3))
        for i in test_word:
            eng_tri_prob=eng_tri_prob*fdist1.freq(i)
            french_tri_prob=french_tri_prob*fdist2.freq(i)
        if eng_tri_prob >= french_tri_prob:
            eng_count = eng_count+1
        elif eng_tri_prob < french_tri_prob:
            french_count = french_count+1
    

Trigram_model(eng_test)

print("Accuracy for English is:",str(eng_count/len(english_test)*100))


# In[ ]:



