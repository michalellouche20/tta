user= input("Enter a string of 10 characters:")
if len(user)<10:
    print('string not long enough')
elif len (user)>10:
    print('string too long')
else :
    print ('Perfect string')
print (user[0], user [-1])
