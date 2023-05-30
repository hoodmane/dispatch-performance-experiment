#!/bin/bash
set -ex

declare -a optflags=("-O2" "-O3" "-Os")
declare -a methods=("switch" "cgoto" "tcall")

export CC_FLAGS="-Wall"
export EMCC_FLAGS="\
	-sALLOW_MEMORY_GROWTH \
	-s STACK_SIZE=5MB \
	--preload-file zz.bin \
	-mtail-call"


for optflag in "${optflags[@]}"; do
   for method in "${methods[@]}"; do

		export CC=gcc
        $CC main.c -o interp_$CC$optflag-$method  \
                $CC_FLAGS $optflag \
			-DCC="\"$CC\"" -DOPTFLAG="\"$optflag\"" -DMETHOD=$method

		export CC=clang
		$CC main.c -o interp_$CC$optflag-$method  \
		    $CC_FLAGS $optflag \
			-DCC="\"$CC\"" -DOPTFLAG="\"$optflag\"" -DMETHOD=$method

		export CC=emcc
		$CC main.c -o interp_$CC$optflag-$method  \
		    $CC_FLAGS $optflag \
			-DCC="\"$CC\"" -DOPTFLAG="\"$optflag\"" -DMETHOD=$method \
			$EMCC_FLAGS 
	done
done
