import pygame
from .scripts import player
from .scripts import asteroid

# helpful const definitions for later
TITLE = "py-asteroids"
WINDOW = (800, 600)
REFRESH = 60

def local_main() -> None:
    ...

# Additonal entrypoint used for: https://github.com/MUNComputerScienceSociety/snakepit
def game_init() -> None:
    local_main()

if __name__ == "__main__":
    local_main()