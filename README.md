# 🛒 Retail Market Basket Analytics Dashboard

[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-ff4b4b?logo=streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)
[![Colab Notebook](https://img.shields.io/badge/View%20Notebook-IPYNB-yellow?logo=jupyter)](Market_Basket_Analysis.ipynb)
[![View Dashboard](https://img.shields.io/badge/Live%20Dashboard-Open-green?logo=streamlit)](https://market-basket-analysis-dashboard-mkjkh2dessyph4qxcb4lr8.streamlit.app/)

---

## 📊 Project Overview

This interactive dashboard uses **Association Rule Mining** to uncover frequently co-purchased product combinations using real-world retail data.  
We use the **Groceries dataset** from the [MLxtend library](http://rasbt.github.io/mlxtend/user_guide/frequent_patterns/apriori/), containing **9,835 transactions** collected from a German grocery store.

---

### 🎯 Goal

Help retail businesses:
- 🛍️ Optimize product bundling  
- 🧠 Improve shelf placement  
- 💸 Launch smarter promotions  
by identifying hidden patterns in customer purchasing behavior.

---

## 🧪 Tech Stack

| Layer         | Tools Used                           |
|---------------|--------------------------------------|
| 📦 Data        | MLxtend Groceries Dataset            |
| 📊 Analytics   | Apriori Algorithm, Association Rules |
| 🧮 Processing  | Pandas, MLxtend                      |
| 📈 Visuals     | Plotly                               |
| 🖥️ Dashboard   | Streamlit                            |
| ☁️ Hosting     | Streamlit Cloud                      |

---

## 🔍 Analytical Workflow

1. **Preprocessing**: Convert transaction records into a binary matrix  
2. **Apriori Algorithm**: Generate frequent itemsets  
3. **Association Rules**: Calculate `support`, `confidence`, and `lift`  
4. **Interactive Filtering**: Explore strongest rules with sliders  
5. **Insight Extraction**: Visual & business interpretations

---

## 📂 Key Resources

- 🚀 **Live Dashboard**: [Launch App](https://market-basket-analysis-dashboard-mkjkh2dessyph4qxcb4lr8.streamlit.app/)
- 📄 **Dashboard PDF Preview**: [market_basket_analysis dashboard.pdf](market_basket_analysis dashboard.pdf)
- 📓 **Colab Notebook**: [Market_Basket_Analysis.ipynb](makrket_basket_analysis.ipynb)
- 📊 **Dataset Source**: [MLxtend Groceries Dataset](http://rasbt.github.io/mlxtend/user_guide/frequent_patterns/apriori/)

---

## 🛠️ Local Setup Instructions

```bash
# 1. Clone this repository
git clone https://github.com/your-username/market-basket-dashboard.git
cd market-basket-dashboard

# 2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

# 3. Install required libraries
pip install -r requirements.txt

# 4. Launch the app
streamlit run app.py

---

---

## 💡 Key Features

✅ Visualize top-purchased products  
✅ Mine strong product pairings using `Lift`, `Support`, `Confidence`  
✅ Intuitive filtering with live sliders  
✅ Business insights below each graph  
✅ Fully hosted web app for easy sharing  
✅ Well-documented analysis in notebook form

---

## 🤝 Acknowledgements

- Dataset from: [MLxtend - Groceries Example](http://rasbt.github.io/mlxtend/user_guide/frequent_patterns/apriori/)
- Built using: Streamlit, Plotly, Pandas, MLxtend

---

## 🙋‍♂️ Author

**Sahil Vachher**  
B.Tech (Mathematics & Computing), Delhi Technological University  
📫 [LinkedIn](https://www.linkedin.com/in/sahilvachher) • ✉️ [sahilvachher@gmail.com](mailto:sahilvachher@gmail.com)

---

