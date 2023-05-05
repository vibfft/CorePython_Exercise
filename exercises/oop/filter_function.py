students = [("stephen","F",45),
          ("crystal","A",6),
          ("sohyun","B",38),
          ("jason","A+",20,),
          ("joy","D",6)]

age = lambda data: data[2] > 6

adults = list(filter(age, students))

for i in adults:
    print(i)


