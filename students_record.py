#================================================================================================================================================
#                                                               MAIN MENU FUNCTION
#================================================================================================================================================
print("                         *******************************                        ")
print("                         ***   STUDENT REPORT CARD   ***                        ")
print("                         *******************************                        ")
print("")
def main_menu():
    c='y'
    while c=='y':
        print("================================= MAIN MENU ===================================")
        print(" 1. RESULT MENU")
        print(" 2. ENTRY/EDIT MENU")
        print(" 3. EXIT")
        print("================================================================================")
        ch=int(input(" PLEASE ENTER YOUR CHOICE : "))
        if ch==1:
            def result_menu():
                c1='y'
                while c1=='y':
                   print("================================ RESULT MENU ==================================")
                   print(" 1. STUDENT REPORT CARD")
                   print(" 2. STUDENT DETAILS")
                   print(" 3. RESULT IN PIE CHART FORM")
                   print(" 4. BACK TO MAIN MENU")
                   print("================================================================================")
                   ch1=int(input(" PLEASE ENTER YOUR CHOICE : "))
                   if ch1==1:
                       student_report_card()
                   elif ch1==2:
                       student_details()
                   elif ch1==3:
                       def result_in_pie_chart():
                                  c2='y'
                                  while c2=='y':
                                   print(" 1. STUDENT PERFORMANCE")
                                   print(" 2. CLASS PERFORMANCE")
                                   print(" 3. BACK TO RESULT MENU")
                                   ch2=int(input(" PLEASE ENTER YOUR CHOICE : "))
                                   if ch2==1:
                                        student_performance()
                                   elif ch2==2:
                                        class_performance()
                                   elif ch2==3:
                                        print(" COMING BACK TO THE RESULT MENU......")
                                        break
                                   else:
                                        print(" WRONG INPUT")
                                        c2=input(" IF YOU WANT TO CONTINUE THEN PRESS Y")
                       result_in_pie_chart()                     
                   elif ch1==4:
                      print(" COMMING BACK TO THE MAIN MENU....")
                      break
                   else:
                    print(" WRONG INPUT")
                    c1=input(" IF YOU WANT TO CONTINUE THEN PRESS Y")
                    
            result_menu()    
        elif ch==2:
            def entry_edit_menu():
                c3='y'
                while c3=='y':
                 print(" 1. CREATE STUDENT RECORD")
                 print(" 2. DISPLAY ALL STUDENTS RECORDS")
                 print(" 3. MODIFY STUDENT RECORDS")
                 print(" 4. DELETE STUDENT RECORD")
                 print(" 5. ADD STUDENT DETAILS")
                 print(" 6. DISPLAY ALL STUDENT DETAILS ")
                 print(" 7. MODIFY STUDENT DETAILS")
                 print(" 8. BACK TO MAIN MENU")
                 ch3=int(input(" PLEASE ENTER YOUR CHOICE : "))
                 if ch3==1:
                      create_student_record()
                 elif ch3==2:
                      display_all_student_records()
                 elif ch3==3:
                      modify_student_record()
                 elif ch3==4:
                      delete_student_record()
                 elif ch3==5:
                      add_student_details()
                 elif ch3==6:
                      student_details()
                 elif ch3==7:
                      modify_student_details()
                 elif ch3==8:
                      print(" COMING BACT TO MAIN MENU")
                      break
                 else:
                      print(" WRONG INPUT")
                      c3=input(" IF YOU WANT TO CONTINUE THEN PRESS Y")
            entry_edit_menu() 
        elif ch==3:
            print(" EXITING.......")
            print("********************************** THANK YOU ***********************************")                                                                              
            break
        else:
            print(" WRONG INPUT")    

#================================================================================================================================================
#                                                FUNCTION TO DISPLAY SPECIFIC STUDENT RECORD
#================================================================================================================================================
            
def student_report_card():
    
     print("===============================STUDENT REPORT CARD==============================")
     import mysql.connector as c
     import matplotlib.pyplot as plt
     db=c.connect(host="localhost",user="root",passwd="kvcbe",database="reportcard")
     cur=db.cursor()
     rollno=int(input(" ROLL NUMBER OF STUDENT : "))
     stmt="select * from student where rollno={}".format(rollno)
     cur.execute(stmt)
     r=cur.fetchall()
     print("========================================")
     print("R.NO  NAME  MATH CHEM PHY CS ENG %AGE ")      
     print("========================================")
     for i in r:
        print(i)
     print("========================================")
     stmt="select maths,chemistry,physics,computerscience,english from student where rollno={}".format(rollno)
     cur.execute(stmt)
     l=cur.fetchall()
     stream=['math','chem','phy','cs','eng']
     explode=[0,0,0,0.1,0]
     colors=['blue','green','red','orange','yellow']
     plt.pie(l,explode=explode,labels=stream,colors=colors,shadow=True)
     plt.show()
            

    
        
#================================================================================================================================================
#                                                FUNCTION TO CREATE STUDENT RECORDS
#================================================================================================================================================

def create_student_record():
     print("=================================================================================")
     import mysql.connector as c
     db=c.connect(host="localhost",user="root",passwd="kvcbe",database="reportcard")
     cur=db.cursor()
     rollno=int(input(" ROLL NUMBER OF STUDENT : "))
     name=input(" NAME OF STUDENT : ")
     maths=int(input(" MARKS IN MATHS : "))
     chemistry=int(input(" MARKS IN CHEMISTRY : "))
     physics=int(input(" MARKS IN PHYSICS : "))
     computerscience=int(input(" MARKS IN COMPUTER SCIENCE : "))
     english=int(input(" MARKS IN ENGLISH : "))
     percentage=(maths+chemistry+physics+computerscience+english)*100/500
     print("=================================================================================")
     print(" PERCENTAGE OF STUDENT : ",percentage)
     print("=================================================================================")
     stmt="insert into student(rollno,name,maths,chemistry,physics,computerscience,english,percentage)values({},'{}',{},{},{},{},{},{})".format(rollno,name,maths,chemistry,physics,computerscience,english,percentage)
     cur.execute(stmt)
     db.commit()
     db.close()

#================================================================================================================================================
#                                                FUNCTION TO DISPLAY ALL STUDENT RECORDS
#================================================================================================================================================



def display_all_student_records(): 
     print("=================================================================================")
     import mysql.connector as c
     db=c.connect(host="localhost",user="root",passwd="kvcbe",database="reportcard")
     cur=db.cursor()
     stmt="select * from student"
     cur.execute(stmt)
     r=cur.fetchall()
     try:
        print("========================================")
        print("R.NO NAME MATH CHEM PHY CS ENG %AGE ")      
        print("========================================")
        for i in r:
         print(i)
         print("")     
     except: 
       print(" UNABLE TO RETRIVE ")
     print("========================================")  
#================================================================================================================================================
#                                                FUNCTION TO MODIFY STUDENT RECORDS
#================================================================================================================================================

def  modify_student_record():
     print("================================================================================")
     import mysql.connector as c
     db=c.connect(host="localhost",user="root",passwd="kvcbe",database="reportcard")
     cur=db.cursor()
     rollno=int(input(" ROLL NUMBER OF STUDENT : "))
     request=input(" ENTER WHAT SHOULD BE CHANGED NAME OR MARKS : ")
     if request=='NAME':
        name=input(" ENTER CORRECT NAME : ")
        stmt="update student set name='{}' where rollno={}".format(name,rollno)
        cur.execute(stmt)
     else:
       subject=input(" ENTER IN WHICH SUBJECT THE MARKS SHOULD BE CHANGE : ")
       if subject=='maths':
          value=int(input(" ENTER THE CORRECTED VALUE : "))
          stmt="update student set maths={} where rollno={}".format(value,rollno)
          cur.execute(stmt)
       elif subject=='chemistry':
          value=int(input(" ENTER THE CORRECTED VALUE : "))
          stmt="update student set chemistry={} where rollno={}".format(value,rollno)
          cur.execute(stmt)
       elif subject=='physics':
          value=int(input(" ENTER THE CORRECTED VALUE : "))
          stmt="update student set physics={} where rollno={}".format(value,rollno)
          cur.execute(stmt)
       elif subject=='computerscience':
          value=int(input(" ENTER THE CORRECTED VALUE : "))
          stmt="update student set computerscience={} where rollno={}".format(value,rollno)
          cur.execute(stmt)
       elif subject=='english':
          value=int(input(" ENTER THE CORRECTED VALUE : "))
          stmt="update student set english={} where rollno={}".format(value,rollno)
          cur.execute(stmt)
       else:
          print(" THE REQUESTED SUBJECT NOT FOUND")
     db.commit()
     print(" RECORD HAS BEEN MODIFIED")
    
    
#================================================================================================================================================
#                                                FUNCTION TO DELETE STUDENT RECORDS
#================================================================================================================================================


def delete_student_record():
     print("=================================================================================")
     import mysql.connector as c
     db=c.connect(host="localhost",user="root",passwd="kvcbe",database="reportcard")
     cur=db.cursor()
     rollno=int(input(" ROLL NUMBER OF STUDENT : "))
     stmt="delete from student where rollno={}".format(rollno)
     cur.execute(stmt)
     db.commit()
     db.close()
     print(" STUDENT RECORD HAS BEEN SUCCESSFULLY DELETED")


#================================================================================================================================================
#                                                FUNCTION TO DISPLAY STUDENT DETAILS
#================================================================================================================================================


def student_details():
     print("=================================================================================")
     import mysql.connector as c
     db=c.connect(host="localhost",user="root",passwd="kvcbe",database="reportcard")
     cur=db.cursor()
     stmt="select * from details"
     cur.execute(stmt)
     r=cur.fetchall()
     print("=========================================================================")
     print("admn_no  name       class   uid     fathername    mothername   phone number ")
     print("=========================================================================")
     for i in r:
           print(i)
     print("=========================================================================")      


#================================================================================================================================================
#                                                FUNCTION TO ADD STUDENT DETAILS
#================================================================================================================================================


def add_student_details():
     print("=================================================================================")
     import mysql.connector as c
     db=c.connect(host="localhost",user="root",passwd="kvcbe",database="reportcard")
     cur=db.cursor()
     admno=int(input(" ENTER THE ADMISSION NUMBER : "))
     name=input(" ENTER STUDENT NAME : ")  
     clas=int(input(" ENTER THE CLASS : "))
     id=int(input(" ENTER THE UID NUMBER : "))
     fname=input(" ENTER FATHER NAME : ")
     mname=input(" ENTER MOTHER NAME : ")
     ph=int(input(" ENTER THE PHONE NUMBER : "))
     stmt="insert into details(admn_no,student_name,class,uid,father_name,mother_name,phone__number)values({},'{}',{},{},'{}','{}',{})".format(admno,name,clas,id,fname,mname,ph)
     cur.execute(stmt)
     db.commit()
     db.close()
     print(" DETAILS OF STUDENT HAS BEEN ADDED ")


#================================================================================================================================================
#                                                FUNCTION TO MODIFY STUDENT DETAILS
#================================================================================================================================================


def modify_student_details():
     print("=================================================================================")
     import mysql.connector as c
     db=c.connect(host="localhost",user="root",passwd="kvcbe",database="reportcard")
     cur=db.cursor()
     admno=int(input(" ENTER THE ADMISSION NUMBER : "))
     detail=input(" ENTER IN WHAT SHOULD BE CHANGED : ")
     value=int(input(" ENTER THE CORRECT DETAIL : "))
     if detail=='NAME':
        stmt="update details set student_name={} where admn_no={}".format(value,admno)
        cur.execute(stmt)
     elif detail=='CLASS':
        stmt="update details set class={} where admn_no={}".format(value,admno)
        cur.execute(stmt)
     elif detail=='UID':
        stmt="update details set uid={} where admn_no={}".format(value,admno)
        cur.execute(stmt)
     elif detail=='FATHER NAME':
        stmt="update details set father_name={} where admn_no={}".format(value,admno)
        cur.execute(stmt)
     elif detail=='MOTHER NAME':
        stmt="update details set mother_name={} where admn_no={}".format(value,admno)
        cur.execute(stmt)
     elif detail=='PHONE NUMBER':
        stmt="update details set phone__number={} where admn_no={}".format(value,admno)
        cur.execute(stmt)    
     else:
        print(" THE REQUESTED SUBJECT NOT FOUND")
     db.commit()

    
#================================================================================================================================================
#                                                     FUNCTION TO PLOT PIE CHART OF CLASS PERFORMANCE          
#================================================================================================================================================
def  class_performance():
     import mysql.connector as c
     import matplotlib.pyplot as plt
     db=c.connect(host="localhost",user="root",passwd="kvcbe",database="reportcard")
     cur=db.cursor()
     stmt1="select count(*) from student where percentage>80"
     cur.execute(stmt1)
     x=cur.fetchall()
     stmt2="select count(*) from student where percentage between 60 and 80"
     cur.execute(stmt2)
     y=cur.fetchall()
     stmt3="select count(*) from student where percentage between 33 and 60"
     cur.execute(stmt3)
     z=cur.fetchall()
     stmt4="select count(*) from student where percentage<33"
     cur.execute(stmt4)
     p=cur.fetchall()
     l=[x,y,z,p]
     stream=['80%-100%','60%-80%','33%-60%','below 33%']
     explode=[0.1,0,0,0]
     colors=['blue','yellow','red','cyan']
     plt.pie(l,explode=explode,labels=stream,colors=colors,shadow=True)
     plt.show()

#================================================================================================================================================
#                                                    FUNCTION TO PLOT PIE CHART OF STUDENT PERFORMANCE 
#================================================================================================================================================
def  student_performance():
     import mysql.connector as c
     import matplotlib.pyplot as plt
     db=c.connect(host="localhost",user="root",passwd="kvcbe",database="reportcard")
     cur=db.cursor()
     print("===================================================================")
     rollno=int(input(" ROLL NUMBER OF STUDENT : "))
     stmt1="select maths from student where rollno={}".format(rollno)
     cur.execute(stmt1)
     M=cur.fetchall()
     stmt2="select chemistry from student where rollno={}".format(rollno)
     cur.execute(stmt2)
     C=cur.fetchall()
     stmt3="select physics from student where rollno={}".format(rollno)
     cur.execute(stmt3)
     P=cur.fetchall()
     stmt4="select computerscience from student where rollno={}".format(rollno)
     cur.execute(stmt4)
     CS=cur.fetchall()
     stmt5="select english from student where rollno={}".format(rollno)
     cur.execute(stmt5)
     E=cur.fetchall()
     print(" MARKS IN MATHS : ",M)
     print(" MARKS IN CHEMISTRY : ",C)
     print(" MARKS IN PHYSICS : ",P)
     print(" MARKS IN COMPUTER SCIENCE : ",CS)
     print(" MARKS IN ENGLISH : ",E)
                         
     stmt="select maths,chemistry,physics,computerscience,english from student where rollno={}".format(rollno)
     cur.execute(stmt)
     l=cur.fetchall()
     stream=['math','chem','phy','cs','eng']
     explode=[0,0,0,0.1,0]
     colors=['blue','green','red','orange','yellow']
     plt.pie(l,explode=explode,labels=stream,colors=colors,shadow=True)
     plt.show()

     
main_menu()

#================================================================================================================================================
#********************************************************END OF PROGRAM**********************************************************************************
#===================================================================================================================================================
      
      

