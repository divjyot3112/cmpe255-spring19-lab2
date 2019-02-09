def mean_num_friends(x):
    sum = 0
    for y in x:
        sum += y
        
    n = len(x)
    return sum/n

def median_num_friends(x):
    if(len(x)%2==0):
        m=len(x)/2
        return (x[m-1] + x[m])/2
    else:
        m = (len(x)-1)/2
        return x[int(m)]    
       

num_friends=[100, 49, 41, 40, 25, 10, 5, 4, 7, 20, 60]
print("mean={}".format(mean_num_friends(num_friends)))
print("median={}".format(median_num_friends(num_friends)))