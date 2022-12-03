def average(data):
    avg=sum(data)/len(data)
    return avg
def outlier(avg,measure,R):
    manhattan=abs(avg-measure)
    return manhattan > R

print(average([3,3,3,3]))
print(outlier(10,2,1))

