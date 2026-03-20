import sys
import logging

def error_message_detail(error: Exception, error_detail: sys) -> str:
    # Extract traceback details
    _, _, exc_tb = error_detail.exc_info()
    
    # Get file name where exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    # Get line number
    line_number = exc_tb.tb_lineno

    # Create error message
    error_message = (
        f"Error occurred in script: {file_name} "
        f"at line number: {line_number} "
        f"error message: {str(error)}"
    )
    
    return error_message


class MyException(Exception):
    
    def __init__(self, error_message: str, error_detail: sys):
        super().__init__(error_message)
        
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message   