import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="sms",
    port=3307
)

cursor = db.cursor()

print("-----Student Management System----- \n")
print(" 1) Add a student")
print(" 2) Remove a student")
print(" 3) Search a student")
print(" 4) View Student")
print(" 5) Update a Student")
print(" 6) EXIT")

choice=int(input("which operation you want to perform = "))

if (choice==1):
    print("-----Add a student-----")
    a1=input("Enter name :- ")
    a2=int(input("Enter roll number :- "))
    a3=input("Enter course name :-")
    a4=input("Gender :- ")
    a5=float(input("Your cgpa :- "))
    querry="INSERT INTO student VALUES (%s,%s,%s,%s,%s)"
    values=(a1,a2,a3,a4,a5)
    cursor.execute(querry,values)
    db.commit()
elif (choice==2):
    print("-----Remove a student-----")
    b=int(input("roll no of student which you want to remove = "))
    querry="DELETE FROM student WHERE rollno=%s"
    values=(b,)
    cursor.execute(querry,values)
    db.commit()
elif (choice==3):
    print("-----Search a student-----")
    b=int(input("roll no of student whoes information you want to know = "))
    querry="SELECT * FROM student WHERE rollno=%s"
    values=(b,)
    cursor.execute(querry,values)
    result=cursor.fetchone()
    if result:
        print(result)
    else:
        print("Student does not")
elif (choice==4):
    print("-----View students-----")
    cursor.execute("SELECT * FROM student")
    for row in cursor:
        print(row)
elif (choice==5):
    print("-----Update a student-----")
    b=int(input("roll no of student which you want to update = "))
    print(" 1) Update Name")
    print(" 2) Update roll number")
    print(" 3) Update course name")
    print(" 4) Update cgpa") 
    print(" 5) Update Gender")
    num=int(input("What you want to update = "))
    if(num==1):
        print("---Updating Name---")
        b1=input("newname = ")
        querry="UPDATE student SET name=%s WHERE rollno = %s"
        values=(b1,b)
        cursor.execute(querry,values)
        db.commit()
    elif(num==2):
        print("---Updating Roll Number---")
        b1=int(input("new roll no = "))
        querry="UPDATE student SET rollno=%s WHERE rollno = %s"
        values=(b1,b)
        cursor.execute(querry,values)
        db.commit()
    elif(num==3):
        print("---Updating Course Name---")
        b1=input("new course name = ")
        querry="UPDATE student SET course=%s WHERE rollno = %s"
        values=(b1,b)
        cursor.execute(querry,values)
        db.commit()
    elif(num==4):
        print("---Updating CGPA---")
        b1=float(input("new cgpa = "))
        querry="UPDATE student SET cgpa=%s WHERE rollno = %s"
        values=(b1,b)
        cursor.execute(querry,values)
        db.commit()
    elif(num==5):
        print("---Updating Gender---")
        b1=input("new Gender ( wrtie M for male and F for female ) = ")
        querry="UPDATE student SET gender=%s WHERE rollno = %s"
        values=(b1,b)
        cursor.execute(querry,values)
        db.commit()
else:
    print("GOODBYE:)")