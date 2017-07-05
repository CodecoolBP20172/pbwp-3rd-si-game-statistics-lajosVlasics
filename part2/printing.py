
# Printing functions

from reports import *


def print_out(report, arg=None, input_file="game_stat.txt"):
    if arg is None:
        print(report(input_file))
    else:
        print(report(input_file, arg))


"""print_out(count_games)
print_out(decide, 2009)
print_out(get_latest)
print_out(count_by_genre, "RPG")
print_out(get_line_number_by_title, "Populous")
print_out(sort_abc)
print_out(get_genres)
print_out(when_was_top_sold_fps)
print_out(get_most_played)
print_out(sum_sold)
print_out(get_selling_avg)
print_out(count_longest_title)
print_out(get_date_avg)
print_out(get_game, "Populous")
print_out(count_grouped_by_genre)"""
print_out(get_date_ordered)
