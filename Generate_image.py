from diffusers import StableDiffusionPipeline
import torch
from PIL import Image

# StableDiffusionXLPipeline example
pipe_xl = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
pipe_xl.to("cuda")

prompt_xl = "generate a greeting card for a person whose likes to visit mountain in spring season and loves to play cricket" # Your prompt here
neg_prompt_xl = "(worst quality, low quality, illustration, 3d, 2d, painting, cartoons, sketch)" # Negative prompt here
imagel = pipe_xl(prompt=prompt_xl, negative_prompt=neg_prompt_xl).images[0]
imagel = imagel.resize((300, 300))  # Resize the image
imagel.save("imagel.png")

