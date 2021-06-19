import configparser

config = configparser.ConfigParser()
config['FTP'] = {'host': 'ftp_host',
                 'usr': 'usr',
                 'pwd': 'password',
                 'path': 'ftp/folder/structure'}
config['DISCORD'] = {'token': 'discord_bot_token',
                     'delay': 'time_in_seconds',
                     'kill_channel': 'discord_channel_id',
                     'chat_channel': 'discord_channel_id',
                     'login_channel': 'discord_channel_id'}

with open('config.ini', 'w') as configfile:
    config.write(configfile)
