import os

class Person:
    def __init__(self, name, ph_num, email):
        self.name= name
        self.ph_num= ph_num
        self.email= email
    def name(self):
        return f'{self.name}'
    def __str__(self):
        return_string="--------\n"
        return f"{self.name} : {self.ph_num} : {self.email}"
cont=list()
if os.path.isfile("contacts.csv"):
    with open("contacts.csv") as f:
        csv_list= f.readlines()
        for contact_line in csv_list:
            contact_data= contact_line.rstrip().split(",")
            contact=Person(contact_data[0],
                           contact_data[1],
                           contact_data[2])
            cont.append(contact)
        

u=""
print("Contact Management sysytem:")
while u!="q":
    print("Available options")
    print("1 - Enter a contact")
    print("2 - Display contact")
    print("3 - update information")
    print("q - quit program")
    u=input("Select option: ")

    if u=="1":
        print("Enter your contact information")
        name=input("Enter name: ")
        ph_num=input("Enter phone number: ")
        email=input("Enter email: ")
        our_contact = Person(name,ph_num,email)
        cont.append(our_contact)
        print("The respnse has been recorded")
    elif u== "2":
        for contact in cont:
            print(contact)
        print("The contacts are displayed")
    elif u.lower()=="q":
        break
    elif u=="3":
         n=input("Enter the name to update information:")
         for c in cont:
            if (n==c.name):
                p=input(" 1- to change number:\n 2- to change email:\n 3 - to change both:")
                if(p=="1"):
                    c.ph_num=input("Enter new number:")
                    print("Update is completed")
                elif (p=="2"):
                    c.email=input("Enter new email:")
                    print("Update is completed")
                elif (p=="3"):
                    c.ph_num=input("Enter new number:")
                    c.email=input("Enter new email:")
                    print("Update is completed")
                    
                else:
                    print("invalid!!")
            else:
                print("Enter corretly")             
with open("contacts.csv","w") as f:
    for c in cont:
        f.write(f"{c.name} , {c.ph_num} , {c.email}\n")
print("END!!")
