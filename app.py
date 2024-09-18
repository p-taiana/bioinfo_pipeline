import re
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Função para filtrar variantes com base nos thresholds de AF e DP
def filter_variants(variants, freq_threshold, dp_threshold):
    filtered_variants = []
    for variant in variants:
        if variant.startswith("#"):
            continue  # Ignora as linhas de cabeçalho

        fields = variant.split("\t")
        info_field = fields[7]
        freq = float(re.search(r'gnomAD_AF=([\d\.]+)', info_field).group(1))
        dp = int(re.search(r'DP=(\d+)', info_field).group(1))

        # Aplica os filtros de frequência e DP
        if freq >= freq_threshold and dp >= dp_threshold:
            filtered_variants.append({
                "variant": fields[1],  # A posição da variante
                "info": variant.strip()  # Todas as informações da variante
            })

    return filtered_variants

# Rota para renderizar o frontend
@app.route('/variants')
def variants():
    return render_template('variants.html')

# Rota para carregar e filtrar o arquivo VCF via API
@app.route('/api/variants', methods=['GET'])
def get_variants():
    vcf_file = './variants_with_gnomad.vcf'
    try:
        freq_threshold = float(request.args.get('freq', 0.0))
        dp_threshold = int(request.args.get('dp', 0))

        with open(vcf_file, 'r') as file:
            variants = file.readlines()

        filtered_variants = filter_variants(variants, freq_threshold, dp_threshold)

        return jsonify(filtered_variants)
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(debug=True)
