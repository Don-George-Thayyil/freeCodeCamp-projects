def add_time(start, duration, day = None):
    #seperate out starting time
    week_days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    if day:
        day = day.lower()
        day_index = week_days.index(day)

    start_elements = start.split(" ")
    period = start_elements[1]
    time_elements = start_elements[0].split(":")
    start_hour = int(time_elements[0])
    if period == "PM":
        start_hour += 12    
    start_minutes = int(time_elements[1])
    #seperate out time to add
    duration = duration.split(":")
    add_time_hour = int(duration[0])
    add_time_minutes = int(duration[1])
    
    #calculate days
    add_time_hour = int(add_time_hour)
    no_of_days = add_time_hour // 24    
    remaining_hour = add_time_hour % 24  

    total_minutes = add_time_minutes + start_minutes
    gained_hours = total_minutes // 60    
    remaining_minutes = total_minutes % 60
    #print(remaining_hour, start_hour, gained_hours)
    total_hour = start_hour + remaining_hour + gained_hours    
    gained_day = total_hour // 24
    current_hour = total_hour % 24
    total_days = no_of_days + gained_day
    #convert periods
    if day:
        day_index += total_days
        newday_index = day_index % 7
        day = week_days[newday_index]

    if current_hour // 12:
        period = "PM"
        current_hour %= 12
    else:
        period = "AM"
    if current_hour == 0:
        current_hour = "12"
    if remaining_minutes < 10:
        remaining_minutes = "0"+str(remaining_minutes)
    if day:
        day_up = ""
        day_up = ""+day[0].upper()
        for i in range(1, len(day)):
            day_up += day[i]
        
    if total_days:
        if total_days == 1:
            if day:
                return f"{current_hour}:{remaining_minutes} {period}, {day_up} (next day)"
            else:
                return f"{current_hour}:{remaining_minutes} {period} (next day)"
        if day:
            return f"{current_hour}:{remaining_minutes} {period}, {day_up} ({total_days} days later)"
        else:
            return f"{current_hour}:{remaining_minutes} {period} ({total_days} days later)"
    else:
        if day:
            return f"{current_hour}:{remaining_minutes} {period}, {day_up}"
        else:
            return f"{current_hour}:{remaining_minutes} {period}"
    
    
    


# print(add_time("3:30 PM", "83:30", "monday"))

#6:18 AM, Monday (20 days later)        6:18 AM (20 days later)