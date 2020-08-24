import datetime

import arrow

from myresources.models import *


def get_date_and_time_by_id(id):
    schedule = Schedule.objects.get(pk=id)

    # recuperons les date starts et debut puis formtons en

    start_ = arrow.get(schedule.start)
    end_ = arrow.get(schedule.end)

    date_start_formated = datetime.datetime.strftime(start_.date(), '%A %d %B %Y')
    date_end_formated = datetime.datetime.strftime(end_.date(), '%A %d %B %Y')
    date_end_formated_time = end_.datetime.time().strftime('%Hh%S')
    date_start_formated_time = start_.datetime.time().strftime('%Hh%S')

    return {'date_start':date_start_formated, 'date_end':date_end_formated,
            'date_start_time':date_start_formated_time ,'date_end_time':date_end_formated_time}
