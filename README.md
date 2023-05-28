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

|        | gcc   | clang | emcc  |
|--------|-------|-------|-------|
| switch | 1.236 | 1.157 | 2.102 |
| goto   | 1.000 | 1.102 | 2.488 |
| tcall  | 1.051 | 1.063 | 1.705 |

#### O3:

|        | gcc   | clang | emcc  |
|--------|-------|-------|-------|
| switch | 1.110 | 1.335 | 2.134 |
| goto   | 0.949 | 1.146 | 2.618 |
| tcall  | 1.102 | 1.126 | 1.976 |

#### Os:

|        | gcc   | clang | emcc  |
|--------|-------|-------|-------|
| switch | 1.654 | 1.362 | 2.756 |
| goto   | 1.264 | 1.209 | 3.012 |
| tcall  | 1.276 | 1.244 | 1.917 |

