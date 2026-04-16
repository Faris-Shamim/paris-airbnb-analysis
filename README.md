# 🗼 Paris Airbnb Data Analysis & Interactive Dashboard

📌 End-to-end workflow: data cleaning, transformation, and interactive visualization

## 📊 Overview
This project analyzes Airbnb listings in Paris to uncover key pricing patterns, neighbourhood dynamics, and market trends.

Built using **Python (Pandas, Matplotlib)** and deployed as an **interactive Streamlit dashboard** for exploration.

---

## 🔍 What This Project Demonstrates
- Cleaning and transforming real-world datasets  
- Performing exploratory data analysis (EDA) to uncover patterns  
- Communicating insights through clear visualizations  
- Building an interactive dashboard using Streamlit  
---

## 🏗️ Project Structure

```
paris-airbnb/
├── data/                  # Raw datasets
├── src/
│   ├── analysis.py        # Data cleaning and analysis
│   ├── visuals.py         # Visualization functions
│   ├── main.py            # Execution script
│   └── dashboard.py       # Streamlit app
├── outputs/               # Generated charts and results
├── README.md
├── requirements.txt
└── .gitignore
```
---
## 🎯 Objectives
- Analyze pricing differences across neighbourhoods  
- Understand how property size affects price  
- Explore trends in reviews and listings  
---

## 🚀 Key Insights

- Central Paris listings command significantly higher prices → strong location premium  
- Entire homes dominate the high-price segment → preference for privacy in premium market  
- Reviews are concentrated in tourist-heavy areas → key demand zones  
- Host activity has increased over time → rising competition in the market 

---

## 📊 Dashboard Preview

### 📍 Neighbourhood Pricing
![Neighbourhood](outputs/neighbourhood.png)

### 📈 Trends Over Time
![Trends](outputs/trends.png)

### ⭐ Review Activity
![Reviews](outputs/reviews.png)

---

## 🧩 Features
- Neighbourhood price comparison  
- Accommodation type analysis  
- Temporal trends in pricing and host activity  
- Review pattern analysis  
- Interactive Streamlit dashboard  

---

## ⚙️ Tech Stack

* **Python** — Core programming language
* **Pandas** — Data manipulation and analysis
* **Matplotlib** — Data visualization
* **Streamlit** — Interactive dashboard development

---

## 📂 Dataset

The dataset contains Airbnb listings and reviews for Paris, including:

* Listing prices
* Neighbourhood information
* Accommodation size and type
* Host activity history
* Review dates and frequency

---

## ▶️ How to Run

1. Clone the repository:

   ```
   git clone <your-repo-link>
   cd paris-airbnb
   ```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Launch the dashboard:

   ```
   streamlit run src/dashboard.py
   ```

---

## 🔮 Future Improvements

* Build a machine learning model to predict listing prices
* Expand analysis to multiple cities
* Deploy the dashboard for public access

---

