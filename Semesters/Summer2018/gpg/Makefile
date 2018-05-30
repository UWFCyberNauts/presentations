DEPS = gpg.md

all: build

init: 
	mkdir -p build/

build: init clean
	pandoc -o build/gpg.pdf --from markdown --template=lib/template.tex --pdf-engine=xelatex --highlight-style=breezeDark src/md/gpg.md

clean: 
	rm -rf build/*
