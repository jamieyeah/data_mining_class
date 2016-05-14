#gettng data into python
#using pandas module
import pandas
data=pandas.read_csv("C:\\Users\\jamie\\Documents\\bank2.csv")
age=data['age']
balance=data['balance']
education=list(data['education'])

#for normalizing numeric variables
#for age attribute
age_list=[]
for i in age:
    MAX=age.max()
    MIN=age.min()
    for j in age:
        age_list.append(abs(i-j)/(MAX-MIN))

#for balance attribute
balance_list=[]
for i in balance:
    MAX=balance.max()
    MIN=balance.min()
    for j in age:
        balance_list.append(abs(i-j)/(MAX-MIN))

#for normalizing ordinal variables
education_list=[]
for i in education: #rank
    if i=='tertiary':
        education_list.append(3)
    elif i=='secondary':
        education_list.append(2)
    elif i=='primary':
        education_list.append(1)
    else:
        education_list.append(0)

education_norm=[] #standardize
for i in education_list:
    if i==3:
        education_norm.append((3-1)/(3-1))
    elif i==2:
        education_norm.append((2-1)/(3-1))
    elif i==1:
        education_norm.append((1-1)/(3-1))
    else:
        education_norm.append(0)

education_manhattan=[] #use Manhattan distance
for i in education_norm:
    for j in education_norm:
        education_manhattan.append(abs(i-j))


import numpy as np

#make a matrices
age_mat=np.array(age_list)
bal_mat=np.array(balance_list)
edu_mat=np.array(education_manhattan)

print("this is age matrix", age_mat)
print("this is balance matrix", bal_mat)
print("this is education matrix", edu_mat)

dissimilarity_matrix=(age_mat+bal_mat+edu_mat)/3 #compute for dissimilarity matrix
print("this is dissimilarity matrix", dissimilarity_matrix)
