try:
    file = open("K:\photoshop\kl\karthi.txt","a")
    file.write("i am bacame very powerfull and innavalible")
    file.close()

    file=open("K:\photoshop\kl\karthi.txt","r")
    print(file.read())
except Exception :
    print("file not found")
else:
    file.close()
