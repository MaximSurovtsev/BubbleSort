with open('C:\\Users\\gr4m0\\Desktop\\b1.dat', 'r') as file:
    s = file.read().rstrip()


a = [int(x) for x in s.split(' ')]
l = len(a)
counter = 0
for i in range(1, l):
    swapped = False
    for j in range(l-i):
        counter += 1
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            swapped = True
    if not swapped:
        break

print(counter)

'''
1 1 1 1 1
do
  swapped = false
  for i = 1 to indexOfLastUnsortedElement-1
    if leftElement > rightElement
      swap(leftElement, rightElement)
      swapped = true
while swapped
'''
