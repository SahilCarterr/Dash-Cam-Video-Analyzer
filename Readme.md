# Animal Detection Model

This repository contains code for a Python-based animal detection model using a pre-trained video classifier. The model can detect various animals in a given video.

## Getting Started

To use this code, follow these instructions:

1. Clone this repository to your local machine or download the code files.
2. Ensure you have Python installed on your system.
3. Install the required dependencies using pip:

```bash
  pip install pytorch
  pip install pytorchvideo
  pip install gradio
```
4. Download the pre-trained model weights and class names file by running `wget https://dl.fbaipublicfiles.com/pyslowfast/dataset/class_names/kinetics_classnames.json`.
5. Open the provided Jupyter notebook (`animal_model_with_interface.ipynb`) in your preferred environment.
## Usage

To use the model:

1. Instantiate the `VideoClassifier` class provided in the notebook.
2. Call the `classify_video()` method, passing the path to the video file you want to analyze.
3. The method returns a dictionary indicating whether any animals were found in the video.

Example usage:
```python
# Instantiate your VideoClassifier
classifier = VideoClassifier()

# Call the classify_video method with the path to your video
result = classifier.classify_video("path/to/your/video.mp4")

# Print the result
print(result)
```
## Gradio Interface
Alternatively, you can use the Gradio interface for easy interaction with the model. The notebook provides instructions and code snippets for setting up and launching the interface.
## License

This code is provided under the [MIT License](https://opensource.org/license/mit). Feel free to modify and distribute it as needed.