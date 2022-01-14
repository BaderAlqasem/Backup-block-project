import pygame
import random
import sys

pygame.init()

#Global Variables
score = 0
game_state = "intro"

#initialize stuff
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])

#Colors
WHITE = (255,255,255)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

font = pygame.font.SysFont('Calibri', 50, True, False)
text = font.render("Title",True,WHITE)
text = font.render("Your Game " , True, WHITE)
screen.blit(text, [400, 30])
pygame.display.flip()

# class for all blocks in the game
class Block(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):

        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()

def main():
    if game_state == "intro":
        button()
    elif game_state == "eat":
        eatBlocks()
    elif game_state == "avoid":
        avoidBlocks()


def button():
    global game_state
    #Local Variables
    # Screen size into a variable

    widthQuit = 850
    widthAvoid = 850
    widthEat= 850
    
    # stores the height of the screen into a variable
    heightQuit = 1100
    heightAvoid = 900
    heightEat = 700
    
    smallfont = pygame.font.SysFont('Corbel',35)
    #Buttons

    quitBtn = smallfont.render("Quit" , True , WHITE)
    avoidBtn = smallfont.render("Avoid" , True , WHITE)
    eatBtn = smallfont.render("Eat" , True , WHITE)

    
    font = pygame.font.SysFont('Calibri', 100, True, False)
    text = font.render("Score: ", True, WHITE)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            #checks if a mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:

                #if the mouse is clicked on the
                # button the game is terminated
                if widthQuit/2 <= mouse[0] <= widthQuit/2+140 and heightQuit/2 <= mouse[1] <= heightQuit/2+40:
                    pygame.quit()
                if widthAvoid/2 <= mouse[0] <= widthAvoid/2+140 and heightAvoid/2 <= mouse[1] <= heightAvoid/2+40:
                    pygame.quit()
                    game_state == "avoid"
                if widthEat/2 <= mouse[0] <= widthEat/2+140 and heightEat/2 <= mouse[1] <= heightEat/2+40:
                    pygame.quit()
                    game_state == "eat"

        # Coordinates of mouse
        mouse = pygame.mouse.get_pos()

        # Background color for buttons
        pygame.draw.rect(screen,GREY,[widthQuit/2,heightQuit/2,140,40])
        pygame.draw.rect(screen,GREY,[widthAvoid/2,heightAvoid/2,140,40])
        pygame.draw.rect(screen,GREY,[widthEat/2,heightEat/2,140,40])
    
        # Placing the text onto button
        screen.blit(quitBtn , (widthQuit/2+50,heightQuit/2))
        screen.blit(avoidBtn , (widthAvoid/2+50,heightAvoid/2))
        screen.blit(eatBtn , (widthEat/2+50,heightEat/2))  

        pygame.display.update()

def eatBlocks():
    name = input("Enter your name: ")

    # Starting coordinates of player block
    x1 = 0
    y1 = 0

    # Changing values of player block when moving
    x1_change = 0       
    y1_change = 0

    score = 0

    pygame.init()

    screen_width = 1000
    screen_height = 600
    screen = pygame.display.set_mode([screen_width, screen_height])

    block_list = pygame.sprite.Group()

    all_sprites_list = pygame.sprite.Group()

    for i in range(50):

        food = Block(YELLOW, 20, 15)

        # Set a random location for the block
        food.rect.x = random.randrange(screen_width)
        food.rect.y = random.randrange(screen_height)

        # Add the block to the list of objects
        block_list.add(food)
        all_sprites_list.add(food)

    # green player 
    player = Block(RED, 20, 20)
    all_sprites_list.add(player)
    # Loop until the user clicks the close button.
    loop = True
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # -------- Main Program Loop -----------
    while loop:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                loop = False
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and score >= 10:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_d and score >= 10:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_w and score >= 10:
                    y1_change = -10
                    x1_change = 0
                elif event.key == pygame.K_s and score >= 10:
                    y1_change = 10
                    x1_change = 0
                elif event.key == pygame.K_a:
                    x1_change = -5
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = 5
                    y1_change = 0
                elif event.key == pygame.K_w:
                    y1_change = -5
                    x1_change = 0
                elif event.key == pygame.K_s:
                    y1_change = 5
                    x1_change = 0
    

        # Positioning of player block updates after key is pressed
        x1 += x1_change
        y1 += y1_change

        # If player block hits walls, game over
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            loop = False
            print ("Game over")
        # Clear the screen
        screen.fill(BLACK)
        # player block positioning which updates after x1, y1 change is applied
        player.rect.x = x1
        player.rect.y = y1

        # See if the player block has collided with anything.
        blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
        # Check the list of collisions.
        for block in blocks_hit_list:
            score +=1
            print(score)

    #High Score Stuff
    file = open("highscore.txt", "a")
    file.write(str(score) + ", " + name + "\n")
    file.close()

    file = open("highscore.txt", "r")
    readthefile = file.readlines()
    sortedData = sorted(readthefile, reverse = True)

    print("Top 3 Scores!")
    print("Pos\tPoints , Name")

    for line in range(3):
        print(str(line + 1) + "\t" + str(sortedData[line]))

    # if score < 10:
    #     score = str(score)
    #     score = score.zfill(2)
    # else:
    #     pass

        # Check for win
        if score == 50:
            print("You won!")
            loop = False

        # Draw all the spites
        all_sprites_list.draw(screen)
        # Score stuff                             bold #Italic
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("Score: " + str(score), True, WHITE)
        screen.blit(text, [350, 10])

        #Update the screen with drawing.
        pygame.display.flip()
        # 60 FPS
        clock.tick(60)
    print("quit")
    pygame.quit()
    
def avoidBlocks():
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 250)
    
    # starting coordinates of player block
    x1 = 0
    y1 = 0
    blockDimensionX = 20
    blockDimensionY = 20

    # Hold updating values of x and y values
    x1_change = 0       
    y1_change = 0

    # Variables
    score = 0

    screen = pygame.display.set_mode([screen_width, screen_height])

    block_list_avoid = pygame.sprite.Group()
    block_list_collectcoin = pygame.sprite.Group()

    all_sprites_list = pygame.sprite.Group()

    player = Block(RED, blockDimensionX, blockDimensionY)
    all_sprites_list.add(player)

    loop = True

    clock = pygame.time.Clock()

    # Create obstacles
    for i in range(50):

        obstacle = Block(BLUE, 20, 15)

        obstacle.rect.x = random.randrange(screen_width)
        obstacle.rect.y = random.randrange(screen_height)

        block_list_avoid.add(obstacle)
        all_sprites_list.add(obstacle)

    # Create a coin
    coin = Block(YELLOW, 20, 15)
    coin.rect.x = 100
    coin.rect.y = 100

    # -------- Main Program Loop -----------
    while loop:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                loop = False
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and score >= 5:
                    x1_change = -5
                    y1_change = 0
                elif event.key == pygame.K_d and score >= 5:
                    x1_change = 5
                    y1_change = 0
                elif event.key == pygame.K_w and score >= 5:
                    y1_change = -5
                    x1_change = 0
                elif event.key == pygame.K_s and score >= 5:
                    y1_change = 5
                    x1_change = 0

                elif event.key == pygame.K_a and score >= 10:
                    x1_change = -7
                    y1_change = 0
                elif event.key == pygame.K_d and score >= 10:
                    x1_change = 7
                    y1_change = 0
                elif event.key == pygame.K_w and score >= 10:
                    y1_change = -7
                    x1_change = 0
                elif event.key == pygame.K_s and score >= 10:
                    y1_change = 7
                    x1_change = 0

                elif event.key == pygame.K_a:
                    x1_change = -3
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = 3
                    y1_change = 0
                elif event.key == pygame.K_w:
                    y1_change = -3
                    x1_change = 0
                elif event.key == pygame.K_s:
                    y1_change = 3
                    x1_change = 0
        # Positioning of player block updates after key is pressed
        x1 += x1_change
        y1 += y1_change 

        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            loop = False
            print ("Game over")

        # Clear the screen
        screen.fill(BLACK)

        # player block positioning which updates after x1, y1 change is applied
        player.rect.x = x1
        player.rect.y = y1

        # See if the player class has collided with anything.
        blocks_hit_list_avoid = pygame.sprite.spritecollide(player, block_list_avoid, True)
        block_hit_list_collectcoin = pygame.sprite.spritecollide(player, block_list_collectcoin, True)

        for block in block_hit_list_collectcoin:
            if block_hit_list_collectcoin:
                score += 1
                coin.rect.x = random.randrange(screen_width) 
                coin.rect.y = random.randrange(screen_height) 

        # Add the block to the list of objects
        block_list_collectcoin.add(coin)
        all_sprites_list.add(coin)


        # Check the list of collisions

        for block in blocks_hit_list_avoid:
            print("Game Over")
            print("Top 3 Scores!")
            print("Prs\tPoints , Name")
            pygame.quit() 

        # Check for win
        if score == 50:
            print("You won!")
            loop = False

        # Draw all the spites
        all_sprites_list.draw(screen)

        # Score stuff                             bold #Italic
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("Score: " + str(score), True, WHITE)
        screen.blit(text, [350, 10])

        #Update the screen with drawing.
        pygame.display.flip()

        # 60 FPS
        clock.tick(60)

    print("quit")

    pygame.quit()

main()