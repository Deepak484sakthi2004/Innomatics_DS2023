# Laptop Price Prediction

## Overview

Welcome to the Laptop Price Prediction project! This project aims to predict the prices of laptops based on various features. Whether you're a tech enthusiast or a consumer looking for the best value, this tool can help you estimate the price of a laptop based on its specifications.

## Table of Contents

- [Dataset](#dataset)
- [Features](#features)
- [Data Preprocessing](#data-preprocessing)
- [Model Training](#model-training)
- [Usage](#usage)
- [Evaluation](#evaluation)

## Dataset

The dataset used for this project includes information about various laptops, such as brand, processor type, RAM size, storage capacity, graphics card, and more. The dataset is available in the `data` folder.

## Features

The features used for predicting laptop prices include:

- Brand
- Processor Type
- RAM Size
- Storage Capacity
- Graphics Card
- Screen Size
- Operating System
- etc.

## Data Preprocessing

Before training the model, the dataset undergoes preprocessing to handle missing values, encode categorical variables, and scale numerical features. The preprocessing steps can be found in the `data_preprocessing.ipynb` notebook.

## Model Training

The machine learning model used for laptop price prediction is trained using a regression algorithm. The training script and model details are available in the `train_model.ipynb` notebook.

## Usage

To predict the price of a laptop using the trained model:

1. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
