
# coding: utf-8

# In[1]:


# Variable Assignment
var = 100


# In[4]:


var


# In[3]:


# Assignment
x = 15
y = 42


# In[5]:


# Naming Convention
variable_name_goes_like_this = 'Python_Naming_Convention'


# In[6]:


variable_name_goes_like_this


# In[7]:


'We can put strings in single quotes'


# In[9]:


"However, we can‘t do ['t] without double quote"


# In[10]:


print('This is the right way of presenting strings')


# In[13]:


n = 36000
school = 'uw'


# In[16]:


print('The school {} has {} students.'.format(school, n))


# In[18]:


print('The school {school_name} has {stud_num} students.'.format(school_name = school, stud_num = n))


# In[19]:


# Like in C, the essence of a string is an array of chars
my_str = 'Hello, World!'


# In[24]:


print(my_str[0])
print(my_str[12])


# In[30]:


# Use of colon in strings
print(my_str[0:])
print(my_str[:5])
print(my_str[7:])
print(my_str[4:13])


# In[2]:


# list in Python
[100, 101, 102] # List of int
['English', 'Math', 'CS'] #List of Str


# In[3]:


# It is possible to declare a list variable
my_list = ['English', 'Math', 'CS']


# In[4]:


# If we want to add one more element in my_list, we do
my_list.append('Economics')


# In[5]:


my_list


# In[8]:


# It is possible to access a list like this
print(my_list[0])
print(my_list[3])


# In[9]:


# It is possible to modify a list like this
my_list[0] = 'French'
my_list


# In[10]:


# List can be an element of another list
my_big_list = [0, [1, 2], [3, 4, [5, 6], 7], 9]
my_big_list


# In[11]:


# In this case, we can do
print(my_big_list[1])
print(my_big_list[2])
print(my_big_list[2][0])
print(my_big_list[2][2])
print(my_big_list[2][2][0])

