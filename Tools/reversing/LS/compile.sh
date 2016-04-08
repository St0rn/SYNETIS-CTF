#!/bin/sh

gcc -Wall -shared -fPIC -m32 -o lib32/hook32.so src/hook.c
gcc -Wall -shared -fPIC -o lib64/hook.so src/hook.c
