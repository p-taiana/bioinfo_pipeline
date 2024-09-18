FROM continuumio/miniconda3

# Instalar mamba para otimizar a instalação do Conda
RUN conda install -n base -c conda-forge mamba

# Criar ambiente Conda e instalar Snakemake, SnpEff, Flask, VEP (Ensembl Variant Effect Predictor)
RUN mamba create -n bioinfo-env -c bioconda -c conda-forge snakemake snpeff flask ensembl-vep

# Ativar o ambiente Conda
ENV PATH /opt/conda/envs/bioinfo-env/bin:$PATH

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos do projeto
COPY . /app

# Rodar o Snakemake para gerar o arquivo VCF anotado usando VEP
RUN snakemake

# Expor a porta 5000 para a API Flask
EXPOSE 5000

# Comando padrão para rodar o Flask
CMD ["python", "app.py"]
