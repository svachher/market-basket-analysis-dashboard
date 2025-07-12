import streamlit as st
import pandas as pd
import plotly.express as px

# Setup
st.set_page_config(layout="wide", page_title="🛍️ Retail Market Basket Analytics", page_icon="🛍️")
st.markdown("<style>body { background-color: #0E1117; color: white; }</style>", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    rules = pd.read_csv("rules.csv")
    top_items = pd.read_csv("top_items.csv", names=["item", "support"])
    freq = pd.read_csv("frequent_itemsets.csv")
    return rules, top_items, freq

rules, top_items, freq = load_data()

st.markdown("""
<h1 style='font-size: 48px; font-weight: 800;'>🛍️ Retail Market Basket Analytics Dashboard</h1>

### 📊 Project Overview
This project leverages <b>Association Rule Mining</b> to uncover frequently co-purchased product combinations using real-world transaction data.  
We use the open-source <b>Groceries dataset</b> from the <a href="http://rasbt.github.io/mlxtend/user_guide/frequent_patterns/apriori/" target="_blank">MLxtend library</a>, which contains <b>9,835 market basket transactions</b> collected from a German retailer.

---

### 💡 Goal  
Help businesses improve <b>product placement</b>, <b>bundling</b>, and <b>promotions</b> by identifying high-affinity product combinations based on real purchasing patterns.

---

### 🧪 Tech Stack  
- 🐍 <b>Python</b> for data processing  
- 🧮 <b>Pandas</b> for preprocessing  
- 📊 <b>MLxtend</b> for Apriori & rule mining  
- 📈 <b>Plotly</b> for interactive visualizations  
- 🌐 <b>Streamlit</b> for dashboard deployment  

---



### 📌 Dashboard Enables You To:
- 📦 <b>Visualize</b> top-selling items  
- 🤝 <b>Identify</b> product pairings with strong associations  
- 🎚️ <b>Filter</b> product rules using lift and confidence  
- 🧠 <b>Extract insights</b> from real customer behavior
""", unsafe_allow_html=True)


# ----------------- Top 10 Items Bar Chart -----------------

st.subheader("📦 Top 10 Most Frequently Bought Items")

fig1 = px.bar(
    top_items.head(10),
    x='support', y='item',
    orientation='h',
    color='item',
    color_discrete_sequence=px.colors.sequential.Viridis,
    title="Most Frequently Purchased Products"
)
fig1.update_layout(yaxis=dict(autorange="reversed"))
st.plotly_chart(fig1, use_container_width=True)

st.markdown("🔍 **Insight:** Products like **Whole Milk**, **Other Vegetables**, and **Yogurt** top the charts, suggesting wide and frequent usage across customers.")

# ----------------- Rule Strength Scatter Plot -----------------

st.subheader("📈 Confidence vs Support (Bubble Size = Lift)")

fig2 = px.scatter(
    rules,
    x='support', y='confidence',
    size='lift', color='lift',
    hover_data=['antecedents', 'consequents'],
    color_continuous_scale='viridis',
    title="Strength of Association Rules"
)
st.plotly_chart(fig2, use_container_width=True)

st.markdown("🔍 **Insight:** Rules with high confidence and lift indicate strong product affinity — ideal for bundling or promotions.")

# ----------------- Rule Filters with Explanation -----------------

st.subheader("🎛️ Explore Product Rules with Filters")

st.markdown("""
Use the sliders below to **filter association rules**:

- 📘 **Confidence**: How often items on the left lead to the ones on the right  
  *E.g. 0.7 → 70% of people who buy item A also buy item B*

- 🎯 **Lift**: Measures the strength of the rule over random chance  
  *Lift > 1 → meaningful rule, Lift > 2 → very strong rule*
""")

min_conf = st.slider("Minimum Confidence", 0.0, 1.0, 0.3,
                     help="How reliably item A predicts item B (e.g. 0.7 = 70%)")
min_lift = st.slider("Minimum Lift", 1.0, 5.0, 2.0,
                     help="Lift > 1 means better than random; higher is stronger.")

filtered = rules[(rules['confidence'] >= min_conf) & (rules['lift'] >= min_lift)].copy()
filtered['antecedents'] = filtered['antecedents'].apply(lambda x: ', '.join(eval(x) if isinstance(x, str) else x))
filtered['consequents'] = filtered['consequents'].apply(lambda x: ', '.join(eval(x) if isinstance(x, str) else x))

st.markdown(f"🔎 Showing rules with **Confidence ≥ {min_conf:.2f}** and **Lift ≥ {min_lift:.2f}**")

st.dataframe(
    filtered[['antecedents', 'consequents', 'support', 'confidence', 'lift']].sort_values(by='lift', ascending=False),
    use_container_width=True
)

st.markdown("💡 **Tip:** Try setting Lift > 2 and Confidence > 0.4 to find tightly linked product pairs.")

# ----------------- Frequent Itemsets -----------------

st.subheader("📊 Frequent Itemsets (Support ≥ 3%)")

freq_filtered = freq[freq['support'] >= 0.03].sort_values(by='support', ascending=False).head(15)
freq_filtered['itemsets'] = freq_filtered['itemsets'].apply(lambda x: ', '.join(eval(x) if isinstance(x, str) else x))

fig3 = px.bar(
    freq_filtered,
    x='support', y='itemsets',
    orientation='h',
    title="Frequently Bought Itemsets",
    color='support',
    color_continuous_scale='blues'
)
fig3.update_layout(yaxis=dict(autorange="reversed"))
st.plotly_chart(fig3, use_container_width=True)

st.markdown("🔍 **Insight:** Combinations like **'Whole Milk & Other Vegetables'** occur frequently, suggesting key anchor products.")

# ----------------- Final Takeaways -----------------

st.markdown("---")
st.subheader("📌 Summary & Business Insights")

st.markdown("""
- 🥛 **Whole milk** acts as a top driver and occurs in multiple rules.
- 🥦 Items like **root vegetables** and **yogurt** often appear alongside other staples.
- 🔗 Strong lifts suggest customers often buy these items together more than by chance.

---

### 📊 Data Analytics Concepts Used:
- Apriori Algorithm (Frequent Pattern Mining)
- Association Rule Metrics: Support, Confidence, Lift
- Interactive Filtering via Streamlit
- Business Interpretation of Item Affinities
- Visual Analytics with Plotly
""")

# Footer
st.markdown("---")
st.markdown("""
🔗 [**Click here to view the detailed analytics notebook**](https://github.com/your-username/market-basket-dashboard/blob/main/Market_Basket_Analysis.ipynb)
""")

st.markdown("🚀 Project by **Sahil Vachher** | Dataset: [Groceries - MLxtend](http://rasbt.github.io/mlxtend/user_guide/frequent_patterns/apriori/) | Built with Streamlit + Plotly")
