# Wine Quality Classification

A machine learning project that predicts wine quality using physicochemical properties of Portuguese "Vinho Verde" red wine.

## 📊 Dataset

The dataset contains 1,599 samples of red wine with 11 physicochemical features and 1 quality rating:

### Features:
1. **Fixed acidity**
2. **Volatile acidity** 
3. **Citric acid**
4. **Residual sugar**
5. **Chlorides**
6. **Free sulfur dioxide**
7. **Total sulfur dioxide**
8. **Density**
9. **pH**
10. **Sulphates**
11. **Alcohol**

### Target Variable:
- **Quality**: Score between 0-10 (converted to binary: Good ≥7, Bad <7)

## 🚀 Models Implemented

### 1. Random Forest Classifier
- **Test Accuracy**: 92.5%
- **Cross-validation Score**: 86.4% (±0.016)
- **Optimized with GridSearchCV**

### 2. Logistic Regression
- **Test Accuracy**: 89.4%
- **Cross-validation Score**: 87.0% (±0.019)
- **Optimized with GridSearchCV**

### 3. Decision Tree Classifier
- **Test Accuracy**: 90.3%
- **Cross-validation Score**: 79.8% (±0.060)

## 🔧 Key Features

- **Data Preprocessing**: Label binarization for quality classification
- **Feature Selection**: Top 5 most important features identified
- **Hyperparameter Optimization**: GridSearchCV for model tuning
- **Cross-validation**: 5-fold CV for robust evaluation
- **Visualization**: Correlation heatmaps and feature analysis

## 📈 Top 5 Most Important Features

1. **Alcohol** (17.7% importance)
2. **Sulphates** (11.7% importance)
3. **Volatile Acidity** (11.0% importance)
4. **Citric Acid** (9.7% importance)
5. **Density** (9.3% importance)

## 🛠️ Installation & Usage

### Prerequisites
```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

### Running the Code
```python
# Clone the repository
git clone https://github.com/beater35/ml-classification-wine-quality.git
cd ml-classification-wine-quality

# Load and run the Jupyter notebook
jupyter notebook classification_model_comparison_wine_quality.ipynb
```

### Making Predictions
```python
# Example prediction with top 5 features
input_data = [10.0, 0.47, 0.65, 0.0, 0.9946]  # [alcohol, sulphates, volatile_acidity, citric_acid, density]
prediction = final_rf_model.predict([input_data])

if prediction[0] == 1:
    print("Good Quality Wine")
else:
    print("Bad Quality Wine")
```

## 📊 Model Performance Summary

| Model | Test Accuracy | CV Score (Mean ± Std) |
|-------|---------------|----------------------|
| **Random Forest** | **92.5%** | **86.4% ± 1.6%** |
| Logistic Regression | 89.4% | 87.0% ± 1.9% |
| Decision Tree | 90.3% | 79.8% ± 6.0% |

## 🔍 Project Structure

```
wine-quality-classification/
├── classification_model_comparison_wine_quality.ipynb
└── README.md
```

## 📝 Methodology

1. **Data Exploration**: Statistical analysis and visualization
2. **Preprocessing**: Binary classification setup (Good/Bad quality)
3. **Model Training**: Three different algorithms tested
4. **Hyperparameter Tuning**: GridSearchCV optimization
5. **Feature Selection**: Importance-based feature ranking
6. **Model Evaluation**: Cross-validation and test accuracy

## 🎯 Results

The **Random Forest Classifier** achieved the best performance with 92.5% test accuracy after hyperparameter optimization and feature selection. The model successfully identifies wine quality based on physicochemical properties, with alcohol content being the most influential factor.

## 📚 References

- Dataset: [Kaggle – Wine Quality Dataset](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009)
