def add_time(start, duration, day = None):
  
    start_time = start.split()[0].split(':')
    am_pm = start.split()[1]
    duration_time = duration.split(':')
    duration_day = 0
    padding = ""
    day_dict = {
        "monday" : 0, 
        "tuesday" : 1 , 
        "wednesday" : 2, 
        "thursday" : 3, 
        "friday" : 4, 
        "saturday" : 5, 
        "sunday" : 6, 
        }
    
    new_time_minute = int(start_time[1]) + int(duration_time[1])

    if(new_time_minute // 60 != 0):
        new_time_hour = int(start_time[0]) + int(duration_time[0]) + new_time_minute // 60
        new_time_minute = new_time_minute % 60
    else:
        new_time_hour = int(start_time[0]) + int(duration_time[0])

    if(len(str(new_time_minute)) == 1):
        padding = "0"

    while(new_time_hour > 24):
        duration_day = duration_day + 1
        new_time_hour = new_time_hour - 24
      
    if(new_time_hour > 12):
        if(am_pm == "AM"):
            am_pm = "PM"
        else:
            am_pm = "AM"
            duration_day = duration_day + 1
        new_time_hour = new_time_hour - 12

    if(new_time_hour % 12 == 0):
        if(am_pm == "AM"):
            am_pm = "PM"
        else:
            am_pm = "AM"
            duration_day = duration_day + 1
     
    if day != None:
        new_day = list(day_dict.keys())[list(day_dict.values()).index((day_dict.get(day.lower()) + duration_day) % 7)]
        new_time = str(new_time_hour) + ':' + padding + str(new_time_minute) + " " + am_pm + ", " + new_day[0].upper() + new_day[1:]
    else:  
        new_time = str(new_time_hour) + ':' + padding + str(new_time_minute) + " " + am_pm

    if(duration_day):
        if(duration_day == 1):
            new_time = new_time + " (next day)"
        else:
            new_time = new_time + " (" + str(duration_day) + " days later)"
  
    return new_time
