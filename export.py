
# Export functions

import time

from reports import *


def export_report(input_file, output_file, report, arg=None):
    with open(output_file, "a") as f:
        if arg is None:
            f.write(str(report(input_file)) + "\n")
        else:
            f.write(str(report(input_file, arg)) + "\n")
        f.close()


def main():
    while True:
        reports_1arg = [count_games, get_latest, sort_abc, get_genres, when_was_top_sold_fps]
        reports_2arg = [decide, count_by_genre, get_line_number_by_title]
        report_list_all = [
                        "this is a list of report functions",
                        count_games,
                        decide,
                        get_latest,
                        count_by_genre,
                        get_line_number_by_title,
                        sort_abc,
                        get_genres,
                        when_was_top_sold_fps]
        print ("\033c")
        print("Choose a report function by number!")
        print("""
        1: count_games
        2: decide
        3: get_latest
        4: count_by_genre
        5: get_line_number_by_title
        6: sort_abc
        7: get_genres
        8: when_was_top_sold_fps\n""")

        choosed_report = int(input())

        if report_list_all[choosed_report] in reports_1arg:
            export_report("game_stat.txt", "export.txt", report_list_all[choosed_report])
            print("Export done!")
            time.sleep(1)
            
        if report_list_all[choosed_report] in reports_2arg:
            print("Give an argument too...")
            user_arg = input()
            export_report("game_stat.txt", "export.txt", report_list_all[choosed_report], user_arg)
            print("Export done!")
            time.sleep(1)

main()
