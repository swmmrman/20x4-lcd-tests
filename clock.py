from rpi_lcd import LCD
import time

lcd = LCD()
lines = []
while True:
    t = time.time()
    t_str = time.strftime("%H:%M:%S", time.localtime(t))
    d_time = time.monotonic()
    d_time_str = time.strftime(":%H:%M:%S", time.gmtime(d_time))
    d_days = int(time.strftime("%j", time.gmtime(d_time)))-1
    date = time.strftime('%Y-%m-%d')
    lcd.text(f"Date      {date} ",1)
    lcd.text(f"Time        {t_str}", 2)
    lcd.text(f"Uptime  {d_days:3d}{d_time_str}", 4)
    time.sleep(.4)
