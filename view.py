import text


def show_main_menu() -> int:
    for idex, menu in enumerate(text.main_menu):
        if idex != 0:
            print(f"{idex}.{menu}")
        else:
            print(menu)
    # show_main_menu()

    while True:
        choice = input(text.choice_main_menu)
        if choice.isdigit() and 0 < int(choice) < len(text.main_menu):
            return int(choice)
        print(text.choice_main_menu_error)


print(show_main_menu())


def show_contacts(phone_book: dict[int, [str]]):
    if phone_book:
        print("\n" + "=" * 71)
        for u_id, contact in phone_book.items():
            print(f' {u_id:>3}. {contact[0]:<20} | {contact[1]:<20} | {contact[2]:<20}')
        print("=" * 71 + "\n")
    else:
        show_message(text.empty_phone_book_error)


def show_message(message: str):
    print("\n" + '=' * len(message))
    print(message)
    print("=" * len(message) + '\n')


def input_new_contact() -> list[str]:
    return [input(massage) for massage in text.input_new_contact]
