def logic_gate(a, b):
    if a >= 0:
        a = True
    elif a < 0:
        a = False
    
    if b >= 0:
        b = True
    elif b < 0:
        b = False

    if a == True and b == False:
        return True
    elif a == False and b == True:
        return True
    elif a == True and b == True:
        return False
    elif a == False and b == False:
        return False

a = int(input('Input a number: '))
b = int(input('Input another number: '))

print('Is one positive and the other negative?')
logic = logic_gate(a, b)
print(logic)