import random

# Config
NUM_COUNT = 20
MIN_NUM = 1
MAX_NUM = 50
numbers = []

def generate_numbers():
    global numbers
    numbers = [random.randint(MIN_NUM, MAX_NUM) for _ in range(NUM_COUNT)]
    print("\nGenerated numbers:", numbers)

def show_stats():
    if not numbers:
        print("\nNo numbers yet! Generate first.")
        return
    print("\nStats:")
    print("Min:", min(numbers))
    print("Max:", max(numbers))
    print("Sum:", sum(numbers))
    print("Average:", round(sum(numbers) / len(numbers), 2))
    print("Even:", [n for n in numbers if n % 2 == 0])
    print("Odd:", [n for n in numbers if n % 2 != 0])

def sort_numbers():
    if not numbers:
        print("\nNo numbers yet! Generate first.")
        return
    print("\nSorted ascending:", sorted(numbers))
    print("Sorted descending:", sorted(numbers, reverse=True))

def find_number():
    if not numbers:
        print("\nNo numbers yet! Generate first.")
        return
    n = int(input("Enter a number to search: "))
    print(f"{n} is in the list!" if n in numbers else f"{n} not found.")

def save_numbers():
    if not numbers:
        print("\nNo numbers yet! Generate first.")
        return
    with open("numbers.txt", "w") as f:
        f.write("\n".join(map(str, sorted(numbers))))
    print("\nNumbers saved to numbers.txt")

def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Generate random numbers")
        print("2. Show stats")
        print("3. Sort numbers")
        print("4. Find a number")
        print("5. Save numbers to file")
        print("6. Quit")
        choice = input("Choose an option: ")

        if choice == "1": generate_numbers()
        elif choice == "2": show_stats()
        elif choice == "3": sort_numbers()
        elif choice == "4": find_number()
        elif choice == "5": save_numbers()
        elif choice == "6":
            print("\nGoodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    menu()
