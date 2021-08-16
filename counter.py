from rpi_lcd import LCD
import time

lcd = LCD()
lines = []
s_time = time.time()
s_time_str = time.strftime("%H:%M:%S", time.localtime(s_time))
for i in range(0x0, 0Xffff):
    if len(lines) == 4:
        lines.pop(0)
    lines.append(F'{i:4x}')
    n = 1
    c_time = time.time()
    d_time = c_time - s_time
    for line in lines:
        if n == 1:
            line = f'{line}     C-{time.strftime("%H:%M:%S", time.localtime(c_time))}'
        if n == 3:
            line = f'{line}     E-{time.strftime("%H:%M:%S", time.gmtime(d_time))}'
        if n == 4:
            line = f'{line}     S-{s_time_str}'
        lcd.text(line, n)
        n += 1
    time.sleep(0.5)
