try:
    file = open("K:\photoshop\kl\karthi.txt","r")
    
    print(file.read())
except Exception :
    print("file not found")
else:
    file.close()
