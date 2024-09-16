FROM continuumio/miniconda3

# Instalar mamba para otimizar a instalação do Conda
RUN conda install -n base -c conda-forge mamba

# Criar ambiente Conda e instalar Snakemake, SnpEff, SnpSift, Flask, Pandas, e Plotly
RUN mamba create -n bioinfo-env -c bioconda -c conda-forge snakemake snpeff snpsift flask pandas plotly

# Ativar o ambiente Conda
ENV PATH /opt/conda/envs/bioinfo-env/bin:$PATH

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos do projeto
COPY . /app

# Baixar o arquivo dbSNP.vcf.gz correto para GRCh37
RUN wget https://ftp.ncbi.nlm.nih.gov/snp/latest_release/VCF/GCF_000001405.25.bgz -O /app/dbSNP.vcf.gz && \
    gunzip /app/dbSNP.vcf.gz

# Rodar o Snakemake para gerar o arquivo VCF anotado
RUN snakemake

# Expor a porta 5000 para a API Flask
EXPOSE 5000

# Comando padrão para rodar o Flask
CMD ["python", "app.py"]
