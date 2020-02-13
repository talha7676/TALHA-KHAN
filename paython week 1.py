#!/usr/bin/env python
# coding: utf-8

# In[1]:


cake=["mango", "peach", "SHAKE"]
cake


# In[4]:


cake[2]


# In[5]:


cake=["mango", "peach", "SHAKE"]


# In[6]:


cake


# In[7]:


cake[1]


# # append & insert  are same but insert work by index an thing that can be added

# In[9]:


len(cake)


# In[10]:


cake.append("apple")


# In[11]:


cake


# In[12]:


cake.append("graph")


# In[13]:


cake


# In[14]:


cake.insert(4, "cherry")


# In[15]:


cake


# # extend append in differnt ways its add more then one value
#  to start a loop
# 

# In[17]:


cake.extend(["apple" , "blue" , "berry"])


# In[18]:


cake


# In[20]:


cake.count("apple")


# In[21]:


cake.index("blue")


# # to clean every thing it can't restore

# In[22]:


cake.clear()


# In[ ]:





# In[23]:


cake


# In[24]:


cake=["mango", "peach", "SHAKE"]


# In[25]:


cake

cake22=cake.copy()     #by value
# In[27]:


cake22


# # by refenrence other way of copy if we append things in current list its add on copy list to.

# In[31]:


cake33 = cake 


# In[32]:


cake33


# # del not function its a statment & value del permanent in list  del by 
# #(del by index)

# In[33]:


del cake22[1]
cake22


# # remove value can restore by value just put value that in list

# In[1]:


len ("cake")


# In[3]:


len (cake)


# In[4]:


cake=["mango", "peach", "SHAKE"]


# In[5]:


cake


# In[6]:


len(cake)


# In[7]:


cake.remove("peach")


# In[8]:


cake


# # pooped is use index for removed a value

# In[9]:


poopedcake=cake.pop()
print("this is from{poopedcake}")
print("the last  is {cake}")


# In[11]:


poopedcake=cake.pop()
print(f"the cites are{poopedcake}")
print(f"the cites are{cake}")


# In[12]:


cake=["mango", "peach", "SHAKE"]
cake


# In[13]:


poopedcake=cake.pop(1)
poopedcake


# In[14]:


cake.sort()
cake


# In[18]:


cake.sort(reverse=True)


# In[19]:


cake.reverse


# In[20]:


cake


# # SLICING IS REMOVE ELEMENTS I ONE TIME

# In[21]:


cake=["mango", "peach", "SHAKE" , "HJHKH" , "KJVKD"]
cake


# In[22]:


#index  -5       -4        -3       -2        -1
cake=["mango", "peach", "SHAKE" , "HJHKH" , "KJVKD"]
#index  0        1        2         3         4


# In[23]:


print(cake[0])
print(cake[-5])


# In[24]:


cake[1:3+1]


# In[25]:


cake[0:2]


# In[26]:


cake[1:2:2]


# In[27]:


cake[-3:-1]


# In[28]:


cake[:]


# In[29]:


cake[3:]


# In[30]:


cake[2:]


# In[33]:


cake[0:-3]


# In[37]:


num=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]


# In[36]:


num=[1,2,3,4,5,6,7,8,,9,10,11,12,13,14,15,16,17]


# In[38]:


num


# In[39]:


num[2:12:2]


# In[40]:


num[::5]


# In[41]:


num[5::3]


# # tuples are immutable can not change aur add value

# In[45]:


atuple=[1,2,4,"ali","e"]
atuple


# In[46]:


len(atuple)


# In[48]:


atuple[3]


# In[49]:


a=12,45


# In[50]:


a


# In[51]:


a.index(12)


# In[53]:


a.count()


# In[ ]:




