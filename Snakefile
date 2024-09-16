rule all:
    input:
        "annotated_variants.vcf"

rule annotate_variants:
    input:
        "input_variants.vcf"
    output:
        "annotated_variants.vcf"
    shell:
        """
        # Cria o diretório de saída com permissões adequadas
        mkdir -p /tmp/snpEff_output
        
        # Executa o SnpEff e direciona todos os arquivos de saída para o diretório /tmp/snpEff_output
        snpEff -Xmx4g ann -v GRCh37.75 {input} -csvStats /tmp/snpEff_output/snpEff_summary.csv > {output}
        """
