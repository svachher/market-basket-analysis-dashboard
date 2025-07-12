# 🛍️ Retail Market Basket Analytics Dashboard

[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-ff4b4b?logo=streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Deployment-LIVE-brightgreen?style=flat&logo=streamlit)](https://market-basket-analysis-dashboard-mkjkh2dessyph4qxcb4lr8.streamlit.app/)

---

## 📊 Project Overview

This interactive dashboard uncovers **frequently co-purchased product combinations** using **Association Rule Mining** techniques.  
We analyze customer shopping patterns using a real-world retail dataset of **9,835 transactions** from a German grocery store.

---

### 🎯 Goal

Help retail businesses optimize:
- 🛍️ **Product bundling**  
- 🧠 **Shelf placement strategies**  
- 💸 **Cross-selling & promotions**

by identifying products that are often bought together.

---

## 🧪 Tech Stack

| Layer         | Tools Used                     |
|---------------|--------------------------------|
| 📦 Data        | MLxtend Groceries Dataset      |
| 📊 Analytics   | Apriori Algorithm, Association Rules |
| 🧮 Processing  | Pandas, MLxtend                |
| 📈 Visuals     | Plotly                         |
| 🖥️ Dashboard   | Streamlit                      |
| ☁️ Hosting     | Streamlit Cloud                |

---

## 🔍 Analytical Workflow

1. 🧹 **Data Preprocessing** – Transaction encoding into binary matrix  
2. 📊 **Frequent Itemset Mining** – Using Apriori algorithm  
3. 🤝 **Association Rule Generation** – Based on `support`, `confidence`, `lift`  
4. 🎛️ **Interactive Filtering** – Explore strongest product rules  
5. 💬 **Insight Extraction** – Visual and business interpretation

---

## 📌 Key Features

✅ Visualize top-selling items  
✅ Mine strong product associations  
✅ Interactively filter rules (lift, confidence)  
✅ Explain rule metrics in simple terms  
✅ Mobile & web-friendly dashboard interface

---

## 🔗 Live Links

- 🚀 **Live Dashboard** → [market-basket-analysis-dashboard.streamlit.app](https://market-basket-analysis-dashboard-mkjkh2dessyph4qxcb4lr8.streamlit.app/)
- 📄 **Dashboard PDF Preview** → [Click to view](dashboard_preview.pdf)
- 📓 **Analytics Notebook (Colab)** → *[Coming soon]*  
- 📂 **Dataset Source** → [MLxtend Groceries Dataset](http://rasbt.github.io/mlxtend/user_guide/frequent_patterns/apriori/)

---

## 🖼️ Dashboard Preview

![Dashboard Preview](images/dashboard_preview.png) <!-- optional: add a PNG here -->

---

## 💻 Run Locally

```bash
# 1. Clone this repository
git clone https://github.com/your-username/market-basket-dashboard.git
cd market-basket-dashboard

# 2. (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run app.py
