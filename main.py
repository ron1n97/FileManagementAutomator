from watchdog.observers import Observer
from OnModifiedListner import OnModifiedListner
from OnModifiedListner import default_download_folder

if __name__=="__main__":
        event_handler = OnModifiedListner()
        observer = Observer()
        observer.schedule(event_handler, default_download_folder, recursive=True)
        observer.start()
        observer.join()        