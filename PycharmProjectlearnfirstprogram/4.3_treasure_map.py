# don't change the code below
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]

map = [row1, row2, row3]

print(f"{row1} \n {row2} \n {row3}")

position = input("where do you want to put the treasure ? ")
# write the code below these line

horizental = int(position[0])
vertical = int(position[1])

selected_row = (map[vertical - 1])
(selected_row[horizental - 1]) = 'x'
