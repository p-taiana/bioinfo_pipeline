rule all:
    input:
        "variants_with_dbsnp.vcf"

rule annotate_dbsnp:
    input:
        "input_variants.vcf"
    output:
        "variants_with_dbsnp.vcf"
    shell:
        """
        # Usar o VEP para anotar com dbSNP IDs
        vep --input_file {input} --output_file {output} --everything --vcf --offline
        """
