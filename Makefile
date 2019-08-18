CC = gcc
CXX = g++
CFLAGS = -Wall -O
CXXFLAGS=$(CFLAGS) -std=c++11
OMP=$(CXXFLAGS) -fopenmp
FILES = ./version ./optimized ./naive ./test

all: $(FILES)

version:
	$(CXX) $(OMP) -o version version.cpp

optimized:
	$(CXX) $(OMP) -o optimized optimized.cpp

test:
	$(CXX) $(OMP) -o test test.cpp

naive:
	$(CXX) -o naive naive.cpp

clean:
	rm -f $(FILES) *.o *~
