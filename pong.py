import pygame, sys , random


'''
where this code differs from the tutorial video:
1. no global variables used
2. code for both "AI" and "non-AI" opponent (player1) is present. change AI = true or false and speed = player1_speed / AI_speed to change modes.
3. outputs the final result in a text file.
'''



pygame.init()
clock = pygame.time.Clock()
file = open('winner.txt' , "w+") #checking if it exits properly (my problem with arch linux)

#setup
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 960
screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
pygame.display.set_caption("Pong")



#making the objects - we need a ball, a centerline, a scoreboard, and 2 handles for players
ball = pygame.Rect( SCREEN_WIDTH/2 -15 , SCREEN_HEIGHT/2 - 15 ,30,30)
player1 = pygame.Rect( 10, SCREEN_HEIGHT/2 - 70 , 10,140)
player2 = pygame.Rect(SCREEN_WIDTH - 20, SCREEN_HEIGHT/2 - 70 , 10,140)
bg_color = (0,0,0)
white = (255,255,255)
player_color = (0,0,255)
AI_color = (255,0,0)
light_grey = (200,200,200) 

#othervariables
ball_speed_x = 8 * random.choice((1,-1))
ball_speed_y = 8 * random.choice((1,-1))
player2_speed = 0
player1_speed = 0
AI_speed = 7
player1_score = 0
player2_score = 0

def ground_reset(speed_x,speed_y):
    ball.center = (SCREEN_WIDTH/2 , SCREEN_HEIGHT/2)
    speed_x *= random.choice((-1,1))
    speed_y *= random.choice((-1,1))
    player1.top = SCREEN_HEIGHT/2 - 70
    player2.top = SCREEN_HEIGHT/2 - 70
    return speed_x,speed_y



def ball_animation(speed_x, speed_y , score1 , score2):
    ball.x += speed_x
    ball.y += speed_y

    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        speed_y *= -1
    if ball.left <=0:
        speed_x, speed_y = ground_reset(speed_x , speed_y)
        score2 += 1
    if ball.right >= SCREEN_WIDTH:
        speed_x, speed_y = ground_reset(speed_x , speed_y)
        score1 += 1
    
    if ball.colliderect(player1) or ball.colliderect(player2):
        speed_x *= -1
    return speed_x,speed_y, score1,score2


def player_animation(player , speed, AI):
    if player.top <= 0: 
        player.top = 0
    if player.bottom >= SCREEN_HEIGHT:
        player.bottom = SCREEN_HEIGHT
        
    if AI == False:
        player.y += speed
    else:
        if player.top < ball.y:
            player.top += speed
        if player.bottom > ball.y:
            player.top  -= speed
    


while player1_score < 5 and player2_score < 5:
    #checking if quit

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            file.write(f"Executed successfully.\n Player 1: {player1_score} \n Player 2: {player2_score}") #checking for proper exit
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player2_speed += 7
            if event.key == pygame.K_UP:
                player2_speed -= 7
            if event.key == pygame.K_s:
                player1_speed += 7
            if event.key == pygame.K_w:
                player1_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player2_speed -= 7
            if event.key == pygame.K_UP:
                player2_speed += 7
            if event.key == pygame.K_s:
                player1_speed -= 7
            if event.key == pygame.K_w:
                player1_speed += 7
        

    
    ball_speed_x , ball_speed_y , player1_score,player2_score = ball_animation(ball_speed_x,ball_speed_y , player1_score,player2_score)
    player_animation(player2 , player2_speed, False)
    player_animation(player1 , AI_speed, True)

    #drawings
    screen.fill(bg_color)
    pygame.draw.rect(screen, player_color, player2)
    pygame.draw.rect(screen, AI_color, player1)
    pygame.draw.aaline(screen, light_grey,(SCREEN_WIDTH/2,0),(SCREEN_WIDTH/2,SCREEN_HEIGHT))
    pygame.draw.ellipse(screen, white, ball)

    #display updates
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
file.write(f" Player 1: {player1_score}\n Player 2: {player2_score}")
if player1_score > player2_score:
    file.write("\nPlayer 1 wins!")
else:
    file.write("\nPlayer 2 wins.")
sys.exit()