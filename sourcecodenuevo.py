#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
#from utils import *


# In[3]:


def char_range(c1, c2):
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)


# In[4]:


order = [str(i) for i in char_range('A','E')]
print(order)


# In[ ]:


"""def load_transactions(path_to_data, order):
    T = []
    with open(path_to_data, 'r') as fid:
        for lines in fid:
            str_line = list(lines.strip().split(','))
            _t = list(np.unique(str_line))
            _t.sort(key= lambda x: order.index(x))"""


# In[ ]:


#path_to_data = "C:\\Users\\alexr\\data.txt"
#Transactionss = load_transactions(path_to_data, order)


# In[5]:


T = [['A', 'C', 'D'],
    ['B', 'C', 'E'],
  ['A', 'B', 'C', 'E'],
  ['B', 'E']]


# In[6]:


#INITIIALIZATION CREATE C1
C = {}
L = {}
itemset_size = 1
Discarded = {itemset_size : []}
C.update({itemset_size : [ [f] for f in order]})


# In[7]:


C


# In[8]:


len(Discarded.keys())


# In[9]:


#CREATE L1


# In[16]:


supp_count_L = {}
min_support = 1/2

f, sup, new_discarded = get_frequent(C[itemset_size], T, min_support, Discarded)
Discarded.update({itemset_size : new_discarded})
L.update({itemset_size : f})
supp_count_L.update({itemset_size : sup})


# In[17]:


print_table(L[1], supp_count_L[1])


# In[23]:


print(L)
print(supp_count_L)


# In[22]:


L = {1: [['A'],['B'], ['C'], ['D'],['E']]}
supp_count_L = {1: [[2],[3], [3], [1],[3]]}


# In[29]:


#C[K]
k = itemset_size +1
convergence = False
while not convergence:
    C.update({k: join_set_itemsets(L[k-1], order)})
    print("table C{}: \n".format(k))
    print_table(C[k], [count_occurrences(it, T) for it in C[k]])
    f, sup, new_discarded = get_frequent(C[k], T, min_support, Discarded)
    Discarded.update({k : new_discarded})
    L.update({k : f})
    supp_count_L.update({k : sup})
    if len(L[k]) == 0:
        convergence = True
    else: 
        print("table L{}: \n".format(k))
        print_table(L[k], supp_count_L[k])
    k+=1
    


# In[31]:


print("table L{}: \n".format(k))
print_table(L[k], supp_count_L[k])


# In[11]:


def get_frequent(itemsets, Transactions, min_support, prev_discarded):
    L = []
    supp_count = []
    new_discarded = []
    
    k = len(prev_discarded.keys())
    
    for s in range(len(itemsets)):
        discarded_before = False
        if k > 0:
            for it in prev_discarded[k]:
                if set(it).issubset(set(itemsets[s])):
                    discarded_before = True
                    break
        if not discarded_before:
            count = count_occurrences(itemsets[s], Transactions)
            if count/len(Transactions) >= min_support:
                L.append(itemsets[s])
                supp_count.append(count)
            else:
                new_discarded.append(itemsets[s])
                
        return L, supp_count, new_discarded


# In[12]:


def count_occurrences(itemset, Transactions):
    count = 0
    for i in range(len(Transactions)):
        if set(itemset).issubset(set(Transactions[i])):
            count += 1
    return count


# In[25]:


def join_two_itemsets(it1, it2, order):
    it1.sort(key=lambda x: order.index(x))
    it2.sort(key=lambda x: order.index(x))
    
    for i in range(len(it1)-1):
        if it1[i] != it2[i]:
            return[]
        
    if order.index(it1[-1]) < order.index(it2[-1]):
        return it1+[it2[-1]]
    
    return []


# In[14]:


def join_set_itemsets(set_of_its, order):
    C =[]
    for i in range(len(set_of_its)):
        for j in range(i+1, len(set_of_its)):
            it_out = join_two_itemsets(set_of_its[i], set_of_its[j], order)
            if len(it_out) > 0:
                C.append(it_out)
    return C


# In[15]:


def print_table(T, supp_count):
    print("Itemset | Frequency")
    for k in range(len(T)):
        print("{} | {}".format(T[k], supp_count[k]))
    print("\n\n")

