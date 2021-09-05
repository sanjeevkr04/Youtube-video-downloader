import datetime


def get_filesize(bytes) -> str:
    post_fix = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'ED', 'ZB', 'YB']
    counter = 0
    while bytes >= 1024:
        bytes /= 1024
        counter += 1
    return str('%.2f '%bytes) + post_fix[counter]

def format_time(seconds) -> str:
    t = datetime.timedelta(seconds=seconds)
    return str(t)