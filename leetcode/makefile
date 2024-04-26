# Compiler and compiler flags
CXX = clang++
CXXFLAGS = -Wall -std=c++11

# Target executable
TARGET = program

# Source file
SRC = Merge_Sorted_Array_88.cpp

all: $(TARGET) run

$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(SRC)

run:
	./$(TARGET)

clean:
	rm -f $(TARGET)
