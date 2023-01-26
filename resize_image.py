from PIL import Image

def resize_img(width, height):    
    image = Image.open('images/1.jpg')
    print(f"Image size: {image.size}")

    resize_image = image.resize((width, height))
    print("----------------")
    print(f"Resized image: {resize_image.size}")
    resize_image.save(f'images/{width}x{height} resized.jpg')
    print("Output location: photo_editor/images/1_resized.jpg")

width = input("Enter new width: ")
height = input("Enter new height: ")

resize_img(int(width), int(height))