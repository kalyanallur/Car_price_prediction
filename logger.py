import logging
import os
import datetime

name = datetime.datetime.now().strftime("%d-%m-%y-%H-%M-%S")
foldername = os.path.join(os.getcwd(),"Logs")
os.makedirs(foldername, exist_ok=True)
log_file_name = os.path.join(foldername,name)

logging.basicConfig( 
    filename=log_file_name,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s' )

logging.info("Loggind started...")