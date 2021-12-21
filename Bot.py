def hello_fromBot():
    print ("Bot : Hello, im your bot; insert your name")
    user_name = input ()
    print ( "Hello " + user_name)
def save_numbers (number):
    print ("this is the number " + str(numbers))

def mapNumebrs_to_person(person):
        print('This is th name of the person ' + person)
#In this main we are going to use the bot functions
#Main

hello_fromBot()
Save_numbers = []
Save_person = []
for i in range (0,3):
    numbers = int(input())
    save_numbers(numbers)
    Save_numbers.append(numbers)

    print ('give me the person name')
    person = input()
    mapNumebrs_to_person(person)
    Save_person.append(person)
print(Save_numbers)
print(Save_person)
#mapping the list values
Phonebook = dict(zip(Save_numbers,Save_person))
print (Phonebook)
