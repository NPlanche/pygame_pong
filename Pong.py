import numbers
import pygame, time, sys,random
import asyncio

def ball_animation():
    global ball_speed_y,ball_speed_x,player_score,opponent_score,score_time
    #moving ball 
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    #ball stays inside our screen 
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y*=-1

    if ball.left <= 0:
       player_score += 1
       score_time = pygame.time.get_ticks()

    if ball.right >= screen_width:
        opponent_score += 1
        score_time = pygame.time.get_ticks()



    #ball hitting the rectangles
    if ball.colliderect(player) or ball.colliderect(opponent):
       ball_speed_x *= -1 

def player_animation():
    player.y += player_speed
    #stop the players bar from moving offscreen
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
            player.bottom = screen_height

def opponent_ai():
	if opponent.top < ball.y:
		opponent.y += opponent_speed
	if opponent.bottom > ball.y:
		opponent.y -= opponent_speed

	if opponent.top <= 0:
		opponent.top = 0
	if opponent.bottom >= screen_height:
		opponent.bottom = screen_height

def ball_restart():
    global ball_speed_x,ball_speed_y,score_time
    current_time = pygame.time.get_ticks()
    ball.center = (screen_width/2,screen_height/2)
    
    if current_time - score_time < 700:
        number_three = game_font.render("3",False,lightgrey)
        screen.blit(number_three,(screen_width/2-10, screen_width/2+20))
    if 700 < current_time - score_time < 1400:
            number_two = game_font.render("2",False,lightgrey)
            screen.blit(number_two,(screen_width/2-10, screen_width/2+20))
    if 1400 < current_time - score_time < 2100:
            number_one = game_font.render("1",False,lightgrey)
            screen.blit(number_one,(screen_width/2-10, screen_width/2+20))

    if current_time - score_time < 2100:
        ball_speed_x, ball_speed_y = 0,0
    else:
        ball_speed_x = 7 * random.choice((1,-1))
        ball_speed_y = 7 * random.choice((1,-1))
        score_time = None

#general setup 
pygame.init()
clock = pygame.time.Clock()

#setting up window
screen_width = 1280
screen_height = 960
screen  = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')

#backgournd color
bg_color = pygame.Color('grey12')
lightgrey = (200,200,200)

#game rectangles 
ball = pygame.Rect(screen_width/ 2 - 15,screen_height/ 2 - 15,30,30)
player = pygame.Rect(screen_width-20,screen_width/2-70, 10,140)
opponent = pygame.Rect(10,screen_height/2-70,10,140)

#moving the ball 
ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 0 
opponent_speed = 7

#text varibles 
player_score = 0
opponent_score = 0

#timer
score_time = True

game_font = pygame.font.Font("freesansbold.ttf",32)


while True:
    #handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #cheks of any key has been pressed down
        if event.type == pygame.KEYDOWN:
            #checks if the down arrow was pressed
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball_animation()
    player_animation()
    opponent_ai()

    #visual 
    screen.fill(bg_color)
    pygame.draw.rect(screen, lightgrey, player)
    pygame.draw.rect(screen, lightgrey, opponent)
    pygame.draw.ellipse(screen, lightgrey, ball)
    pygame.draw.aaline(screen,lightgrey,(screen_width/2,0),(screen_width/2,screen_height))

    if score_time:
        ball_restart()

    #text payer surface (display payer score ) 
    player_text = game_font.render(f"{player_score}", False,lightgrey)
    #puts on surface
    screen.blit(player_text,(660,470))

    #text surface (display opponent score ) 
    opponent_text = game_font.render(f"{opponent_score}", False,lightgrey)
    #puts on surface
    screen.blit(opponent_text,(600,470))

    #updating the window
    pygame.display.flip()
    clock.tick(60)


