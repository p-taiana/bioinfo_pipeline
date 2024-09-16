#!/bin/bash
echo "Baixando o arquivo dbSNP..."

wget https://ftp.ncbi.nih.gov/snp/latest_release/VCF/GCF_000001405.40.gz -O dbSNP.vcf.gz
gunzip dbSNP.vcf.gz

echo "Download completo."
