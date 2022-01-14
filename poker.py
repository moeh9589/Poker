import pygame
import random
import math
import time
from Card import Card as Card
from Hand import Hand as Hand

pygame.init()
pygame.font.init()

rows = 7
cols = 7

blue = (0, 0, 255)
white = (255, 255, 255)
red = (200, 0, 2)
black = (0, 0, 0)
green = (0, 205, 0)
light_red = (100, 0, 0)
gray = (52, 52, 52)
yellow = (255, 255, 0)
bright_green = (0, 255, 0)

Width = 700
Height = 800
window = pygame.display.set_mode((Width, Height))
players = []


def get_hands(deck):
    Card1 = 0,0
    Card2 = 0,0
    Hand1 = Hand(Card1, Card2)
    Hand2 = Hand(Card1, Card2)
    Hand3 = Hand(Card1, Card2)
    Hand4 = Hand(Card1, Card2)

    Hand5 = Hand(Card1, Card2)

    players.append(Hand1)
    players.append(Hand2)
    players.append(Hand3)
    players.append(Hand4)
    players.append(Hand5)

    for i in range(len(players)):
        players[i].get_cards(deck)

    for i in range (len(players)):
        print(str(players[i].Card1.value) + players[i].Card1.suit, str(players[i].Card2.value) + players[i].Card2.suit)


def main():

    suits = ["H", "S", "D", "C"]

    deck = [Card(value, suit) for value in range(1, 14) for suit in suits]

    window.fill(black)

    my_font = pygame.font.SysFont("javanesetext", 75)

    run = True

    pygame.display.update()

    get_hands(deck)

    for i in range(len(players)):
        turn_text = my_font.render(players[i].Card1.card_string() + players[i].Card2.card_string(), 1, red)
        window.blit(turn_text, (Width / 2 - turn_text.get_width() / 2, i*100))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            pygame.display.update()


main()
