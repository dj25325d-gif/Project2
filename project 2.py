print("Welcome to the Pattern Generator and Number Analyzer!")

while True:
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = input("Enter your choice: ")


    if choice == "1":
        rows = int(input("Enter number of rows: "))

        print("\nPattern:")
        for i in range(1, rows + 1):
            for j in range(i):
                print("*", end=" ")
            print()



    elif choice == "2":
        start = int(input("Enter start number: "))
        end = int(input("Enter end number: "))

        if end <= start:
            print("End number must be greater than start number.")
            continue

        for num in range(start, end + 1):
            if num % 2 == 0:
                print(num, "is Even")
            else:
                print(num, "is Odd")

        total = sum(range(start, end + 1))
        print("Sum of all numbers from", start, "to", end, "is", total)


    elif choice == "3":
        print("Thank you for using the Student Data Organizer!")
        break

    else:
        print("Invalid choice. Please select 1, 2, or 3.")
