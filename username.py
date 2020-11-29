listofusers = ['B.Mcgeever', 'T.Louis', 'A.Foy','J.Diedong']
print(listofusers)

while True:
    firstname = input('What is your firstname?')

    if firstname == 'exit':
        break
    
    lastname = input('What is your lastname?')
    listofusers.append(firstname[0] +'.' + lastname)  

    print(listofusers)
    print('type exit to quit')