import pygame, sys, random, os
from button import Button
from sounds import Sounds
pygame.init()

class GameStart:
    def __init__(self):
        #GAME SETTINGS
        WIDTH, HEIGHT = 1000, 800
        SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("CLAW-A-DOG")
        
        #INITIALIZE SOUND EFFECTS
        self.sound_effect = Sounds() 
        
        #ASSIGN CLOCK AND FPS
        clock = pygame.time.Clock()
        FPS = 60
        
        #CURSOR
        CURSOR_IMAGE = pygame.image.load(os.path.join('images', 'cursor.cur'))
        CURSOR = pygame.cursors.Cursor((5, 5), CURSOR_IMAGE)
        pygame.mouse.set_cursor(CURSOR) 

        #BACKGROUNG IMAGE
        BG = pygame.image.load(os.path.join('images', 'bg.png'))
        
        #COLORS
        BLUE = (0, 102, 204)
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        YELLOW = (255, 255, 0)
        GREEN = (76, 187, 23)


        #RETURNS FONT AND SIZE
        def get_font(font, size):
            if font == 1:
                return pygame.font.Font(os.path.join('fonts', 'font1.ttf'), size)
            else:
                return pygame.font.Font(os.path.join('fonts', 'font2.ttf'), size)
             
              
        #MAIN MENU
        def main_menu():
            self.sound_effect.start_menu()          
             
            MENU_BG = pygame.image.load(os.path.join('images', 'menu_bg.png'))           
            MENU_TITLE = get_font(1, 100).render("MAIN MENU", True, BLUE)
            MENU_RECT = MENU_TITLE.get_rect(center=(500, 70))              
            PLAY_BUTTON = Button(image=pygame.image.load(os.path.join('images', 'play.png')), pos=(500, 175))
            DOG_IMAGE = pygame.image.load(os.path.join('images', 'aussie1.png'))  
            EXIT_BUTTON = Button(image=pygame.image.load(os.path.join('images', 'exit.png')), pos=(500, 700))
            
            while True:
                clock.tick(FPS)              
                menu_mouse_pos = pygame.mouse.get_pos()  
                
                SCREEN.blit(MENU_BG, (0, 0))
                SCREEN.blit(MENU_TITLE, MENU_RECT)
                SCREEN.blit(PLAY_BUTTON.image, PLAY_BUTTON.rect)
                split_string(SCREEN, get_font(2, 30), 50, 950, 250, "The game starts as a cat with 9 lives and the goal is to claw as many dogs as possible to earn points. Dog faces will randomly appear in different areas of the screen, earn points by trying to claw the dogs EXCEPT THE ONE DISPLAYED BELOW! When the cat claws the wrong dog, it gets sprayed and loses a life. Once all 9 lives are used up or time runs out, it's game over.", BLACK)
                SCREEN.blit(DOG_IMAGE, (150, 550))
                SCREEN.blit(EXIT_BUTTON.image, EXIT_BUTTON.rect)
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if PLAY_BUTTON.Input(menu_mouse_pos):
                            self.sound_effect.stop_menu()
                            play()
                        if EXIT_BUTTON.Input(menu_mouse_pos):
                            pygame.quit()
                            sys.exit()

                pygame.display.update()
                
                              
        #MULTI-LINE TEXT FORMATTING
        def split_string(screen, font, start_x, end_x, start_y, text, color):
            beginning_x = start_x
            beginning_y = start_y
            words = text.split(' ')

            for word in words:
                split_word = font.render(word, True, color)
                if split_word.get_width() + beginning_x <= end_x:
                    screen.blit(split_word, (beginning_x, beginning_y))
                    beginning_x += split_word.get_width() * 1.2
                else:
                    beginning_y += split_word.get_height() * 1.2
                    beginning_x = start_x
                    screen.blit(split_word, (beginning_x, beginning_y))
                    beginning_x += split_word.get_width() * 1.2


        #GAME SCREEN
        def play():
            ready_set_claw()
            self.sound_effect.start_game()   
        
            clawed = 0
            lives = 9
            dont_claw_me = False
            spray = False
            can_claw_dog = False
            timer = 5640
            spawn_time = 50
            
            while True:
                clock.tick(FPS)           
                play_mouse_pos = pygame.mouse.get_pos()
                
                if timer == 3760:
                    self.sound_effect.faster()
                    spawn_time = 45
                if timer == 1880:
                    self.sound_effect.faster()
                    spawn_time = 40
                
                if  timer % spawn_time == 0: 
                    whichDog = random.randint(1, 3)
                    if whichDog == 1:
                        im = pygame.image.load(os.path.join('images', 'aussie1.png'))
                        dont_claw_me = True
                    elif whichDog == 2:
                        im = pygame.image.load(os.path.join('images', 'aussie2.png'))
                        dont_claw_me = False
                    elif whichDog == 3:
                        im = pygame.image.load(os.path.join('images', 'aussie3.png'))
                        dont_claw_me = False
                    coorX = random.randint(50,950)
                    coorY = random.randint(200,750)
                    dog_button = Button(image=im, pos=(coorX, coorY))
                    update_screen(clawed, lives, dog_button, spray)
                    spray = False
                    can_claw_dog = True
                  
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()      
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if can_claw_dog:
                            can_claw_dog = False
                            if dog_button.Input(play_mouse_pos):
                                if dont_claw_me:
                                    spray = True
                                    lives -= 1
                                    self.sound_effect.angry_cat() 
                                else:
                                    clawed += 1
                                    self.sound_effect.whining_dog()  
                                    
                if timer == 0 or lives == 0:
                    update_screen(clawed, lives, dog_button, spray)
                    self.sound_effect.stop_game()
                    pygame.time.delay(1000)
                    end_game(clawed, lives)
                                
                timer -= 1                


        #UPDATE GAME SCREEN WITH NEW VALUES
        def update_screen(clawed, lives, dog_button, spray):
            TITLE_TEXT = get_font(1, 100).render("CLAW-A-DOG", True, GREEN)
            TITLE_RECT = TITLE_TEXT.get_rect(center=(500, 95))
            clawed_text = "CLAWED:" + str(clawed)
            lives_text = "LIVES:      " + str(lives) 
            SPRAY_IMAGE = pygame.image.load(os.path.join('images', 'spray.png'))
            
            SCREEN.blit(BG, (0, 0))
            SCREEN.blit(TITLE_TEXT, TITLE_RECT)
            SCREEN.blit(get_font(2, 40).render(clawed_text, True, YELLOW), (15, 50))
            SCREEN.blit(get_font(2, 40).render(lives_text, True, RED), (15, 100))
            if spray:
                SCREEN.blit(SPRAY_IMAGE, (750, 150))
            SCREEN.blit(dog_button.image, dog_button.rect)
            pygame.display.update()

        
        #GAME COUNTDOWN
        def ready_set_claw():
            countdown_text = ""
            countdown = 3
            position = (400, 275) 
            TITLE_TEXT = get_font(1, 100).render("CLAW-A-DOG", True, GREEN)
            TITLE_RECT = TITLE_TEXT.get_rect(center=(500, 95))   
            
            loop = True
            while loop:
                if countdown > 0:
                    self.sound_effect.beep1()
                    countdown_text = str(countdown)
                    countdown -= 1
                else:
                    self.sound_effect.beep2()
                    position = (50, 275)
                    countdown_text = "CLAW!!"
                    loop = False

                SCREEN.blit(BG, (0, 0))
                SCREEN.blit(TITLE_TEXT, TITLE_RECT)
                SCREEN.blit(get_font(2, 275).render(countdown_text, True, WHITE), position)
                pygame.display.flip()
                pygame.time.delay(1000)                                
        
        
        #END GAME MENU
        def end_game(clawed, lives):
            GAME_OVER_IMAGE = pygame.image.load(os.path.join('images', 'game_over.png'))
            WELL_DONE_IMAGE = pygame.image.load(os.path.join('images', 'well_done.png')) 
            TRY_AGAIN_IMAGE = pygame.image.load(os.path.join('images', 'try_again.png'))             
            BACK_MENU_BUTTON = Button(image=pygame.image.load(os.path.join('images', 'back_to_menu.png')), pos=(500, 650))
            
            if lives == 0:
                self.sound_effect.game_over()
                SCREEN.blit(GAME_OVER_IMAGE, (375, 200))
            elif clawed >= 50:
                self.sound_effect.well_done()
                SCREEN.blit(WELL_DONE_IMAGE, (375, 200))
            else:
                self.sound_effect.try_again()
                SCREEN.blit(TRY_AGAIN_IMAGE, (375, 275))
  
            while True: 
                clock.tick(FPS)             
                MENU_MOUSE_POS = pygame.mouse.get_pos()   
                SCREEN.blit(BACK_MENU_BUTTON.image, BACK_MENU_BUTTON.rect)
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if BACK_MENU_BUTTON.Input(MENU_MOUSE_POS):
                            main_menu()

                pygame.display.update()


        main_menu()
       
    
if __name__ == "__main__":
    game = GameStart()
    pygame.quit()