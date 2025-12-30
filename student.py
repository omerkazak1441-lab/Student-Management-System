#Create Student Menü 
def menü():
    print("\nStudent Management System")
    print("="*40)
    print("\n1-Add Student ")
    print("-"*20)
    print("2- List")
    print("-"*20)
    print("3-Search Student")
    print("-"*20)
    print("4-Class Statistic") 
    print("-"*20)
    print("Q-Quit")
    print("-"*20)

students={}

def add_student():
    #Student İnformatin
    number=int(input("Enter your student number:"))
    
   
    if number in students:
        print("This Student Is Already Registered In The System")
        return

    name_surname=input("Enter your Name and Surname:")

    #Student Notes 
    note1=float(input("Enter Your First Note:"))
    note2=float(input("Enter Your Second Note:"))

    #STUDENT INFORMATION HAS BEEN ADDED TO THE SYSTEM.
   
    students[number]={
        "name": name_surname, 
        "note": [note1,note2]
    }

    #Add Message
    print(f"{name_surname} successfully added to the system")

def view_list():
    if not students:
        print("\n No registered students were found in the system")
        return
    print("\n" + "-"*50)
    print(f"{'Number':<10} {'Name-Surname':<20} {'Note':<15} {'Avarage'}")
    print("-"*50)
    for number,information in students.items():
        name=information["name"]
        note=information["note"]
        avarege=sum(note)/len(note) if note else 0
        print(f"{number:<10} {name:<20} {str(note):<15} {avarege:.2f}")
    
    print("-"*50)

#questioning whether the student is
def search_student():
    
    numbers=int(input("Enter the student number you wish to inquire about:"))
    if numbers in students:
        information = students[numbers]
        print("\n--- ÖĞRENCİ BİLGİLERİ ---")
        print(f"Number: {numbers}")
        print(f"Name Surname: {information['name']}")
        print(f"Note: {information['note']}")
       
        avarage=sum(information['note'])/ len(information["note"])
        print(f"Avarage: {avarage:.2f}")
        if avarage>50:
            print("Situation: Student Passed ✅")
        else:
            print("Situation: Student Remained ❌")
    else:
        print("No student record was found for this number")

#Class Statistic
def class_statistic():
    if not students:
        print("There is not enough data to perform the calculation.")
        return
    
    total_point=0
    more_succesful_student=""
    max_avarage=-1
    
    for number,information in students.items():
        note=information["note"]
        avarage=sum(note)/len(note)
        
        #Class Avarage
        total_point+=avarage

       
        if avarage > max_avarage:
            max_avarage = avarage
            more_succesful_student = information["name"]
    
    overal_avarage=total_point/len(students)

    print("\n" + "="*30)
    print("📊 CLASS STATİCS")
    print("="*30)
    print(f"Total Students  : {len(students)}")
    print(f"Class Avarage     : {overal_avarage:.2f}")
    print(f"Most successful student   : {more_succesful_student} ({max_avarage:.2f})")
    print("="*30)

#It includes details on how to proceed according to the elections.
while True:
    menü()
   
    choose = input("Select the action you wish to perform: ").upper()
    
    if choose == "1":
        add_student()
    elif choose == "2":
        view_list()
    elif choose == "3":
        search_student()
    elif choose == "4":
        class_statistic()
    elif choose == "Q":
        print("Log Out of the System...")
        break