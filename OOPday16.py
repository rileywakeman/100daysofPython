# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable
pokemon_index = PrettyTable()
pokemon_index.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
pokemon_index.add_column("Type", ["Electric", "Water", "Fire"])
pokemon_index.align = "l"

print(pokemon_index)


