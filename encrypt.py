import cv2
import numpy as np

def encode_secret(secret_text, user_key, output_filename="encodedImage.png"):
    original_img = cv2.imread("mypic.jpeg", cv2.IMREAD_UNCHANGED)  # Load base image
    img_height, img_width, _ = original_img.shape  # Extract dimensions

    # Validate message length
    if len(secret_text) + 7 > img_height * img_width:  # Reserve space for end marker
        print("\n❌ Error: Message too lengthy for the image!")
        return

    secret_text += "<<<END>>>"  # Append termination marker
    char_values = np.array([ord(char) for char in secret_text], dtype=np.uint8)

    # Flatten image matrix
    flat_img = original_img.flatten()
    
    # Insert message
    flat_img[:len(char_values)] = char_values
    
    # Reshape back to original structure
    altered_img = flat_img.reshape(img_height, img_width, -1)
    
    cv2.imwrite(output_filename, altered_img, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    
    # Store credentials and message length
    with open("secret_key.txt", "w") as key_file:
        key_file.write(f"{user_key}\n{len(char_values)}")

    print("\n✅ Encryption Completed Successfully!")

if __name__ == "__main__":
    user_message = input("\n📝 Enter the hidden message: ")
    user_password = input("🔑 Set an encryption password: ")
    encode_secret(user_message, user_password)
