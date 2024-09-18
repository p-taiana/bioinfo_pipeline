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
                    "variant": variant.split('\t')[1],  # Assume que a posição da variante está na segunda coluna
                    "info": variant
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

        # Assume que você tem funções para gerar gráficos, se necessário

        return jsonify(filtered_variants)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def index():
    return render_template('variants.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
