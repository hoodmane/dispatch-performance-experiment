## Interpreter Dispatch

Based on Eli Bendersky's blog:
https://github.com/eliben/code-for-blog/tree/master/2012/computed-goto-dispatch-tables

This compares three methods of interpreter dispatch:
1. loop + switch
2. computed goto
3. tail calls

### Results

On my personal setup with:

* gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.1) 
* clang version 17.0.0 (https://github.com/llvm/llvm-project 671eeece457f6a5da7489f7b48f7afae55327b8b)
* emcc (Emscripten gcc/clang-like replacement + linker emulating GNU ld) 3.1.33 (c1927f22708aa9a26a5956bab61de083e8d3e463)
* node v20.0.0


I got the following numbers: 

Table normalized so that gcc + O2 + goto is 1.

#### O2:

|        |   gcc | clang |  emcc |
|--------|-------|-------|-------|
| switch | 1.145 | 1.133 | 2.069 |
| cgoto  | 1.000 | 1.048 | 2.339 |
| tcall  | 1.061 | 1.065 | 1.659 |


#### O3:

|        |   gcc | clang |  emcc |
|--------|-------|-------|-------|
| switch | 1.150 | 1.121 | 2.152 |
| cgoto  | 0.983 | 1.070 | 2.342 |
| tcall  | 1.044 | 1.052 | 1.604 |


#### Os:

|        |   gcc | clang |  emcc |
|--------|-------|-------|-------|
| switch | 1.319 | 1.176 | 2.094 |
| cgoto  | 1.062 | 1.073 | 2.392 |
| tcall  | 1.120 | 1.031 | 1.638 |
