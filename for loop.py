s= str(input("enter a word:"))
v= 'aeiouAEIOU'
count= 0

for char in v:
    if char in s:
        count += 1

print(count)