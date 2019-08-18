CC = gcc
CXX = g++
CFLAGS = -Wall -O -g
CXXFLAGS=$(CFLAGS) -std=c++11
OMP=$(CXXFLAGS) -fopenmp
FILES = ./version

all: $(FILES)

version:
	$(CXX) $(OMP) -o version version.c
