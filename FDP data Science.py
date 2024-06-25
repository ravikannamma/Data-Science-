#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Reverse 
a = "Hello Python"
print(a[::-1])
#print entire
a = "Hello Python"
print(a[::])


# In[9]:


a="welcome"
for i in range(len(a)+1):
    print(a[:i])


# In[10]:


a="welcome"
for i in range(len(a),0,-1):
    print(a[:i])


# In[11]:


mytuple=(13,56.7,"mother")
mytuple


# In[12]:


#single value with comma act as tuple type
mytuple=(13,)
mytuple


# In[13]:


mytuple=()
type(mytuple)


# In[15]:


#single value act as integer type
mytuple=(123)
type(mytuple)


# In[22]:


tuple1=(3,4),(7,8),(8,)
tuple2=(6,7),
print(len(tuple1))
print(len(tuple1))
res=tuple1+tuple2
print(res)
len(res)


# In[24]:


t=(1,2,4,3)
t[1:-1]


# In[25]:


t=(1,2,4,3)
t[1:]


# In[26]:


t=(1,2,4,3)
t[-1:]


# In[27]:


t=(1,2,4,3)
t[:-1]


# In[28]:


t=(1,2,4,3)
t[:]


# In[29]:


t=(1,2,4,3)
t[::-1]


# In[5]:


t = [1, 2, 4, 3, 8, 9,10]
t1=[]
[t1[i] for i in range(0, len(t), 2)]
print(t1)


# In[7]:


mylist=[13,]
print(mylist)
type(mylist)


# In[8]:


mylist=[13]
print(mylist)
type(mylist)


# In[10]:


mylist=[1,3],9,9
print(mylist)
type(mylist)


# In[ ]:




