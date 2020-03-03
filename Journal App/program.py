import journal


def main():
    print_header()
    run_event_loop()


def print_header():
    print("----------------------")
    print("     Journal App     ")
    print("----------------------")


def run_event_loop():
    print('What do you want to do with your journal?')
    cmd = None
    journal_name = 'default'
    journal_data = journal.load(journal_name)

    while cmd != 'x':
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x':
            print("Sorry, we don't understand '{}'.".format(cmd))

    print('Well Done, Good Bye')

    journal.save(journal_name, journal_data)


def list_entries(data):
    print('Your journal entries: ')
    entries = reversed(data)
    for index, entry in enumerate(entries):
        print('* [{}] {}'.format(index+1, entry))


def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    # data.append(text)
    journal.add_entry(text, data)


if __name__ == '__main__':
    main()
