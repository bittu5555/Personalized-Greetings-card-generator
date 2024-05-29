![image](https://github.com/bittu5555/Personalized-Greetings-card-generator/assets/106305917/df9fc3c8-d54c-4db3-b78b-80963de5d36f)

**Introduction:**

The "Personalized Greetings Card Generator" is a creative system to send heartfelt expressions. Using advanced techniques like the Stable Diffusion model from Hugging Face, according to the prompt it transforms into unique background images, for greeting cards. Through a user-friendly gradio interface, individuals input details like the recipient's name, occasion, and preferences. Extract data from Excel sheets, that contain all details of employees. The process involves generating images with the pre-trained model, integrating personal photos, and adding custom text, with features like background removal and font selection. Finally, the generator saves each customized card with a unique filename, ready for preview and download. This innovative tool redefines how we offer a personalized wish in every greeting card.

**Model Details:**

Stable Diffusion is a latent text-to-image diffusion model capable of generating photo-realistic images given any text input.
Model type: Diffusion-based text-to-image generation model
Model Description: This is a model that can be used to generate and modify images based on
text prompts. It is a Latent Diffusion Model that uses a fixed, pre trained text encoder (CLIP
ViT-L/14) as suggested in the Imagen paper.
If GPU memory have less than 4GB of GPU RAM available, please make sure to load the
StableDiffusionPipeline in float16 precision instead of the default float32 precision as done
above.

**Library used:**

* **torch:** PyTorch library, commonly used for deep learning tasks. In this case, it seems to be utilized for the Stable Diffusion model.

* **Diffusers:-** Diffusers is the go-to library for state-of-the-art pre-trained diffusion models for generating images, audio, and even 3D structures.

* **PIL (Python Imaging Library):** Used for image processing tasks. It's employed for opening, manipulating, and saving images.

* **pandas:** A powerful data manipulation library used to read data from an Excel file into a Data-Frame.

* **OS:** The Python os module provides a way to interact with the operating system. It's used here to create directories and handle file operations.

* **time:** The time module is used for generating a timestamp that's appended to the generated image filenames.

* **rembg (Remove Background):** A library for removing the background from images. It seems to be applied to a personal photo in the project.

* **numpy:** A library for numerical operations. In this case, it's used to convert images to arrays for processing.

* **gradio:** A library , used for generating a interface for the user to give input and take output.

**Work Flow:**

* **User Input:**

The process begins when a user interacts with the Gradio interface. Users put input an employee ID and specify the number of personalized greeting cards they want to generate.

* **Excel Data Extraction:**

The process begins with extracting information from an Excel spreadsheet based on the provided employee id on gradio. It extracts information according to employee id that we put in gradio. This spreadsheet likely contains data about individuals, including attributes like their name, birthday, preferences (season, colour, food, travel, flower, music, activity ), and paths to their personal photos.

* **Prompt Construction:**

Once the relevant information is extracted by Unique id from the Excel sheet, the system constructs a personalized prompt for each individual based on their preferences. This message serves as a prompt for generating the unique greeting card. And According to the prompt greetings card will generate.

* **Background Image Generation:**

A Stable Diffusion Pipeline is initialized using a pre-trained model. This pipeline is responsible for generating images based on textual prompts provided to it. Using a pre-trained text to image generation stablediffusion model (CompVis/stable-diffusion-v1-4)  that is taken form hugging face , the code generates an image based on the constructed prompt based on employee preferences. The diffusion model is a deep learning model capable of generating high-quality images conditioned on textual prompts. It also specifies the device to be used for computation. In this case, the device is set to "cpu" for local machine.

* **Function Definition:-**

‘add_text_to_image’: A function that adds text to an image using PIL's ImageDraw module.
‘extract_info_from_excel’: This function reads data from an Excel file located at a specific path based on a specific employee ID (target ID) in the Excel file.

If the ID is found: It extracts various attributes associated with the ID from the Excel row (e.g., name, season, travel, colour,place etc.).
If the ID is not found then it shows error.

* **Personalization:**

After generating the background image, the code personalizes it further by: Adding the individual's personal photo onto the generated image. This personal photo is retrieved from the provided path in the Excel spreadsheet . Adding additional text elements such as the individual's name and birthday onto the image.There are multiple format of text you can choose anyone of them.

* **Image Saving:**

After generating the personalized greeting card, the generated greeting card images are saved to a specified directory with unique filenames using timestamp and files are not replaced. This ensures that each card is uniquely identifiable and can be retrieved later.

* **Output to Gradio Interface:**

The function returns the constructed prompt and a list of generated images to the Gradio interface. The prompt may include details about the employee's preferences and characteristics. The interface displays the generated images in a gallery format, allowing users to preview and download them.

**Result**

![image](https://github.com/bittu5555/Personalized-Greetings-card-generator/assets/106305917/d6adfd6f-cc61-4a8f-971d-af91543c4cdb)
