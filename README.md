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

## Expected Output

Once the model is successfully executed, it will generate high-quality images based on Stable Diffusion.

Example output:

- Model starts training/inference using the provided weights.
- Images are generated and saved in the output directory.
- Log messages indicating progress, such as:
  ```
  [INFO] Loading pre-trained weights...
  [INFO] Running inference...
  [INFO] Image saved to output/generated_image.png
  ```

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
