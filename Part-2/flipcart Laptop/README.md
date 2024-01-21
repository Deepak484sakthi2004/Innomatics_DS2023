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

For detailed information about the dataset, please refer to the [Dataset Information](./Flipcart laptop.docx) file in the repository.


## Features

1. **MRP (Maximum Retail Price):**
   - Description: The maximum retail price of the laptop.

2. **Company:**
   - Description: The company or brand of the laptop.

3. **Processor:**
   - Description: The type or model of the laptop's processor.

4. **CPU:**
   - Description: The central processing unit (CPU) information for the laptop.

5. **OS (Operating System):**
   - Description: The operating system installed on the laptop.

6. **RAM_size:**
   - Description: The size of Random Access Memory (RAM) in the laptop.

7. **RAM_type:**
   - Description: The type or category of RAM used in the laptop.

8. **Memory:**
   - Description: The overall memory capacity of the laptop.

9. **Memory_chips:**
   - Description: Information about the memory chips used in the laptop.

## Usage

- This dataset can be used for machine learning tasks related to predicting laptop prices.
- Preprocess the data, handle categorical variables, and perform feature scaling before training a predictive model.












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
