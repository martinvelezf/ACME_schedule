import sys
from functions import Scheduler

if __name__ == "__main__":
    if len(sys.argv) >1:
        no_format = sys.argv[1]
    else:
        no_format = 0
        
    schedule=Scheduler(no_format)
    for i in schedule.get_scheduled_workers():
        print(i)