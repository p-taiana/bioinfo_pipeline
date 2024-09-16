rule all:
    input:
        "variants_with_impact.vcf"

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
        snpEff -Xmx4g ann -v GRCh37.75 {input} -csvStats /tmp/snpEff_output/snpEff_summary.csv > /tmp/snpEff_output/annotated_variants.vcf

        # Copia o VCF anotado de volta para o diretório de trabalho
        cp /tmp/snpEff_output/annotated_variants.vcf {output}
        """

rule snpsift_annotate:
    input:
        "annotated_variants.vcf"
    output:
        "variants_with_impact.vcf"
    shell:
        """
        # Usa SnpSift para adicionar dados de impacto e anotar com dbSNP
        SnpSift annotate dbSNP.vcf {input} > {output}
        """
