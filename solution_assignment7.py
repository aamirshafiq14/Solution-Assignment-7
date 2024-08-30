def main():
    # Prompt user for their name
    user_name = input("Enter your name: ")

    # Prompt user for three favorite numbers
    favorite_numbers = []
    for i in range(3):
        num = float(input(f"Enter your favorite number {i+1}: "))
        favorite_numbers.append(num)

    # Greet the user
    print(f"Hello, {user_name}! Let's explore your favorite numbers.")

    # Check if numbers are even or odd
    even_odd_info = []
    for num in favorite_numbers:
        parity = "even" if num % 2 == 0 else "odd"
        even_odd_info.append((num, parity))

    # Print even/odd information
    print("\nYour favorite numbers and their parity:")
    for num, parity in even_odd_info:
        print(f"{num} is {parity}.")

    # Create tuples with number and its square
    number_and_square = [(num, num**2) for num in favorite_numbers]

    # Print number and square information
    print("\nYour favorite numbers and their squares:")
    for num, square in number_and_square:
        print(f"{num} squared is {square}.")

    # Calculate the sum of the three numbers
    total_sum = sum(favorite_numbers)
    print(f"\nThe sum of your favorite numbers is {total_sum}.")

    # Check if the sum is prime
    is_prime = check_prime(total_sum)
    if is_prime:
        print("Wow! The sum is a prime number. 🌟")
    else:
        print("Keep exploring! The sum is not a prime number.")

def check_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

if __name__ == "__main__":
    main()