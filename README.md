Este projeto é um pipeline de bioinformática que utiliza Flask para fornecer uma interface web interativa para filtrar variantes genéticas por frequência alélica (AF) e profundidade (DP). Ele permite que os usuários carreguem arquivos VCF (Variant Call Format) e façam filtragens específicas diretamente pela web. O projeto também é containerizado com Docker para facilitar a implementação em diferentes ambientes.

Sobre o Projeto
A pipeline foi criado para facilitar a análise de variantes genéticas filtrando-as por frequência alélica mínima (AF) e profundidade de cobertura mínima (DP). O projeto usa Flask para a construção da API e da interface web, e Docker para a fácil configuração e execução do pipeline em diferentes ambientes. Isso torna o projeto replicável e portável para diferentes plataformas sem a necessidade de configuração manual complexa.

Funcionalidades
Carregamento de arquivos VCF para análise de variantes.
Filtragem de variantes por frequência alélica (AF) e profundidade de cobertura (DP).
Interface web interativa para visualização de variantes filtradas.
Gráficos interativos gerados com Chart.js para visualização da distribuição de variantes.
Containerização com Docker para fácil deploy em diferentes ambientes.

Instalação
Pré-requisitos
Python >3.x
Docker (se preferir rodar o projeto em contêiner)
Pip (para instalação de pacotes Python)

_Rodando localmente
1. Clone o repositório:
git clone https://github.com/p-taiana/bioinfo_pipeline.git

cd bioinfo_pipeline

2. Crie um ambiente virtual (opcional, mas recomendado):
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

3. Instale as dependências:
pip install -r requirements.txt

5. Execute a aplicação Flask:
python app.py

7. Abra seu navegador e acesse:
http://127.0.0.1:5000

_Rodando com Docker
1. Clone o repositório:
git clone https://github.com/p-taiana/bioinfo_pipeline.git
cd bioinfo_pipeline

2. Construa a imagem Docker:
docker build -t bioinfo_pipeline .

3. Rode o contêiner:
docker run -p 5000:5000 bioinfo_pipeline

4. Abra seu navegador e acesse:
http://127.0.0.1:5000


Como Usar
1. Carregue o arquivo VCF: O sistema processa automaticamente arquivos VCF carregados.
2. Filtre variantes: Use os campos no formulário para filtrar variantes por frequência alélica mínima (AF) e profundidade mínima (DP).
3. Visualize os resultados: As variantes filtradas serão exibidas em uma tabela com informações detalhadas.
4. Visualize os gráficos: Gráficos de distribuição para AF e DP são gerados automaticamente com base nos resultados.


Contribuição
Se você quiser contribuir para este projeto:

Faça um fork do repositório.
Crie uma branch para sua nova funcionalidade (git checkout -b feature/nova-funcionalidade).
Faça commit das suas mudanças (git commit -m 'Adiciona nova funcionalidade').
Envie para o repositório remoto (git push origin feature/nova-funcionalidade).
Abra um Pull Request.
Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.

Contato
Taiana Silva Pereira - taianat7@gmail.com

Link para o projeto: https://github.com/p-taiana/bioinfo_pipeline

