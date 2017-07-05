
# Report functions
import math
from statistics import mean


def read_file(file_name):
    with open(file_name, "r") as f:
        read_data = f.read()
        f.close
        return read_data


def read_games(file_name):
    all_games = []
    for row in read_file(file_name).split("\n"):
        game = {}
        KEY_NAMES = ("title", "copies", "release", "genre", "publisher")
        i = 0
        for word in row.split("\t"):
            game[(KEY_NAMES[i])] = word
            i += 1
        if game["title"] == "":
            break
        game["copies"] = float(game["copies"])
        game["release"] = int(game["release"])
        all_games.append(game)
    return all_games


def count_games(file_name):
    return len(read_games(file_name))


def decide(file_name, year):
    for game in read_games(file_name):
        if game["release"] == int(year):
            return True


def get_latest(file_name):
    latest_release = 0
    for game in read_games(file_name):
        if game["release"] > latest_release:
            latest_game = game["title"]
            latest_release = game["release"]
    return latest_game


def count_by_genre(file_name, genre):
    genre_count = 0
    for game in read_games(file_name):
        if game["genre"] == genre:
            genre_count += 1
    return genre_count


def get_line_number_by_title(file_name, title):
    line_count = 1
    for game in read_games(file_name):
        if game["title"] == title:
            return line_count
        line_count += 1
    raise ValueError


def sort_abc(file_name):
    titles = []
    for game in read_games(file_name):
        titles.append(game["title"])
    sorted_titles = quicksort(titles)
    return sorted_titles


def quicksort(lst):
    if not lst:
        return []
    return (quicksort([x for x in lst[1:] if x < lst[0]]) +
            [lst[0]] +
            quicksort([x for x in lst[1:] if x >= lst[0]]))


def get_genres(file_name):
    genres_set = set()
    for game in read_games(file_name):
        genres_set.add(game["genre"])
    return sorted(list(genres_set), key=str.lower)


def when_was_top_sold_fps(file_name):
    sold_num = 0
    for game in read_games(file_name):
        if game["genre"] == "First-person shooter":
            if game["copies"] > sold_num:
                sold_num = game["copies"]
                release_year = game["release"]
    return release_year


def get_most_played(file_name):
    sold_num = 0
    for game in read_games(file_name):
        if game["copies"] > sold_num:
            sold_num = game["copies"]
            most_played_game = game["title"]
    return most_played_game


def sum_sold(file_name):
    copies_list = []
    for game in read_games(file_name):
        copies_list.append(game["copies"])
    return sum(copies_list)


"""def get_selling_avg(file_name):
    copies_list = []
    for game in read_games(file_name):
        copies_list.append(game["copies"])
    return mean(copies_list)"""


def get_selling_avg(file_name):
    copies_list = []
    for game in read_games(file_name):
        copies_list.append(game["copies"])
    return sum(copies_list) / len(copies_list)


def count_longest_title(file_name):
    max_title_lenght = 0
    for game in read_games(file_name):
        if len(game["title"]) > max_title_lenght:
            max_title_lenght = len(game["title"])
    return max_title_lenght


def get_date_avg(file_name):
    release_list = []
    for game in read_games(file_name):
        release_list.append(game["release"])
    return math.ceil(mean(release_list))


def get_game(file_name, title):
    game_properties = []
    for game in read_games(file_name):
        if game["title"] == title:
            for i in range(5):
                KEY_NAMES = ("title", "copies", "release", "genre", "publisher")
                game_properties.append(game[KEY_NAMES[i]])
            return game_properties


def count_grouped_by_genre(file_name):
    genre_groups = {}
    for game in read_games(file_name):
        if game["genre"] in genre_groups:
            genre_groups[game["genre"]] += 1
        else:
            genre_groups[game["genre"]] = 1
    return genre_groups


def get_date_ordered(file_name):
    year_and_title = []
    for game in read_games(file_name):
        ab = []
        ab.append(game["release"])
        ab.append(game["title"])
        year_and_title.append(ab)
    sorted_title_by_release = sorted(year_and_title, key=lambda student: student[1], reverse=False)
    sorted_title_by_release = sorted(sorted_title_by_release, key=lambda student: student[0], reverse=True)
    titles_by_release = []
    for i in sorted_title_by_release:
        titles_by_release.append(i[1])
    return titles_by_release
