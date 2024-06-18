from PIL import Image
import numpy as np
import time

def load_image(image_path):
    return Image.open(image_path)

def save_image(image, path):
    image.save(path)

def encrypt_image(image, key):
    np_image = np.array(image)
    np.random.seed(key)
    perm = np.random.permutation(np_image.size)
    flat_image = np_image.flatten()
    encrypted_image = flat_image[perm]
    encrypted_image = encrypted_image.reshape(np_image.shape)
    return Image.fromarray(encrypted_image)

def decrypt_image(image, key):
    np_image = np.array(image)
    np.random.seed(key)
    perm = np.random.permutation(np_image.size)
    decrypted_image = np.zeros_like(np_image.flatten())
    decrypted_image[perm] = np_image.flatten()
    decrypted_image = decrypted_image.reshape(np_image.shape)
    return Image.fromarray(decrypted_image)

def main():
    print("Welcome to the Image Encryption/Decryption tool!")
    
    while True:
        print("\nMenu:")
        print("1. Encrypt an image")
        print("2. Decrypt an image")
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            image_path = input("Enter the path to the image you want to encrypt: ")
            key = int(input("Enter the encryption key (an integer): "))
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            encrypted_image_path = f'encrypted_image_{timestamp}.png'
            
            original_image = load_image(image_path)
            encrypted_image = encrypt_image(original_image, key)
            save_image(encrypted_image, encrypted_image_path)
            
            print(f"Image encrypted and saved as {encrypted_image_path}")

        elif choice == '2':
            image_path = input("Enter the path to the encrypted image you want to decrypt: ")
            key = int(input("Enter the decryption key (an integer): "))
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            decrypted_image_path = f'decrypted_image_{timestamp}.png'

            encrypted_image = load_image(image_path)
            decrypted_image = decrypt_image(encrypted_image, key)
            save_image(decrypted_image, decrypted_image_path)

            print(f"Image decrypted and saved as {decrypted_image_path}")

        else:
            print("Invalid choice. Please enter either 1 or 2.")
            continue
        
        continue_choice = input("\nDo you want to continue encrypting or decrypting images? (yes/no): ").lower()
        if continue_choice != 'yes':
            print("Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()
