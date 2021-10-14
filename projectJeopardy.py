#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# Display full content of the columns names in full
pd.set_option('display.max_colwidth', None)


# In[3]:


# Read jeopardy.csv file using pandas
jeopardy_data = pd.read_csv('jeopardy.csv')


# In[4]:


# Inspect the columns of jeopardy_csv
print(jeopardy_data.columns)


# In[5]:


# Rename columns properly
jeopardy_data = jeopardy_data.rename(
    columns = {
        ' Air Date' : 'Air Date',
        ' Round' : 'Round',
        ' Category': 'Category',
        ' Value' : 'Value',
        ' Question' : 'Question',
        ' Answer' : 'Answer'
    }
)


# In[6]:


# Inspect jeopardy_data
print(jeopardy_data.head())


# In[7]:


# A function that filters the jeopardy_data for Question that contains all of the words in a list of words
def filter_jeopardy(data, list_words):
    # Return true for rows in data that contain the words in list_word
    return data.loc[data['Question'].apply(lambda x: all(word.lower() in x.lower() for word in list_words))]

# Testing filter_jeopardy function on jeopardy_data
filtered = filter_jeopardy(jeopardy_data, ["King", "England"])

# Examine filtered on the 'Question' column for jeopardy_data
print(filtered['Question'])


# In[12]:


# Examine the data for the 'Value' column
print(jeopardy_data['Value'].head())


# In[19]:


'''
1. Create a new column called Float Value
2. Assign a float data of the 'Value' column by stripping the '$' sign 
3. and replacing ',' with nothing if the data point is not None, else 0
'''
jeopardy_data['Float Value'] = jeopardy_data['Value'].apply(                                                            lambda x:                                                             float(x.strip('$')                                                                  .replace(',','')) if x != "None" else 0)


# In[24]:


# Filtering jeopardy_data and finding the average value of those questions
filtered = filter_jeopardy(jeopardy_data, ['King'])
print(filtered['Float Value'].mean())


# In[25]:


# A function to find the unique answers of a set of data
def get_answer_counts(data):
    return data['Answer'].value_counts()

# Testing the answer count function
print(get_answer_counts(filtered))


# In[26]:


print(jeopardy_data.columns)


# In[27]:


print(jeopardy_data['Air Date'].head())


# In[33]:


#Calculating number of questions containing the word "computer" for each decade
#Add a column called 'Question Year' to jeopardy_data formatted to year
jeopardy_data['Question Year'] = jeopardy_data['Air Date'].apply(lambda x: x[:4])

#Use filter_jeopardy function to filter the word 'Computer'
computer = filter_jeopardy(jeopardy_data, ['Computer'])

# Grouping computer BY 'Question Year'
computer_by_year = computer.groupby('Question Year')['Show Number'].count().reset_index()

# Select rows where 'Question Year' is in the 90s
computer_90s = computer_by_year[(computer_by_year['Question Year'] < '2000') & (computer_by_year['Question Year'] > '1989')]

# Select rows where 'Question Year' is in the 2000s
computer_2000s = computer_by_year[(computer_by_year['Question Year'] < '2010') & (computer_by_year['Question Year'] > '1999')]

# Calculate the total number of questions containing the search term by decade
print("The number of questions featuring the word \"computer\" in the 1990s = " + str(computer_90s['Show Number'].sum()) + "\nThe number of questions containing the word \"computer\" in the 2000s = " + str(computer_2000s['Show Number'].sum()))


# In[36]:


# Display number of instances of Category occuring in particular Round
category_round = jeopardy_data.groupby(['Category', 'Round'])['Show Number'].count().reset_index()

# Plot in a pivot table to increase readability
category_round_pivot = category_round.pivot(columns = 'Round', index = 'Category', values = 'Show Number').reset_index()

# Rename columns
#category_round_pivot.columns = ['category', 'double', 'final', 'single']

# Display resulting pivot table
print(category_round_pivot)

# To find data on specific category
literature = category_round_pivot[(category_round_pivot.Category == 'LITERATURE')]
print(literature)


# In[ ]:




