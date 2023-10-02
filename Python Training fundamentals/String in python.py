# String in python :
#   In Python, a string is a sequence of characters enclosed within either single quotes (' ') or double quotes (" ").
#  It is an immutable data type, which means once a string is created, it cannot be modified. However,
#  it is possible to create a new string by concatenating two or more strings.

# Sliceoperator :
#   variable [index]
#   variable [start:end]
#   variable [start:]
#   variable [:end]

s = "welcome "
print(s)
print(type(s))

print(s[2])
print(s[2:5])
print(s[2:])
print(s[:5])
print(s[-2])
print(s[-2:-5])
print(s[-5:-2])

# method : variable.method_name()

#function : function_name()

# len() - function

p = "welcome to python class"
print(p)
i = len(p)
print(i)

# startswith
x = p.startswith("welcome")
print(x)

# endswith
y = p.endswith("class")
print(y)

# find() - first accurence 
i = s.find("e")
print(i)

# rfind() - last accurence
i1 = s.rfind("e")
print(i1)

#index()
l = s.index ("m")
print(l)

#rindex()
l1 = s.index ("e")
print(l1)

#count()
c = s.count("e")
print(c)

#upper()
u = s.upper()
print(u)

#lower()
u1 = s.lower()
print(u1)

# capitalize()
x = s.capitalize()
print(x)

#title()
t = s.title()
print(t)

#strip()- right & left space remove 1) lstrip - left space remove. 2) rstrip - right space remove.
o = "welcome py class"
print(o)
r = o.strip()
print(r)

#replace() - replace the words
b = o.replace("e",'#')
print(b)

#split() - split the words
i = o.split()
print(i)

print("w" in o)
print("w" not in o)

for q in o:
    print(q)

