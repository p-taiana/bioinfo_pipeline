# Usando Miniconda para configurar o ambiente base
FROM continuumio/miniconda3:latest

# Criar ambiente Conda e instalar dependências
RUN conda install -n base -c conda-forge mamba \
    && mamba create -n bioinfo-env -c bioconda -c conda-forge snakemake snpeff snpsift flask matplotlib pandas

# Ativar o ambiente Conda
ENV PATH /opt/conda/envs/bioinfo-env/bin:$PATH

# Criar diretório de trabalho
WORKDIR /app

# Copiar todos os arquivos para dentro do container
COPY . /app

# Instalar qualquer dependência adicional necessária (como Flask, Matplotlib)
RUN pip install Flask matplotlib pandas

# Comando padrão para rodar o servidor Flask
CMD ["python", "app.py"]
