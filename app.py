import hashlib

def main():
    print("Welcome to the Hash Generator!")
    print("Please enter the string you want to hash:")
    user_input = input()

    print("\nAvailable hash types:")
    hash_algorithms = sorted(hashlib.algorithms_guaranteed)  # Get all supported hash algorithms
    for idx, algo in enumerate(hash_algorithms, start=1):
        print(f"{idx}. {algo}")

    try:
        choice = int(input("\nEnter the number corresponding to your choice: "))
        if 1 <= choice <= len(hash_algorithms):
            selected_algo = hash_algorithms[choice - 1]
            hash_func = hashlib.new(selected_algo)
            hash_func.update(user_input.encode('utf-8'))
            print(f"\n{selected_algo.upper()} Hash: {hash_func.hexdigest()}")
        else:
            print("Invalid choice. Please select a valid option.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
