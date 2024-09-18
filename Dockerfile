FROM continuumio/miniconda3

# Instalar mamba para otimizar a instalação do Conda
RUN conda install -n base -c conda-forge mamba

# Criar ambiente Conda e instalar Flask, pandas e outras dependências necessárias
RUN mamba create -n bioinfo-env -c bioconda -c conda-forge snakemake snpeff snpsift flask vep

# Ativar o ambiente Conda
ENV PATH /opt/conda/envs/bioinfo-env/bin:$PATH

# Baixar o cache do VEP para GRCh37 (ajustar conforme necessário)
RUN vep_install -a cf -s homo_sapiens -y GRCh37

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos do projeto
COPY . /app

# Comando padrão para rodar o Flask
CMD ["python", "app.py"]
