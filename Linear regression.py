#%%
#importing libraries
import matplotlib.pyplot as plt
from scipy import stats

#data sets 
x=[1,2,3,4,5,6,7,8,9,10,11,12,13]
y=[99,86,87,88,111,86,103,87,94,78,77,85,86]

#slope function
slope,intercept,r,p,std_err = stats.linregress(x,y)

#equation of regression line
def regressfunc(x):
    return slope * x + intercept 

#mapping the y values of the line to its corresponding x values and storing it in a list
mymodel= list(map(regressfunc,x))

#plotting the graph
plt.scatter(x,y)
plt.plot(x,mymodel)
plt.xlabel('Time')
plt.ylabel('Speed')
plt.show()

speed = regressfunc(10)

print(speed)
