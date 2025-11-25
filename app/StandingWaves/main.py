# Imports
import pygame 
pygame.init()
import numpy as np
from .axes import axes
from .standing_wave_functions import *
from .curve import curve
from .button import Button

# Constants (matched to Fourier Series)
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
BUTTON_PURPLE = (134, 91, 235)


WIDTH = 1080
HEIGHT = 720
FPS = 60

def main() -> None :

    # Define primary screen variables
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Standing Waves")
    clock = pygame.time.Clock()
    running = True

    # Define physical string properties
    string_length   = 200
    string_elements = np.linspace(0,800,500)

    sinusoid_locked_ends    = curve(WHITE,[[] for _ in range(len(string_elements))])
    sinusoid_locked_end     = curve(RED,[[] for _ in range(len(string_elements))])
    sinusoid_unlocked_ends  = curve(PURPLE,[[] for _ in range(len(string_elements))])

    # Example placeholder buttons (kept from original)

    # Create an axes
    main_axes = axes(screen,800,10,400,10)

    # Return to menu button (bottom left)
    back_button_rect = pygame.Rect(20, HEIGHT - 60, 200, 40)
    back_button_text = Button.font.render("Return to menu", True, WHITE)

    # Screen loop
    while running : 

        # Event handling
        for event in pygame.event.get() :

            if event.type == pygame.QUIT :
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(event.pos):
                    running = False

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE :
                    running = False


        # Logic steps
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_UP] :
            axes.scale += 0.025

        if keys_pressed[pygame.K_DOWN] :
            axes.scale -= 0.025    

        # Update entities
        axes.update(main_axes)

        for i,x in enumerate(string_elements) : 

            t = pygame.time.get_ticks()/1000

            curve.update(sinusoid_locked_ends,[x,standing_wave_locked_ends(x,t,amplitude=200,order=1,string_length=string_length,wave_speed=100)],i)   
            curve.update(sinusoid_locked_end,[x,standing_wave_locked_end(x,t,amplitude=200,order=1,string_length=string_length,wave_speed=100)],i)   
            curve.update(sinusoid_unlocked_ends,[x,standing_wave_unlocked_ends(x,t,amplitude=200,order=1,string_length=string_length,wave_speed=100)],i)   

        for entity in Button.buttons : 
            entity.update()

        # Drawing
        screen.fill(DIM_GRAY)

        main_axes.draw(screen)

        main_axes.draw_to_axes_curve(screen,sinusoid_locked_ends)
        main_axes.draw_to_axes_curve(screen,sinusoid_locked_end)
        main_axes.draw_to_axes_curve(screen,sinusoid_unlocked_ends)

        for entity in Button.buttons :
            entity.draw(screen)

        # Draw return-to-menu button
        pygame.draw.rect(screen, LIGHT_BLUE, back_button_rect, border_radius=12)
        screen.blit(back_button_text, back_button_text.get_rect(center=back_button_rect.center))

        pygame.display.flip()

        clock.tick(FPS)

if __name__ == "__main__" :
    main()
