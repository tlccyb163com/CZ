# -*- coding:utf8 -*-

import time
from apscheduler.schedulers.blocking import BlockingScheduler

def job():
    print ("Now time is {}".format(time.strftime("%y-%m-%d %H:%M:%S",time.localtime())))


if __name__=="__main__":
    scheduler=BlockingScheduler()
# 间隔10s执行
    scheduler.add_job(job,'interval', seconds=10)

#定时时间执行
#    scheduler.add_job(job, 'date', run_date='2020-04-03 10:55:00')

# 采用corn的方式,在每年 1-3、7-9 月份中的每个星期一、二中的 00:00, 01:00, 02:00 和 03:00 执行 job_func 任务
#    scheduler.add_job(job,'cron',month='1-3,7-9',day='0, tue', hour='0-3')

    '''
        year (int|str) – 4-digit year
        month (int|str) – month (1-12)
        day (int|str) – day of the (1-31)
        week (int|str) – ISO week (1-53)
        day_of_week (int|str) – number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun)
        hour (int|str) – hour (0-23)
        minute (int|str) – minute (0-59)
        econd (int|str) – second (0-59)

        start_date (datetime|str) – earliest possible date/time to trigger on (inclusive)
        end_date (datetime|str) – latest possible date/time to trigger on (inclusive)
        timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations (defaults to scheduler timezone)

        *    any    Fire on every value
        */a    any    Fire every a values, starting from the minimum
        a-b    any    Fire on any value within the a-b range (a must be smaller than b)
        a-b/c    any    Fire every c values within the a-b range
        xth y    day    Fire on the x -th occurrence of weekday y within the month
        last x    day    Fire on the last occurrence of weekday x within the month
        last    day    Fire on the last day within the month
        x,y,z    any    Fire on any matching expression; can combine any number of any of the above expressions
        '''
    scheduler.start()