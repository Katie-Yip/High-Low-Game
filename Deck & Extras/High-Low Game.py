import random
import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
LIGHT_GREEN = (0, 120, 0)
RED = (255, 0, 0)
LIGHT_RED = (120, 0, 0)
TABLE_GREEN = (53, 101, 77)

MARGIN_WIDTH = 230
MARGIN_HEIGHT = 150

button_width_x = 220
button_height_x = 460
button_y = 370

state = 0
chances = 3
score = 0
choice = -1
result = -1
game_over = False

card_suits = ["Spades","Hearts","Clubs","Diamonds"]
card_suits = {"Spades":4,"Hearts":3,"Clubs":2,"Diamonds":1}
card_values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
card_values_define = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13}

pygame.init()

deck = []

small_font = pygame.font.Font("C:/Windows/Fonts/Arial.ttf",32)
large_font = pygame.font.Font("C:/Windows/Fonts/Arial.ttf",50)

# Set the width and height of the screen [width, height]
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode([WIDTH,HEIGHT])
 
pygame.display.set_caption("High-Low Card Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Create a card object to define value and suit.
class Card():
    def __init__(self,my_value,my_suit):
        self.value = my_value
        self.suit = my_suit
        self.image_path = "C:\\Users\\katie\\Desktop\\Deck & Extras\\" + self.value + self.suit + ".png.png"
        self.in_use = False      

card_backing = "C:\\Users\\katie\\Desktop\\Deck & Extras\\Card_Back.png.png"
table_top = "C:\\Users\\katie\\Desktop\\Deck & Extras\\table_top.png"

#Creating a deck of cards into a deck array.
for suit in card_suits:
    for value in card_values:
        deck.append(Card(value,suit))

# Creating the beginning backing card.
previous_card_image = pygame.image.load(card_backing).convert()
previous_card_image.set_colorkey(BLACK)
previous_card_image = pygame.transform.scale(previous_card_image,[100,160])

#Picking another not used card from deck.
current_card = deck[random.randrange(53)]
while current_card.in_use == True or current_card.value == "A" or current_card.value == "K":
    current_card = deck[random.randrange(53)]    
current_card.in_use = True

current_card_image = pygame.image.load(current_card.image_path).convert()
current_card_image.set_colorkey(BLACK)
current_card_image = pygame.transform.scale(current_card_image,[100,160])
current_card.in_use = True

next_card_image = pygame.image.load(card_backing).convert()
next_card_image.set_colorkey(BLACK)
next_card_image = pygame.transform.scale(next_card_image,[100,160])

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Clicked on the High Button
            if button_width_x <= mouse[0] <= button_width_x+125 and button_y <= mouse[1] <= button_y+60 and game_over == False:
                choice = 1 
            # Clicked on the Low Button
            elif button_height_x <= mouse[0] <= button_height_x+125 and button_y <= mouse[1] <= button_y+60 and game_over == False:
                choice = 0     
        # Button To Begin Game
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                state = 1
            if event.key == pygame.K_q:
                pygame.quit()      

        # --- Game logic should go here
        if choice != -1 and game_over == False:
            previous_card = current_card
            previous_card_image = pygame.image.load(previous_card.image_path).convert()
            previous_card_image.set_colorkey(BLACK)
            previous_card_image = pygame.transform.scale(previous_card_image,[100,160])

            #Removes Used Card From Deck
            current_card = deck[random.randrange(len(deck))]
            deck.remove(current_card)

            current_card_image = pygame.image.load(current_card.image_path).convert()
            current_card_image.set_colorkey(BLACK)
            current_card_image = pygame.transform.scale(current_card_image,[100,160])

            #Check if card is High or Low
            if current_card.value > previous_card.value:
                result = 1
            elif current_card.value < previous_card.value:
                result = 0
            else:
                result = -1

            # Check after attempt if correct.
            if result == -1:
                continue
            elif result == choice:
                score += 1
            else:
                chances -= 1

            #If Chances are 0
            if chances == 0 or len(deck) == 0:
                game_over = True
            
        # Reset choices
        choice = -1

    # # --- Screen-clearing code goes here
 
    # # Here, we clear the screen to white. Don't put other drawing commands
    # # above this, or they will be erased with this command.
 
    # # If you want a background image, replace this clear with blit'ing the
    # # background image.
    screen.fill(TABLE_GREEN)
 
    # --- Drawing code should go here
    mouse = pygame.mouse.get_pos()

    if state == 0:
        screen.fill(BLACK)
        table_top_image = pygame.image.load(table_top).convert()
        table_top_image.set_colorkey(WHITE)
        table_top_image = pygame.transform.scale(table_top_image,[WIDTH,HEIGHT])
        screen.blit(table_top_image,[0,0])
        
        start_button = large_font.render("Press SPACE to Begin",True,WHITE)
        start_button_rect = start_button.get_rect()
        start_button_rect.center = (WIDTH/2,HEIGHT/2)
        screen.blit(start_button, start_button_rect)

    elif state == 1:
        #Button Texts
        high_button = large_font.render("High",True,WHITE)
        high_button_rect = high_button.get_rect()
        high_button_rect.center = (button_width_x + 60,button_y + 30)

        low_button = large_font.render("Low",True,WHITE)
        low_button_rect = low_button.get_rect()
        low_button_rect.center = (button_height_x + 60,button_y + 30)

        # Buttons Choices
        if button_width_x <= mouse[0] <= button_width_x+125 and button_y <= mouse[1] <= button_y+60:
            pygame.draw.rect(screen,LIGHT_GREEN,[button_width_x,button_y,125,60])
        else:
            pygame.draw.rect(screen,GREEN,[button_width_x,button_y,125,60])
        if button_height_x <= mouse[0] <= button_height_x+125 and button_y <= mouse[1] <= button_y+60:
            pygame.draw.rect(screen,LIGHT_RED,[button_height_x,button_y,125,60])
        else:
            pygame.draw.rect(screen,RED,[button_height_x,button_y,125,60])

        #Scoreboard
        pygame.draw.rect(screen, TABLE_GREEN, [270, 40, 255, 90])
        score_string = "Score = " + str(score)
        score_text = small_font.render(score_string,True,BLACK)
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (WIDTH//2, 70)
    
        chances_string = "Chances = " + str(chances)
        chances_text = small_font.render(chances_string,True,BLACK)
        chances_text_rect = chances_text.get_rect()
        chances_text_rect.center = (WIDTH//2, 100)  

        #Load game elements
        screen.blit(high_button,high_button_rect)
        screen.blit(low_button,low_button_rect)
        screen.blit(previous_card_image,[MARGIN_WIDTH+240,MARGIN_HEIGHT])
        screen.blit(score_text, score_text_rect)
        screen.blit(chances_text, chances_text_rect)
        screen.blit(previous_card_image,[MARGIN_WIDTH,MARGIN_HEIGHT])
        screen.blit(current_card_image,[MARGIN_WIDTH+120,MARGIN_HEIGHT])
        screen.blit(next_card_image,[MARGIN_WIDTH+240,MARGIN_HEIGHT])   

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()