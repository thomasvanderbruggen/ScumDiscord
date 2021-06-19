import ftplib
import configparser
import datetime as dt
import os


def convert_to_datetime(date):
    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:8])
    hour = int(date[8:10])
    minute = int(date[10:12])
    second = int(date[12:14])
    return dt.datetime(year, month, day, hour, minute, second)


def check_files(ftp_info, last_chat_dt, last_kill_dt, last_login_dt):
    new_files = []
    ftps = ftplib.FTP()
    ftps.connect(ftp_info['host'], int(ftp_info['port']))
    ftps.login(ftp_info['usr'], ftp_info['pwd'])
    ftps.cwd(ftp_info['path'])
    for file_data in ftps.mlsd():
        file_name, meta = file_data
        modified_date = convert_to_datetime(meta['modify'])
        if file_name.startswith("chat_"):
            if modified_date > last_chat_dt:
                new_files.append(file_name)
        elif file_name.startswith("kill_"):
            if modified_date > last_kill_dt:
                new_files.append(file_name)
        elif file_name.startswith("login_"):
            if modified_date > last_login_dt:
                new_files.append(file_name)
    for file in new_files:
        with open(file, "wb") as wfile:
            ftps.retrbinary('RETR %s' % file, wfile.write)
    return new_files


def delete_files(files):
    for i in range(len(files)):
        print("deleting ", files[i])
        os.remove(files[i])


