#!/bin/bash
set -ex

declare -a optflags=("-O2" "-O3" "-Os")
declare -a methods=("switch" "cgoto" "tcall")
declare -a compilers=("gcc" "clang" "emcc")

CC_FLAGS="-Wall"
emcc_FLAGS="\
	-sALLOW_MEMORY_GROWTH \
	-s STACK_SIZE=5MB \
	--preload-file zz.bin \
	-mtail-call"

rm -rf bin
mkdir bin

cp zz.bin bin

for optflag in "${optflags[@]}"; do
   for method in "${methods[@]}"; do
		for CC in "${compilers[@]}"; do
			flags_name="${CC}_FLAGS"
			$CC main.c -o bin/interp_$CC$optflag-$method  \
				$CC_FLAGS $optflag \
				-DCC="\"$CC\"" -DOPTFLAG="\"$optflag\"" -DMETHOD=$method \
				${!flags_name}
		done
	done
done
