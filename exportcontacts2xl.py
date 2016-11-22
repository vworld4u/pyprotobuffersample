#!/usr/bin/python3

import sys
import contact_pb2 as ab
import xlwt

def main():
    print("Sample Application to export contacts to Excel sheet")
    if (len(sys.argv) != 2):
        print("Usage: " + str(sys.argv[0]) + " ADDRESS_BOOK_FILE")
        sys.exit(0)
    
    address_book = ab.AddressBook()

    # Read the existing address book.
    try:
        f = open(sys.argv[1], "rb")
        address_book.ParseFromString(f.read())
        f.close()
    except IOError:
        print("{}: Could not open file. ".format(sys.argv[1]))
        sys.exit(0)
      
    xlFileName = sys.argv[1].split('.')[0] + '.xls'
    print("Exporting to Excel: " + xlFileName)
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("Contacts")
    header = sheet.row(0)
    header.write(0, "Id")
    header.write(1, "Name")
    header.write(2, "Email")
    header.write(3, "Phone 1")
    header.write(4, "Phone Type 1")
    header.write(5, "Phone 2")
    header.write(6, "Phone Type 2")
    header.write(7, "Phone 3")
    header.write(8, "Phone Type 3")
    header.write(9, "Phone 4")
    header.write(10, "Phone Type 4")
    header.write(11, "Phone 5")
    header.write(12, "Phone Type 5")
    
    index = 1
    for contact in address_book.contact:
        row = sheet.row(index)
        index += 1
        row.write(0, contact.id)
        row.write(1, contact.name)
        row.write(2, contact.email)
        contactIndex = 3
        for phone in contact.phone:
            row.write(contactIndex, phone.number)
            phone_type = get_phone_type(phone.type)
            row.write(contactIndex + 1, phone_type)
            contactIndex += 2
    
    workbook.save(xlFileName)
    print("Done.")

def get_phone_type(phone_type):
    if (phone_type == ab.Contact.MOBILE): return "Mobile"
    elif (phone_type == ab.Contact.WORK): return "Work"
    else: return "Home"

if (__name__ == "__main__") : main()