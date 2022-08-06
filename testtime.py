import datetime


def write_time():
    today = datetime.date.today()
    formatted_today = today.strftime('%d')
    print(formatted_today)

    with open('checklist.txt', 'w+') as f:
        f.write(formatted_today)
        f.close()


def get_time():
    today = datetime.date.today()
    formatted_today = today.strftime('%d')

    with open('checklist.txt', 'r+') as f:
        last_modified = f.read()
        f.close()
    if formatted_today == last_modified:
        return True
    else:
        return False
