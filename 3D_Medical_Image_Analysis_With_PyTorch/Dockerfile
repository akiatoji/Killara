#FROM continuumio/miniconda3
FROM nvidia/cuda:10.2-base
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"
RUN apt-get update

RUN apt-get install -y wget git libgl1-mesa-glx && rm -rf /var/lib/apt/lists/*

RUN wget \
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh 
RUN conda --version

RUN conda create -n py37-ml python=3.7
RUN conda install -c fastai -c pytorch fastai
RUN conda install jupyter
RUN conda install imageio
RUN echo "source activate py37-ml" > ~/.bashrc
ENV PATH /opt/conda/envs/env/bin:$PATH
#git clone https://github.com/fastai/fastbook.git
RUN pip install -Uqq fastbook
CMD ["jupyter", "notebook", "--no-browser", "--allow-root", "--ip=0.0.0.0"]
