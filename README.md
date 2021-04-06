# Building Interpretable Artificial Intelligence (AI) for Digital Pathology 


Deep learning algorithms may hide inherent risks such as the codification of biases, weak accountability and bare transparency of the decision-making. Giving little insights about their final output, deep models are perceived by clinicians as black-boxes. 
Clinicians, on their side, are the sole people legally responsible and accountable for the diagnoses and treatment decisions. 
Providing justifications for automated predictions may have a positive impact of computer aided diagosis, for example, by increasing the uptake of automated support within the decision making process.

This repository is created with the purpose of showcasing multiple ways in which developers may interpret automated decision making for digital pathology. The repository provides the necessary material for the anonymous workshop at the Applied Machine Learning Days of EPFL 2021. 

#### The problem

You have a deep learning model, may it be a Convolutional Neural Network (CNN) or a graph-netork. 
Your model works on high magnification croppings of histopathology input images, also called patches or tiles. 
The main task is the classification of patches containing evidence of tumor from those without. 
This is modeled as a binary classification task with one output node and a logistic regression activation function, where 1 corresponds to the "tumor" class and 0 to the non-tumor class. 

Common theme:
\li histopathology image input: you may use any of your histopathology datasets, or public data collections
\li continuous or categorical output: a single node output is used for demostration purposes. Similar applications can be derived for multiple node outputs, e.g. multi-class classification tasks. 

#### Part 1: Interpreting 2D CNNs 

This part focuses on understanding the decision process on ConvNets with:
\li feature and 
\li concept attribution

You will work on the implementation of Class Activation Mapping as an example of  heatmaps of salient input pixels. 
Regression Concept Vectors will be applied to generate complementary explanations in terms of clinically relevant measures such as nuclei area and appearance. 

#### Part 2: Learning biologica-entities by cell graphs 

Learning at the biological-entity level: cell graph, graph neural networks & explainability  
Graph Neural Networks will be explained together with their application to cell graphs, showing how they can directly incorporate a higher level of transparency in terms of entity importance, which can be interpreted by graph-pruning. 
