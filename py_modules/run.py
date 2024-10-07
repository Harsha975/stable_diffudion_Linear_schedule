import model_loader
import pipeline
from PIL import Image
from pathlib import Path
from transformers import CLIPTokenizer
import torch
import numpy as np
import matplotlib.pyplot as plt

# Device setup
DEVICE = "cpu"
ALLOW_CUDA = True  # Set to True to allow CUDA
ALLOW_MPS = False

if torch.cuda.is_available() and ALLOW_CUDA:
    DEVICE = "cuda"
elif (torch.has_mps or torch.backends.mps.is_available()) and ALLOW_MPS:
    DEVICE = "mps"
print(f"Using device: {DEVICE}")

# Load tokenizer and model
tokenizer = CLIPTokenizer("/content/Stable_diffusion/vocab.json", merges_file="/content/Stable_diffusion/merges.txt")
model_file = "/content/Stable_diffusion/v1-5-pruned-emaonly.ckpt"
models = model_loader.preload_models_from_standard_weights(model_file, DEVICE)

# Text to Image settings
prompt = "A cat stretching on the floor, highly detailed, ultra sharp, cinematic, 100mm lens, 8k resolution."
uncond_prompt = ""  # Negative prompt
do_cfg = True
cfg_scale = 8  # Config scale

# Image to Image settings
input_image = None
strength = 0.9  # Strength for image to image generation

# Sampler settings
sampler = "ddpm"
num_inference_steps = 50
seed = 42

# Generate the image
output_image = pipeline.generate(
    prompt=prompt,
    uncond_prompt=uncond_prompt,
    input_image=input_image,
    strength=strength,
    do_cfg=do_cfg,
    cfg_scale=cfg_scale,
    sampler_name=sampler,
    n_inference_steps=num_inference_steps,
    seed=seed,
    models=models,
    device=DEVICE,
    idle_device="cpu",
    tokenizer=tokenizer,
)

# Convert the output_image tensor into a format suitable for saving
if isinstance(output_image, torch.Tensor):
    output_image = output_image.cpu().detach().numpy()

# Debugging: Print the shape and pixel value range
print(f"Image shape: {output_image.shape}")
print(f"Min pixel value: {output_image.min()}, Max pixel value: {output_image.max()}")

# Ensure output_image is a NumPy array and in the correct format
output_image = np.clip(output_image, 0, 255).astype(np.uint8)  # Clip values and convert to uint8

# If the output image is in (C, H, W) format, transpose to (H, W, C)
if len(output_image.shape) == 3 and output_image.shape[0] in [3, 4]:  # Check if it's channel-first
    output_image = np.transpose(output_image, (1, 2, 0))  # Convert from (C, H, W) to (H, W, C)

### Save the image as a JPG file ###
output_image_pil = Image.fromarray(output_image)  # Convert NumPy array to PIL Image

save_path = "/content/generated_image.jpg"  # Define the path to save the image
output_image_pil.save(save_path, "JPEG")  # Save the image as a JPG

print(f"Image saved at {save_path}")
