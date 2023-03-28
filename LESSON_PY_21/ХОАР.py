# Хоар 2

from random import choice
def hoar_sort(A):
    if len(A) <= 1:
        return A
    barier = choice(A)
    left = [x for x in A if  x < barier]
    middle = [x for x in A if x == barier]
    right = [x for x in A if x > barier]
    left = hoar_sort(left)
    right = hoar_sort(right)
    return left + middle + right
A=[2,4,3,6,4,7,5,1,2,4,3]
x=hoar_sort(A)
print(x)

# EVKLIDE ALGORITHM
a = int(input("Введите 1-е натуральное число: "))
b = int(input("Введите 2-е натуральное число: "))
sa = a; sb = b
b = min(sa, sb)
a = max(sa, sb)
while b:
    a,b = b, a%b
 
print("НОД(%d, %d) = %d"%(sa,sb,a))
