# Makefile for hoppity

CC = gcc 
FLAGS = -pedantic -W -Wall -O2 -ansi

hoppity : main.o
	$(CC)$(FLAGS) -o hoppity main.o

main.o : main.c
	$(CC)$(FLAGS) -c main.c