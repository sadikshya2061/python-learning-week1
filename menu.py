#a program to give customer a menu,ask them what they want to order , receive the informattion and tell them Hey,name (whatever they want to order) will be ready in few moments.

print("Hello, welcome to the cafe")

#creating a name variable to store the name of the customer
name=input("what is your name?\n")

# if the name of the customer is Sadikshya then we will not serve her.
if name == "Sadikshya":
 print("You are not welcome here Just get out of here!")
 exit()
 # exit() function is used to stop the program.
 
else:
 print("hey "   + name +  ", Thank you for coming to our cafe")

#creating a menu variable to store the menu of the cafe
menu="1. Coffee\n2. Tea\n3. Sandwich\n4. Cake"

print("Here is our menu:\n" + menu + "\n what would you like to order?")

#creating an order variable to store the order of the customer
order=input()
price = 8
quantity =input("How many " + order+ " would you like?\n")
# here we are converting the quantity variable into integer using int() function because price is integer and quantity is string which couldnot be multiplied as int and string cannot be multiplied. So we put quantity int.

print("Hey " + name + ", your  " + quantity + " " +  order + " will be ready in few moments.")
total= price * int(quantity)

print("Your total is $" + str(total) + ".")
# here we are converting the total variable into string using str() function because we cannot concatenate string with integer.