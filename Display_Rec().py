import pickle
def Display_Rec():
    f1=open("STORE.DAT","rb")
    c=0
    try:
        while True:
            rec=pickle.load(f1)
            c+=1
            if rec[2]>35:
                print(rec)
    except EOFError:
        print("The total no of records are:",c)
        f1.close()
Display_Rec()
