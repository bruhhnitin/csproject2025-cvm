import csv
def main():
    f=open("details.csv","r")
    choice=int(input("Enter your choice: 1) Show data 2) Write Data 3) Append Data 4) Update Data 5) Delete Data : "))
    while True:
        if choice==1:
            read_csv()
        elif choice==2:
            write_csv()
        elif choice==3:
            append_csv()
        elif choice==4:
            update_csv()
        elif choice==5:
            delete_csv()
        con=input("Do you want to continue?? (y/n) :")
        if con.lower()=='n':
            break

#check commit