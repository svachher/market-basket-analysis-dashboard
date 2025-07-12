# 🛒 Retail Market Basket Analytics Dashboard

A live interactive dashboard to uncover frequently co-purchased product combinations using association rule mining — helping retailers optimize product placement, bundling, and promotions.

🔗 **Live Dashboard**: [Streamlit App](https://market-basket-analysis-dashboard-mkjkh2dessyph4qxcb4lr8.streamlit.app/)  
📄 **Dashboard PDF Preview**: [market_basket_analysis dashboard.pdf](market_basket_analysis%20dashboard.pdf)
📓 **Colab Notebook**: [Market Basket Analysis - Google Colab](https://colab.research.google.com/drive/1C3dyi_cexPW968BnMD3j6nTvIWPqNZ84?usp=sharing)

---

## 📊 Project Overview

This project leverages **Association Rule Mining** to uncover frequently co-purchased product combinations from real retail data.  
We use the open-source **Groceries dataset** from the [MLxtend library](http://rasbt.github.io/mlxtend/user_guide/frequent_patterns/apriori/), containing **9,835 transactions** from a German retail store.

### 🔧 Tech Stack & Workflow

- **Data Source**: MLxtend's Groceries dataset
- **Preprocessing**: Transaction encoding using `TransactionEncoder`
- **Analytics**: Association Rules using `Apriori` + `MLxtend`
- **Dashboarding**: Built with **Streamlit** and **Plotly**
- **Deployment**: Hosted on [Streamlit Cloud](https://streamlit.io/cloud)
- **Exploration**: Analysis notebook on Google Colab

---

## 🚀 Dashboard Features

✅ Visualize top-selling items  
✅ Discover product pairings with strong `Lift`, `Confidence`, and `Support`  
✅ Filter rules interactively with sliders  
✅ Interpret graph-level insights directly on the dashboard  
✅ Export and share as PDF or Web app  

---

## 📌 Key Insights

- Strong rules often have **moderate support and high lift** (e.g., `root vegetables` → `whole milk`)  
- Bundles containing **"whole milk", "yogurt", "vegetables"** frequently co-occur  
- High lift > 2 shows **niche but actionable** product affinities

---

## 🤝 Acknowledgements

- **Dataset**: [MLxtend – Groceries Dataset](http://rasbt.github.io/mlxtend/user_guide/frequent_patterns/apriori/)  
- **Libraries**: Streamlit, Pandas, Plotly, MLxtend, Scikit-learn

---

## 👨‍💻 Author

**Sahil Vachher**  
B.Tech (Mathematics & Computing), Delhi Technological University  
🔗 [LinkedIn](https://www.linkedin.com/in/sahilvachher) • ✉️ [sahilvachher@gmail.com](mailto:sahilvachher@gmail.com)
