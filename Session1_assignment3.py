#Input user first name
firstname = input('Hi, Thanks for the login to Acadgild portal. Please enter your first name : '  , )
lastname = input ("Hello " + firstname + ',Reqeuest you to please enter your last name :')

#Reverse order
rfirstname = firstname[::-1]
rlastname = lastname[::-1]
print(rlastname, rfirstname)
