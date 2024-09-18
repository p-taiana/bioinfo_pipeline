rule all:
    input:
        "variants_with_gnomad.vcf"

rule annotate_with_vep:
    input:
        "annotated_variants.vcf"
    output:
        "variants_with_gnomad.vcf"
    shell:
        """
        vep --input_file {input} --output_file {output} --cache --offline --assembly GRCh37 \
            --plugin gnomAD,/path/to/gnomad/data.gz --format vcf --vcf --symbol --tsl --hgvs \
            --fasta /path/to/human_g1k_v37.fasta --species homo_sapiens --everything
        """
