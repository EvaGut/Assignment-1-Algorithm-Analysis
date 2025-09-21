import random
random_list1 = random.choices(range(1,9),k =5)
print( random_list1)
random_list2= random.choices(range(1,9),k =5)
print( random_list2)
file_name = "Test.txt"
file = open(file_name,'r')
content = file.read()
file.close()
print(type(content))
print(content)
print( "git hub sync test") 
def selectionSort(list,length):
    for i in range(length):  # do this for all elements in list/array 
        min = i #use value as the minimum start 
        for j in range (i + 1 , length): # move to the next element till the end is reached 
                if list[j] < list[min]: # if element j is less than element desinated as min then j is new min 
                    min = j  #make j the new min 
        (list[i],list[min]) = (list[min],list[i]) #swap the elements to sort the list/array
length = len(random_list1) # get the length of my random list to use as thhe size 
selectionSort(random_list1,length)
print(random_list1)

def insertSort(list, length):
     for i in range (length):
           key = list[i]
           j = i-1
           while j >= 0 and key < list[j]:
                list[j+1]=list[j]
                j-=1
           list[j+1] = key
insertSort(random_list2,length)
print(random_list2)

#def mergesort(list , length):
     
