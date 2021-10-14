l=[]
#1, 2 
for i in range(1,101):
    if (i%3==0) and (i%5==0):
        l.append('FizzBuzz')
    elif (i%5)==0:
        # print("Buzz")
        l.append("buzz")
    elif (i%3)==0:
        # print('Fizz')
        l.append('Fizz')
    else:
        l.append(i)


   
print(l)

