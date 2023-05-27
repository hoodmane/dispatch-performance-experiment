# Makefile to build the sample
#
# Eli Bendersky [https://eli.thegreenplace.net]
# This code is in the public domain.


CC_FLAGS := -Wall -O3 
EMCC_FLAGS= \
	-sALLOW_MEMORY_GROWTH \
	-s STACK_SIZE=5MB \
	--preload-file zz.bin \
	-mtail-call \

EXE_TARGETS := \
	interp_clang \
	interp_gcc  \
	interp_emcc \

all: results.txt
.PHONY: all

interp_gcc: main.c
	gcc -o $@ $(CC_FLAGS) $^ -DCC='"gcc  "'

interp_clang: main.c
	clang -o $@ $(CC_FLAGS) $^ -DCC='"clang"'

interp_emcc: main.c
	emcc -o $@ $(CC_FLAGS) $(EMCC_FLAGS) $^ -DCC='"emcc "'

results.txt: interp_gcc interp_clang interp_emcc
	rm -f raw_results.txt
	rm -f results.txt
	./interp_gcc >> raw_results.txt
	./interp_clang >> raw_results.txt
	node ./interp_emcc >> raw_results.txt
	python3 render_results.py raw_results.txt >> results.txt

clean:
	rm -f a.out *.o *.a $(EXE_TARGETS) raw_results.txt results.txt

format:
	clang-format -style=file -i *.c

.PHONY: clean format
