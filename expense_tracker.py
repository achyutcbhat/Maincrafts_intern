import csv 
import os
FILE_NAME= "expences.csv"

# add expenses 
def add_expences():
    description=input("Enter expence decription :")
    amount= input("Enter amount")

    with open(FILE_NAME,"a",newline="")as file:
        Writer= csv.writer(file)
        Writer.writerow([description,amount])

    print("Expense added successfully!\n")

# Veiw Expenses
def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expense found.\n")
        return
    
    with open(FILE_NAME,"r") as file:
        reader= csv.reader(file)
        print("\n All Expenses : ")
        print("-----------------")
        for row in reader:
            print(f"{row[0]}-{row[1]}")
        print()

# Veiw total expenses amount 
def total_expnses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found! \n")
        return
    total=0
    with open(FILE_NAME,"r")as file:
        reader= csv.reader(file)
        for row in reader:
            total+= float(row[1])
    print(f"\nTotal spent : {total}\n")

# main function 
def main():
    while True:
        print("====  Expense Tracker ====")
        print("1.Add Expense\n2. Veiw Expenses\n3. Veiw Total\n4. Exit\n")
        
        choice= input("Choose an option (1-4): ")
        if choice=='1':
            add_expences()
        elif choice=='2':
            view_expenses()
        elif choice=='3':
            total_expnses()
        elif choice=='4':
            print("Exiting Program....")
            break
        else :
            print("Invalid choice. Try agian.\n")
    
if __name__ == "__main__":
    main()
