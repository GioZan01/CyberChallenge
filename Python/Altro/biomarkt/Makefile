.PHONY: clean

NAME=biomarkt

CC=g++
CXX=g++
CXXFLAGS=-std=c++17
LDFLAGS=-lpthread -ljemalloc -lpqxx

all: ${NAME}

${NAME}.o: ${NAME}.cpp
${NAME}: ${NAME}.o

clean:
	rm -fr *.o ${NAME}
