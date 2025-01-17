import pygame
import sys
from game_logic import SnakeGame, Direction
from ai_agent import AIAgent
from gui import GUI

def main():
    pygame.init()
    game = SnakeGame(width=20, height=20)
    ai_agent = AIAgent(game)
    gui = GUI(game, cell_size=30)

    clock = pygame.time.Clock()
    running = True

    # Check command-line arguments for AI mode
    ai_mode = "AI" if len(sys.argv) > 1 and sys.argv[1].lower() == 'ai' else "Manual"
    
    if ai_mode == "AI":
        print("AI Mode activated. Choose AI algorithm:")
        print("1. Greedy Best-First Search")
        print("2. Uniform Cost Search")
        print("3. Breadth-First Search")
        print("4. Depth-First Search")
        print("5. Iterative Deepening Search")
        print("6. A* Search")
        choice = input("Enter a number (1-6): ")
        ai_agent.set_algorithm(int(choice))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and ai_mode == "Manual":
                if event.key == pygame.K_UP:
                    game.set_direction(Direction.UP)
                elif event.key == pygame.K_DOWN:
                    game.set_direction(Direction.DOWN)
                elif event.key == pygame.K_LEFT:
                    game.set_direction(Direction.LEFT)
                elif event.key == pygame.K_RIGHT:
                    game.set_direction(Direction.RIGHT)

        if ai_mode == "AI":
            move = ai_agent.get_move()
            game.set_direction(move)

        game.update()

        # Update GUI
        gui.draw(ai_mode)
        pygame.display.flip()

        clock.tick(10)  # Control game speed

    pygame.quit()

if __name__ == "__main__":
    main()

