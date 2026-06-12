import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(path):
    return pd.read_csv(path)

def encode_gender(df):
    df["Gender"] = df["Gender"].map({"Male": 1, "Female": 0})
    return df

def scale_features(df):
    scaler = StandardScaler()
    scaled_df = scaler.fit_transform(df)
    scaled_df = pd.DataFrame(scaled_df, columns=df.columns)
    return scaled_df, scaler

def preprocess(path):
    df = load_data(path)
    df = encode_gender(df)
    df_scaled, scaler = scale_features(df)
    return df, df_scaled, scaler
