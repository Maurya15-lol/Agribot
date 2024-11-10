print("Welcome to 'Agribot' \n made by 'Maurya' and 'Hardhik' of 10th")
print("\n")
print("This bot can suggest you what crops to grow , predict the disease your crops have \n or \n Answer your general agriculture related questions")
print("\n")


print("Please choose the options")
z=int(input(" (1)Getting to know what kind of crop is best suitable for your region: \n (2) Idenitfy your plants disease using its symptoms: \n (3)Any questions or doubts in farming: \n (4) To Exit \n Type your answer :- "))

if z==1:

    print("You chose (1)")
    print("\n")
    from subprocess import call

    def open_py_file():

        call(["python","crop_operation.py"])

    open_py_file()

elif z==2:
    print("You chose (2)")
    print("\n")
    from subprocess import call

    def open_py_file():
        call(["python", "disease_operation.py"])

    open_py_file()

elif z==3:
    print("You chose(3)")
    print("\n")
    from subprocess import call

    def open_py_file():
        call(["python", "chat.py"])

    open_py_file()

else:
    print("Invalid option")
