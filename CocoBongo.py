# In this script there is two versions of the CocoBongo Challenge. The Cocobongo1 has a condition that if the number is a multiple of 3 and also has the digit 5 in it, it will print the word "CocoBongo". And in the CocoBongo2 I just followed the instructions and did not cover the scenario.

def CocoBongo1():
    for number in range(1,101):
        if (number % 3 == 0) and ('5' in str(number)):
            print('CocoBongo')
        elif number % 3 == 0:
            print('Coco')
        elif '5' in str(number):
            print ('Bongo')
        else: print(number)
        
def CocoBongo2():
    for number in range(1,101):
        if number % 3 == 0:
            print('Coco')
        elif '5' in str(number):
            print ('Bongo')
        else: print(number)
    
version = str(input("Pick one version of the CocoBongo Challenge:\n- 1\n- 2\n\nVersion: "))
if version == '1': CocoBongo1()
elif version =='2': CocoBongo2()
else: print('You did not pick any of the versions available.')