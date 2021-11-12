# Python_Exam_Remainder
This is the exam remainder app that simply give the notifications about how exact time is left for the exam to start.

-There are two python  files one is main.py and another is get_date_time.py
-.ico and .mp3 files are required for icon and notification sound but .mp3 file is not used in this version of the app.
-we have used plyer module for notification.
-get_date_time.py file is imported inside the main.py in order to get the remaining time for exam to start.
-In my case, my preboard exam was set at 7:00:00 on sunday i.e, 2021/11/14
-This app will check the remaining time from the current datetime and returns the exact date_time remaining in every 5 hours.
-we can use this app to run background use following commmand in command prompt:
            >>>pythonw ./main.py
            
 -to stop we can use ctrl+c.
