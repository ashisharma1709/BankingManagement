#BANKING MANAGEMENT SYSTEM
import mysql.connector
mydb=mysql.connector.connect(
                             host='localhost',
                             user='root',
                             password='Ashish12345@',
                             database='bank2'
                             )
def OpenAcc():
    name=input('enter the customer name: ')
    accno=input('enter the Ac/No: ')
    dob=input('enter the DOB: ')
    address=input('enter the Address: ')
    contact=int(input('enter the contact no: '))
    opnbalance=int(input('enter the balance: '))

    data1=(name,accno,dob,address,contact,opnbalance)
    sql1=('insert into AccountDetail values(%s,%s,%s,%s,%s,%s)')

    data2=(name,accno,opnbalance)
    sql2=('insert into AmountDetail values(%s,%s,%s)')

    x=mydb.cursor()
    x.execute(sql1,data1)
    x.execute(sql2,data2)
    mydb.commit()
    print('Congratulations your Account is opened successsfully!!')
    main()
                
def DepoAmo():
    amount=input('enter the amount you want to deposit: ')
    ac=input('enter the account no. :')
    a='select bal from AmountDetail where accno=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    t=result[0]+ int(amount)
    sql=('update AmountDetail set bal=%s where accno=%s')
    d=(t,ac)
    x.execute(sql,d)
    mydb.commit()
    print('Amount deposited successfully...')
    main()

def WithdrawAmount():
    amount=input('enter the amount you want to withdraw..')
    ac=input('enter the account no. ')
    a='select bal from AmountDetail where accno=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    t=result[0]-int(amount)
    sql=('update AmountDetail set bal=%s where accno=%s')
    d=(t,ac)
    x.execute(sql,d)
    mydb.commit()
    print('available balance is..',t)
        
    main()
        
        
    
    
def BalEnq():
    ac=int(input('enter the account no. '))
    a='select bal from AmountDetail where accno=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    print('Balance for Account ',ac,'is',result[0])
    main()

def DisDetails():
    ac=int(input('enter the account no. '))
    a='select * from AccountDetail where accno=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    for i in result:
        print(i,end=' ')
    main()

def CloseAcc():
    ac=int(input('enter the account no. you want to close '))
    sql1='delete from AmountDetail where accno=%s'
    sql2='delete from AccountDetail where accno=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(sql1,data)
    x.execute(sql2,data)
    mydb.commit()
    print('account closed successfully....')
    main()
    
def main():
    print('''
          1. OPEN NEW ACCOUNT
          2. DEPOSIT AMOUNT
          3. WITHDRAW AMOUNT
          4. BALANCE ENQUIRY
          5. DISPLAY CUSTOMER DETAILS
          6. CLOSE AN ACCOUNT''')
    choice=input('Enter the task you want to perform: ')

    if (choice=='1'):
        OpenAcc()
    elif(choice=='2'):
        DepoAmo()
    elif(choice=='3'):
        WithdrawAmount()    
    elif(choice=='4'):
        BalEnq()
    elif(choice=='5'):
        DisDetails()
    elif(choice=='6'):
        CloseAcc()
    else:
        print('Invalid Choice')
        main()


                
main()
