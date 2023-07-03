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
