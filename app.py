from flask import Flask, jsonify, request, render_template
import re
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Variant Filtering API!"

@app.route('/variants')
def variants():
    return render_template('variants.html')

def filter_variants(variants, freq_threshold, dp_threshold):
    filtered_variants = []
    for variant in variants:
        if variant.startswith("#"):
            continue

        match_freq = re.search(r'AF=([\d\.]+)', variant)  # Ajuste conforme o formato de frequência no VCF
        match_dp = re.search(r'DP=(\d+)', variant)

        if match_freq and match_dp:
            freq = float(match_freq.group(1))
            dp = int(match_dp.group(1))

            if freq >= freq_threshold and dp >= dp_threshold:
                variant_info = {
                    "variant": variant.split("\t")[1],  # Posição da variante
                    "info": variant.strip()
                }
                filtered_variants.append(variant_info)

    return filtered_variants

@app.route('/api/variants', methods=['GET'])
def get_variants():
    vcf_file = './variants_with_frequencies.vcf'
    try:
        freq_threshold = float(request.args.get('freq', 0.0))
        dp_threshold = int(request.args.get('dp', 0))

        with open(vcf_file, 'r') as file:
            variants = file.readlines()

        filtered_variants = filter_variants(variants, freq_threshold, dp_threshold)
        return jsonify(filtered_variants)
    except Exception as e:
        app.logger.error(f"Failed to filter variants: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
