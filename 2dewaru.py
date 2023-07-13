N = int(input())
listA = []
counter = 0
syuryo_flag = 0
 
listA = list(map(int,input().split()))
 
def warizan(n):
    return n // 2
 
while syuryo_flag == 0:
    for i in listA:
        if i % 2 != 0:
            syuryo_flag = 1
            break
        
    listA = list(map(warizan,listA))
    counter += 1
    
print(counter - 1)
