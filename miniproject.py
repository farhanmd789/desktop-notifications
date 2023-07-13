from plyer import notification
import time
while True:
    notification.notify(title='TAKE A BREAK',
                        message="look away at distance of more than 20m for more than 20 seconds",
                        app_icon='D:\eye.ico',
                        timeout=2)
    time.sleep(10)


    notification.notify(title='DRINK SOME WATER',
                        message="drink water to stay hydrated",
                        app_icon='D:\glass.ico',
                        timeout=3)
    time.sleep(20)
    notification.notify(title='Remove Earphones',
                        message="Damages Ear for keeping longtime",
                        app_icon='D:\ear.ico',
                        timeout=3)
    time.sleep(5)
    notification.notify(title='KEEP YOUR POSTURE STRAIGHT',
                        message="poor posture can be bad for your health",
                        app_icon='D:\BODY.ico',
                        timeout=2)
    time.sleep(15)
    notification.notify(title='GO TO SLEEP',
                        message="It's too late shutdown and go to bed",
                        app_icon='D:\BED.ico',
                        timeout=4)
    time.sleep(30)
