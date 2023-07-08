import sys
from logger import logging

def error_message_details(error, error_detail:sys):
    _,_,exec_tb=error_detail.exc_info()
    file_name = exec_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script [{0}], in line [{1}]. Error: [{2}]".format(file_name,exec_tb.tb_lineno,str(error))

    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_detail=error_detail)


