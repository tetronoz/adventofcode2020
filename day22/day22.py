filename = "./input/input.txt"

import sys
import copy
from collections import deque

def build_decks_from_file(filename):
    deck1 = deque()
    deck2 = deque()

    p1 = False
    p2 = False
    with open(filename) as fp:
        for line in fp:
            if line == '\n':
                continue
            elif line.startswith("Player 1"):
                p1 = True
                p2 = False
                continue
            elif line.startswith("Player 2"):
                p1 = False
                p2 = True
                continue
            
            if p1:
                deck1.append(int(line.strip()))
            elif p2:
                deck2.append(int(line.strip()))
    
    return deck1, deck2

deck1, deck2 = build_decks_from_file(filename)

def count_score(deck):
    score = 0
    count = 0

    while deck:
        v = deck.pop()
        count += 1
        score += count * v
    
    return score


def play_game(deck1, deck2):
    
    while deck1 and deck2:
        c1 = deck1.popleft()
        c2 = deck2.popleft()

        if c1 > c2:
            deck1.append(c1)
            deck1.append(c2)
        elif c2 > c1:
            deck2.append(c2)
            deck2.append(c1)
        else:
            print("ERROR")
            sys.exit()

    return count_score(deck1) if deck1 else count_score(deck2)

def play_recursive_game(deck1, deck2):


    def recursive_combat(deck1, deck2):
        player_one_decks = {}
        player_two_decks = {}

        while deck1 and deck2:
            if tuple(deck1) in player_one_decks or tuple(deck2) in player_two_decks:
                return 1
            
            player_one_decks[tuple(deck1)] = True
            player_one_decks[tuple(deck2)] = True
            
            c1 = deck1.popleft()
            c2 = deck2.popleft()


            if len(deck1) >= c1 and len(deck2) >= c2:
                d1_copy = deck1.copy()
                d2_copy = deck2.copy()

                while c1 < len(d1_copy):
                    d1_copy.pop()
                
                while c2 < len(d2_copy):
                    d2_copy.pop()

                result = recursive_combat(d1_copy, d2_copy)
                
                if result == 1:
                    deck1.append(c1)
                    deck1.append(c2)
                elif result == 2:
                    deck2.append(c2)
                    deck2.append(c1)
                
            else:
                if c1 > c2:
                    deck1.append(c1)
                    deck1.append(c2)
                elif c2 > c1:
                    deck2.append(c2)
                    deck2.append(c1)
        
        if deck1:
            return 1
        if deck2:
            return 2
        
    winner_deck = recursive_combat(deck1, deck2)
    
    return count_score(deck2) if winner_deck == 2 else count_score(deck1)


print(play_game(deck1.copy(), deck2.copy()))
print(play_recursive_game(deck1, deck2))