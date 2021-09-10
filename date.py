import datefinder
import winsound
import datetime

def alarm(text):
    dTimeA=datefinder.find_dates(text)
    for mat in dTimeA:
        print(mat)
    sringA=str(mat)
    timeA=stringA[11:] 
    hourA=int(hourA)
    minA=timeA[3:-3]
    minA=int(minA)


    while True:
        if hourA==datetime.datetime.now().hour:
            if minA==datetime.datetime.now().min:
                 print(" alarm is running")
                 winsound.PlaySound('C:\\Users\\arora\\OneDrive\\Desktop\\alarm\\emergency_bell_alarm_small_ring.mp3',winsound.SND_LOOP)

    

alarm("set alarm at 8 pm")    