## Interpreter Dispatch

Based on Eli Bendersky's blog:
https://github.com/eliben/code-for-blog/tree/master/2012/computed-goto-dispatch-tables

This compares three methods of interpreter dispatch:
1. loop + switch
2. computed goto
3. tail calls

### Requirements

gcc, clang, emcc, node, and Python

### To Use

Run the following commands:
```sh
./fill_file.py
./build.sh
./render_results.py
```

### Results

On my personal setup with:

* gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.1) 
* clang version 17.0.0 (https://github.com/llvm/llvm-project 671eeece457f6a5da7489f7b48f7afae55327b8b)
* emcc (Emscripten gcc/clang-like replacement + linker emulating GNU ld) 3.1.33 (c1927f22708aa9a26a5956bab61de083e8d3e463)
* node v20.0.0


I got the following numbers. The table normalized so that gcc + O2 + goto is 1.

#### O2:

|        |   gcc | clang |  emcc |
|--------|-------|-------|-------|
| switch | 1.258 | 1.144 | 1.891 |
| cgoto  | 1.000 | 1.074 | 2.127 |
| tcall  | 1.076 | 1.066 | 1.658 |


#### O3:

|        |   gcc | clang |  emcc |
|--------|-------|-------|-------|
| switch | 1.261 | 1.148 | 1.896 |
| cgoto  | 0.999 | 1.078 | 2.152 |
| tcall  | 1.076 | 1.068 | 1.666 |


#### Os:

|        |   gcc | clang |  emcc |
|--------|-------|-------|-------|
| switch | 1.444 | 1.191 | 1.897 |
| cgoto  | 1.110 | 1.073 | 2.136 |
| tcall  | 1.075 | 1.067 | 1.659 |
