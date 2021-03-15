from datetime import datetime
import shutil


def Log_info(counter,mult,url):

	b='\b'

	Len=len(str(counter))

	if int(shutil.get_terminal_size().columns) < len(url) \
	or len(url) == int(shutil.get_terminal_size().columns):
		size=(shutil.get_terminal_size().columns) - 32
		url=url[:size]
	

	print(

		f"\033[38;5;231m|  {counter}     {b*mult}|"\
		f"\033[38;5;227m{datetime.time(datetime.now())}\033[38;5;231m|"\
		f"\033[38;5;46m{url}\033[0m"

		)