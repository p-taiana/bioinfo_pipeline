import re
import os
import pandas as pd
from flask import Flask, render_template, request, jsonify
import matplotlib.pyplot as plt

app = Flask(__name__)

# Função para filtrar variantes por AF e DP
def filter_variants(variants, af_threshold, dp_threshold):
    filtered_variants = []
    for variant in variants:
        if variant.startswith("#"):
            continue  # Ignora cabeçalhos
        
        # Regex para capturar AF e DP
        match_af = re.search(r'AF=([\d\.]+)', variant)
        match_dp = re.search(r'DP=(\d+)', variant)

        if match_af and match_dp:
            af = float(match_af.group(1))
            dp = int(match_dp.group(1))

            # Filtra variantes com AF >= af_threshold e DP >= dp_threshold
            if af >= af_threshold and dp >= dp_threshold:
                filtered_variants.append(variant)

    return filtered_variants

# Rota para filtrar e exibir gráficos
@app.route('/api/filter', methods=['GET'])
def filter_and_plot():
    af_threshold = float(request.args.get('af', 0.0))
    dp_threshold = int(request.args.get('dp', 0))

    vcf_file = './annotated_variants.vcf'
    
    try:
        with open(vcf_file, 'r') as file:
            variants = file.readlines()

        # Filtra as variantes
        filtered_variants = filter_variants(variants, af_threshold, dp_threshold)

        # Gera gráficos (exemplo: distribuições de AF e DP)
        af_values = [float(re.search(r'AF=([\d\.]+)', v).group(1)) for v in filtered_variants]
        dp_values = [int(re.search(r'DP=(\d+)', v).group(1)) for v in filtered_variants]

        # Gráfico de AF
        plt.hist(af_values, bins=10, alpha=0.7, label='AF')
        plt.title('Distribuição de AF')
        plt.xlabel('AF')
        plt.ylabel('Frequência')
        plt.savefig('static/af_plot.png')
        plt.clf()

        # Gráfico de DP
        plt.hist(dp_values, bins=10, alpha=0.7, label='DP')
        plt.title('Distribuição de DP')
        plt.xlabel('DP')
        plt.ylabel('Frequência')
        plt.savefig('static/dp_plot.png')
        plt.clf()

        # Retorna os gráficos e o número de variantes filtradas
        return jsonify({
            "num_variants": len(filtered_variants),
            "af_plot": '/static/af_plot.png',
            "dp_plot": '/static/dp_plot.png'
        })

    except Exception as e:
        return str(e), 500

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True)
