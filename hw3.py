#gettng data into python
#using pandas module
import pandas
data=pandas.read_csv("C:\\Users\\jamie\\Documents\\crime_data.csv")

crime=data['Crime Occurrences']
fore=data['Foreigners']
pop=data['Population Density']
unem=data['Unemployment Rate']
al=data['Alcohol Consumption']
vi=data['Visiting Tourists']


def pearson_cor(a,b):
    n = len(a) #the number of attibutes
    sxx = sum(a**2) - ((sum(a)**2)/n) #calculate sum of squares of deviation
    syy = sum(b**2) - ((sum(b)**2)/n) #calculate sum of squares of deviation
    sxy = sum(a*b) - ((sum(a)*sum(b))/n) #calculate sum of deviation of a and b
    print(sxy / ((sxx*syy)**0.5)) #calculate Pearson Correlation

pearson_cor(crime,pop)
pearson_cor(crime,fore)
pearson_cor(crime,unem)
pearson_cor(crime,vi)
pearson_cor(crime,al)

