
# Printing functions

from reports import *

print(count_games("game_stat.txt"))
print(decide("game_stat.txt", 2009))
print(get_latest("game_stat.txt"))
print(count_by_genre("game_stat.txt", "RPG"))
print(get_line_number_by_title(("game_stat.txt"), "Populous"))
print(sort_abc("game_stat.txt"))
print(get_genres("game_stat.txt"))
print(when_was_top_sold_fps("game_stat.txt"))
