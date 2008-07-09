VERSION = 07.08.10
PROGS = threads

SRCS = threads.c
OBJS = $(SRCS:.c=.o)

CFLAGS = -Wall -g $(DEFS) -Werror -I.
LDFLAGS = -lpthread  -lm -lX11 -lpng

DEFS = -DVERSION="\"$(VERSION)\""

all: $(PROGS)

asusosd: $(OBJS)

clean:
	$(RM) $(PROGS) *.o

