
# coding: utf-8

# In[91]:

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

eng_train=list(english_train)
#print(eng_train)

eng_train = [''.join(c for c in s if c not in string.punctuation) for s in eng_train]

#eng_train = [s for s in eng_train if s]

eng_train = [s.rstrip() for s in eng_train]

eng_train=[item.lower() for item in eng_train]

unigrams=eng_train

#unigrams=list(ngrams(eng_train,1))
bigrams = list(ngrams(eng_train,2))
trigrams = list(ngrams(eng_train,3))


#print(unigrams)

fdist1 = nltk.ConditionalFreqDist(bigrams)

fdist1

eng_test=list(english_test)
#print(eng_train)

eng_test = [''.join(c for c in s if c not in string.punctuation) for s in eng_test]

#eng_train = [s for s in eng_train if s]

eng_test = [s.rstrip() for s in eng_test]

eng_test=[item.lower() for item in eng_test]

eng_test=[item for item in eng_test if not item.isdigit()]


#print(eng_test)

fdist2 = nltk.FreqDist(unigrams)

fdist2


#prob=abc['a']['b']/fdist2['a']
#print(prob)




#-----------------------------------------------------------

french_training=list(french_train)


french_training = [''.join(c for c in s if c not in string.punctuation) for s in french_training]



french_training = [s.rstrip() for s in french_training]

french_training=[item.lower() for item in french_training]

unigrams_french=french_training


bigrams_french = list(ngrams(french_training,2))
trigrams_french = list(ngrams(french_training,3))



fdist3 = nltk.ConditionalFreqDist(bigrams_french)
print(fdist3)
fdist3

fdist4 = nltk.FreqDist(unigrams_french)
print(fdist4)
fdist4


listoftestwords=[]
prob_eng=1
prob_french=1
for i in eng_test:
    prob_eng=1
    prob_french=1
    for j in i :
        
        if(i.index(j)==0):
            prob_eng*=fdist1[''][j]/fdist2['']
            prob_french*=fdist3[''][j]/fdist4['']
       
    
        else: 
            ele=i[i.index(j)-1]
             
            if((ele=='x')or(ele=='z')):
                prob_eng*=1
                
            
            else:
                prob_eng*=fdist1[ele][j]/fdist2[ele]
            
            if((ele=='w')or(ele=='k')or(ele=='z')):
                 prob_french*=1
                  
            else:
                 prob_french*=fdist3[ele][j]/fdist4[ele]
                
                
        
    
    if(prob_eng>prob_french):
         listoftestwords.append("english")
        
    else:
         listoftestwords.append("french")




fdistaccuracy = nltk.FreqDist(listoftestwords)
fdistaccuracy

if(fdistaccuracy['english']>fdistaccuracy['french']):
    print("Test language is Englisgh as accuracy is more for English")
    accuracy=fdistaccuracy['english']/(fdistaccuracy['french']+fdistaccuracy['english'])

    print(accuracy*100)
        
        


# In[ ]:




# In[54]:




# In[ ]:



