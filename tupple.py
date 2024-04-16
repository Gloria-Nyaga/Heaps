#Accessing tuple elements
fruits = ("Guava", "Apples", "Oranges", "Peaches", "Pineapples")
print(fruits[3])

#Negative indexing
print(fruits[-5])

#Accessing items within a specific range
print(fruits[2: ])
print(fruits[ :-2])

#Check if an item is in tuple
if "Pineapples"  in fruits:
    print("I have Pineapples!")

#Slicing
ages =(10,20,30,40,50,1,34,56,78,90)
print(ages[3:9])
print(ages[-1: ])
print(ages[3:-5])

#Identifying the length of items
print(len(ages))

#Add item in a tupple
students=("Gloria", "Karen", "Joan", "Charles", "Brea", "Talia", "Christine")
newStudents=list(students)
newStudents.append("Rose")
print(newStudents)

#Remove item in a temple
studentsNames=list(students)
studentsNames.remove("Joan")
print(studentsNames)

#count
countries=("Kenya", "Malawi", "Tanzania", "Rwanda", "South Africa", "Malawi", "Ethiopia","Rwanda")
res = countries.count("Malawi")
print("count of Malawi in countires:",res)

#index
numbers=(10,2,3,4,5,3,24,8,9,10,98,76,3,10,31,24,10)
res = numbers.index(24)
print("index occurrence of 24 is",res)
