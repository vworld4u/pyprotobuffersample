#!/usr/bin/python3

import sys
import contact_pb2 as ab


def main():
    new = ab.Contact()
    new.name = "Venkat"
    new.id = 1
    new.email = "vworld4u@gmail.com"
    phone = ab.Contact.PhoneNumber
    phone = new.phone.add()
    phone.number = "9940392921"
    phone.type = ab.Contact.MOBILE
    print("New Contact = " + str(new))
    print("Simple Hello!")
    
if __name__ == "__main__": main()