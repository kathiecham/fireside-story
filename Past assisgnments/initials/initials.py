def get_initials(name):
    name = name.upper()
    name_list = name.split(' ')
    initals = len(name_list)
    if initals == 1:
        first_initial = name_list[0][0]
        return first_initial
    if initals == 2:
        first_initial = name_list[0][0]
        second_initial = name_list[1][0]
        return first_initial+second_initial
    if initals == 3:
        first_initial = name_list[0][0]
        second_initial = name_list[1][0]
        third_initial = name_list[2][0]
        return first_initial+second_initial+third_initial


def main():
    get_initials(name)

if __name__ == "__main__":
    main()

