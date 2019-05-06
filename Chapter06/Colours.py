# Now we will try working with colours
# Import a library of functions called 'pygame'
# Imported sys library as well since I was getting an error
# video system not initialized

import pygame
import sys

# Initialize the game engine
pygame.init()

# Lets define some colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PI = 3.141592653

size = (400, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Professor Craven's Cool Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#------Main Program Loop ------

while not done:

    # --- Main event Loop

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
    # --- Game logic should go here
    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    # Draw on the screen a line from (0,0) to (100,100)
    # and 5 pixels wide.
    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)

    # Draw on the screen several lines from (0, 10) to (100, 110)
    # 5 pixel wide using a loop
    for y_offset in range(0, 100, 10):
        pygame.draw.line(screen, RED, [0, 10 + y_offset], [100, 110 + y_offset], 5)

    # Draw a rectangle
    pygame.draw.rect(screen, BLACK, [20, 20, 250, 100], 2)

    # Draw an ellipse, using a rectangle as the outside boundries
    pygame.draw.ellipse(screen, BLACK, [20, 20, 250, 100], 2)

    # Draw an arc as part of an ellipse. Use radians to determine what angle to draw.
    pygame.draw.arc(screen, BLACK, [20, 220, 250, 200], 0, PI / 2, 2)
    pygame.draw.arc(screen, GREEN, [20, 220, 250, 200], PI / 2, PI, 2)
    pygame.draw.arc(screen, BLUE, [20, 220, 250, 200], PI, 3 * PI / 2, 2)
    pygame.draw.arc(screen, RED, [20, 220, 250, 200], 3 * PI /2, 2 * PI, 2)


    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(240)

    # Close the window and quit.
    # If you forget this line, the program will "hang"
    # on exit if runnin from IDLE.

    pygame.quit()
    sys.exit()
