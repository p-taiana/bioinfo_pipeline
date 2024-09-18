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
                filtered_variants.append(variant)

    return filtered_variants

@app.route('/filter', methods=['GET', 'POST'])
def filter_and_plot():
    if request.method == 'POST':
        af_threshold = float(request.form.get('af', 0.0))
        dp_threshold = int(request.form.get('dp', 0))

        try:
            with open('annotated_variants.vcf', 'r') as file:
                variants = file.readlines()

            filtered_variants = filter_variants(variants, af_threshold, dp_threshold)
            af_values = [float(re.search(r'AF=([\d\.]+)', v).group(1)) for v in filtered_variants if re.search(r'AF=([\d\.]+)', v)]
            dp_values = [int(re.search(r'DP=(\d+)', v).group(1)) for v in filtered_variants if re.search(r'DP=(\d+)', v)]

            plt.figure()
            plt.hist(af_values, bins=10, alpha=0.7, label='AF')
            plt.title('Distribuição de AF')
            plt.xlabel('AF')
            plt.ylabel('Frequência')
            af_path = 'static/af_plot.png'
            plt.savefig(af_path)
            plt.close()

            plt.figure()
            plt.hist(dp_values, bins=10, alpha=0.7, label='DP')
            plt.title('Distribuição de DP')
            plt.xlabel('DP')
            plt.ylabel('Frequência')
            dp_path = 'static/dp_plot.png'
            plt.savefig(dp_path)
            plt.close()

            return render_template('results.html', af_image=url_for('static', filename='af_plot.png'), dp_image=url_for('static', filename='dp_plot.png'), num_variants=len(filtered_variants))
        
        except Exception as e:
            return str(e), 500
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
