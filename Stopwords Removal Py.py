#!/usr/bin/env python
# coding: utf-8

# # Stop Words Removal

# Assume project to identify the category of a news article as one of politics, sports, business, and other.
# For this project, suppose we have already used an efficient sentence segmenter and word tokenizer.
# 
# Some of the words in the corpus such as a, an, the, of, in, etc., do not add much value to the information that is required for the classification.
# 
# We typically remove such words, called stop words

# ### Why remove stop words

# stop words are present in abundance.
# 
# remove low-level information from the content to focus on important information.
# 
# By removing these words, we retain most of the important information so no negative consequences our model.
# 
# The cleaning of stop words helps us reduce the size of the dataset
# 

# ### Why not remove stop words

# The decision to remove the stop words depends upon the task and goal that we want to achieve.
# For sentiment analysis, on several occasions, the removal of stop words may be disastrous

# ## Stop Word Libraries 

# ### 1. NLTK

# In[8]:


import nltk


# In[9]:


from nltk.corpus import stopwords


# In[11]:


nltk.download('stopwords')


# In[12]:


stopwords_nltk = stopwords.words('english')


# In[13]:


print(stopwords_nltk)  # print all nltk stopwords


# In[14]:


print("total number of stopwords in nltk library is : ",len(stopwords_nltk))


# #### Let’s remove the stop words

# In[101]:


text = '''Doglapan by Ashneer Grover is hands down one of the most interesting books I've ever read and now my favourite.
Ashneer's life according to me is a full-blown masala Bollywood story, and that's one of the best parts of this book! Nowhere does he shy away from admitting his vulnerability, his failures, or his insecurities.
His book maybe titled as "Doglapan", but has a lot of "Sachhai". 
This book, although written in English, avoids technical jargon like a plague. Simple, non heavy words, and heavy recall value.
As Ashneer in his inimitable style says, "4 shabd se zyada mein baat samjhani pade to bekaar hai phir." Ashneer, in this book, takes you through a founder's birth, his life, his highs and lows, and finally a martyr's death.
But, as we all know, "ke picture abhi baaki hai mere dost", so waiting for the Phoenix to rise yet again, and to take the world by storm, with another idea, another product. We believe in you Ashneer.
And we know you'll emerge stronger and with another market disrupter.'''


# In[32]:


words = [word for word in text.split() if word.lower() not in stopwords_nltk]


# In[33]:


new_text = " ".join(words)


# In[34]:


new_text


# In[35]:


print("length of of old text : ",len(text))


# In[36]:


print("length of new text : ",len(new_text))

The steps are
    Declare the text
    Split the text into words because stop words is a list of words
    Change the words to lowercase because the list of stop words is in lowercase
    Create a list of all words which are not in the stop words list.
    The resulting list is then joined to form the sentence again.
# ### 2. spaCy

# In[47]:


#!python -m spacy download en_core_web_sm


# In[44]:


import spacy


# In[46]:


s = spacy.load("en_core_web_sm")


# In[48]:


stopwords_spacy = s.Defaults.stop_words


# In[49]:


print(stopwords_spacy)


# In[50]:


print("number of stopwords in spacy library : ",len(stopwords_spacy))


# #### removing stopwords from text by spacy

# In[51]:


words = [word for word in text.split() if word.lower() not in stopwords_spacy]


# In[52]:


new_text = " ".join(words)


# In[53]:


print(new_text)


# In[54]:


print("old text length : ",len(text))


# In[55]:


print("new text length : ",len(new_text))


# We can clearly see that the removal of stop words reduced the length of the sentence from 756 to 700,
# 
# Shorter than NLTK because the spaCy library has more stop words than NLTK.
# 
# The results, in this case, are quite similar though.

# ### Gensim 
# Gensim (Generate Similar) is an open-source software library that uses modern statistical machine learning.

# In[57]:


import gensim


# In[58]:


from gensim.parsing.preprocessing import remove_stopwords, STOPWORDS


# In[59]:


print(STOPWORDS)


# In[60]:


print(len(STOPWORDS))


# In[64]:


new_text = remove_stopwords(text)


# In[65]:


print(new_text)


# In[67]:


print("length of new_text : ",len(new_text))


# ### 4. Sklearn

# In[76]:


from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS


# In[77]:


print(ENGLISH_STOP_WORDS)


# In[78]:


print(len(ENGLISH_STOP_WORDS))


# In[81]:


n = [word for word in text.split() if word.lower() not in ENGLISH_STOP_WORDS]


# In[82]:


new_text = " ".join(n)


# In[83]:


print(new_text)


# In[84]:


print("old text length : ",len(text))


# In[85]:


print("new text length: ",len(new_text))

                     nltk   spacy	gensim	 scikit-learn
Words in Library 	 179 	326 	337 	 318
Output Length 	     756 	700 	727 	 705
# ## Stop Words Custom Lists 

# In[86]:


stopwords_nltk.extend(['first','second','third','why'])


# In[87]:


print(len(stopwords_nltk))


# the number of words in the list increased from 179 to 183

# ## Remove Words 

# In[91]:


stopwords_nltk.remove('why')


# In[92]:


print(len(stopwords_nltk))


# The number of words in the list reduced from 183 to 182

# ## Create Custom List

# In[93]:


custom_list = ['was','a','many','in','the','after','of','where','her','they']


# In[96]:


w = [word for word in text.split() if word.lower() not in custom_list]


# In[97]:


new_text = " ".join(w)


# In[104]:


print(new_text)


# In[105]:


print(len(new_text))


# by  - Ayush Singh Rawat
# 
# email - ayush191302013@gmail.com

# In[ ]:




