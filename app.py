import re
import os
from flask import Flask, render_template, request, jsonify, url_for
import matplotlib.pyplot as plt

app = Flask(__name__)

def filter_variants(variants, af_threshold, dp_threshold):
    af_count = 0
    dp_count = 0
    for variant in variants:
        if variant.startswith("#"):
            continue
        
        match_af = re.search(r'AF=([\d\.]+)', variant)
        match_dp = re.search(r'DP=(\d+)', variant)
        if match_af and match_dp:
            af = float(match_af.group(1))
            dp = int(match_dp.group(1))
            if af >= af_threshold:
                af_count += 1
            if dp >= dp_threshold:
                dp_count += 1

    return af_count, dp_count

@app.route('/api/variants', methods=['GET'])
def api_filter():
    af_threshold = float(request.args.get('af', 0.0))
    dp_threshold = int(request.args.get('dp', 0))

    try:
        with open('annotated_variants.vcf', 'r') as file:
            variants = file.readlines()

        af_count, dp_count = filter_variants(variants, af_threshold, dp_threshold)

        # Generate simple bar charts
        plt.figure()
        plt.bar(['AF'], [af_count], color='blue')
        plt.title('Variantes por AF')
        plt.savefig('static/af_count.png')
        plt.close()

        plt.figure()
        plt.bar(['DP'], [dp_count], color='red')
        plt.title('Variantes por DP')
        plt.savefig('static/dp_count.png')
        plt.close()

        return jsonify({"af_plot": url_for('static', filename='af_count.png'), "dp_plot": url_for('static', filename='dp_count.png')})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def index():
    return render_template('variants.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
