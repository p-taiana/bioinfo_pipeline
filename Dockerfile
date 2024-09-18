# Usar Miniconda como base
FROM continuumio/miniconda3

# Instalar mamba para otimizar a instalação do Conda
RUN conda install -n base -c conda-forge mamba

# Criar o ambiente Conda e instalar as dependências necessárias (snakemake, snpeff, snpsift, flask)
RUN mamba create -n bioinfo-env -c bioconda -c conda-forge snakemake snpeff snpsift flask

# Ativar o ambiente Conda
ENV PATH /opt/conda/envs/bioinfo-env/bin:$PATH

# Instalar Perl (necessário para VEP) e dependências do VEP
RUN apt-get update && apt-get install -y \
    perl \
    build-essential \
    curl \
    git \
    zlib1g-dev \
    libdbi-perl \
    libdbd-mysql-perl \
    cpanminus \
    make \
    libssl-dev \
    libexpat1-dev

# Instalar o módulo DBI via cpanm
RUN cpanm --force DBI

# Baixar e instalar o VEP
RUN git clone https://github.com/Ensembl/ensembl-vep.git && \
    cd ensembl-vep && \
    perl INSTALL.pl -a a -s homo_sapiens -y GRCh37 --CONVERT --NO_UPDATE

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos do projeto para dentro do contêiner
COPY . /app

# Expor a porta 5000 para o Flask
EXPOSE 5000

# Comando padrão para rodar o Flask
CMD ["python", "app.py"]
