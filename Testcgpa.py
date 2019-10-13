import matplotlib.pyplot as plt
index=[]
index.append("A+\n")
index.append("A\n")
index.append("A-\n")
index.append("B+\n")
index.append("B\n")
index.append("B-\n")
index.append("C+\n")
index.append("C\n")
index.append("D\n")
index.append("F\n")

aplus = 0
a = 0
aminus = 0
bplus = 0
b = 0
bminus = 0
cplus = 0
c = 0
d = 0
f = 0
file=open("semester.txt","r")
for x in file:
    y = float(x)
    if (y >= 4.00):
        aplus = aplus + 1
    elif (y >= 3.75 and y < 4.00):
        a = a + 1;
    elif (y >= 3.50 and y <= 3.74):
        aminus = aminus + 1
    elif (y >= 3.25 and y <= 3.49):
        plus = bplus + 1
    elif (y >= 3.00 and y <= 3.24):
        b = b + 1
    elif (y >= 2.75 and y <= 2.99):
        bminus = bminus + 1
    elif (y >= 2.50 and y <= 2.74):
        cplus = cplus + 1
    elif (y >= 2.25 and y <= 2.49):
        c = c + 1
    elif (y >= 2.00 and y <= 2.24):
        d = d + 1
    else:
        f = f + 1

cgpa = [aplus, a, aminus, bplus, b, bminus, cplus, c, d, f]
plt.bar(index, cgpa)
print("Software showing Diagram")
plt.xlabel("CGPA Name")
plt.ylabel("Value of Each CGPA")
plt.title("2-2 Semester result")
plt.show()

take=[]
while(True):

    print("Press 1 for Input CGPA.....\nPress 2 for show Diagram....\nPress 3 for EXIT")
    test=int(input())
    if(test==1):
        aplus = 0
        a = 0
        aminus = 0
        bplus = 0
        b = 0
        bminus = 0
        cplus = 0
        c = 0
        d = 0
        f = 0
        grade=input("Enter student GPA...\n")
        take.append(grade)
        print(len(take))
        file1=open("semester.txt","w")
        for i in range(0,len(take)):
            file1.write(take[i]+"\n")
        file1.close()
        file=open("semester.txt","r")
        for x in file:
            y = float(x)
            if (y >= 4.00):
                aplus = aplus + 1
            elif (y >= 3.75 and y < 4.00):
                a = a + 1;
            elif (y >= 3.50 and y <= 3.74):
                aminus = aminus + 1
            elif (y >= 3.25 and y <= 3.49):
                bplus = bplus + 1
            elif (y >= 3.00 and y <= 3.24):
                b = b + 1
            elif (y >= 2.75 and y <= 2.99):
                bminus = bminus + 1
            elif (y >= 2.50 and y <= 2.74):
                cplus = cplus + 1
            elif (y >= 2.25 and y <= 2.49):
                c = c + 1
            elif (y >= 2.00 and y <= 2.24):
                d = d + 1
            else:
                f = f + 1

        cgpa = [aplus, a, aminus, bplus, b, bminus, cplus, c, d, f]



    #elif(test==2):
        plt.bar(index, cgpa)
        print("Software showing Diagram")
        plt.xlabel("CGPA Name")
        plt.ylabel("Value of Each CGPA")
        plt.title("2-2 Semester result")
        plt.show()
    else:
        break
