CC=gcc
CFLAGS=-c -Wall
LDFLAGS=
SOURCES=DEV_Config.c main.c MCP2515.c
OBJECTS=$(SOURCES:.c=.o)
EXECUTABLE=send

all: $(SOURCES) $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS)
	$(CC) $(LDFLAGS) $(OBJECTS) -o $@ -l wiringPi

.c.o:
	$(CC) $(CFLAGS) $< -o $@ -l wiringPi

clean:
	rm -rf *.o $(EXECUTABLE)