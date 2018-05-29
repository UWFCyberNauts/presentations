DEPS = gpg.md

all: clean build

build: clean
	mkdir build/
	pandoc -o build/gpg.pdf --from markdown --pdf-engine=xelatex --highlight-style=breezeDark gpg.md

clean: 
	rm -rf build/
