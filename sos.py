N=int(input("enter any integer"))

sum_of_sq = 0
sq_of_sum = 0

for i in range(N+1):
    sum_of_sq+= i*i
    sq_of_sum+= i
    
sq_of_sum*= sq_of_sum

result = sq_of_sum - sum_of_sq 

print(" the difference of sum of squares and the square of sum is : ", result)
    
    
