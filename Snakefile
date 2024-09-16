rule all:
    input:
        "variants_with_impact.vcf"

rule download_dbsnp:
    output:
        "dbSNP.vcf"
    shell:
        """
        wget ftp://ftp.ncbi.nih.gov/snp/organisms/human_9606_b142_GRCh37p13/VCF/00-All.vcf.gz -O dbSNP.vcf.gz
        gunzip dbSNP.vcf.gz
        """

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

rule snpsift_annotate:
    input:
        "annotated_variants.vcf", "dbSNP.vcf"
    output:
        "variants_with_impact.vcf"
    shell:
        """
        # Usa SnpSift para adicionar dados de impacto e anotar com dbSNP
        SnpSift annotate {input[1]} {input[0]} > {output}
        """
