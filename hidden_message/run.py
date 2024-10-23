'''
Developed by ladopixel
We use the Least Significant Bit (LSB) Embedding technique.

This program generates an image called 'image_with_hidden_message.png' in which it hides a message.
You only have to call the function 'lsb_hidden_message' to hide the message you want.

'''


from PIL import Image


def lsb_occult_message(imagen_path, message):
    image = Image.open(imagen_path)
    data = message.encode('utf-8') + b'\0'
    print(data)

    index = 0   
    for y in range(image.height):
        for x in range(image.width):
            pixel = list(image.getpixel((x, y)))
            for i in range(3):
                if index < len(data) * 8:
                    pixel[i] &= 0xFE
                    pixel[i] |= (data[index // 8] >> (7 - index % 8)) & 1 
                    index += 1
            image.putpixel((x, y), tuple(pixel))
    
    image.save('image_with_hidden_message.png')
    print(f'Message correctly hidden, it is in the image named: image_with_hidden_message.png')


lsb_occult_message('image.png', 'Hello, this is my hidden message')