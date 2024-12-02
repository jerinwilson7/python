phonebook = {}

phonebook["John"] = 1234567890
phonebook["Jane"] = 9876543210
phonebook["Bob"] = 5555555555

for name,number in phonebook.items():
    print("phone number of %s is %d" %(name,number))



del phonebook['John']

phonebook['Jake'] = 465454545  
print(phonebook)


if "Jake" in phonebook:
    print("Jake is listed in the phonebook")
if "jill" not in phonebook:
    print('jill is not listed in the phone book')    