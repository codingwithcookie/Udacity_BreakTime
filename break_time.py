import time
import webbrowser

count = 0
print("Break Time Scheduler started at "+time.ctime())
while (count < 3):
    time.sleep(60)
    webbrowser.open("http://www.youtube.com/watch?v=LHCob76kigA")
    count = count + 1
