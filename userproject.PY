mypass=input("Enter MySQL password: ")

#creating database railway
def Create_Database_Railway():
    import mysql.connector 
    mycon=mysql.connector.connect(host='localhost',user='root',passwd=mypass)    
    cursor=mycon.cursor()
    mycon.autocommit=True
    s1="create database railway"
    cursor.execute(s1)
    print('OK')
Create_Database_Railway()

#connecting to MySQL
def connection():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd=mypass,database='railway')
    if mycon.is_connected():
        print("Successfully connected to SQL")
connection()

#creating table railway
def table_creation_railway():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd=mypass,database='railway')
    cursor=mycon.cursor()
    mycon.autocommit=True
    s1="create table railway(pnr_number numeric(20) primary key,name varchar(20),phno varchar(10),age int(4),gender varchar(10),from_f varchar(20),to_t varchar(20),date_d varchar(20), price numeric(6))"
    cursor.execute(s1)
table_creation_railway()


#reating table user_accounts for personal information of user
def table_creation_user_accounts():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd=mypass,database='railway')
    cursor=mycon.cursor()
    mycon.autocommit=True
    s1="create table user_accounts(fname varchar(15),lname varchar(15),user_name varchar(16) ,password varchar(16) primary key, phno varchar(10),gender varchar(10),dob varchar(50),age varchar(4))"
    cursor.execute(s1)
table_creation_user_accounts()

def menu():
    print('1.YES')
    print('2.NO\n')
    ch=int(input('DO YOU WANT TO CONTINUE OR NOT:'))
    while ch==1:
        print('WELCOME TO RAILWAY RESERVATION SYSTEM\n')
        print('1.SIGN IN')
        print('2.SIGN UP')
        print('3.DELETE ACCOUNT')
        print('4.EXIT\n')
        ch1=int(input('ENTER YOUR CHOICE:'))
        if ch1==1:
            a=checking()
            if a==True:
                print('WELCOME')
                main()
            else:
                
                continue
        elif ch1==2:
            a=checking_1()
            if a==True:
                main()
            else:
                print('PASSWORD ALREADY EXISTS')
                continue
            
            
        elif ch1==3:
            c=checking_2()
            if c==True:
               
                print('ACCOUNT DELETED\n')
                continue
            else:
                print('YOUR PASSWORD OR USER_NAME IS INCORRECT')
                continue
        elif ch1==4:
            print('THANK YOU')
            break
        else:
            print('ERROR 404:PAGE NOT FOUND')
            break
        
def main():
    print("COVID-19 TRAVEL GUIDELINES AND ALERTS\n")
    print("1.All Incoming passengers aged 2 years and above arriving shall have to mandatorily carry RT-PCR negative test report")
    print("issued from a ICMR approved lab, subject to condition that RTPCR test should have been taken within 48 hours.\n")
    print("2.Wear Mask, Follow Physical Distancing, Maintain Hand Hygiene.\n")
    print("3.All passengers are hereby informed that downloading of Aarogya Setu App on")
    print("their mobile phone,that they are carrying along,is advisable.\n")
    print("4. Passengers should produce Vaccination Certification of both doses\n")

    print('1.YES')
    print('2.NO')
    c=int(input("Do you want to continue or not?: "))
    while (c==1):
        print(' 1.TICKET BOOKING',"\n", '2.TICKET CHECKING',"\n",'3.TICKET CANCELLING',"\n",'4.ACCOUNT DETAILS',"\n",'5.LOG OUT')
        ch=int(input('Enter your choice: '))
        if ch==1:
            ticket_booking()
        elif ch==2:
            ticket_checking()
        elif ch==3:
            ticket_cancelling()
        elif ch==4:
            checking_3()
            
                
        elif ch==5:
            print('THANK YOU!')
            break
        else:
            print('WRONG INPUT')
    else:
        print('ERROR 404: ERROR PAGE NOT FOUND\n')

# main code for ticket booking        
def ticket_booking():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd=mypass,database='railway')
    cursor=mycon.cursor()
    mycon.autocommit=True
    print("*******ATTENTION PLEASE**********\n")
    print("Due to COVID-19, we currently operate for trains between Delhi, Mumbai, Hyderabad and Varanasi.")
    n= int(input("Enter number of passengers: "))
    tpc=0
    #stations list
    print(''' 
          DELHI: D 
          MUMBAI:M 
          HYDERABAD:H 
          VARANASI:V ''')
    print("\n")
    fr=input('Enter your starting point: ')
    to=input('Enter your destination: ')
    c=fr+to
    print("Journey code:",c)
    dic={'DM':1200,'MD':1300,'HV':2400,'VH':2300,'MV':3000,'VM':3200,'MH':1450,'HM':1600,'DH':3200,'HD':3400,'DV':800,'VD':750}
    pc=dic.get(c.upper())
    phno=int(input('Enter your phone number: '))
    

    date1=input('Enter date(dd):')
    date2=input('Enter month(mm):')
    date3=input('Enter year(yyyy):')
    date=date1+"/"+date2+"/"+date3
    print("\n")
    
    #entering passenger details
    for i in range(0,n):
        nm=input('Enter your name: ')
        age=int(input('Enter your age:'))
        print('M=MALE','\n','F=FEMALE','\n','N=NOT TO MENTION')
        
        gender=input('Enter your gender: ')
        Gender=gender.upper()
        a={'M':'MALE','F':'FEMALE','N':'NOT TO MENTION'}
        v=a[Gender]
        
        k=str((phno*age)*2)
        pnr=k[-1:-13:-1]
        
        #concession as per age
        ci=0
        if age>59:
            ci+=(1-0.4)*pc
            print("40 percent concession applied on senior citizens\n")
        elif age<3:
            ci=0
            print("Ticket free for infants\n")
        else:
            ci=pc
        
        print("Passenger Fee: ",ci)
        tpc+=ci
        print("\n")
        s1="insert into railway values({},'{}',{},{},'{}','{}','{}','{}',{})".format(pnr,nm,phno,age,v,fr,to,date,ci)
        cursor.execute(s1)

    tpc=int(tpc)
    print("Total Fare: ",tpc)
    
    #the unique code
    d=str(phno+tpc)
    x=d[-1:-7:-1]
    print(x)
        
    
    print("You will get a payment link from AD-RRMS on your phone number. Click on the link and make payment.\n")
    print("After payment confirmation, a six digit secret code will be displayed.\n")
    
    
    scode=int(input("Enter six digit code for ticket confirmation:\n"))
    
    if scode==int(x):
        print('Payment received.')
        print('TICKET BOOKED SUCCESSFULLY!')
        
    else:
        print("ERROR! Ticket not booked.")
    
def ticket_checking():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd=mypass,database='railway')
    cursor=mycon.cursor()
    mycon.autocommit=True
    print('1.Yes')
    print('2.No')
    ch=int(input("Do you want to continue or not:"))

    if ch==1:
        phno=int(input('Enter your phone number:'))
        try:
            s1="select * from railway where phno=phno"
            cursor.execute(s1)
            data=cursor.fetchall()[0]
            Data=list(data)
            a=['PNR NUMBER','NAME','PHONE NUMBER','AGE','GENDER','STARTING POINT','DESTINATION','DATE','PRICE']
            print(a[0],'::::',Data[0])
            print(a[1],'::::',Data[1].upper())
            print(a[2],'::::',Data[2])
            print(a[3],'::::',Data[3])
            print(a[4],'::::',Data[4].upper())
            print(a[5],'::::',Data[5].upper())
            print(a[6],'::::',Data[6].upper())
            print(a[7],'::::',Data[7].upper())
            print(a[8],'::::',Data[8])
            
        except:
            print('TICKET DOES NOT EXISTS')
    elif ch==2:
        print('THANK YOU')
    else:
        print('ERROR 404:PAGE NOT FOUND')
    
#cancel the ticket
def ticket_cancelling():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd=mypass,database='railway')
    cursor=mycon.cursor()
    mycon.autocommit=True
    print('1.Yes')
    print('2.No')
    ch=int(input("Do you want to continue or not:"))
    if ch==1:
        phno=input('Enter your phone number: ')
        s1="Delete from railway where phno=phno"
        cursor.execute(s1)
        print('TICKET CANCELLED')
    elif ch==2:
        print('THANK YOU')
    else:
        print('ERROR 404:PAGE NOT FOUND')
        
#delete account
def checking_2():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd=mypass,database='railway')
    cursor=mycon.cursor()
    mycon.autocommit=True
    a=input('USER NAME: ')
    b=input('PASS WORD: ')
    try:
        s1="select user_name from user_accounts where password='{}'".format(b)
        cursor.execute(s1)
        data=cursor.fetchall()[0]
        data=list(data)
        if data[0]==a:
             print('IS THIS YOUR ACCOUNT')
             s1="select user_name from user_accounts where password='{}'".format(b)
             c1="select fname,lname from user_accounts where password='{}'".format(b)
             cursor.execute(c1)
             data1=cursor.fetchall()[0]
             data1=list(data1)
             data1=data1[0]+' '+data1[1]
             cursor.execute(s1)
             data=cursor.fetchall()[0]
             data=list(data)
             if data[0]==a:
                 x=['FIRST NAME','LAST NAME','PHONE NUMBER','GENDER','DATE OF BIRTH','AGE']
                 s1="select fname,lname,phno,gender,dob,age from user_accounts where password='{}'".format(b)
                 cursor.execute(s1)
                 data=cursor.fetchall()[0]
                 data=list(data)
                 print(x[0],':::',data[0])
                 print(x[1],':::',data[1])
                 print(x[2],':::',data[2])
                 print(x[3],':::',data[3])
                 print(x[4],':::',data[4])
                 print(x[5],':::',data[5])
                 print('1.yes')
                 print('2.no')
                 vi=int(input('Enter your choice:'))
                 if vi==1:
                     b1="delete from user_accounts where password = '{}'".format(b)
                     cursor.execute(b1)
                     return True
                 elif vi==2:
                     print('Thank you')
                 else:
                     print('ERROR 404:PAGE NOT FOUND')
        else:
            return False
    except:
        print('ACCOUNT DOES NOT EXIST')
        
#sign up
def checking_1():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd=mypass,database='railway')
    cursor=mycon.cursor()
    mycon.autocommit=True
    f=input("FIRST NAME: ")
    l=input("LAST NAME: ")
    n=f+" "+l
    a=input('USER NAME: ')
    b=input('PASS WORD: ')
    c=input('RE-ENTER YOUR PASS WORD: ')
    ph=input("PHONE NUMBER: ")
    print('M=MALE','\n','F=FEMALE','\n','N=NOT TO MENTION')
    print("write in small letters")
    gen=input('ENTER YOUR GENDER: ')
    print("ENTER YOR DATE OF BIRTH")
    d=input("DD:")
    o=input("MM:")
    p=input("YYYY:")
    dob=d+'/'+o+'/'+p
    age=input('YOUR AGE:')
    v={'m':'MALE','f':'FEMALE','n':'NOT TO MENTION'}
    if b==c:
            c1="insert into user_accounts values('{}','{}','{}','{}','{}','{}','{}','{}')".format(f,l,a,b,ph,v[gen],dob,age)
            cursor.execute(c1)
            print('WELCOME ',f,' ',l)
            return True
    else:
        print('BOTH PASSWORDS ARE NOT MATCHING')
        

def checking():
    #sign in
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd=mypass,database='railway')
    cursor=mycon.cursor()
    mycon.autocommit=True
    a=input('USER NAME: ')
    b=input('PASS WORD: ')
    try:
        s1="select user_name from user_accounts where password='{}'".format(b)
        c1="select fname,lname from user_accounts where password='{}'".format(b)
        cursor.execute(c1)
        data1=cursor.fetchall()[0]
        
        data1=list(data1)
        data1=data1[0]+' '+data1[1]
        cursor.execute(s1)
        data=cursor.fetchall()[0]
        data=list(data)[0]
        if data==a:
            print('Hello ',data1)
            return True
        else:
            return False
    except:
        print('ACCOUNT DOES NOT EXIST')

#account details
def checking_3():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd=mypass,database='railway')
    cursor=mycon.cursor()
    mycon.autocommit=True
    a=input('USER NAME: ')
    b=input('PASS WORD: ')
    try:
        s1="select user_name from user_accounts where password='{}'".format(b)
        c1="select fname,lname from user_accounts where password='{}'".format(b)
        cursor.execute(c1)
        data1=cursor.fetchall()[0]
        data1=list(data1)
        data1=data1[0]+' '+data1[1]
        cursor.execute(s1)
        data=cursor.fetchall()[0]
        data=list(data)
        if data[0]==a:
            
            x=['FIRST NAME','LAST NAME','PHONE NUMBER','GENDER','DATE OF BIRTH','AGE']
            s1="select fname,lname,phno,gender,dob,age from user_accounts where password='{}'".format(b)
            cursor.execute(s1)
            data=cursor.fetchall()[0]
            data=list(data)
            print(x[0],':::',data[0])
            print(x[1],':::',data[1])
            print(x[2],':::',data[2])
            print(x[3],':::',data[3])
            print(x[4],':::',data[4])
            print(x[5],':::',data[5])
            
            
        else:
            return False
    except:
        print('ACCOUNT DOES NOT EXIST')

menu()  
