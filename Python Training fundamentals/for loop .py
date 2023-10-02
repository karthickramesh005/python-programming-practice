# for loop
#    A for loop in Python is a control flow statement that is used to repeatedly
#  execute a group of statements as long as the condition is satisfied.

for i in range (1,10):
    if i == 5:
        break
    print(i)

print("end")

for i in range (1,10):
    if i == 5:
        continue
    print(i)

print("end")

for i in range (1,10):
    if i == 5:
        exit(0)
    print(i)

print("end")
