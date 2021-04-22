
![Logo of the project](https://www.ai4media.eu/wp-content/uploads/2021/04/Twitter_Building-Interpretable-AI-for-Digital-Pathology-1024x575.png)

**Presented by:**

- Mara Graziani
    - Pre-doc researcher with HES-SO Valais & UniGe
    - mara.graziani@hevs.ch


- Guillaume Jaume
    - Pre-doc researcher with EPFL & IBM Research 
    - gja@zurich.ibm.com  


- Pushpak Pati 
    - Pre-doc researcher with ETH & IBM Research
    - pus@zurich.ibm.com
    
Welcome to the AMLD 2021 workshop about **Building Interpretable AI for Digital Pathology**. This hands-on session is created with the purpose of showcasing multiple ways in which developers may interpret automated decision making for digital pathology. 

<!---
Deep learning algorithms may hide inherent risks such as the codification of biases, weak accountability and bare transparency of the decision-making. Giving little insights about their final output, deep models are perceived by clinicians as black-boxes. 
Clinicians, on their side, are the sole people legally responsible and accountable for the diagnoses and treatment decisions. 
Providing justifications for automated predictions may have a positive impact of computer aided diagosis, for example, by increasing the uptake of automated support within the decision making process.
-->

## Schedule 

The workshop will take place on the 27th of April from 9:00 to 12:00 CET. 

| Time      | Title                                | Presenter              |                  
|-----------|--------------------------------------|------------------------|
| 9:00-9:05 | Welcome                                | Guillaume Jaume, Pushpak Pati|
| 9:05-9:25 | Introduction to Digital Pathology      | Prof. Dr. Inti Zlobec  |
| 9:25-9:45 | Introduction to Interpretability       | Mara Graziani          |
| 9:45-9:55 | Break 1                                | -                      |
| 9:55-10:35 | Hands-on session 1: CNNs & Concept Attribution | Mara Graziani |
| 10:35-10:45 | Break 2                              | -                      |
| 10:45-11:55 | Hands-on session 2: Graph-based interpretability | Guillaume Jaume, Pushpak Pati |
| 11:55-12:00 | Closing remarks                      | -                      |

## What to do before the workshop: 

The participants need to bring their own laptop with basic development setup. We recommend testing the following steps before starting the workshop:

- Cloning the repository 

```
>> git clone https://github.com/maragraziani/interpretAI_DigiPath.git && cd interpretAI_DigiPath
```

- Launch Jupyter Notebook 

```
>> jupyter notebook
```

- Test opening one of the notebooks in Colab, e.g., [hands-on-session-1/feature_attribution_demo.ipynb](https://github.com/maragraziani/interpretAI_DigiPath/blob/main/hands-on-session-1/feature_attribution_demo.ipynb).


## Content

Deep learning algorithms may hide inherent risks such as the codification of biases, weak accountability and bare transparency of the decision-making. Giving little insights about their final output, deep models are perceived by clinicians as black-boxes. 
Clinicians, on their side, are the sole people legally responsible and accountable for the diagnoses and treatment decisions. 
Providing justifications for automated predictions may have a positive impact of computer aided diagosis, for example, by increasing the uptake of automated support within the decision making process.

<!---
You have a deep learning model, may it be a Convolutional Neural Network (CNN) or a graph-network. 
Your model works on high magnification croppings of histopathology input images, also called patches or tiles. 
The main task is the classification of patches containing evidence of tumor from those without. 
This is modeled as a binary classification task with one output node and a logistic regression activation function, where 1 corresponds to the "tumor" class and 0 to the non-tumor class. 

Common theme:
<li> histopathology image input: you may use any of your histopathology datasets, or public data collections 
<li> continuous or categorical output: a single node output is used for demonstration purposes. Similar applications can be derived for multiple node outputs, e.g. multi-class classification tasks. 
-->

### Part 1: Interpreting 2D CNNs 

This part focuses on understanding the decision process on ConvNets with:
* feature attribution: Class Activation Mapping (CAM) and its Gradient-weighted version 
* concept attribution: Regression Concept Vectors (RCV)

You will work on the implementation of Gradient-weighted Class Activation Mapping (Grad-CAM) as an example of feature attribution.
RCVs will be applied to generate complementary explanations in terms of clinically relevant measures such as nuclei area and appearance. 

The notebooks and instructions for this part are in the folder 2DCNNs. 

### Part 2: Explainable Graph-based Representations in Digital Pathology

The second part of this tutorial will guide you to build **interpretable entity-based representations** of tissue regions. The motivation starts from the observation that cancer diagnosis and prognosis is driven by the distribution of histological entities, *e.g.,* cells, nuclei, tissue regions. A natural way to  characterize the tissue is to represent it as a set of interacting entities, *i.e.,* a graph. Unlike most of the deep learning techniques operating at pixel-level, the entity-based analysis preserves the notion of histopathological entities, which the pathologists can relate to and reason with. Thus, explainability of the entity-graph based methodologies can be interpreted by pathologists, which can potentially lead to build trust and adoption of AI in clinical practice. Notably, the produced explanations in the entity-space are better localized, and therefore better discernible.

  
## Reference papers


```
@article{graziani2020,
    title = "Concept attribution: Explaining {{CNN}} decisions to physicians",
    author = "Mara Graziani, Vincent Andrearczyk, Stephane Marchand-Maillet, Henning Müller"
    booktitle = "Computers in Biology and Medicine",
    pages = "103865",
    year = "2020",
    doi = "https://doi.org/10.1016/j.compbiomed.2020.103865"
}

@inproceedings{pati2021,
    title = "Hierarchical Graph Representations in Digital Pathology",
    author = "Pushpak Pati, Guillaume Jaume, Antonio Foncubierta, Florinda Feroce, Anna Maria Anniciello, Giosuè Scognamiglio, Nadia Brancati, Maryse Fiche, Estelle Dubruc, Daniel Riccio, Maurizio Di Bonito, Giuseppe De Pietro, Gerardo Botti, Jean-Philippe Thiran, Maria Frucci, Orcun Goksel, Maria Gabrani",
    booktitle = "arXiv",
    url = "https://arxiv.org/abs/2102.11057",
    year = "2021"
} 

@inproceedings{jaume2021,
    title = "Quantifying Explainers of Graph Neural Networks in Computational Pathology",
    author = "Guillaume Jaume, Pushpak Pati, Behzad Bozorgtabar, Antonio Foncubierta-Rodríguez, Florinda Feroce, Anna Maria Anniciello, Tilman Rau, Jean-Philippe Thiran, Maria Gabrani, Orcun Goksel",
    booktitle = "IEEE CVPR",
    url = "https://arxiv.org/abs/2011.12646",
    year = "2021"
} 
```
