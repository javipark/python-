## main.py

from game import Game

def main():
    game = Game()
    game.start_game()

    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.change_direction('up')
                elif event.key == pygame.K_DOWN:
                    game.change_direction('down')
                elif event.key == pygame.K_LEFT:
                    game.change_direction('left')
                elif event.key == pygame.K_RIGHT:
                    game.change_direction('right')

        # Update game state
        game.update()

        # Draw game elements
        game.draw()

if __name__ == "__main__":
    main()
