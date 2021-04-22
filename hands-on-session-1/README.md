
![Logo of the project](https://introinterpretableai.files.wordpress.com/2021/03/cropped-screenshot-2021-03-22-at-17.11.49.png)

# Introduction to AI Interpretability 
> Hands-on-session #1. 
> 
> Presented by: Mara Graziani (PhD student at HES-SO Valais and University of Geneva)
>

The notebooks in this folder will help you to apply Gradient-weighted Class Activation Mapping (Grad-CAM) on you CNN classifier. 
This explainability technique generates a heatmap the relevant input features. 
You will also understand how high-level concepts are used in the decision making in the notebook about concept attribution. The examples in this notebook will guide you to apply Regression Concept Vectors to explain automated decision-making in terms of high-level concepts. 
Both notebooks are applied on the task of classifying tumor from non-tumor in breast histopathology images at high-magnification (40x). 

## Installing / Getting started

The notebooks can be directly run in the Colab workspace, so no installation / or setup of virtual environments is needed for the workshop. 
You are strongly encouraged, however, to get the set up and datasets ready before starting the workshop. The notebook data_setup.ipynb will drive you through the data preparation steps. 
If you encounter any isses please let us know. 

## Developing

You can also directly clone the folder to your computer to start developing
the project further:

```shell
git clone https://github.com/maragraziani/interpretAI_DigiPath
```

## Features

* Generate CAM heatmaps for imagenet-pretrained model
* Load your own model and weights to generate CAM
* Apply latest research to interpret your model with Regression Concept Vectors

## Links

Some useful links for more information about this hands-on session:

- Funding Project homepage: https://www.ai4media.eu/
- Repository: https://github.com/maragraziani/interpretAI_DigiPath/
- Issue tracker: https://github.com/maragraziani/interpretAI_DigiPath/issues
- 
- Related projects:
  - Your other project: https://introinterpretableai.wordpress.com/
  - Someone else's project: https://github.com/maragraziani/rcvtool/

## Licensing
The code in this project is licensed under MIT license.
