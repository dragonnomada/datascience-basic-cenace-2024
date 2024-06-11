x = [1, 2, 3, 4, 5, 6, 7] # Eje 1
y = [6, 5, 4, 3, 1, 1, 2] # Eje 2
z = [9, 9, 5, 3, 2, 1, 3] # Eje 3

T = zip(x, y, z) # datalist (lista de frames)

print(list(T))

Tp1 = filter(lambda t: t[2] == 9, T)

print(list(Tp1))