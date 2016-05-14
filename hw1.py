#gettng data into python
#using pandas module
import pandas
data=pandas.read_csv("C:\\Users\\jamie\\Documents\\bank.csv")
age=data['age']
age=list(age)
age.sort()#becomes sorted

#how to get midrange
maximum_age=max(age)
minumum_age=min(age)
print("The midrange is", (maximum_age+minumum_age)/2)


#how to get median
def median(a): #make a function on my own
    srt = sorted(a) #sorting
    mid = len(a)//2 #compute the length and count how many values are in the list
    if len(a) % 2: #for the even numbers of values
            return srt[mid] #get the midth value
    else: #for odd numbers
        med = (srt[mid] + srt[mid-1]) / 2 #for the odd numbers of values, choose the middle value and the one right before the middle value, and divide them by 2
        return med
median(age)
print("the median is",median(age))


#how to get mean
#1. compute Q1, Q3
part1=age[0:len(age)//2] #divide into 2 parts to compute Q1 and Q3
part2=age[len(age)//2:]
Q1 = median(part1) #use the median code wrote above
Q3 = median(part2)

fence1=Q3+(1.5*(Q3-Q1)) #calculate the fences so that I can extract the outliers
fence2=Q1-(1.5*(Q3-Q1))
print("the fence1 is", fence1)
print("the fence2 is", fence2)

#2. Extract the outliers and get the trimmed age values
trimmed_age_values=[i for i in age if fence2<i<fence1] #select the values satisfying the range
print("The trimmed age values' list is", trimmed_age_values)
#this trimmed_age_values list ends by 70 because the fence1 is 70.5 Above 70.5, which means from 71 until the max value, are got rid of from the list.

#3. sum up the elements
def addup(list):
    s = 0
    for i in list:
        s = s+i
    return s

#4. compute the trimmed mean
trimmed_mean=addup(trimmed_age_values)/len(trimmed_age_values) #add up the values and divided by the number of values
print("The trimmed mean is", trimmed_mean)


#how to get mode
mode=max(set(age), key=age.count) #all the values are substituted into key function and max pick the max value
print("The mode is ", mode) # the result is 32 and this is unimodal.
