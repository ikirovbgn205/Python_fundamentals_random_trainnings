def main():

    contests_participated_counter = {}
    contests_participants = {}

    participants_data = input()

    while participants_data != "no more time":

        user, contest, points = participants_data.split(" -> ")

        if contest not in contests_participated_counter.keys():
            contests_participated_counter[contest] = 1
        else:
            contests_participated_counter[contest] += 1

        if user not in contests_participants.keys():
            contests_participants[user] = {}

        if contest not in contests_participants[user].keys():
            contests_participants[user][contest] = int(points)

        else:
            if contests_participants[user][contest] < int(points):
                contests_participants[user][contest] = int(points)

        participants_data = input()

    total_score_dictionary = {}

    for username in contests_participants.keys():
        total_score = 0
        for result in contests_participants[username].values():
            total_score += int(result)
        if username not in total_score_dictionary.keys():
            total_score_dictionary[username] = total_score

    for contest_name, count in contests_participated_counter.items():
        print(f"{contest_name}: {count} participants")
        row = 1
        for user in contests_participants.keys():
            if contest_name in contests_participants[user].keys():
                points = contests_participants[user][contest_name]
                print(f"{row}. {user} <::> {points}")
                row += 1
    print("Individual standings:")
    count = 1
    for individual, total_points in sorted(total_score_dictionary.items(), key=lambda x: (-x[1], x[0])):
        print(f"{count}. {individual} -> {total_points}")
        count += 1
main()