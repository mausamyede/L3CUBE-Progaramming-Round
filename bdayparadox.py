import numpy as np

noofexps = input("Enter the number of times each experiment is to be performed:") #no. of times the experiment is repeated

experiment23 = np.random.randint(1,356,(23,int(noofexps))) #simulating scenario of 23 people in a place with random birthdays assigned
experiment75 = np.random.randint(1,356,(75,int(noofexps))) #simulating scenario of 75 people in a place with random birthdays assigned
countpos=0 #count positive cases
countneg=0 #count negative cases

def checkRepeat(x): #function to check if two people with same b'day found in an experiment
    d = dict()
    flag=0
    global countpos
    global countneg
    for i in range(len(x)): 
        if x[i] in d:  
            countpos=countpos+1
            flag=1
            break
        d[x[i]] = 1
    if flag==0:
        countneg=countneg+1
    return i+1

#calculating probablity of two people having same birthday among 23 people
np.apply_along_axis(checkRepeat,0,experiment23)

print("Number of cases where two people out of 23 with same b'day found: ",countpos)
print("Number of cases where no people out of 23 with same b'day found: ",countneg)

print("Probablity of two people having same birthday: ",float(countpos)/float(countpos+countneg))

#calculating probablity of two people having same birthday among 75 people
countpos=0
countneg=0
np.apply_along_axis(checkRepeat,0,experiment75)

print("Number of cases where two people out of 75 with same b'day found: ",countpos)
print("Number of cases where no people out of 75 with same b'day found: ",countneg)

print("Probablity of two people having same birthday: ",float(countpos)/float(countpos+countneg))


#end of code

