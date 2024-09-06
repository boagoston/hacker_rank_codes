from collections  import Counter

n = 9
ar = [10,20, 20, 10, 10, 30, 50, 10, 20]

total = Counter(ar)
count = 0 

for i,j in total.items():
    count += j // 2
    
print(count)

#exercicio
#         
            
    
        

