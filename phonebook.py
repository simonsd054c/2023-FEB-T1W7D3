from pprint import pprint

'''
[
   {
       "name": "John Smith",
       "address": "Sydney",
       "phone": {
           "home": "1234",
           "mobile": "2345"
       }
   },
   {
       "name": "Jane Doe",
       "address": "Melbourne",
       "phone": {
           "home": "6789",
           "mobile": "5678"
       }
   }
]
'''

phonebook = [
    {
        "name": "John Smith",
        "address": "Sydney",
        "phone": {
            "home": "1234",
            "mobile": "2345"
        }
    },
    {
        "name": "Jane Doe",
        "address": "Melbourne",
        "phone": {
            "home": "6789",
            "mobile": "5678"
        }
    }
]

name = input("Enter name: ")
address = input("Enter address: ")
home = input("Enter home number: ")
mobile = input("Enter mobile number: ")

phonebook.append({
    "name": name,
    "address": address,
    "phone": {
        "home": home,
        "mobile": mobile
    }
})

pprint(phonebook)

number_to_find = input("Enter a number to find: ")

def find_number(num):
    for phone_entry in phonebook:
        print(phone_entry)
        for number in phone_entry["phone"].values():
            print(number)
            if(num == number):
                print("Number found")
                return num
            
    print("Number not found")

number_found = find_number(number_to_find)

print(number_found)
