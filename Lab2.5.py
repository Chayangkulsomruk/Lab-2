D = [["Number ID","Name","Count","Status"],[]]
D = list(D)
print(len(D))
D[1] = ([1,"Rubber",0,"Out of stock"])
D.append([2,"Ruler",5,"In stock"])
D.append([3,"Pencil",1,"In stock"])
D.append([4,"Pen",10,"In stock"])
D.append([5,"Color pencil",5,"In stock"])
D.append([6,"A4 Paper",0,"Out of stock"])
for V in range (1,len(D),1):
    if D[V][3] == "In stock":
        print(D[V])
for V in range (1,len(D),1):
    if D[V][3] == "Out of stock":
        print(D[V])
D[2][2] -= 1
D[3][2] -= 1
D[4][2] -= 2
D[5][2] -= 1
for V in range (1,len(D),1):
    if D[V][2] == 0:
        D[V][3] = "Out of stock"
for V in range (0,len(D),1):
    print(D[V])

