#!/usr/bin/env python
# coding: utf-8

# This tutorial is for anyone that is a beginner to programming.
# It is designed to help you get started immeidately working on python projects. It is not intended as a complete course. Good Luck, Remember first rule in programming:
# #Don't Panic
# 
# If you would like me to make more lanuages like
# 
# R in One Post
# 
# Go in One Post
# 
# GGplot in One Post
# 
# Pandas in One Post 
# 
# Anything data science related in One Post
# 
# Support my efforts and see my story at the bottom of the page. 
# 

# Start by downloading Python
# https://www.python.org/downloads/
# Pick the latest version for your operating system.  
# Then download jupyter notebook
# https://jupyter.readthedocs.io/en/latest/install.html

# Basic math
# 

# In[ ]:


2+2


# In[4]:


2*2


# In[5]:


2/2


# In[6]:


2-2


# In[7]:


9.0/2.0


# Basic Variable types. A variable is an identifier. In basic math x = 2. X is the variable 2 is its value. It is important that we learn what each type is and how to assign it

# In[9]:


type(2)


# In[11]:


type(2.0)


# In[12]:


type('2')


# In[13]:


x = 2
print(x)


# In[14]:


x = x + 1
print(x)


# In[18]:


#if you want to write x = x+1 shorthand. This is common when you want to write loops in functions. 
x = 2
x += 1
print(x)


# In[19]:


x*7


# In[20]:


x/x


# In[21]:


x-2


# In[22]:


x+1


# Identifiers are Case Sensitive

# In[23]:


X = 1
x = 2
print(X)
print(x)


# Identifiers should have names that are meaningful

# In[24]:


colorofmycar = 'red'
print(colorofmycar)


# In[27]:


name = 'henry'
lastname = 'bernreuter'
print(name + lastname)


# The str or string type is a string of letters. If you want to access a specific letter in a string you can. Just remebr to count the first postion as 0 not 1. 

# In[28]:


name[0]


# In[34]:


name[4]


# In[30]:


lastname[0]


# In[32]:


lastname[9]


# In[42]:


all_letters = 'abcdefghijklmnopqrstuvwxyz'
all_letters[7]+all_letters[4]+all_letters[13]+all_letters[17]+all_letters[24]


# In[43]:


#list out all letters from the first position to the last position
all_letters[0:25]


# In[45]:


#list out all the letters from the first positions ot the third position
all_letters[0:3]


# In[46]:


all_letters[:]


# In[47]:


all_letters[:25]


# In[48]:


all_letters[0:]


# In[49]:


all_letters[0::1]


# In[50]:


all_letters[0::2]


# In[51]:


all_letters[::-1]


# In[53]:


#to find the length of string we can use a function. More about what functions are further down.
len(all_letters)


# In[ ]:


#another great str function is upper to use it name the string and .upper. You can research many more str functions 


# In[55]:


all_letters.upper()


# In[57]:


#To split a string into other strings
new_string = 'This is my name Henry Bernreuter'
new_string.split()


# In[58]:


#Count how many e's are in a str
new_string.count('e')


# In[59]:


#Find something specific at a specific place in a str
new_string.find('Henry')


# In[60]:


#Replace a word in a string with another word
new_string.replace('This','That')


# You have already seen the print() function but lets add it to a str.

# In[62]:


print("My name is", name)


# In[72]:


#If you want to print on two sepereate lines use an escape clause
print('My name is \n',name)


# In[7]:


#Now write a program that asks what you name is
first_name = input('What is your first name: ')
last_name = input('What is your last name: ')
print('Your full name is',first_name,last_name)


# Functions. If you wanted to use the about code over and over you will use a function.These are the powerhouse of the program. First define the function with def. Then give it a name. Then add some code to it. 

# In[9]:


def whats_your_name():
    first_name = input('What is your first name: ')
    last_name = input('What is your last name: ')
    print('Your full name is',first_name,last_name)
    return


# In[10]:


#now lets call the function. It just like the print() function.
whats_your_name()


# Lists. Lists are inportant if you want to make a frame that has different variables. 

# In[46]:


list_1 = [1,2,3,'four','five','six']


# In[22]:


#list are like strings as they are indexed the same way.
list_1[3]


# In[23]:


list_1[:3]


# In[24]:


list_1[3:]


# In[41]:


#add to the list
list_1 = list_1 + [7,8,9]
list_1


# In[31]:


#mulitple the list
list_1 *2


# In[42]:


#How to change an element in a list. This will change 'four' to 4
list_1[3] = 4
print(list_1)


# In[47]:


#apend the list
list_1.append('ten')
print(list_1)


# In[48]:


#append the list at a specific index point, in this case we will inser 'one' at the index location one.
list_1.insert(1,'one')
print(list_1)


# In[49]:


#to delete something from the list
del list_1[1]
print(list_1)


# In[52]:


#remove something if you do not know where it is
list_1.remove('ten')
print(list_1)


# Lets Make a tuple. A tuple is like a list, but once created it can not be changed. The first example we are going to make two list and combine them into a tuple using the zip() function.

# In[21]:


num_list = [1,2,3,4,5]
letter_list = ['a','b','c','d','e']
tuple_1 = zip(num_list,letter_list)
result = list(tuple_1)
print(result)
result[1]


# In[15]:


len(result)


# In[16]:


result *2


# Dictionaries.A dictionary is a collection which is unordered, changeable and indexed. 
# In Python dictionaries are written with curly brackets, and they have keys and values.

# In[31]:


d_keys = range(26)
d_values = list('abcdefghijklmnopqrstuvwxyz')
dic = dict(zip(d_keys,d_values))
dic


# In[32]:


#locate the object at position 25
dic[25]


# In[34]:


#Change the object at postiion 25
dic[25] = '0'
dic[25]


# In[36]:


#Delete the object at position 20
del dic[20]
dic


# In[39]:


#want to ask if something is in a dictionary we can use the get() function. 
#it works like this nameofdicionary.get('key_value_you_are_searching_for','the_value_you_want_if_its_not_in_there')
d = {'first_name': 'henry','last_name': 'bernreuter','location' : 'Atlanta'}
d


# In[45]:


#Its a good idea to add message indicating that the value is not there.
#In case you are searching with a loop. (more on that later)
d.get('name','its not here boss')


# In[46]:


d.get('first_name')


# In[49]:


#If you want to add a key to your dictionary
d.setdefault('state', 'Georgia')
d


# Now we can start telling the computer what to do.
# IF Statement. This are the instructions for the program.
# IF you see this do this. 
# IF you see a red light stop.

# In[50]:


light = 'red' 
if light == 'red': #IF you see this
    print("Stop")#do this


# if-elif-else statement. We are telling the computer IF you see this do this ELSE do this. This is so that you can check 
# for different values.

# In[52]:


light = 'green'
if light == 'red': #IF you see this
    print('stop')#do this
elif light == 'green':#Else IF you see this
    print('go')#do this
else:#IF you see nothing else 
    print("These lights are not working")#do this


# In[53]:


light = 'red'
if light == 'red': #IF you see this
    print('stop')#do this
elif light == 'green':#Else IF you see this
    print('go')#do this
else:#IF you see nothing else 
    print("These lights are not working")#do this


# In[54]:


light = 'yellow'
if light == 'red': #IF you see this
    print('stop')#do this
elif light == 'green':#Else IF you see this
    print('go')#do this
else:#IF you see nothing else 
    print("These lights are not working")#do this


# FOR loop. Loops are the powerhouse of all programming lanuages. If you need to do something twice you need to loop it. 

# In[62]:


num_list = range(10)
for all_the_numbers in num_list:
    print(all_the_numbers)


# In[66]:


#Here we can combine everything we have learned to make a Christmas tree.

count_spaces = 34
start_count = 0
while count_spaces > 0 and start_count < 33 :
        print('\33[1;32;48m'+' '*count_spaces+'*'+'*'*start_count+'\33[0m')
        count_spaces -= 1
        start_count += 2
for christmas_tree in range(3):
    print(' '*33,'||')
print(' '*32, end = '\====/')
print('')


# See my Story and Support my efforts here:
# 
# https://www.gofundme.com/manage/digital-inovation-masters-degree
