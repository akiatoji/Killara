# Data Application example using Steamlit

[Streamlit](https://www.streamlit.io/) is an open source framework for building a Data Visualization webapp in Python.   

Streamlit is not yet another charting software.  Rather, it is an easy to use library for converting your exisitng Python code to interactive web page by adding layouts and widgets around the charts you plot with the library of choice.


## t-SNE visualization demo

I wrote a Streamlit app that displays t-SNE results using different perplexity.  This is a very common simple demo that takes random 10000 samples from MNIST data, then run t_SNE on it to visualize different clusters of handwritten digits in 2D space.

Streamlit is not a data exploration tool. Rather, Streamlit is a curated data presentation tool.  So the t-SNE data is pre-generated (see generate_tsne.py), and the DataApp merely selects which data set to display dpepending on the slider input.

![](streamlit_tsne_screenshot.png)


Streamlit can do quite a bit more, but it is also very easy to just start using.  Converting an existing Python code to Streamlit takes matter of minutes.  