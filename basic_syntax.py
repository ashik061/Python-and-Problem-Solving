
#Printing current date and time

import datetime

now = datetime.datetime.now()

print ("Current date and time is: ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

#Printing 
print(datetime.__doc__)