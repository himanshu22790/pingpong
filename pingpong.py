import pygame, sys, random

def ball_animation():
    global ball_speed_x, ball_speed_y, opponent_score, player_score, score_time
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    #now what if the ball touches the boundary, we need to reverse the speed
    if ball.top <=0 or ball.bottom >= screen_height:
        #pygame.mixer.Sound.play(pong_sound)
        ball_speed_y *= -1
    #if player or opponent score
    if ball.left <=0:
        pygame.mixer.Sound.play(score_sound)
        score_time = pygame.time.get_ticks()
        player_score += 1
    if ball.right >= screen_width:
        pygame.mixer.Sound.play(score_sound)
        score_time = pygame.time.get_ticks()
        opponent_score += 1
    #colliderect for ball to collide
    if ball.colliderect(player) and ball_speed_x > 0:
        pygame.mixer.Sound.play(pong_sound)    
        ball_speed_x *= -1
    
    if ball.colliderect(opponent) and ball_speed_x < 0:
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_x *= -1    

def player_animation():
    player.y += player_speed
    #what if player 1 goes out of screen (below)
    if player.top <= 0:
        player.top=0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def comp_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_restart():
    global ball_speed_y, ball_speed_x,score_time

    current_time = pygame.time.get_ticks()
    ball.center = (screen_width/2, screen_height/2)

    if current_time - score_time < 700:
        number_three = game_font.render("3",False,col)
        screen.blit(number_three,(screen_width/2 - 10,screen_height/2 + 20))

    if 700 < current_time - score_time < 1400:
        number_two = game_font.render("2", False, col)
        screen.blit(number_two, (screen_width/2 - 10, screen_height/2 + 20))

    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render("1", False, col)
        screen.blit(number_one, (screen_width/2 - 10, screen_height/2 + 20))

    if current_time - score_time < 2100:
        ball_speed_x, ball_speed_y = 0,0
    
    else:
        ball_speed_y = 7*random.choice((1,-1))
        ball_speed_x = 7*random.choice((1,-1))
        score_time= None
    


pygame.init()
clock = pygame.time.Clock()

screen_height = 600
screen_width = 1200
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('PingPong by Himanshu')

#Game Rectangle
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 20, 20)
player = pygame.Rect(screen_width-20,screen_height/2-70,10,120)
opponent=pygame.Rect(10,screen_height/2-70, 10, 120)

#horizontal and vertical speeds

ball_speed_x = 7* random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7

#Text Variables
player_score = 0
opponent_score = 0
game_font = pygame.font.SysFont("comicsansms",32)

bg_color = (0,100,0)
col = pygame.Color("Yellow")
score_col = pygame.Color("blue")

#game variables
score_time = True

#Sound
pong_sound = pygame.mixer.Sound("pong.ogg")
score_sound = pygame.mixer.Sound("score.ogg")


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        #release
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    
    ball_animation()
    player_animation()
    comp_ai()


    screen.fill(bg_color)
    pygame.draw.rect(screen,col,player)
    pygame.draw.rect(screen,col,opponent)
    pygame.draw.ellipse(screen,col,ball)
    pygame.draw.aaline(screen,col,(screen_width/2,0),(screen_width/2,screen_height))#anti alias line
    if score_time:
        ball_restart()

    created_by = game_font.render("Created By Himanshu Bakshi", False, col)
    screen.blit(created_by, (400, 20))
    player_text = game_font.render("Player score: " + f"{player_score}",False,score_col)
    screen.blit(player_text,(650,550))
    opponent_text = game_font.render("Computer score: " + f"{opponent_score}", False, score_col)
    screen.blit(opponent_text, (250, 550))

    pygame.display.flip()
    # loop runs 60 times per second else computer will run 10000s frames per sec
    clock.tick(60)

pygame.quit()





