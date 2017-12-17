import datetime

def days_diff(date1, date2):

    start_year = date1[0]
    start_month = date1[1]
    start_day = date1[2]

    end_year = date2[0]
    end_month = date2[1]
    end_day = date2[2]

    start = datetime.date(start_year, start_month, start_day)
    end = datetime.date(end_year, end_month, end_day)

    gap = (end-start).days

    if gap > 0:
        return gap
    else:
        return -gap
