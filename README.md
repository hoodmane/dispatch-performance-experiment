Based on Eli Bendersky's blog:
https://github.com/eliben/code-for-blog/tree/master/2012/computed-goto-dispatch-tables

I addded a third tail call method. To use need:
1. gcc
2. clang
3. emcc
4. node version 20 (on older versions it would work with an experimental flag)

Running `make` generates a time table in `results.txt`.
