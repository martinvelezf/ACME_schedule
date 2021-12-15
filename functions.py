
from constants import Constant
from datetime import datetime
class Scheduler(object):
    def __init__(self,ignore_error=0):
        """
         @param: flag to ignore the error in format
        """
        self.cte=Constant(ignore_error)

    def check_valid_input(self,text):
        """Check input
        
         @param: check if the text has the correct format
         
        """
        if len(text)==13 and text[:2] in self.cte.WEEK_DAYS and text[7]=="-" and \
                text[2:4].isdigit() and int(text[8:10])<60 and text[4]==':' and \
                text[5:7].isdigit() and int(text[5:7])<25 and text[8:10].isdigit()\
                and int(text[8:10])<25 and text[10]==':' and text[11:].isdigit() \
                and int(text[11:])<60 and int(text[2:4])<=int(text[8:10]):
            return True
        else:
            if self.cte.ALLOW_BAD_INPUTS==1:
                return False
            else:
                raise ValueError(self.cte.ERROR_FORMAT)

    def check_interval(self,time1,time2):
        """Check time interval
        
        @param time1 tuple of start and end time
        @param time2 tuple of start and end time
        
        """
        if (time1[0] <= max(time2) and time1[0] >= min(time2) 
                and time1[1] <= max(time2) and time1[1] >= min(time2)) or (time2[0] <= max(time1)
                and time2[0] >= min(time1) and time2[1] <= max(time1) and time2[1] >= min(time1)):
            return True
        return False 
    def get_scheduled_workers(self):
        """Find employees with the same scheduler
         
        """
        schedule_by_name={} 
        self.file_name=input("Your file name: ")
        try:
            with open(self.file_name) as file:
                for line in file:
                    data=line.replace(' ','').strip().split('=')
                    if len(data)==2:
                        name,schedule=data
                        schedule_by_name[name]={
                            time[:2]:(
                                datetime.strptime(time[2:7], '%H:%M'),
                                datetime.strptime(time[8:], '%H:%M')) 
                            for time in filter(self.check_valid_input,schedule.split(','))
                        }
                    elif not self.cte.ALLOW_BAD_INPUTS:
                        raise ValueError(self.cte.ERROR_FORMAT)
        except FileNotFoundError:
            raise ValueError(self.cte.ERROR_FILE)
        except ValueError:
            raise
        except Exception as e:
            raise ValueError(self.cte.ERROR_UNKNOW)

        name_list=list(schedule_by_name.keys())
        
        for i in range(len(name_list)-1):
            for j in range(i+1,len(name_list)):
                #intersec the common days
                intersec=set(schedule_by_name[name_list[i]].keys())\
                .intersection(set(schedule_by_name[name_list[j]].keys()))
                common_time=list(filter(lambda day:self.check_interval(
                    schedule_by_name[name_list[i]][day],
                    schedule_by_name[name_list[j]][day]
                    ),intersec))
                if common_time:
                    schedule=len(common_time)
                    yield(f"{name_list[i]}-{name_list[j]}: {schedule}")

