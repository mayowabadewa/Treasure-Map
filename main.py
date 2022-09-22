row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
# Storing row information in a variable
map = [row1, row2, row3]
# Visualization for the user to make selection
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

#coverting the position input to a two item list
split = list(position)
# Storing the column and row positions in respective vars and changing data type
column = int(split[0])
row = int(split[1])
# Marking the spot "X" to the selected positions
map[row -1][column -1] = "X"
# "X" marks the spot.
print(f"{row1}\n{row2}\n{row3}")