#Create Student Menü 
def menü():
    print("\nStudent Management System")
    print("="*40)
    print("\n1-Add Student ")
    print("-"*20)
    print("2- List")
    print("-"*20)
    print("3-Statistic")
    print("-"*20)
    print("Q-Quit")
    print("-"*20)
students={}

#It includes details on how to proceed according to the elections.
while True:
    menü()
    choose=int(input("Select the action you wish to perform:"))
    if choose==1:
        add_student()
    if choose==2:
        view_list()
    if choose==3:
        statistic()
    elif choose=="Q":
        print("Log Out of the System")
        break
