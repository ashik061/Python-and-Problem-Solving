print('hello python world !')
print('Hello World')

message_1 = "ashikur"
message_2 = "rahman" 

full_message= f"hello, {message_1.capitalize()} {message_2.capitalize()} !"

print(full_message)

url= "https://drive.google.com/drive/my-drive"

url2= url.removeprefix("https://")
# this is a comment
print(url.removeprefix("https://"))
print(url2 + '\n')

# the Zen of Python
# import this


student_names= ['ashik', 'sadik', 'farzana']

print('\n' + student_names[1].title())

print('\n' + student_names[-1].title())

student_names.append('lovely')

student_names.sort()

print(student_names)

del student_names[3]

print(student_names)

student_names.append('taher')

print(student_names)

student_names.pop()

print(student_names)

print(f"My mother is {student_names[-1]}")

for i in student_names:
    print(i)







