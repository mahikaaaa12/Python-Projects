import pickle
def create():
    f=open("Attendence.dat","ab")
    Admission_no=int(input("Enter the admission no:"))
    Attendence=int(input("Enter the attendence:"))
    Working_days=int(input("Enter the no. of working days:"))
    rec=[Admission_no,Attendence,Working_days]
    pickle.dump(rec,f)
    f.close()
def count_short():
    f1=open("Attendence.dat","rb")
    try:
        while True:
            rec=pickle.load(f1)
            if rec[1]<=75:
                 print(rec)
    except EOFError:
        f1.close()
create()
create()
create()
count_short()
