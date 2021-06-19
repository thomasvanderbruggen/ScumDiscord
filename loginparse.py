import codecs
import datetime as dt


def parse_login(file_name, last_login_dt):
    text = codecs.open(file_name, 'r', 'utf-16-le')
    usernames = []
    for line in text:
        if "logged in" in line:
            event = {}
            line = line.split("'")
            line[0] = line[0].split(":")[0]
            line[0] = line[0].replace("-", ".")
            year, month, day, hour, minute, second = [int(x) for x in line[0].split(".")]
            user_info = line[1].replace(" ", ",").replace(":", ",").split(",")[2]
            date = dt.datetime(year, month, day, hour, minute, second)
            if date > last_login_dt:
                event['user'] = user_info.split("(")[0]
                event['date'] = dt.datetime(year, month, day, hour, minute, second)
                usernames.append(event)
                last_login_dt = date
    return usernames
