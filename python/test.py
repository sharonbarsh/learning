def is_prime(num):
    if num < 2:
        return False
    else:
        for i in range(2,num):
            if(num % i == 0):
                return False
            else:   
                i += 1
    return True    
    print(num)   

arr = []
for i in range(1,1001):
    if i % 2 != 0:
        arr.append(i)

  
        
for i in arr:
    if is_prime(i): 
        print(i)