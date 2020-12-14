# The C compiler
CC=gcc
CXX=g++

# Debug flags
DBG_CXXFLAGS=-g -Wall -Wno-sign-compare

# Optimization flags
OPT_CXXFLAGS=-O2 -Wall -Wno-sign-compare

# libraries
INCLUDES=-I./src

LNK=src/libsla.a

sleighexample:	sleighexample.o
	$(CXX) $(DBG_CXXFLAGS) -o sleighexample sleighexample.o $(LNK)

sleighexample.o:	sleighexample.cc
	$(CXX) -c $(DBG_CXXFLAGS) $(INCLUDES) $< -o $@


clean:
	rm -rf *.o sleighexample

