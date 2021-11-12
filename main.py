from plyer import notification
import time
import get_date_time
import os

if __name__ == "__main__":
    try:
        while True:
            notification.notify(
                title="Example Remainder!\nPlease read for exam.",
                message=f"Exact time remaing for proboard: {get_date_time.get_remaining_time()}",
                app_name="Exam_Remainder_App",
                app_icon="C:\\Users\\default.LAPTOP-6IMDNNN0\\Documents\\pythontut\\python_projects\\exam_remainder\\icon.ico",
                timeout=120
            )

            time.sleep(5*3600)

    except KeyboardInterrupt:
        print("Thank you for using this app.")
        os._exit(True)