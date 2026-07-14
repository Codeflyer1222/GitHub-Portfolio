"""total = 0
for num in range(101):
    #the value of total is growing exponentially
    total = total + num

    #num is already incremented in the for loop so adding to it
    #cuts time in half to finish the loop.
    num += 1
    
    #the total variable starts at 1 because num is added to, hence the final 
    #value of total is added by 101 at the end of the loop.
    #total += 1
#the value of total is always 5050
print(num)
"""
#first nmbr is starting, second is ending, thrid is the counting iteration
for i in range( 0, 10, 10):
    print(i)