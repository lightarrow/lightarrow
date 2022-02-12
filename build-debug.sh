#!/bin/bash
gcc -g -Wall insertion-sort.c -o insertion-sort
gdb ./insertion-sort
(gdb) break 11
(gdb) run
