gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "r" | grep -Ev [bdefghjklmpqstuvwxy] | grep -E ".{4,}"
