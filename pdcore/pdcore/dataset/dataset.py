import pandas as pd

# DATASET 1
splits = {
    "train": "symptom-disease-train-dataset.csv",
    "test": "symptom-disease-test-dataset.csv",
}
df = pd.read_csv(
    "hf://datasets/duxprajapati/symptom-disease-dataset/" + splits["train"]
)

# DATASET 2
df_train = pd.read_csv(
    "https://raw.githubusercontent.com/anujdutt9/Disease-Prediction-from-Symptoms/refs/heads/master/dataset/training_data.csv"
)
df_test = pd.read_csv(
    "https://raw.githubusercontent.com/anujdutt9/Disease-Prediction-from-Symptoms/refs/heads/master/dataset/test_data.csv"
)

# DATASET 3
df = pd.read_csv("hf://datasets/QuyenAnhDE/Diseases_Symptoms/Diseases_Symptoms.csv")

# DATASET 4
