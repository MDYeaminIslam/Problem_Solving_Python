#A function is a block of code which only runs when it is called.
def name():
    print("Assalamu Alaikum. This is Md. Yeamin Islam")

#calling the function
name()

print("________________________________________")
def mail(fname):
    print(fname + "@gmail.com")

mail("yeamin15-13529")
mail("tasnim16-234")
mail("zayan02307")

print("________________________________________")
#sending multiple argument into a function

def name(fname,lname):
    print("My first name is " + fname + " and my last name is "+ lname)

name("Md.Yeamin","Islam")

print("________________________________________")

#If you do not know how many arguments that will be passed into your function,
# add a * before the parameter name in the function definition.

def kids_name(*name):
    print("My second niece name is "+ name[1] )

kids_name("Tasnim","Zayan","Mim")

print("________________________________________")

#If the number of keyword arguments is unknown, add a double ** before the parameter name:

def my_function(**kid):
  print("His first name is " + kid["fname"])

my_function(fname = "Tobias", lname = "Refsnes")

print("________________________________________")
#returning value from a function
def add_value(x,y):
    return x+y
print(add_value(10,25))

print("________________________________________")

#use of lambda function

x = lambda a,b : a+b
print(x(10,44))
    
