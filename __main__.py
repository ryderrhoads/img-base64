import base64
import datetime

def image_to_base64_string(img_path):
    """
    Convert an image to a base64 encoded string.
    """
    with open(img_path, 'rb') as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    return encoded_string

def base64_string_to_image(base64_string, output_path):
    """
    Convert a base64 encoded string back to an image.
    """
    decoded_bytes = base64.b64decode(base64_string)
    with open(output_path, 'wb') as img_file:
        img_file.write(decoded_bytes)

if __name__ == "__main__":
    choice = input("Do you want to encode an image to text or decode text to an image? (encode/decode): ")

    if choice == "encode":
        # Get user input for the image path
        img_path = input("Enter the path of the image you want to encode to text: ")

        # Encode the image to a base64 string
        encoded_string = image_to_base64_string(img_path)
        
        # Save the encoded string to a .txt file named by the current date
        current_day = datetime.datetime.now().strftime('%Y-%m-%d')
        txt_path = f"{current_day}.txt"
        with open(txt_path, 'w') as txt_file:
            txt_file.write(encoded_string)
        print(f"Encoded image saved to: {txt_path}")

    elif choice == "decode":
        # Get user input for the text file path
        txt_path = input("Enter the path of the text file you want to decode to an image: ")

        # Read the encoded string from the .txt file
        with open(txt_path, 'r') as txt_file:
            encoded_string_from_file = txt_file.read()
        
        current_day = datetime.datetime.now().strftime('%Y%m%d')
        output_img_path = f"decoded_{current_day}.jpg"
        base64_string_to_image(encoded_string_from_file, output_img_path)
        print(f"Decoded image saved to: {output_img_path}")

    else:
        print("Invalid choice.")
