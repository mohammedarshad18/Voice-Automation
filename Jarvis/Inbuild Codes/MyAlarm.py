import datetime
import winsound

def alarm(Timing):
    alttime = str(datetime.datetime.now().strptime(Timing,"%I:%M %p"))
    altime = alttime[11:-3]
    print(altime)
    Horeal = altime[:2]
    Horeal = int(Horeal)
    Mireal = altime[3:5]
    Mireal = int(Mireal)
    print(f"Done,Alarm is set for {Timing}")
    while True:
        if Horeal==datetime.datetime.now().hour:
            if Mireal==datetime.datetime.now().minute:
                print("Alarm is running")
                winsound.PlaySound('beep',winsound.SND_LOOP)
            elif Mireal<datetime.datetime.now().minute:
                break
