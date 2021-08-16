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
    text1 = f"{date}"
    text2 = f"{c_time_str}.{int(c_time*1000000%1000000):06d} "
    text3 = f"{s_time_str}.{int(s_time*1000000%1000000):06d} "
    text4 = f"{d_time_str}.{int(c_time*1000000%1000000):06d} "
    lcd.text(text1, 1)
    lcd.text(text2, 2)
    lcd.text(text3, 3)
    lcd.text(text4, 4)
