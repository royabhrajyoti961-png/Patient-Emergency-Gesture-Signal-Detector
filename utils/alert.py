import pygame

pygame.mixer.init()

def play_alert():
    pygame.mixer.music.load("assets/alarm.wav")
    pygame.mixer.music.play()

def show_alert(message):
    print("ALERT:", message)
