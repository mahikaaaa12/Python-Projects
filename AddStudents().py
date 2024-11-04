import pickle
def AddStudents():
    f=open("STUDENTS.dat","wb")
    rno=int(input("Enter the roll no:"))
    name=input("Enter the name:")
    percent=float(input("Enter the percentage:"))
    rec=[rno,name,percent]
    pickle.dump(rec,f)
    f.close()
AddStudents()
AddStudents()
AddStudents()
