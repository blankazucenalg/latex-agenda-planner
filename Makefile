all:
	python create_tex.py
	pdflatex agenda.tex
clean: 
	rm -r *.out *.toc *.log *.aux *.lof *.lot *.fls *.fdb_latexmk *.dvi 
