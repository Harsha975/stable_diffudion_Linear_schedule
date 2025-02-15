import model_loader
import pipeline
from PIL import Image
from transformers import CLIPTokenizer
import torch
import numpy as np

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
prompt = input("Enter your prompt: ")
uncond_prompt = ""  # Negative prompt
do_cfg = True
cfg_scale = 8  # Config scale

# Sampler settings
sampler = "ddpm"
num_inference_steps = 50
seed = 42

# Generate the image
output_image = pipeline.generate(
    prompt=prompt,
    uncond_prompt=uncond_prompt,
    input_image=None,
    strength=0.9,  # Strength for image to image generation
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

img=Image.fromarray(output_image)

img.save("output.png")
