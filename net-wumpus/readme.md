# net-wumpus

Basic cave with a stationary wumpus and hardcoded application protocol.

## Compiling

Use the Makefile to build the server with `make`.

If `make` is unavailable on your platform, compile the source files the same way as the target all:

```
javac wumpus/Room.java
javac wumpus/Player.java
javac wumpus/ClientHandler.java
javac wumpus/Game.java
javac wumpus/wumpServer.java
```

## Running

With the Makefile: `make server`

Without `make`: 

```
java wumpus.wumpServer
```
