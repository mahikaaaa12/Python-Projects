import pickle
def GetStudents():
    f=open("STUDENTS.dat","rb")
    percent=float(input("Enter the percent to be modified:"))
    flag=False
    try:
        while True:
            rec=pickle.load(f)
            if percent>75:
                print(rec[1],"\t",rec[2])
                flag=True
    except EOFError:
        f.close()
        if flag==False:
            print("Record not found")
GetStudents()
