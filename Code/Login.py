usernames = ["JOHN","CATH","LIAM","AVA"]#stores usernames 
passwords = ["Password","12345","0000","123123","picture1"]#stores passwords
#-----------------------------------------------------------------------------------------------------------
inputUsername = input("Enter your username:\n").upper()#asking for username
print(inputUsername)
inputPassword = input("Enter your password:\n")#asking for password
print(inputPassword)
#------------------------------------------------------------------------------------------------------------
if inputUsername in list(usernames) and inputPassword in list(passwords):#checks both usernames and passwords
    print("Logged in")
else:
    print("Loggin incorrect")
