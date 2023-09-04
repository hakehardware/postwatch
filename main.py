import pyinotify
import datetime
import time

# Define a callback function to handle file read events
def process_file_read(event):
    current_datetime = datetime.datetime.now()

    # Format the current date and time as a string
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print(f"{formatted_datetime}: File Read = {event.pathname}")


            

def main():
    # Initialize a WatchManager
    wm = pyinotify.WatchManager()

    # Define the watch mask to only monitor read events
    mask = pyinotify.IN_ACCESS

    # Create a Notifier object
    notifier = pyinotify.Notifier(wm, default_proc_fun=process_file_read)

    # Add a watch on the directory or file you want to monitor
    path_to_monitor = "/media/postdata"
    wm.add_watch(path_to_monitor, mask)

    while True:
            notifier.process_events()
            time.sleep(10)

            if notifier.check_events():
                    notifier.read_events()

if __name__ == "__main__":
       main()