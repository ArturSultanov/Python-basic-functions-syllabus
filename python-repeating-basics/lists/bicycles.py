bicycles = ['treck', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[-2].title()
# print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati') 
# print(motorcycles)
motorcycles.insert(1, 'harley davidson')
# print(motorcycles)
del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop(1)
print("popped motorcycle is " + popped_motorcycle)
print(motorcycles)

too_expensive  = 'ducati'
motorcycles.remove(too_expensive)
print(f"A {too_expensive.title()} is too expensive for me.")
print(motorcycles)
