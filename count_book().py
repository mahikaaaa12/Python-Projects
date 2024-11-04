import pickle
def count_book():
    with open("Book.dat","rb") as f1:
        c=0
        for record in f1:
            if 100 <= record[3] <= 500:
                c+= 1
        return c
print("The total number of books between 100 and 500 are:",count_book())
