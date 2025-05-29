# When users post an update on social media,such as a URL, image, status update etc.,
# other users in their network are able to view this new post on their news feed.
# Users can also see exactly when the post was published, i.e,
# how many hours, minutes or seconds ago.

# Since sometimes posts are published and viewed in different time zones, 
# this can be confusing. 
# You are given two timestamps of one 
# such post that a user can see on his newsfeed in the following format:

# Day dd Mon yyyy hh:mm:ss +xxxx

# Here +xxxx represents the time zone.
# Your task is to print the absolute difference (in seconds) between them.
#!/bin/python3

import math
import os
import random
import re
import sys
import datetime
from datetime import timezone

# # Complete the time_delta function below.
# def time_delta(t1, t2):
#     format_string = "%a %d %b %Y %H:%M:%S %z"

#     def parse_timestamp(ts):
#         # match = re.match(r"(\w{3}) (\d{2}) (\w{3}). (\d{2}:\d{2}:\d{2}) ([+-]\d{4})", ts)
#          match = re.match(r"(\w{3}) (\d{2}) (\w{3})\<\?\> (\d{2}:\d{2}:\d{2}) ([+-]\d{4})", ts)

#         if not match:
#             raise ValueError("Invalid timestamp format")

#         day_abbr, day, month_abbr, time_str, timezone_str = match.groups()
#         year = datetime.datetime.now().year  # Assume current year for calculation
#         full_timestamp_str = f"{day_abbr} {day} {month_abbr} {year} {time_str} {timezone_str}"
#         dt_object = datetime.datetime.strptime(full_timestamp_str, "%a %d %b %Y %H:%M:%S %z")
#         tz_hours = int(timezone_str[:3])
#         tz_minutes = int(timezone_str[3:]) if len(timezone_str) > 3 else 0
#         tz_offset = datetime.timedelta(hours=tz_hours, minutes=tz_minutes)
#         tz = timezone(tz_offset)
#         return dt_object.replace(tzinfo=tz)

#     datetime1 = parse_timestamp(t1)
#     datetime2 = parse_timestamp(t2)

#     difference = datetime2 - datetime1
#     return str(abs(int(difference.total_seconds())))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input())

#     for t_itr in range(t):
#         t1 = input()

#         t2 = input()

#         delta = time_delta(t1, t2)

#         fptr.write(delta + '\n')

#     fptr.close()



import math
import os
import random
import re
import sys
import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    format_string = "%a %d %b %Y %H:%M:%S %z"
    
    datetime1 = datetime.datetime.strptime(t1, format_string)
    datetime2 = datetime.datetime.strptime(t2, format_string)

    difference = abs((datetime1 - datetime2).total_seconds())
    return str(int(difference))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
