from PIL import Image
import numpy as np


def encrypt(image_path,key):
    image=Image.open(image_path)
    image_arr=np.array(image)
   

    key=np.resize(key,image_arr.shape)
  
    encrypted_array=np.bitwise_xor(image_arr,key)
    encrypted_img=Image.fromarray(encrypted_array)

    encrypted_img.save("Encrypted_image.jpg")
    print("Encryption successfull")

def decrypt(encrypted_img_path,key):
    encrypted_img=Image.open(encrypted_img_path)
    encrypted_array=np.array(encrypted_img)
    
    key=np.resize(key,encrypted_array.shape)

    decrypted_array = np.bitwise_xor(encrypted_array, key)
    decrypted_img = Image.fromarray(decrypted_array)
    
    decrypted_img.save("decrypted_image.png")
    print("Image decrypted successfully.")
    
def main():
    print("################ Image cryptography tool############################")

    while True:
        inp=input("\nSelect an option: \ne-Encryption \nd-Decryption \nq-Quit\n")
        if(inp=='q'):
            break

        elif inp== 'e':
            image=input("Enter path of the image file:  ")
            key = np.random.randint(0, 256, size=(3,), dtype=np.uint8)   
            encrypt(image,key)
        elif inp =='d':
            image=input("Enter path of the image file:  ")
            key = np.random.randint(0, 256, size=(3,), dtype=np.uint8)
            decrypt(image,key)
        else:
            print("Invalid input")


if __name__== "__main__":
    main()
