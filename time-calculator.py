from datetime import datetime, timedelta
def add_time(start, duration, day=""):

    st, sp = start.split(" ")           # start time and period
    sh = int(st.split(":")[0])          # start hour
    sm = int(st.split(":")[1])          # start min
    shl = sh if sp == "AM" else sh + 12 # start hour in 24 hrs

    dh = int(duration.split(":")[0])    # duration hour
    dm = int(duration.split(":")[1])    # duration min

    rt = datetime(2000, 1, 1, shl, sm)  # creatin a referance time on randdom date with start hour and min
    delta = timedelta(hours=dh, minutes=dm)
    ft = rt + delta                     # final time
    fdt = ft.strftime("%d")             # final date

    diff = int(fdt) - 1            
        
    if day == "":
        if diff == 0:
            return(ft.strftime('%#I:%M %p'))
        elif diff == 1:
            return(ft.strftime('%#I:%M %p (next day)'))
        else:
            return(ft.strftime(f'%#I:%M %p ({diff} days later)'))

    elif day != "":
        day = day.lower()
        days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        sdi = days.index(day)           # start day index
        fdi = sdi + diff if sdi + diff < 6 else sdi + diff % 7 - 7
        fd = days[fdi].title()

        if diff == 0:
            return(ft.strftime(f'%#I:%M %p, {fd}'))
        elif diff == 1:
            return(ft.strftime(f'%#I:%M %p, {fd} (next day)'))
        else:
            return(ft.strftime(f'%#I:%M %p, {fd} ({diff} days later)'))



print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("6:30 PM", "205:12"))
print(add_time("3:30 PM", "2:12"))
print(add_time("11:55 AM", "3:12"))
print(add_time("9:15 PM", "5:30"))
print(add_time("11:40 AM", "0:25"))
print(add_time("2:59 AM", "24:00"))
print(add_time("11:59 PM", "24:05"))
print(add_time("8:16 PM", "466:02"))
print(add_time("5:01 AM", "0:00"))
print(add_time("3:30 PM", "2:12", "Monday"))
print(add_time("2:59 AM", "24:00", "saturDay"))
print(add_time("11:59 PM", "24:05", "Wednesday"))
print(add_time("8:16 PM", "466:02", "tuesday"))