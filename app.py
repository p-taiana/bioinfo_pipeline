import re
import os
from flask import Flask, render_template, request, jsonify, url_for
import matplotlib.pyplot as plt

app = Flask(__name__)

def filter_variants(variants, af_threshold, dp_threshold):
    filtered_variants = []
    for variant in variants:
        if variant.startswith("#"):
            continue
        
        match_af = re.search(r'AF=([\d\.]+)', variant)
        match_dp = re.search(r'DP=(\d+)', variant)
        if match_af and match_dp:
            af = float(match_af.group(1))
            dp = int(match_dp.group(1))
            if af >= af_threshold and dp >= dp_threshold:
                filtered_variants.append({
                    "position": variant.split('\t')[1],  # Assume que a posição da variante está na segunda coluna
                    "info": variant.strip()
                })

    return filtered_variants

@app.route('/api/variants', methods=['GET'])
def filter_and_plot():
    af_threshold = float(request.args.get('af', 0.0))
    dp_threshold = int(request.args.get('dp', 0))

    try:
        with open('annotated_variants.vcf', 'r') as file:
            variants = file.readlines()

        filtered_variants = filter_variants(variants, af_threshold, dp_threshold)

        # Gerar gráficos
        af_values = [float(v['info'].split(';')[3].split('=')[1]) for v in filtered_variants]  # Adapte conforme o formato do seu VCF
        dp_values = [int(v['info'].split(';')[4].split('=')[1]) for v in filtered_variants]  # Adapte conforme o formato do seu VCF

        plt.figure()
        plt.hist(af_values, bins=10, alpha=0.7)
        plt.title('Distribuição de AF')
        plt.xlabel('Allele Frequency (AF)')
        plt.ylabel('Count')
        af_path = 'static/af_plot.png'
        plt.savefig(af_path)
        plt.close()

        plt.figure()
        plt.hist(dp_values, bins=10, alpha=0.7)
        plt.title('Distribuição de DP')
        plt.xlabel('Depth of Coverage (DP)')
        plt.ylabel('Count')
        dp_path = 'static/dp_plot.png'
        plt.savefig(dp_path)
        plt.close()

        # Enviar dados filtrados e caminhos de gráficos
        return jsonify({
            "variants": filtered_variants,
            "af_plot": url_for('static', filename='af_plot.png'),
            "dp_plot": url_for('static', filename='dp_plot.png')
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def index():
    return render_template('variants.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
