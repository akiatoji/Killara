import streamlit as st
import time

import pandas as pd
import numpy as np

from sklearn.datasets import fetch_openml
from sklearn.manifold import TSNE

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


N = 10000

feat_cols, df = load_data()

for perplexity in [5,10,25, 50]:
    df_subset, data_subset = select_data(df, feat_cols, size = N)
    tsne_results = run_tsne(data_subset, perplexity)
    df_subset['tsne-2d-one'] = tsne_results[:,0]
    df_subset['tsne-2d-two'] = tsne_results[:,1]

    df_subset.to_csv("tsne_data_{perplexity}".format(perplexity = perplexity))

