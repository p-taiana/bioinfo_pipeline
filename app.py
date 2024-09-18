import re
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Função para filtrar variantes com base nos thresholds de AF e DP
def filter_variants(variants, freq_threshold, dp_threshold):
    filtered_variants = []
    for variant in variants:
        if variant.startswith("#"):
            continue  # Ignora as linhas de cabeçalho

        # Regex para extrair a frequência (AF) e profundidade (DP) do campo INFO
        match_freq = re.search(r'AF=([\d\.]+)', variant)
        match_dp = re.search(r'DP=(\d+)', variant)

        if match_freq and match_dp:
            freq = float(match_freq.group(1))
            dp = int(match_dp.group(1))

            # Aplica os filtros de frequência e DP
            if freq >= freq_threshold and dp >= dp_threshold:
                # Adiciona o variant como dicionário JSON estruturado
                variant_info = {
                    "variant": variant.split("\t")[2],  # A posição da variante é a terceira coluna (ajustar conforme a posição real)
                    "info": variant.strip()  # Todas as informações da variante
                }
                filtered_variants.append(variant_info)

    return filtered_variants

# Rota para renderizar o frontend
@app.route('/variants')
def variants():
    return render_template('variants.html')  # Isso deve renderizar o HTML

# Rota para carregar e filtrar o arquivo VCF via API
@app.route('/api/variants', methods=['GET'])
def get_variants():
    vcf_file = './annotated_variants.vcf'
    try:
        # Parâmetros de filtragem da URL
        freq_threshold = float(request.args.get('freq', 0.0))  # Exemplo: ?freq=0.05
        dp_threshold = int(request.args.get('dp', 0))  # Exemplo: ?dp=100

        # Carrega o arquivo VCF
        with open(vcf_file, 'r') as file:
            variants = file.readlines()

        # Filtra as variantes com base nos parâmetros fornecidos
        filtered_variants = filter_variants(variants, freq_threshold, dp_threshold)

        # Retorna as variantes filtradas em formato JSON
        return jsonify(filtered_variants)
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
