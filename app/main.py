import os
import sys
import pygame

# Ensure we run from this file's directory
# Import visualisations from subpackages
from .FourierSeries import main as fourier_main
from .StandingWaves import main as standing_main

# Shared style constants (matched to Fourier Series)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)
YELLOW = (255, 255, 0)
PURPLE = (203, 195, 227)
GRAY = (169, 169, 169)
DIM_GRAY = (16, 16, 16)
ORANGE = (255, 165, 0)
BROWN = (222, 184, 135)

WIDTH = 1080
HEIGHT = 720
FPS = 60

pygame.init()
pygame.display.set_caption("Physics Visualisations")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font_title = pygame.font.SysFont('didot.ttc', 48)
font_button = pygame.font.SysFont('didot.ttc', 36)

class MenuButton:
    def __init__(self, text, center_pos, size=(320, 80)):
        self.text = text
        self.width, self.height = size
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = center_pos
        self.text_surf = font_button.render(self.text, True, WHITE)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def draw(self, surface):
        pygame.draw.rect(surface, LIGHT_BLUE, self.rect, border_radius=12)
        surface.blit(self.text_surf, self.text_rect)

    def is_hovered(self, pos):
        return self.rect.collidepoint(pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False

def run_menu():
    # Center buttons vertically in middle of screen
    btn_spacing = 20
    btn_size = (320, 80)
    total_height = btn_size[1] * 2 + btn_spacing
    top_y = HEIGHT // 2 - total_height // 2

    fourier_btn = MenuButton("Fourier Series", (WIDTH // 2, top_y + btn_size[1] // 2), size=btn_size)
    standing_btn = MenuButton("Standing Waves", (WIDTH // 2, top_y + btn_size[1] // 2 + btn_size[1] + btn_spacing), size=btn_size)

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if fourier_btn.handle_event(event):
                fourier_main.main()
                # Reset screen after returning
                pygame.display.set_caption("Physics Visualisations")
                pygame.display.set_mode((WIDTH, HEIGHT))

            if standing_btn.handle_event(event):
                standing_main.main()
                # Reset screen after returning
                pygame.display.set_caption("Physics Visualisations")
                pygame.display.set_mode((WIDTH, HEIGHT))

        screen.fill(DIM_GRAY)

        title_surf = font_title.render("Physics Visualisations", True, PURPLE)
        title_rect = title_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
        screen.blit(title_surf, title_rect)

        fourier_btn.draw(screen)
        standing_btn.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    run_menu()
