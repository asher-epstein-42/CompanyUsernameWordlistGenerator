def main():
    welcome()
    company_name = input("input company name(if there is no company, press Enter): ").strip()
    filename = input("input the your filename: ")
    user_file = read_username_list(filename)
    write_wordlist((name_list(user_file)), company_name)
    print('Username wordlist generated at UsernameWordList.txt')


# reads the file uploaded by the user
def read_username_list(filename: str):
    user_file = open(filename, "r").read()
    return user_file


# creates wordlist of possible usernames
def write_wordlist(name_list: list, company_name: str):
    for full_name in name_list:
        username_list = username_patterns(full_name[0], full_name[1], company_name)
        save_to_wordlist(username_list)


# creates list of names from the user file
def name_list(user_file: str):
    list_of_full_names = user_file.split('\n')
    list_of_names = []
    for i in range(len(list_of_full_names)):
        list_of_names.append(list_of_full_names[i].split())
    return list_of_names


# saves possible usernames to the UsernameWordList.txt
def save_to_wordlist(username_wordlist: list):
    for username in username_wordlist:
        f = open("UsernameWordList.txt", "a")  # opens a file and appends to existing content
        f.write(f"{username}\n")


# creates every possible pattern for a username
def username_patterns(first: str, last: str, company_name: str):
    patterns_list = [f'{first}{last}', f'{first}.{last}', f'{first}-{last}', f'{first[0]}{last}', f'{last}{first}',
                        f'{first}{last[0]}', f'{first}_{last}', f'{last}_{first}']
    # if the user if the user inputted a company name
    if company_name != '':
        company_patterns_list = [f'{username}@{company_name}.com' for username in patterns_list]
        return patterns_list + company_patterns_list
    return patterns_list


def welcome():
    print("Welcome To The Username Wordlist Generator!")
    print("Please create a file with full names(one name in each line,"
          "with a space between the first and the last name")
    print("made by Asher-Epstein-42", end="\n\n")


if __name__ == '__main__':
    main()


