import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")

st.title("📊 E-Commerce Customer Dashboard")

# Load data
df = pd.read_csv("data/raw/data.csv")

# Clean columns
df.columns = df.columns.str.strip().str.replace(" ", "_")

# Rename columns
df = df.rename(columns={
    "Say_for_example_,_a_similar_product_with_similar_features_is_being_sold_at_half_the_price_by_an_unknown_seller_as_compared_to_a_branded_product._Would_you_purchase_that_product?_or_Simply_Do_you_prefer_cost_over_brands?": "Prefer_Cheap_Product",
    
    "On_a_scale_of_1_to_5_,_how_often_do_you_shop_in_the_selected_product_category_monthly?": "Shopping_Frequency"
})

# ------------------ SIDEBAR ------------------
st.sidebar.header("🔎 Filters")

gender = st.sidebar.selectbox("Gender", ["All"] + list(df["Gender"].unique()))
state = st.sidebar.selectbox("State", ["All"] + list(df["State"].unique()))

# Apply filters
if gender != "All":
    df = df[df["Gender"] == gender]

if state != "All":
    df = df[df["State"] == state]

# ------------------ KPIs ------------------
st.subheader("📌 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("👥 Total Users", len(df))
col2.metric("🛍️ Top Category", df["Product_Category"].mode()[0])
col3.metric("💰 Top Spend Range", df["Avg_Spend"].mode()[0])

# ------------------ CHARTS ------------------

# Row 1
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Product Category")
    fig1, ax1 = plt.subplots()
    sns.countplot(y="Product_Category", data=df, ax=ax1)
    st.pyplot(fig1)

with col2:
    st.subheader("💰 Spending Distribution")
    fig2, ax2 = plt.subplots()
    sns.countplot(x="Avg_Spend", data=df, ax=ax2)
    plt.xticks(rotation=45)
    st.pyplot(fig2)

# Row 2
col3, col4 = st.columns(2)

with col3:
    st.subheader("🛒 Shopping Frequency")
    fig3, ax3 = plt.subplots()
    sns.countplot(x="Shopping_Frequency", data=df, ax=ax3)
    st.pyplot(fig3)

with col4:
    st.subheader("🏷️ Brand vs Cheap")
    fig4, ax4 = plt.subplots()
    sns.countplot(x="Prefer_Cheap_Product", data=df, ax=ax4)
    st.pyplot(fig4)