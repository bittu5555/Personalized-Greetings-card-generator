import torch
from diffusers import StableDiffusionPipeline
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
import time
import gradio as gr
import rembg
import numpy as np

model_id = "CompVis/stable-diffusion-v1-4"
device = "cpu"

pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)
pipe = pipe.to(device)

def add_text_to_image(image, text, font_path, font_size, position, text_color):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)
    draw.text(position, text, font=font, fill=text_color)

def extract_info_from_excel(target_id, num_images):
    excel_file_path = "G:\Database.xlsx"
    df = pd.read_excel(excel_file_path)

    target_row = df[df['NGS'] == target_id]

    if not target_row.empty:
        id_value = target_row['NGS'].values[0]
        name = target_row['NAME'].values[0]
        season = target_row['SEASON'].values[0]
        travel = target_row['TRAVEL'].values[0]
        colour = target_row['COLOUR'].values[0]
        food = target_row['FOOD'].values[0]
        flower = target_row['FLOWER'].values[0]
        music = target_row['MUSIC'].values[0]
        activity = target_row['ACTIVITY'].values[0]
        image_path = target_row['IMAGE_PATH'].values[0]
        birthday = target_row['BIRTHDAY'].values[0]

        images = []
        #text_positions = [(0.1, 0.3), (0.7, 0.3), (0.1, 0.7), (0.7, 0.7), (0.4, 0.5)]  # Different positions for text
        #image_positions = [(0.55, 0.1), (0.1, 0.1), (0.55, 0.55), (0.1, 0.55), (0.3, 0.3)]  # Different positions for personal image

        for i in range(num_images):
            prompt = "Background image with {} season, {}, {} colour, {} food, {} flower, {} music and {}".format(season, travel, colour, food, flower, music, activity)
            image = pipe(prompt).images[0]
            images.append(image)
            width, height = image.size

            personal_photo = Image.open(image_path).convert("RGBA")
            personal_photo = personal_photo.resize((int(width * 0.4), int(height * 0.8)))

            # Apply background removal to the personal photo
            input_array = np.array(personal_photo)
            output_array = rembg.remove(input_array)
            personal_photo = Image.fromarray(output_array)
            # Define dynamic text and image positions
            text_positions = [(int(width * 0.05), int(height * 0.4)),
                              (int(width * 0.4), int(height * 0.4)),
                              (int(width * 0.4), int(height * 0.1)),
                              (int(width * 0.1), int(height * 0.1)),
                              (int(width * 0.2), int(height * 0.3))]

            image_positions = [(int(width * 0.6), int(height * 0.3)),
                               (int(width * 0.1), int(height * 0.4)),
                               (int(width * 0.1), int(height * 0.4)),
                               (int(width * 0.5), int(height * 0.3)),
                               (int(width * 0.6), int(height * 0.4))]

            image.paste(personal_photo, image_positions[i], mask=personal_photo)
            # Get positions for text and personal photo
            #text_position = (int(width * text_positions[i][0]), int(height * text_positions[i][1]))
            #image_position = (int(width * image_positions[i][0]), int(height * image_positions[i][1]))

            #image.paste(personal_photo, image_position, mask=personal_photo)
            
            text = f"Happy\n{birthday}\n{name}"
            font_path = "D:\AILABS_6 month\BelieveIt-DvLE.ttf"
            font_size = int(min(width, height) * 0.1)
            text_color = "black"
            add_text_to_image(image, text, font_path, font_size, text_positions[i], text_color)

            save_directory = "P:"
            os.makedirs(save_directory, exist_ok=True)

            image_filename = f"{save_directory}Generated_Image_{target_id}_{int(time.time())}_{i}.png"
            image.save(image_filename)
        return prompt,images
iface = gr.Interface(
    fn=extract_info_from_excel,
    inputs=["number", "number"],
    outputs=["text", gr.Gallery(label="Generated Images")],
    title="Greeting Card Generator",
    description="Enter an employee ID and the number of images to generate personalized greeting cards."
)

iface.launch()
