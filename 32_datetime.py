import datetime
import time

#wyciąganie daty
today = datetime.datetime.now()
print(today)
print(type(today))

d1 = today.strftime('Moj string //%d%Y....%H%Mcokolwiek%S')
print(d1)

d2 = today.strftime('Plik_%H%M%S.csv')
print(d2)

#wyciągnięcie godziny i daty
now = datetime.datetime.now()
timer = now.strftime('%H:%M:%S')
date = now.strftime('year = %Y,    month = %m,   day = %d')
print('Time now is : ', timer)
print('Date now is :', date)

file = 'report.txt'
#report_06_10_23_33.txt

for i in range(10):
    now = datetime.datetime.now()
    timer = now.strftime('%d_%m_%y_%S')
    filename = file[:6] + timer + file[6:]
    print(filename)
    time.sleep(2)


