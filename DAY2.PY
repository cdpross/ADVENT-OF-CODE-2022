# rock - A, X
# paper - B, Y
# scissors - C, Z


# Rock beats scissors
# Paper beats rock
# Scissors beat paper

# AX, AY, AZ / XA, YA, ZA
# BX, BY, BZ / XB, YX, ZB
# CX, CY, CZ / CX, CY, CZ


# points based on shape:
    # rock - 1
    # paper - 2
    # scissors - 3
# outcome of round score:
    # lost - 0
    # draw - 3
    # win - 6

rps = open(r'C:\Users\Courtney\OneDrive\Desktop\programming\ADVENT OF CODE 2022\DAY2\rock_paper_scissors.txt')
rps = rps.read().splitlines()
# rps = ['A Y','B X','C Z']

TeamXYZ_Points = 0

lost = 0
draw = 3
win = 6

rock = 1
paper = 2
scissors = 3

#PART 1
for n in rps:
    game = str(n)
    if game[2] == 'X': #rock
        TeamXYZ_Points = TeamXYZ_Points + rock 
        if game[0] == 'A': # rock
            TeamXYZ_Points = TeamXYZ_Points + draw
        if game[0] == 'B': # paper
            TeamXYZ_Points = TeamXYZ_Points + lost #rock loses paper
        if game[0] == 'C': #scissors
            TeamXYZ_Points = TeamXYZ_Points + win #rock beats scissors
    if game[2] == 'Y': #paper
        TeamXYZ_Points = TeamXYZ_Points + paper 
        if game[0] == 'B': # paper
            TeamXYZ_Points = TeamXYZ_Points + draw
        if game[0] == 'A': # rock
            TeamXYZ_Points = TeamXYZ_Points + win #paper beats rock
        if game[0] == 'C': #scissors
            TeamXYZ_Points = TeamXYZ_Points + lost #paper loses to scissors
    if game[2] == 'Z': #scissors
        TeamXYZ_Points = TeamXYZ_Points + scissors 
        if game[0] == 'C': # scissors
            TeamXYZ_Points = TeamXYZ_Points + draw
        if game[0] == 'A': # rock
            TeamXYZ_Points = TeamXYZ_Points + lost #scissors loses to rock
        if game[0] == 'B': #paper
            TeamXYZ_Points = TeamXYZ_Points + win #scissors beats paper
print(TeamXYZ_Points)  


# X - LOSE
# Y - DRAW
# Z - WIN

Points_Part2 = 0

#PART 2
for n in rps:
    game2 = str(n)
    if game2[2] == 'X': #lose
        Points_Part2 = Points_Part2 + lost 
        if game2[0] == 'A': # rock beats scissors
            Points_Part2 = Points_Part2 + scissors
        if game2[0] == 'B': # paper beats rock
            Points_Part2 = Points_Part2 + rock
        if game2[0] == 'C': # scissors beats paper
            Points_Part2 = Points_Part2 + paper
    if game2[2] == 'Y': #draw
        Points_Part2 = Points_Part2 + draw 
        if game2[0] == 'A': # rock
            Points_Part2 = Points_Part2 + rock
        if game2[0] == 'B': # paper
            Points_Part2 = Points_Part2 + paper 
        if game2[0] == 'C': # scissors
            Points_Part2 = Points_Part2 + scissors
    if game2[2] == 'Z': # win
        Points_Part2 = Points_Part2 + win 
        if game2[0] == 'A': # rock loses to paper
            Points_Part2 = Points_Part2 + paper
        if game2[0] == 'B': # paper loses to scissors
            Points_Part2 = Points_Part2 + scissors 
        if game2[0] == 'C': # scissors loses to rock
            Points_Part2 = Points_Part2 + rock
print(Points_Part2)