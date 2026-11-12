print("=================================================================================")
print("              STUDENT RECORDS MANAGEMENT SYSTEM                                  ")
print("=================================================================================")
student={
    "101":{
        "Name":"Aman",
        "Marks":[85,90,78]
        },
    "102":{
        "Name":"Riya",
        "Marks":[92,88,95]
        },
    "103":{
        "Name":"Karan",
        "Marks":[74,80,82]
        }    
        }
def calculate_results(marks):
    total=0
    for i in marks:
        total+=i
    average=total/len(marks)
    return total,average
def display_student(record):
    for roll in record:
        print("Roll No:",roll)
        print("Name:",record[roll]["Name"])
        marks=record[roll]["Marks"]
        print("Marks:",marks)
        total,average=calculate_results(marks)
        print("Total:",total)
        print("Average:",average)
        print("-------------------------------")

def add_student(records,roll,name,marks):    
    records[roll]={
        "Name":name,
        "Marks":marks
    }
while True:
    print("\nSelect an Operation:")
    print("1. Displays All Students")
    print("2. Add New Students")
    print("3. Search Student")
    print("4. Exit")
    choice=int(input("Enter your choice(1-4):"))
    if choice==1:
        print("----------All Student Record---------")
        display_student(student)
    elif choice==2:
        roll_no=input("Enter Roll No: ")
        if roll_no in student:
            print("ROLL NO ALREADY EXISTS!")
            continue
        else:
            print("--------Add New Student-----------")
            name=input("Enter Student Name: ")
            subject1=int(input("Enter marks of subject1: "))
            subject2=int(input("Enter marks of subject2: "))
            subject3=int(input("Enter marks of subject3: "))
            if subject1<0 or subject1>100 or subject2<0 or subject2>100 or subject3<0 or subject3>100:
                print("INVALID MARKS.")
            else:    
                marks=[subject1,subject2,subject3]
                add_student(student,roll_no,name,marks)
                print(" Student Added Successfully!")

    elif choice==3:
        search=input("Enter Roll Number to search: ")
        if search in student:
            print("[RECORD FOUND]")
            print("Roll No:",search)
            print("Name:",student[search]["Name"])
            print("Marks:",student[search]["Marks"])
            marks=student[search]["Marks"]
            total,average=calculate_results(marks)
            print("Total:",total)    
            print("Average:",average)
        else:
            print("[RECORD NOT FOUND]")    
    elif choice==4:
        print("THANKS FOR USING STUDENT RECORD MANAGEMENT SYSTEM!!!<'__'>")
        break        
    else:
        print("RECORD NOT FOUND!")
      

        

