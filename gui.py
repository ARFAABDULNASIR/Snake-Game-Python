import pygame

class GUI:
    def __init__(self, game, cell_size):
        self.game = game
        self.cell_size = cell_size
        self.width = game.width * cell_size
        self.height = game.height * cell_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake AI")
        self.font = pygame.font.Font(None, 36)

    def draw(self, ai_mode):
        self.screen.fill((50, 50, 50))  # Dark gray background

        # Draw grid
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, (70, 70, 70), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, (70, 70, 70), (0, y), (self.width, y))

        # Draw snake
        for i, segment in enumerate(self.game.snake):
            color = (0, 255, 0) if i == 0 else (0, 200, 0)  # Brighter green for head
            pygame.draw.rect(self.screen, color, (
                segment[0] * self.cell_size + 1,
                segment[1] * self.cell_size + 1,
                self.cell_size - 2,
                self.cell_size - 2
            ))

        # Draw food
        pygame.draw.circle(self.screen, (255, 0, 0), (
            self.game.food[0] * self.cell_size + self.cell_size // 2,
            self.game.food[1] * self.cell_size + self.cell_size // 2
        ), self.cell_size // 2 - 2)

        # Draw score
        score_text = self.font.render(f"Score: {self.game.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

        if self.game.game_over:
            game_over_text = self.font.render("Game Over", True, (255, 255, 255))
            text_rect = game_over_text.get_rect(center=(self.width // 2, self.height // 2))
            self.screen.blit(game_over_text, text_rect)

        # Draw AI mode indicator
        ai_text = self.font.render(f"Mode: {ai_mode}", True, (255, 255, 255))
        self.screen.blit(ai_text, (self.width - 150, 10))

