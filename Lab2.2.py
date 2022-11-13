w = [7,5,10,14,3,9,7]
x = [9,10,3,4,2,5,7,1]
y = x.copy()
z = y.copy()
w.append(15)
x.append(14)
y.sort()
w.extend(x)
x.extend(y)
z.reverse()
y.remove(7)
ArrayofNum = len(w)
print(ArrayofNum)
Ans1 = w.count(7)
print(Ans1)
Ans2 = y.count(7)
print(Ans2)
print(y)
print(z)



