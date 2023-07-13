N = int(input())
lista = []
flag = 0

suretu = list(map(int,input().split()))

seisu = int(input())

for i in range(seisu):
    ix = int(input())
    lista.append(ix)
    
for i in lista:
    for j in suretu:
        if j == i:
            print("Yes")
            flag = 1
    
    if flag == 0:
        print("No")
        
    else:
        flag = 0