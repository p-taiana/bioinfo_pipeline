Este projeto é um pipeline de bioinformática que utiliza Flask para fornecer uma interface web interativa para filtrar variantes genéticas por frequência alélica (AF) e profundidade (DP). Ele permite que os usuários carreguem arquivos VCF (Variant Call Format) e façam filtragens específicas diretamente pela web. O projeto também é containerizado com Docker para facilitar a implementação em diferentes ambientes.

**Sobre o Projeto**

A pipeline foi criado para facilitar a análise de variantes genéticas filtrando-as por frequência alélica mínima (AF) e profundidade de cobertura mínima (DP). O projeto usa Flask para a construção da API e da interface web, e Docker para a fácil configuração e execução do pipeline em diferentes ambientes. Isso torna o projeto replicável e portável para diferentes plataformas sem a necessidade de configuração manual complexa.


**Pré-requisitos para Configuração do Ambiente**

_Python:_
Versão: Python 3.8 ou superior.
Python é utilizado para a programação do backend, scripts de automação e processamento de dados.
Instalação: Pode ser instalado via Python official website ou usando gerenciadores de pacotes como brew em macOS (brew install python) ou apt em Debian-based systems (sudo apt-get install python3).


_Docker:_
Docker é utilizado para criar um ambiente isolado que pode executar o projeto com todas as dependências instaladas, garantindo a consistência entre diferentes máquinas.
Instalação: Instruções para instalação podem ser encontradas em Docker official website.



_Git:_
Necessário para clonar o projeto do repositório do GitHub.
Instalação: Pode ser instalado através de Git official website ou via linha de comando (sudo apt install git para Debian/Ubuntu, brew install git para macOS).


_Snakemake:_
Snakemake é usado para automatizar o pipeline de execução de tarefas, como análise de dados e processamento de VCFs.
Instalação: Pode ser instalado via pip (pip install snakemake) ou conda (conda install -c bioconda snakemake).


_Flask:_
Framework web utilizado para construir a API e a interface web interativa.
Instalação: Pode ser instalado via pip (pip install Flask).


_Matplotlib (opcional):_
Utilizado para a geração de gráficos no backend, se necessário.
Instalação: Pode ser instalado via pip (pip install matplotlib).


_Bibliotecas adicionais de Python:_
Pandas: para manipulação de dados (pip install pandas).
Requests: para fazer requisições HTTP se necessário (pip install requests).


**Configuração do Ambiente**

Após instalar os pré-requisitos, o projeto pode ser configurado e executado usando Docker, o que simplifica o processo ao não exigir a configuração manual do ambiente:


**Clonar o repositório do GitHub:**

Comando: git clone [URL do Repositório]
Construção e Execução com Docker:
Construir a imagem Docker: docker build -t nome_do_projeto .
Rodar a aplicação: docker run -p 5000:5000 nome_do_projeto
Incluindo esses detalhes no seu README ou documentação assegura que os usuários têm todas as informações necessárias para começar a trabalhar com seu projeto sem entraves, proporcionando uma experiência inicial positiva e eficiente.



**Funcionalidades**

Carregamento de arquivos VCF para análise de variantes.
Filtragem de variantes por frequência alélica (AF) e profundidade de cobertura (DP).
Interface web interativa para visualização de variantes filtradas.
Gráficos interativos gerados com Chart.js para visualização da distribuição de variantes.
Containerização com Docker para fácil deploy em diferentes ambientes.


**Instalação**

conda install -n base -c conda-forge mamba \
    && mamba create -n bioinfo-env -c bioconda -c conda-forge snakemake snpeff snpsift flask matplotlib pandas

**Rodando localmente**

1. Clone o repositório:
git clone https://github.com/p-taiana/bioinfo_pipeline.git;

cd bioinfo_pipeline


2. Crie um ambiente virtual (opcional, mas recomendado):
python3 -m venv venv;
source venv/bin/activate;  # No Windows: venv\Scripts\activate


3. Instale as dependências:
pip install -r requirements.txt;


5. Execute a aplicação Flask:
python app.py;


7. Abra seu navegador e acesse:
http://127.0.0.1:5000


**Rodando com Docker**

1. Clone o repositório:
git clone https://github.com/p-taiana/bioinfo_pipeline.git
cd bioinfo_pipeline


2. Construa a imagem Docker:
docker build -t bioinfo_pipeline .


3. Rode o contêiner:
docker run -p 5000:5000 bioinfo_pipeline


4. Abra seu navegador e acesse:
http://127.0.0.1:5000


**Como Usar**
1. Carregue o arquivo VCF: O sistema processa automaticamente arquivos VCF carregados.
2. Filtre variantes: Use os campos no formulário para filtrar variantes por frequência alélica mínima (AF) e profundidade mínima (DP).
3. Visualize os resultados: As variantes filtradas serão exibidas em uma tabela com informações detalhadas.
4. Visualize os gráficos: Gráficos de distribuição para AF e DP são gerados automaticamente com base nos resultados.


**Contribuição**
Se você quiser contribuir para este projeto:


Contato
Taiana Silva Pereira - taianat7@gmail.com

Link para o projeto: https://github.com/p-taiana/bioinfo_pipeline

