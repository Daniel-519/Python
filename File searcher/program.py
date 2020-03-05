import os
import collections


SearchResult = collections.namedtuple('SearchResult', 'file, line, text')


def main():
    print_the_header()
    folder = get_folder_from_user()
    if not folder:
        print("Sorry, we can't search that location.")
        return

    text = get_search_text_from_user()
    if not text:
        print("Sorry, we can't search for anything.")
        return

    matches = search_folder(folder, text)
    matches_count = 0
    for match in matches:
        matches_count += 1
    print("Found {} matches".format(matches_count))
    for match in matches:
        # print(match)
        print("------Match------")
        print('file: ' + match.file)
        print('line: {}'.format(match.line))
        print('match: ' + match.text)


def print_the_header():
    print('=====================')
    print('    File Searcher')
    print('=====================')
    print()


def get_folder_from_user():
    folder = input("What folder do you want to search?")
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    print('You are searching {}'.format(os.path.abspath(folder)))
    return os.path.abspath(folder)


def get_search_text_from_user():
    text = input("What are you searching for [single phrases only]?")
    return text.lower()


def search_folder(folder, text):
    all_matches = []
    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            matches = search_folder(full_item, text)
            all_matches.extend(matches)
        else:
            matches = search_file(full_item, text)
            all_matches.extend(matches)

    return all_matches


def search_file(filename, search_text):
    matches = []
    with open(filename, 'r', encoding='utf-8') as fin:
        line_number = 0
        for line in fin:
            line_number += 1
            if line.lower().find(search_text) >= 0:
                m = SearchResult(line=line_number, file=filename, text=line)
                matches.append(m)
        return matches


if __name__ == '__main__':
    main()
