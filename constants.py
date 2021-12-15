class Constant:
    """
    
    Class for the constat strings
    
    """
    def __init__(self, bad_case=0):
        """Init
        
        @param if the user input the ignore case flag
        
        """
        self.__dict__["WEEK_DAYS"] = ["MO", "TU", "WE", "TH", "FR", "SA", "SU"]
        self.__dict__["ALLOW_BAD_INPUTS"] = bad_case
        self.__dict__["ERROR_FORMAT"] = "The input has not the correct format"
        self.__dict__["ERROR_FILE"] = "The input file does not exist"
        self.__dict__["ERROR_UNKNOW"] = "Unknow exception"
        