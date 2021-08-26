# Build the first overflow target

CC = gcc
CFLAGS = -m32 -g -z execstack


firstOverflow: firstOverflow.c

	$(CC) $(CFLAGS) firstOverflow.c -o firstOverflow


all: firstOverflow

