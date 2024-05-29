from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Replace 'path/to/your/image.jpg' with the actual path to your image
image_path = r"C:\Users\SAYAK\Downloads\Generated_Image.png"
image_to_paste_path = r"C:\Users\SAYAK\Downloads\Photo-removebg-preview.png"  # Replace with the path to the image you want to paste
image_to_paste_path2 = r"C:\Users\SAYAK\Downloads\White_Gold_Handwritten_Elegant_Happy_Birthday_Greetings_Card__2_-removebg-preview.png"#'C:\Users\SAYAK\Downloads\Violet_Traditional_Happy_Birthday_Greeting_Card-removebg-preview.png'

# Open the images
img = Image.open(image_path)
img_to_paste = Image.open(image_to_paste_path).convert("RGBA")
img_to_paste2 = Image.open(image_to_paste_path2).convert("RGBA")
width, height = img.size
# Resize the image (adjust the width and height as needed)
#new_size = (1000, 1000)  # Specify the new size (width, height)
#img_resized = img.resize(new_size)

# Define the coordinates and size of the box (left, bottom, width, height)
box_coords = (int(width * 0.6), int(height * 0.0000001),int(width * 0.4), int(height * 0.6))  # Adjust these values as needed

# Resize the image to fit inside the box
img_to_paste_resized = img_to_paste.resize((box_coords[2], box_coords[3]))

# Paste the second image onto the specified region of the first image
img.paste(img_to_paste_resized, (box_coords[0], box_coords[1]), mask=img_to_paste_resized)

# Define the coordinates and size of the box (left, bottom, width, height)
box_coords2 = (int(width * 0.05), int(height * 0.01),int(width * 0.5), int(height * 0.5))  # Adjust these values as needed

# Resize the image to fit inside the box
img_to_paste2_resized = img_to_paste2.resize((box_coords2[2], box_coords2[3]))

# Paste the second image onto the specified region of the first image
img.paste(img_to_paste2_resized, (box_coords2[0], box_coords2[1]), mask=img_to_paste2_resized)

# Create a subplot
fig, ax = plt.subplots()

# Display the resized image using Matplotlib
ax.imshow(img)
ax.axis('off')  # Hide axis labels and ticks

# Define the rectangle (box) to be drawn
box = patches.Rectangle((box_coords[0], box_coords[1]), box_coords[2], box_coords[3], linewidth=1, facecolor='none')

# Define the rectangle (box) to be drawn
box2 = patches.Rectangle((box_coords2[0], box_coords2[1]), box_coords2[2], box_coords2[3], linewidth=1, facecolor='none')

# Add the box to the plot
ax.add_patch(box)
ax.add_patch(box2)

# Show the plot
plt.show()