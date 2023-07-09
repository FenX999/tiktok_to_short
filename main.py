from conf.reports import path_configuration
from tools.scheduler import validate_schedule
from short.run import run_short, fetch_file_or_none
from short.tiktok_downloader import prep_daily_post
from tools.first_run import check_all_conf
                      
if __name__ == "__main__":
    check_all_conf()
    paths = path_configuration(tiktok = True)

    check_file = fetch_file_or_none(paths['video_source'])
    if check_file:
        while True:
            schedule = ['00:45', '04:23', '08:42', '12:05', '16:28', '20:50']
            start = validate_schedule(schedule)
            if start :
               run_short()
    else:
        prep_daily_post()
