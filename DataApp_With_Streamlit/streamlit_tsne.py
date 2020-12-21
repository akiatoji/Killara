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
def load_data():
    mnist = fetch_openml('mnist_784')
    X = mnist.data / 255.0
    y = mnist.target

    feat_cols = ['pixel' + str(i) for i in range(X.shape[1])]
    df = pd.DataFrame(X, columns=feat_cols)
    df['y'] = y
    df['label'] = df['y'].apply(lambda i: str(i))

    return (feat_cols, df)

def select_data(df, feat_cols, size=10000):
    rndperm = np.random.permutation(df.shape[0])
    df_subset = df.loc[rndperm[:size], :].copy()
    data_subset = df_subset[feat_cols].values
    return (df_subset, data_subset)

def run_tsne(data_subset, perplexity=40):
    time_start = time.time()
    tsne = TSNE(n_components=2, verbose=1, perplexity=perplexity, n_iter=300)
    tsne_results = tsne.fit_transform(data_subset)
    print('t-SNE done! Time elapsed: {} seconds'.format(time.time() - time_start))
    return tsne_results


feat_cols, df = load_data()

perplexity = st.select_slider('Perplexity', [5, 10, 25, 50])

df_subset, data_subset = select_data(df, feat_cols)
tsne_results = run_tsne(data_subset, perplexity)

df_subset['tsne-2d-one'] = tsne_results[:,0]
df_subset['tsne-2d-two'] = tsne_results[:,1]
plt.figure(figsize=(16,10))
fig, ax = plt.subplots()
sns.scatterplot(
    x="tsne-2d-one", y="tsne-2d-two",
    hue="y",
    palette=sns.color_palette("hls", 10),
    data=df_subset,
    legend="full",
    alpha=0.3,
    ax=ax
)

st.pyplot(fig)
