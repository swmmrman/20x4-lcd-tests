from rpi_lcd import LCD
import time

lcd = LCD()
lines = []
s_time = time.time()
s_time_str = time.strftime("%H:%M:%S", time.localtime(s_time))
while True:
    c_time = time.time()
    c_time_str = time.strftime("%H:%M:%S", time.localtime(c_time))
    d_time = c_time - s_time
    d_time_str = time.strftime("%H:%M:%S", time.gmtime(d_time))
    date = time.strftime('%Y-%m-%d')
    text = f"Date     {date} "\
           f"Start      {s_time_str} "\
           f"Current    {c_time_str} "\
           f"Duration   {d_time_str} "
    lcd.text(text, 1)
    time.sleep(.4)
