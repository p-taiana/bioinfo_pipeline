FROM continuumio/miniconda3

# Instalar mamba para otimizar a instalação do Conda
RUN conda install -n base -c conda-forge mamba

# Criar ambiente Conda e instalar Flask, Pandas e Requests (para APIs)
RUN mamba create -n bioinfo-env -c conda-forge flask pandas requests

# Ativar o ambiente Conda corretamente
ENV PATH="/opt/conda/envs/bioinfo-env/bin:$PATH"

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos do projeto
COPY . /app

# Expor a porta 5000 para a API Flask
EXPOSE 5000

# Comando padrão para rodar o Flask
CMD ["python", "app.py"]
