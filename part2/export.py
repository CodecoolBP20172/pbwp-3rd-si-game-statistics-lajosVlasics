
# Export functions

import time
from reports import *


def export_report(report, input_file, output_file, arg=None):
    with open(output_file, "a") as f:
        if arg is None:
            f.write(str(report(input_file)) + "\n")
        else:
            f.write(str(report(input_file, arg)) + "\n")
        f.close()


def exporter():
    input_file = input("Choose your input file: ")
    output_file = input("Choose your output file: ")
    choosed_report = ""
    while True:
        reports_1arg = [
                        count_games,
                        get_latest,
                        sort_abc,
                        get_genres,
                        when_was_top_sold_fps,
                        get_most_played,
                        sum_sold,
                        get_selling_avg,
                        count_longest_title,
                        get_date_avg,
                        count_grouped_by_genre,
                        get_date_ordered]

        reports_2arg = [
                        decide,
                        count_by_genre,
                        get_line_number_by_title,
                        get_game]

        report_list_all = [
                        0,
                        count_games,
                        decide,
                        get_latest,
                        count_by_genre,
                        get_line_number_by_title,
                        sort_abc,
                        get_genres,
                        when_was_top_sold_fps,
                        get_most_played,
                        sum_sold,
                        get_selling_avg,
                        count_longest_title,
                        get_date_avg,
                        get_game,
                        count_grouped_by_genre,
                        get_date_ordered]
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
        8: when_was_top_sold_fps
        9: get_most_played
        10: sum_sold
        11: get_selling_avg
        12: count_longest_title
        13: get_date_avg
        14: get_game
        15: count_grouped_by_genre
        16: get_date_ordered
        """)

        choosed_report = int(input())

        if report_list_all[choosed_report] in reports_1arg:
            export_report(report_list_all[choosed_report], input_file, output_file)
            print("Export done!")
            time.sleep(1)
        if report_list_all[choosed_report] in reports_2arg:
            print("Give an argument too...")
            user_arg = input()
            export_report(report_list_all[choosed_report], input_file, output_file, arg=user_arg)
            print("Export done!")
            time.sleep(1)


def main():
    while True:
        try:
            exporter()
        except ValueError as err:
            print("Watcha ya doin maaan????\n %s" % err)            
            time.sleep(3)


main()
