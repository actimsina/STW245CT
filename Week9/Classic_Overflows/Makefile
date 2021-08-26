
CC = gcc
CFLAGS = -m32 -g -z execstack  -fno-stack-protector -no-pie


overflow: classic.c
	$(CC) $(CFLAGS) classic.c -o overflow


all: overflow
