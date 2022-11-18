
A = set(['P','o','l','i','t','e','c','h','n','i','k','a','B','y','d','g','o','s','k','a'])
B = set(['U','n','i','w','e','r','s','y','t','e','t','T','e','c','h','n','o','l','o','g','i','c','z','n','o','-','P','r','z','y','r','o','d','n','i','c','z','y'])
C = set(['A','k','a','d','e','m','i','a','T','e','c','h','n','i','c','z','n','o','-','R','o','l','n','i','c','z','a'])

D = A.union(B).union(C)
print(list(D)) # a rozróżniam małe i wielkie litery jako osobne znaki

print(A.intersection(C)) # b

# c
setB = B.difference(A).difference(C)

print('Znaki unikalne dla set B z rozróżnieniem na małe i wielkie litery', setB)

# d
setA = A.difference(B).difference(C)
print('Znaki unikalne dla set A z rozróżnieniem na małe i wielkie litery', setA)
setC = C.difference(A).difference(B)
print('Znaki unikalne dla set C z rozróżnieniem na małe i wielkie litery', setC)