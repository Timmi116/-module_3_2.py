def send_email(message, recipient, *, sender="university.help@gmail.com"):

    valid_domains = [".com", ".ru", ".net"]

    def is_valid_email(email):
        return "@" in email and any(email.endswith(domain) for domain in valid_domains)
    if not is_valid_email(sender) or not is_valid_email(recipient):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
        print(f"Отправляем письмо от {sender} к {recipient}")
    print(message)


send_email('Письмо успешно отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com', 'vasyok1337@gmail.com', sender='urban.info@gmail.com')
send_email('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru', 'urban.fan@mail.ru', sender='urban.info@gmail.com' )
send_email('urban.teacher@mail.uk ', 'urban.student@mail.uk')
send_email('Нельзя отправить письмо самому себе!','university.help@gmail.com', sender='university.help@gmail.com')
