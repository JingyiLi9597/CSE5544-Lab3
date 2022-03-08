import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import altair as alt




st.title("CSE 5544 lab3")
st.markdown("Author: Jingyi Li (li.9597)")

st.header("Display data")
df_data = pd.read_csv("https://raw.githubusercontent.com/JingyiLi9597/CSE5544lab3/main/ClimateDataNew.csv")
df_data


st.markdown("# Perspective 1: Ethical Perspective")
st.markdown("## Extended Blackbody Visualization")

data2 = df_data.drop(columns=['Non-OECD Economies'])
data2 = data2.set_index('Country\year')
data2 = data2.apply(pd.to_numeric, errors='coerce')

data2=np.log(data2)
fig2, ax2 = plt.subplots(figsize=(16, 7), dpi = 50)
ax2 = sns.heatmap(data2.T, linewidths=.5, cmap='inferno')

ax2.set_xlabel('country')
ylabel2 = ax2.set_ylabel('year')
xaxis2 = plt.xticks(rotation=90, ha='center', fontsize=8)
yaxis2 = plt.yticks(fontsize=8)
title2 = ax2.set_title('The heatmap to show the emissions of countries among years')
st.pyplot(fig2)

"I think this Extended Blackbody visualization is from an ethical perspective. The color range is from light yellow to dark red. The country with lighter color mains that its emission is greater. This visualization is easy to compare the emissions of each country. "
"From this visualization, it is easy to find out that China and United States have the highest emissions except all unions. Liechtenstein and Monaco have the lowest emissions."
"Also, it is clear to see that the data missed in which year and which country."


st.markdown("# Perspective 2: Unethical Perspective")
st.markdown("## Rainbow Visualization")

data = df_data.drop(columns=['Non-OECD Economies'])
data = data.set_index('Country\year')
data = data.apply(pd.to_numeric, errors='coerce')

fig, ax = plt.subplots(figsize=(16, 7), dpi = 50)
ax = sns.heatmap(data.T, linewidths=.5, cmap='rainbow')
ax2.set_xlabel('country')
xaxis = plt.xticks(rotation=0, ha='center', fontsize=8)
yaxis = plt.yticks(fontsize=8)
title = ax.set_title('The heatmap to show the emissions of countries among years')
st.pyplot(fig)

"I think this rainbow visualization is from an unethical perspective, because it is hard to compare the emissions of each country. Rainbow color is hard for people to find which color represents the big emssion. "
"For example, it is hard for most people to identify which emissions are greater in the countries with green and the countries with blue at the first time without seeing the label. "
"Additionally, the country names on x-axis overlap each other. People cannot read what countries are."
"Moreover, the color of most countries are purple. People cannot compare the emissions in the countries with purple. I recommend to use log for all data.  "
"The last shortage of this visualization is that it missed y label."





st.markdown("# Extra Credits")
st.markdown("## Swarmplot")

data9 = df_data.drop(columns=['Non-OECD Economies'])
top_5_countries = ['OECD - Total','OECD America','OECD - Europe','China (People\'s Republic of)','United States','Russia']
data9= data9[data9['Country\year'].isin(top_5_countries)]
data9 = pd.melt(data9, id_vars=['Country\year'], var_name='year')
data9['value'] = data9['value'].apply(pd.to_numeric, errors='coerce')

fig, ax = plt.subplots(figsize=(9, 6), dpi = 50)
ax.grid(alpha = 0.3) 
ax.set_axisbelow(True) 
ax.margins(x=0.01) 
ax = sns.boxplot(x="Country\year", y="value", data=data9, boxprops=dict(alpha=.7))
ax = sns.swarmplot(x="Country\year", y="value", data=data9, color=".2", size = 5)

ax.set_xlabel('Country / Region')
ax.set_ylabel('Emissions')
xaxis = plt.xticks(rotation=0, ha='center', fontsize=8)
yaxis = plt.yticks(fontsize=8)
st.pyplot(fig)

"In this visualization, it is clear to show the emissions in China, OECD - Europe, OECD - Total, OECD America, Russia, and United States. We can find the average emissions in these regions. Also, we can compare the variations of each region. In this visualization, China has the highest variance compared to these regions and the highest average emission. Additionally, we can find that the United States plays a big role in OECD America. Most emissions of OECD America are from the United States."






