import pygame
from scripts.app import App


def main():
    pygame.init()
    app = App()
    app.run()
    pygame.quit()


if __name__ == "__main__":
    main()
