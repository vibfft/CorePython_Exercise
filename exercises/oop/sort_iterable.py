# sort method used for lists
# sort() function used for iterables

# students = ["stephen", "crystal", "sohyun"]

# students.sort(reverse=True)

# for i in students:
#     print(i)

# new_students = ("stephen", "crystal", "sohyun")
# sorted_students = sorted(new_students,reverse=True)

# for j in sorted_students:
#     print(j)    
    
students = [("stephen","F",45),
          ("crystal","A",6),
          ("sohyun","B",38)]

grade = lambda grades: grades[1]
students.sort(key=grade)

for i in students:
    print(i)
    
age = lambda ages: ages[2]  #ages refer to students list
students.sort(key=age)

for i in students:
    print(i)
    
name = lambda names: names[0]  #names refer to students list
for i in sorted(students,key=name):
    print(i)   

