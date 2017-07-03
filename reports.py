
# Report functions

def read_file(file_name):
    with open(file_name, "r") as f:
        read_data = f.read()
        f.close
        return read_data


def read_to_dict(file_name):
    all_games = []
    key_names = ("title", "copies", "release", "genre", "publisher")
    read_data = read_file(file_name)
    for row in read_data.split("\n"):
        game_for_dict = {}
        i = 0
        for word in row.split("\t"):
                game_for_dict[(key_names[i])] = word
                i += 1
        if game_for_dict["title"] == "":  # clean
            break
        all_games.append(game_for_dict)
    return all_games


def count_games(file_name):
    return len(read_to_dict(file_name))


def decide(file_name, year):
    for game in read_to_dict(file_name):
        if int(game["release"]) == year:
            return True


def get_latest(file_name):
    latest_game = ""
    latest_release = 1900
    for game in read_to_dict(file_name):
        if int(game["release"]) > latest_release:
            latest_game = game["title"]
            latest_release = int(game["release"])
    return latest_game


def count_by_genre(file_name, genre):
    genre_count = 0
    for game in read_to_dict(file_name):
        if game["genre"] == genre:
            genre_count += 1
    return genre_count


def get_line_number_by_title(file_name, title):
    line_count = 1
    for game in read_to_dict(file_name):
        if game["title"] == title:
            return line_count
        line_count += 1
    raise ValueError


def sort_abc(file_name):
    titles = []
    sorted_titles = []
    for game in read_to_dict(file_name):
        titles.append(game["title"])
    sorted_titles = quicksort(titles)
    return sorted_titles


def quicksort(lst):
    if not lst:
        return []
    return (quicksort([x for x in lst[1:] if x <  lst[0]])
            + [lst[0]] +
            quicksort([x for x in lst[1:] if x >= lst[0]]))


def get_genres(file_name):
    genres_set = set()
    for game in read_to_dict(file_name):
        genres_set.add(game["genre"])
    return sorted(list(genres_set), key=str.lower)


def when_was_top_sold_fps(file_name):
    sold_num = 0
    release_year = 0
    for game in read_to_dict(file_name):
        if game["genre"] == "First-person shooter":
            if float(game["copies"]) > sold_num:
                sold_num = float(game["copies"])
                release_year = int(game["release"])
    return release_year


#print(count_games("game_stat.txt"))
#decide("game_stat.txt", 2000)
#get_latest("game_stat.txt")
#print(count_by_genre("game_stat.txt", "First-person shooter"))
#print(get_line_number_by_title("game_stat.txt", "Counter-Strike"))
#print(sort_abc("game_stat.txt"))
#print(get_genres("game_stat.txt"))
#when_was_top_sold_fps("game_stat.txt")
