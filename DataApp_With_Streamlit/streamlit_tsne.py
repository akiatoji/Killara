import streamlit as st
import time

import pandas as pd
import numpy as np

from sklearn.datasets import fetch_openml
from sklearn.manifold import TSNE

import matplotlib.pyplot as plt
import seaborn as sns

N = 100

np.random.seed(42)

st.title('Visualizing t-SNE in Streamlit')

@st.cache
def load_data(perplexity):
    df = pd.read_csv("tsne_data_{data_size}.zip".format(data_size=perplexity))
    return df

perplexity = st.select_slider('Perplexity', [5, 10, 25, 50])

df = load_data(perplexity)

plt.figure(figsize=(16,10))
fig, ax = plt.subplots()
sns.scatterplot(
    x="tsne-2d-one", y="tsne-2d-two",
    hue="y",
    palette=sns.color_palette("hls", 10),
    data=df,
    legend="full",
    alpha=0.3,
    ax=ax
)

st.pyplot(fig)
