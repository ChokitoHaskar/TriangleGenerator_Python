userInput = input("Enter desired symbol as indicator : ")
symbolCustom = str(userInput)
userInput = input("Enter desired number to generate the symbol : ")
countRange = int(userInput)
endStar = ''

# right triangle
print('Right Triangle on Left anchor')
for i in range(countRange):
    endStar = symbolCustom*(i+1)
    print(endStar)

print('\nRight Triangle on Right anchor')
for i in range(countRange):
    endStar = ' '*(countRange-(i+1))+(symbolCustom*(i+1))
    print(endStar)


# Inverted right triangle
print('\nInverted right Triangle on Left anchor')
for i in range(countRange):
    endStar = symbolCustom*(countRange-i)
    print(endStar)

print('\nInverted right Triangle on Right anchor')
for i in range(countRange):
    endStar = (' '*i)+symbolCustom*(countRange-i)
    print(endStar)


# Inverted Triangle
print('\nTriangle')
if countRange % 2 == 1: 
    space = int((countRange-1) / 2)
    baseRange = int(countRange / countRange)
elif countRange % 2 == 0:
    space = int(countRange / 2)
    baseRange = int(0)
while space >= 0:
    container = []
    endStar = (' '*space)+(symbolCustom*baseRange)+(' '*space)
    if baseRange == 0:
        space -= 1
        baseRange += 2
        continue
    elif baseRange != 0:
        container.append(endStar)
    space -= 1
    baseRange += 2
    print(container)

# Inverted Triangle
print('\nInverted riangle')
space = 0
while countRange > 0:
    container = []
    endStar = (' '*space)+(symbolCustom*countRange)+(' '*space)
    container.append(endStar)
    space += 1
    countRange -= 2
    print(container)