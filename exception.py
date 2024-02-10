import sys
import os

def build_message(error):
    _,_,exc_tb = sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    messsage = f"Exception occured in the file named {file_name}, line number: {exc_tb.tb_lineno}, message: {error}"
    return messsage

class CustomException(Exception):
    def __init__(self, error) -> None:
        super().__init__(error)
        self.error_message = build_message(error)


    def __str__(self) -> str:
        return self.error_message

try:
    print(1/0)
except Exception as e:
    raise CustomException(e)