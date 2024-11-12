#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


data = np.genfromtxt("ASTR19_F24_group_project_data.txt", dtype = [('day', 'i8'), ('time', 'U6'), ('height', 'f8')])

day = []
time = []
height = []

for i in range(82):
    day.append(data[i][0])
    time.append(data[i][1])
    height.append(data[i][2])
    
print(day)
print(' ')
print(time)
print(' ')
print(height)


# In[ ]:




