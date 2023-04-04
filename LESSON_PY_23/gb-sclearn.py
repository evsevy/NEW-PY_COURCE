lst=([
  { "name": "John", "age": 21, "budget": 23000 },
  { "name": "Steve",  "age": 32, "budget": 40000 },
  { "name": "Martin",  "age": 16, "budget": 2700 }
])


























def get_budgets():
    return sum(i['budget'] for i in lst)
print(get_budgets())



#https://pythonru.com/uroki/linear-regression-sklearn
