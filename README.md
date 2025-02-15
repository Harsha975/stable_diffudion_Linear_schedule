# Stable Diffusion from Scratch

This project implements Stable Diffusion from scratch using pre-trained weights. The implementation is provided in a structured GitHub repository with necessary modules and dependencies.

## Installation & Setup

Follow these steps to set up and run the project in Google Colab.

### Clone the Repository

```bash
!git clone https://github.com/Harsha975/stable_diffudion_Linear_schedule.git
```

### Install Dependencies

#### Install gdown

```bash
!pip uninstall --yes gdown # After running this line, restart Colab runtime
!pip install gdown -U --no-cache-dir
```

#### Install PyTorch Lightning

```bash
!pip install pytorch_lightning -q
```

### Download Pre-trained Weights

```python
import gdown

url = 'https://drive.google.com/drive/folders/1nmtKx00HRayYlw3HrskMix3Q48uhW2ta?usp=sharing'
gdown.download_folder(url)
```

### Run the Code

```bash
cd /content/stable_diffudion_Linear_schedule/py_modules
!python run.py
```

## Running the Model

The script allows users to generate images using Stable Diffusion with customizable parameters.

### Steps:

1. Set up the device:
   - The script automatically selects CUDA, MPS, or CPU based on availability.

2. Load the tokenizer and model:
   - Uses `CLIPTokenizer` and loads the model from pre-trained weights.

3. Provide user inputs:
   - Prompt
   - Negative prompt (optional)
   - Classifier-Free Guidance (CFG) option
   - CFG scale (default: 8)
   - Sampler name (default: 'ddpm')
   - Number of inference steps (default: 50)
   - Random seed (default: 42)

4. Generate the image:
   ```python
   output_image = pipeline.generate(
       prompt=prompt,
       uncond_prompt=uncond_prompt,
       input_image=None,
       strength=0.9,
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
   ```

5. Save and display the output image:
   ```python
   img = Image.fromarray(output_image)
   img.save("output.png")
   print("Image saved as output.png")
   ```

## Expected Output

Once the model is successfully executed, it will generate high-quality images based on Stable Diffusion.

Example output:

- Model starts training/inference using the provided weights.
- User inputs are processed to generate the desired image.
- Images are generated and saved in the output directory.
- Log messages indicating progress, such as:
  ```
  [INFO] Using device: cuda
  [INFO] Loading pre-trained weights...
  [INFO] Running inference...
  [INFO] Image saved as output.png
  ```

### Example Input and Output

#### Example Input
```
Prompt: A futuristic cityscape at sunset
Negative Prompt: Blurry, low quality
CFG Scale: 8
Sampler: ddpm
Inference Steps: 50
Seed: 42
```

#### Example Output

![Generated Image](output.png)

## Repository Structure

```
stable_diffudion_Linear_schedule/
│── py_modules/
│   ├── run.py          # Main script to run Stable Diffusion
│   ├── model.py        # Model architecture
│   ├── utils.py        # Utility functions
│── README.md           # Project documentation
│── requirements.txt    # List of dependencies
```

## Notes

- Ensure you restart the Colab runtime after uninstalling `gdown` before proceeding.
- The pre-trained weights must be successfully downloaded before running the script.

## Author

[Harsha975](https://github.com/Harsha975)

