uname='cherry'
pwd='cherry@123'

aname=input("Enter your name: ")
apwd=input("Enter your password: ")

if aname==uname and apwd==pwd:
	print('''
	1.Deposit
	2.withdraw
	3.ministatement
	4.exit
	''')
	amt=50000
	opt=int(input("select your option: "))
	if opt==1:
		deposit=int(input("Enter the amount "))
		amt+=deposit
		print("Total amount : ",amt)
	elif opt==2:
		withdraw=int(input("Enter the amount "))
		amount-=withdraw
		print("Total amount: ",amt)
	elif opt==3:
		print("==============ATM==============")
		print("Username:",uname)
		print("Total amount: ",amt)
		print("Thanks for visitng")
		print("=====================")
	elif opt==4:
		exit()
else:
	print("please enter the correct details")
