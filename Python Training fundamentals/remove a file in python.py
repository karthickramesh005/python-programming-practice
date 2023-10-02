import os

if os.path.exists("K:\photoshop\kl\delete.txt"):
    os.remove("K:\photoshop\kl\delete.txt")
else:
    print("file not found")
