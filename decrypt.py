import cv2
import numpy as np

def decode_secret():
    encrypted_img = cv2.imread("encodedImage.png", cv2.IMREAD_UNCHANGED)  # Load encoded image

    with open("secret_key.txt", "r") as key_file:
        stored_key = key_file.readline().strip()
        msg_size = int(key_file.readline().strip())  # Retrieve message size

    input_key = input("🔑 Enter the decryption password: ")
    
    if input_key != stored_key:
        print("\n❌ Error: Incorrect password!")
        return

    # Extract image data
    img_data = encrypted_img.flatten()
    
    # Retrieve hidden message
    retrieved_chars = [chr(img_data[i]) for i in range(msg_size)]
    hidden_message = "".join(retrieved_chars).strip()
    
    # Remove termination marker if present
    if "<<<END>>>" in hidden_message:
        hidden_message = hidden_message.replace("<<<END>>>", "")
    
    print("\n✅ Decrypted Message:", hidden_message)

if __name__ == "__main__":
    decode_secret()
