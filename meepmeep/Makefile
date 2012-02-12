# Makefile for meepmeep

CC = gcc 
FLAGS = -pedantic -W -Wall -O2 -ansi

meepmeep : main.o
	$(CC)$(FLAGS) -o meepmeep main.o

main.o : main.c
	$(CC)$(FLAGS) -c main.c