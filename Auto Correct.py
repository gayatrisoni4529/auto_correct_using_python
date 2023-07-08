#!/usr/bin/env python
# coding: utf-8

# In[98]:


pip install nltk


# In[99]:


import nltk
nltk.download('punkt')
nltk.download('omw-1.4')


# In[100]:


pip install textblob


# In[101]:


pip install autocorrect


# In[102]:


pip install pyspellchecker


# In[103]:


pip install pattern


# In[104]:


pip install Correct


# In[105]:


from spellchecker import SpellChecker


# In[106]:


dir(SpellChecker)


# In[107]:


spell = SpellChecker()


# In[108]:


docx = ["calender","lightening","misspel","neccessary","bussiness","recieve","adress"]


# In[109]:


for word in docx:
    print(f'{word}:{spell.correction(word)}')


# In[110]:


for word in docx:
    print(f'{word}:{spell.candidates(word)}')


# In[111]:


name = "firstee"


# In[112]:


spell.correction(name)


# In[113]:


spell.candidates(name)


# In[116]:


from autocorrect import spell


# In[117]:


docx


# In[118]:


for word in docx:
    print(spell(word))


# In[119]:


from textblob import TextBlob,Word


# In[120]:


ex = TextBlob("He was very accomondation in the new location")


# In[121]:


for word in ex.words:
    print(word,":",word.correct())


# In[122]:


w = Word("abscence")


# In[123]:


w.spellcheck()

