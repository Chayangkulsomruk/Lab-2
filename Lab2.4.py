D = [["Number ID","Name","Count","Status"],[]]
D = list(D)
print(len(D))
D[1] = ([1,"Rubber",0,"Out of stock"])
D.append([2,"Ruler",5,"In stock"])
D.append([3,"Pencil",1,"In stock"])
print(D[1])
print(D[2])
print(D[3])

