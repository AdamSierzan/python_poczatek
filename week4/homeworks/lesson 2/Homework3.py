fav_colours = input(("Type your favourite calours here: "))
# fav_colours = list(fav_colours)
# ",".join(fav_colours)
print(fav_colours)

if "blue" in fav_colours.lower():
    print("Blue is one of your favourite colours!")


if fav_colours.lower().find("blue") != -1:
    print("Blue is one of your favourite colours!")
