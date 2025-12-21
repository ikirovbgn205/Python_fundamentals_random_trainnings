def main():
    initial_contests_dictionary = {}
    initial_contests = input()

    while initial_contests != "end of contests":

        contest, contest_password = initial_contests.split(":")

        initial_contests_dictionary[contest] = contest_password

        initial_contests = input()

    submissions_dictionary = {}
    submissions = input()

    while submissions != "end of submissions":

        current_submission, current_password, username, points = submissions.split("=>")

        if current_submission in initial_contests_dictionary.keys()\
            and current_password == initial_contests_dictionary[current_submission]:

            if username not in submissions_dictionary.keys():
                submissions_dictionary[username] = {}

            if current_submission not in submissions_dictionary[username].keys():
                submissions_dictionary[username][current_submission] = int(points)

            else:
                if submissions_dictionary[username][current_submission] < int(points):
                    submissions_dictionary[username][current_submission] = int(points)

        submissions = input()

    total_result_dictionary = {}

    for username in submissions_dictionary.keys():
        total_result = 0
        for result in submissions_dictionary[username].values():
            total_result += int(result)
        if username not in total_result_dictionary.keys():
                total_result_dictionary[username] = total_result

    best_result = max(total_result_dictionary.values())

    for best_result_username, result in total_result_dictionary.items():
        if result == best_result:
            print(f"Best candidate is {best_result_username} with total {best_result} points.")
            break

    print("Ranking:")
    for username in sorted(submissions_dictionary.keys()):
        print(f"{username}")
        for contest_latest, points_latest in sorted(submissions_dictionary[username].items(),key=lambda x: x[1], reverse=True):
            print(f"#  {contest_latest} -> {points_latest}")

main()