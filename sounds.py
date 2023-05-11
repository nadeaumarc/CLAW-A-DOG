import pygame
import os

class Sounds:
    def __init__(self):
        self.MENU_MUSIC = pygame.mixer.Sound(os.path.join('audio', 'menu.mp3'))
        self.MENU_MUSIC.set_volume(0.50)
        self.BACKGROUND_MUSIC = pygame.mixer.Sound(os.path.join('audio', 'main.mp3'))
        self.BEEP_1 = pygame.mixer.Sound(os.path.join('audio', 'beep1.mp3'))
        self.BEEP_1.set_volume(0.25)
        self.BEEP_2 = pygame.mixer.Sound(os.path.join('audio', 'beep2.mp3'))
        self.BEEP_2.set_volume(0.25)
        self.ANGRY_CAT_SOUND = pygame.mixer.Sound(os.path.join('audio', 'cat_angry.mp3'))
        self.WHINING_DOG_SOUND = pygame.mixer.Sound(os.path.join('audio', 'dog_whining.mp3'))        
        self.GAME_OVER_SOUND = pygame.mixer.Sound(os.path.join('audio', 'game_over.mp3'))
        self.GAME_OVER_SOUND.set_volume(0.25)
        self.WELL_DONE_SOUND = pygame.mixer.Sound(os.path.join('audio', 'well_done.mp3'))
        self.WELL_DONE_SOUND.set_volume(0.25)
        self.TRY_AGAIN_SOUND = pygame.mixer.Sound(os.path.join('audio', 'try_again.mp3'))
        self.TRY_AGAIN_SOUND.set_volume(0.25)                

    def start_menu(self):
        self.MENU_MUSIC.play(-1)
        
    def stop_menu(self):
        self.MENU_MUSIC.stop()

    def start_game(self):
        self.BACKGROUND_MUSIC.play()
        
    def stop_game(self):
        self.background_music.stop()
        
    def beep1(self):
        self.BEEP_1.play()
        
    def beep2(self):
        self.BEEP_2.play()
        
    def angry_cat(self):
        self.ANGRY_CAT_SOUND.play()        
        
    def whining_dog(self):
        self.WHINING_DOG_SOUND.play()
        
    def game_over(self):
        self.GAME_OVER_SOUND.play()

    def well_done(self):
        self.WELL_DONE_SOUND.play()

    def try_again(self):
        self.TRY_AGAIN_SOUND.play()