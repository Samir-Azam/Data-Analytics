import pandas as pd

def clean_data():
    df = pd.read_csv("data/raw/raw.csv")

    df = df.drop(columns=[
        "Which product among Electronics do you shop very often?",
        "Which product among Fashion do you shop very often?",
        "Which product among Clothing do you shop very often?",
        "Which OTT subscriptions do you use the most?",
        "Which type of Books do you buy the most?"
    ])

    df = df.rename(columns={
        "Current State or Union Territory": "State",
        "Which Tier does your city belong to?": "City_Tier",
        "Marital Status": "Marital_Status",
        "What is your financial status?": "Financial_Status",
        "What is the Product Category that you shop very frequently?": "Product_Category",
        "How much time do you spend while picking the right product to buy?": "Decision_Time",
        "What is the average money that you spend while shopping the above items in one time?": "Avg_Spend"
    })

    df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors='coerce')
    df["City"] = df["City"].fillna("Unknown")

    df = df.drop_duplicates()

    df.to_csv("data/processed/cleaned_data.csv", index=False)

    print("Data cleaned successfully!")

if __name__ == "__main__":
    clean_data()