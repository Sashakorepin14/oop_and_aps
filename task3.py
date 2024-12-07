b = [23, 96, 53, 45, 9, 25, 80, 13, 79, 52]
def kub(a):
  if a % 2 == 0: 
    return a**3
  else:
    return a
c = list(map(kub, b))  
print(c)