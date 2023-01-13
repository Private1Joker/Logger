#used library
import os
from datetime import datetime

# Universal logger for different programs
class Logger:

	def __init__(self, parent = ''):

		# Name of parent programm
		self._parent = parent

		# Default time's settings
		self._date = False
		self._format_date = ''
		# self._str_data = ''

		# Default color's settings
		# self.color = False
		# self._color_mes = {}

		# Default file's settings
		self._file_log = False
		self._path_to_log_file = os.getcwd()

		# Work messages
		self._info_mess = ''
		self._warn_mess = ''
		self._deb_mess = ''
		self._err_mess = ''
		self._another_mess = []

	# Setup colore settings
	# def set_color(self, color = True, color_mes = {"Warning" : "ORANGE", "Info" : "BLUE", "Error" : "RED", "Debug" : "GREEN"}):
	# 	self.color = color
	# 	self.color_mes = color_mes

	# Setup filelog's setting
	def set_file(self, continue_log = False, name_of_log_file = "Programm.log"):
		self._file_log = True
		self._path_to_log_file = self._path_to_log_file + '/' +  name_of_log_file

		if not os.path.exists(self._path_to_log_file) or not continue_log:
			log_f = open(self._path_to_log_file, "w")
			log_f.write('<-----LOG FILE ' + self._parent + '----->\n')
			log_f.close()
		else:
			log_f = open(self._path_to_log_file, "a")
			log_f.write('<-----CONTINUE LOG FILE ' + self._parent + '----->\n')
			log_f.close()


	# Setup date settings
	def set_date(self, format_date = "%H:%M:%S-%d-%m-%Y"):
		self._date = True
		self._format_date = format_date

	# Setup messages
	def set_info_mess(self, info_message) -> None:
		self._info_mess = info_message

	def set_warn_mess(self, warn_message) -> None:
		self._warn_mess = warn_message

	def set_err_mess(self, err_message) -> None:
		self._err_mess = err_message

	def set_deb_mess(self, deb_message) -> None:
		self._deb_mess = deb_message

	def set_another_mess(self, message_name ,another_mess) -> None:
		self._another_mess.append(message_name)
		self._another_mess.append(another_mess)

	# Work with file
	def __work_with_file(self, log_mess) -> None:
		log_f = open(self._path_to_log_file, "a")
		log_f.write(log_mess)
		log_f.close()

	# Date message making
	def __show_date(self) -> str:
		date = datetime.now().strftime(self._format_date)

		return date

	# Info log message
	def Info(self) -> None:
		message = 'INFO:'

		# With date
		if self._date:
			message = self.__show_date() + "||" + message

		message = '<-----' + message + self._info_mess + '----->\n'

		if self._file_log:
			self.__work_with_file(message)
		else:
			print(message)

	def Warning(self) -> None:
		message = 'WARNING:'

		# Whith date
		if self._date:
			message = self.__show_date() + "||" + message

		message = '<-----' + message + self._warn_mess + '----->\n'

		if self._file_log:
			self.__work_with_file(message)
		else:
			print(message)

	def Error(self) -> None:
		message = 'ERROR:'

		# Whith date
		if self._date:
			message = self.__show_date() + "||" + message

		message = '<-----' + message + self._err_mess + '----->\n'

		if self._file_log:
			self.__work_with_file(message)
		else:
			print(message)

	def Debug(self) -> None:
		message = 'DEBUG:'

		# Whith date
		if self._date:
			message = self.__show_date() + "||" + message

		message = '<-----' + message + self._deb_mess + '----->\n'

		if self._file_log:
			self.__work_with_file(message)
		else:
			print(message)

	def Another(self) -> None:
		message = self._another_mess[0] + ':'

		# Whith date
		if self._date:
			message = self.__show_date() + "||" + message

		message = '<-----' + message + self._another_mess[1] + '----->\n'

		if self._file_log:
			self.__work_with_file(message)
		else:
			print(message)
