#Создали главное меню
main_menu= ["Главное меню",
            "Открыть  телефонную книгу",
            "Сохранить телефонную книгу",
            "Показать контакт",
            "Создать контакт",
            "Найти контакт",
            "Изменить контакт",
            "Удалить контакт",
            "Выход"]


choice_main_menu = f"Выбери пункт из главного меню({1}-{len(main_menu)-1}): "
# print(choice_main_menu)
choice_main_menu_error = f"Нужно ввести число от 1 до {len(main_menu)-1}"

phone_book_opened_succes = "Телефонная книга открыта успешно"
phone_book_saved_succes = "Телефонная книга сохранена успешно"
empty_phone_book_error = 'Телефонная книга пуста или не открыта'

input_new_contact = ["Введите имя контакта: ",
                     "Введите номер контакта: ",
                     "Введите комментарий для контакта: "]


def new_contact_added_succs(name: str) -> str:
    return f"Контакт '{name}' успешно добавлен!"