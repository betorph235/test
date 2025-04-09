def main():
    import sys
    from utils.hash_utils import generate_md5, generate_sha1, generate_sha256, generate_sha512

    print("Welcome to the Hash Generator!")
    print("Please enter the string you want to hash:")
    user_input = input()

    print("Select the hash type:")
    print("1. MD5")
    print("2. SHA-1")
    print("3. SHA-256")
    print("4. SHA-512")

    choice = input("Enter the number corresponding to your choice: ")

    if choice == '1':
        print("MD5:", generate_md5(user_input))
    elif choice == '2':
        print("SHA-1:", generate_sha1(user_input))
    elif choice == '3':
        print("SHA-256:", generate_sha256(user_input))
    elif choice == '4':
        print("SHA-512:", generate_sha512(user_input))
    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()