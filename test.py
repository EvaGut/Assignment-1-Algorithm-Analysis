import random
random_list1 = random.choices(range(1,9),k =5)
print( random_list1)
file_name = "Test.txt"
file = open(file_name,'r')
content = file.read()
file.close()
print(type(content))
print(content)