line_one = input().split()
line_two = input().split()
line_three = input().split()

player_one = False
player_two = False
winner = ''


if ((line_one[0] == '1' and line_two[1] == '1' and line_three[2] == '1') or
        (line_one[2] == '1' and line_two[1] == '1' and line_three[0] == '1')):
    player_one = True

elif ((line_one[0] == '2' and line_two[1] == '2' and line_three[0] == '2') or
      (line_one[2] == '2' and line_two[1] == '2' and line_three[0] == '2')):
    player_two = True

elif line_one[0] =='1' and line_one[1] == '1' and line_one[2] == '1':
    player_one = True

elif line_two[0] =='2' and line_two[1] == '2' and line_two[2] == '2':
    player_two = True

else:
    for i in range(3):
        if line_one[i] == '1' and line_two[i] == '1' and line_three[i] == '1':
            player_one = True
            break

        elif line_one[i] == '2' and line_two[i] == '2' and line_three[i] == '2':
            player_two = True
            break

if player_one:
    winner = "First player won"
elif player_two:
    winner = "Second player won"
else:
    winner = "Draw!"

print(winner)