# Now we will try working with colours
# Import a library of functions called 'pygame'

import pygame

# Initialize the game engine

pygame.init()

# Lets define some colours

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = (700, 500)
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
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)
    # Close the window and quit.
    # If you forget this line, the program will "hang"
    # on exit if runnin from IDLE.

    pygame.quit()
