# tuples - immutable values

dismensions = (200, 50)
print(f"{dismensions[0]}, {dismensions[1]}")

# dismensions[0] = 250
for i in range (2):
    for dismension in dismensions:
        print(dismension)
    if i == 1:
        break
    dismensions = (400, 100)
