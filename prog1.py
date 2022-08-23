# contacts manage 
# get new contatc from the user -(not yet)
# print all contacts -(not yet)
# sort all contacts -(not yet)
# delete contact-(not yet)
# search contact - (not yet)
# main - to call all other function (in process)

contacts=[]

def add_new_contact():
    contact={"name":"itay","tel":"123"}
    contacts.append(contact)
    print("a contact added")

def print_all_contacts():
    print(contacts)

def del_contact():
    print("make a function that kill a contact")

def search_contact():
    print("make a function that pika bo a contact")

def main():
    user_selection=""
    while user_selection != "x":
        # menu
        print("a - add new contact")
        print("d - delete a contact")
        print("s - search a  contact")
        print("p - print all  contacts")
        print("x - exit")

        # get the user selection
        user_selection = input("select an option: ")
        print ("The user select: "+user_selection)

        # implement the user selection
        if user_selection == "a": add_new_contact()
        if user_selection == "p": print_all_contacts()
        if user_selection == "d": del_contact()
        if user_selection == "s": search_contact()
        # if user_selection == "x": print("make a function that exit from the program")

if __name__ == "__main__":
    main()

