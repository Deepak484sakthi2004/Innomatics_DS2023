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

For detailed information about the dataset, please refer to the [Dataset Information](./Flipcart%20laptop.docx) file in the repository.


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





## Trained Model

The machine learning model has been trained on the dataset and saved as a pickle (pkl) file.

- **Model File:** [laptop_price_prediction_model.pkl](./Model/pipe.pkl)

### Usage

To use the trained model in your Python code:

```python
import pickle

# Load the model
with open('Model/laptop_price_prediction_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Example prediction
sample_data = {
    'MRP': 1200,
    'Company': 'ExampleBrand',
    'Processor': 'i7',
    # Add other features here...
}

prediction = model.predict([sample_data])
print(f'Predicted Price: {prediction[0]}')
```

