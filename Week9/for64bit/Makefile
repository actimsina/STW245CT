
CC = gcc
CFLAGS = -g -z execstack  -fno-stack-protector -no-pie


overflow: classic.c
	$(CC) $(CFLAGS) classic.c -o overflow


all: overflow
