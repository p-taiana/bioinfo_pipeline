import re
import requests
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Função para consultar a API do Ensembl VEP e obter anotações de variantes
def annotate_variant_with_vep(chrom, pos, ref, alt):
    url = "https://rest.ensembl.org/vep/human/region"
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    
    # Preparar a variante no formato esperado
    variant_data = {
        "variants": [f"{chrom}:{pos}_{ref}/{alt}"]
    }
    
    response = requests.post(url, headers=headers, json=variant_data)
    
    if response.status_code == 200:
        return response.json()  # Retorna as anotações da variante
    else:
        return None

# Função para filtrar variantes com base nos thresholds de AF e DP
def filter_variants(variants, freq_threshold, dp_threshold):
    filtered_variants = []
    for variant in variants:
        if variant.startswith("#"):
            continue  # Ignora as linhas de cabeçalho

        # Extrair informações da linha VCF
        variant_data = variant.strip().split("\t")
        chrom, pos, ref, alt = variant_data[0], variant_data[1], variant_data[3], variant_data[4]
        
        # Chamar a API do Ensembl VEP para obter anotações
        annotation = annotate_variant_with_vep(chrom, pos, ref, alt)
        
        if annotation:
            info_field = annotation[0]['transcript_consequences'][0] if 'transcript_consequences' in annotation[0] else None
            if info_field:
                freq = float(info_field.get('gnomad_AF', 0.0))  # Frequência do gnomAD
                dp = int(variant_data[5])  # Usamos a profundidade da coluna DP do VCF

                # Aplica os filtros de frequência e DP
                if freq >= freq_threshold and dp >= dp_threshold:
                    variant_info = {
                        "variant": pos,  # A posição da variante
                        "info": f"Chrom: {chrom}, Pos: {pos}, Ref: {ref}, Alt: {alt}, gnomAD_AF: {freq}, DP: {dp}"  # Todas as informações da variante
                    }
                    filtered_variants.append(variant_info)

    return filtered_variants

# Rota para renderizar o frontend
@app.route('/variants')
def variants():
    return render_template('variants.html')  # Renderiza o HTML

# Rota para carregar e filtrar o arquivo VCF via API
@app.route('/api/variants', methods=['GET'])
def get_variants():
    vcf_file = './input_variants.vcf'  # Arquivo de variantes sem anotações (apenas com variantes básicas)
    
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
    app.run(host='0.0.0.0', port=5000)
