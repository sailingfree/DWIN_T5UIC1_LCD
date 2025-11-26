#!/usr/bin/env python3
from dwinlcd import DWIN_LCD
import sys

# define the interface pins and serial port on the raspberry pi
encoder_Pins = (26, 19)
button_Pin = 13
LCD_COM_Port = '/dev/ttyAMA0'

# Read the api key from a local file named apikey.txt
try:
        f = open("/home/pi//DWIN_T5UIC1_LCD/apikey.txt")
        API_Key = (f.read()).strip()
except:
       sys.exit("Cannot read the api key please make sure the file exists")

# Init the lcd driver
DWINLCD = DWIN_LCD(
	LCD_COM_Port,
	encoder_Pins,
	button_Pin,
	API_Key
)
