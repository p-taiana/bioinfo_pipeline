rule all:
    input:
        "variants_with_frequencies.vcf"

rule annotate_dbsnp:
    input:
        "input_variants.vcf"
    output:
        "variants_with_dbsnp.vcf"
    shell:
        """
        # Anotação com o dbSNP ID
        SnpSift annotate dbSNP.vcf {input} > {output}
        """

rule annotate_gnomad:
    input:
        "variants_with_dbsnp.vcf"
    output:
        "variants_with_frequencies.vcf"
    shell:
        """
        # Anotação com a frequência populacional do gnomAD
        SnpSift annotate gnomAD.vcf {input} > {output}
        """
