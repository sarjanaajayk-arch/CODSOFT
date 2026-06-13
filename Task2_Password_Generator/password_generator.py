" Importing the required modules for the code."
import random
import string
"Taking the inputs from the user and validating the lenght  of password."
length = int(input("enter the length of the password you want : "))
if length <6 or length  > 16 :
    print("the length is not valid")
    "if the length is valid then we will generate the password using random and string module."
else :
    characters =( string.ascii_letters + string.digits + string.punctuation)
    password = "".join(random.sample(characters,length))
    print("your password is : ",password)
    