'''

Developed by ladopixel
We use the Least Significant Bit (LSB) Embedding technique.

When you want to read the hidden message you call the other function 'lsb_extract_message_hidden_message'.

'''


from PIL import Image


def lsb_extract_message_hidden_message(image_path):
    image = Image.open(image_path)
    binary_message = ""
    
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.getpixel((x, y))
            for i in range(3):
                binary_message += str(pixel[i] & 1)
    
    message = ""
    
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        message += chr(int(byte, 2))
        if message.endswith('\0'):
            break
    
    return message


extracted_message = lsb_extract_message_hidden_message('image_with_hidden_message.png')
print(f'Hidden message extracted: {extracted_message}')