#!/usr/bin/python3

import sys
import contact_pb2 as ab

def main():
    address_book = ab.AddressBook()
    print("Arguments = {}".format(sys.argv))
    
    if len(sys.argv) != 2:
        print("Usage: " + str(sys.argv[0]) + " ADDRESS_BOOK_FILE")
        sys.exit(-1)
    
    # Read the existing address book.
    try:
      f = open(sys.argv[1], "rb")
      address_book.ParseFromString(f.read())
      f.close()
    except IOError:
      print("{}: Could not open file.  Creating a new one.".format(sys.argv[1]))
    
    # Add an address.
    PromptForAddress(address_book.contact.add())
    
    # Write the new address book back to disk.
    f = open(sys.argv[1], "wb")
    f.write(address_book.SerializeToString())
    f.close()

    print("Address Book Enumeration:: => ")
    for contact in address_book.contact:
        print(contact)

# This function fills in a Person message based on user input.
def PromptForAddress(contact):
  contact.id = int(input("Enter person ID number: "))
  contact.name = input("Enter name: ")

  email = input("Enter email address (blank for none): ")
  if email != "":
    contact.email = email

  while True:
    number = input("Enter a phone number (or leave blank to finish): ")
    if number == "":
      break

    phone_number = contact.phone.add()
    phone_number.number = number

    type = input("Is this a mobile, home, or work phone? ")
    if type == "mobile":
      phone_number.type = ab.Contact.MOBILE
    elif type == "home":
      phone_number.type = ab.Contact.HOME
    elif type == "work":
      phone_number.type = ab.Contact.WORK
    else:
      print("Unknown phone type; leaving as default value.")

if __name__ == "__main__": main()