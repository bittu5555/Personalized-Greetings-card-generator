from PIL import Image, ImageDraw

generated_image_path = r"C:\Users\SAYAK\Downloads\background.png"
generated_image = Image.open(generated_image_path)
# Create a block on the generated image
block_size = (600,900)  # Adjust the block size as needed
block_position = (1000, 100)  # Adjust the block position as needed

draw = ImageDraw.Draw(generated_image)
draw.rectangle([block_position, (block_position[0] + block_size[0], block_position[1] + block_size[1])], fill="white")

# Create a block on the generated image
block_size1 = (800,800)  # Adjust the block size as needed
block_position1 = (200,200)  # Adjust the block position as needed

draw = ImageDraw.Draw(generated_image)
draw.rectangle([block_position1, (block_position1[0] + block_size1[0], block_position1[1] + block_size1[1])], fill="white")
# Load another image to insert inside the block
insert_image_path = r"C:\Users\SAYAK\Downloads\image.png"
insert_image = Image.open(insert_image_path)

insert_image_path1=r"C:\Users\SAYAK\Downloads\text.png"
insert_image1 = Image.open(insert_image_path1)

# Resize the insert image to fit the block size
insert_image = insert_image.resize(block_size)
insert_image1=insert_image1.resize(block_size1)

# Paste the insert image inside the block
generated_image.paste(insert_image, block_position)
generated_image.paste(insert_image1, block_position1)
 #Save the final generated image with the block and inserted image
generated_image.save(r"C:\Users\SAYAK\Downloads\Generated_Image_With_Block.png")

import cv2

# Read the image from a file
image_path = r"C:\Users\SAYAK\Downloads\Generated_Image_With_Block.png"
image = cv2.imread(image_path)
image1=cv2.resize(image, (600,600))

# Display the image
cv2.imshow("image",image1)
cv2.waitKey(0)
