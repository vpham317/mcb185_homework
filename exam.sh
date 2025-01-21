gunzip -c ../MCB185/data/C.elegans.gff.gz | cut -f 7 | sort | uniq -c
gunzip -c ecoli.gff.gz | grep -c "transposase"
gunzip -c ecoli.gff.gz | grep -c "helicase"
