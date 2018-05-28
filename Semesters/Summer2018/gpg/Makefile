DEPS = gpg.md

all: clean build

build: clean
	mkdir build/
	pandoc -o build/gpg.pdf --toc --highlight-style=breezeDark gpg.md

clean: 
	rm -rf build/
