import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import time
import webbrowser as wb
import pyjokes
import fitz
import pyautogui
import smtplib
import os
import random
import json
import requests
from urllib.request import urlopen
from time import sleep
from sinchsms import SinchSMS
import csv
import cv2
import smtplib, ssl
import getpass

engine=pyttsx3.init();	#initializing the pyttsx3 module
def speak(audio):
	engine.say(audio);
	engine.runAndWait()

def time():
	Time = datetime.datetime.now().strftime("%I:%M:%S");	#This is 12 hour format, To get 24 hour format use %H instead of %I
	speak("The current time is ");
	speak(Time)


def date():
	year=datetime.datetime.now().year
	month=datetime.datetime.now().month
	day=datetime.datetime.now().day
	speak("Today's date is ")
	speak(day)
	speak(month)
	speak(year)


def greet():
	hour=datetime.datetime.now().hour
	if hour>=6 and hour<12:
		speak("Good Morning")
	elif hour>=12 and hour<16:
		speak("Good Afternoon")
	elif hour>=16 and hour<=22:
		speak("Good evening")
	else:
		pass
	speak("I'm at your service. Please tell me how can i help you")	

def takeCommand():
	r=sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		audio=r.listen(source)
	try:
		print("Recognizing...")
		query = r.recognize_google(audio,language='en-US')
		print(query)
	except Exception as e:
		print(e)
		print("Please Say it again ")
		return "None"
	return query
	
def joke():
	j=pyjokes.get_joke('en','neutral')
	print(j)
	speak(j)


def musicplayer():
	for file in os.listdir('/home/karthik/Mini Project CSE2'):
		if file.endswith(".mp3"):
			fileparse = str('vlc' + ' ' + file)
			os.system(fileparse)

def read_pdf(filename):
	file=fitz.open(filename)
	for pageNumber, page in enumerate(file.pages(), start=1):
		text=page.getText()
		speak(text)
		
def screenshot():
	img=pyautogui.screenshot()
	img.save('/home/karthik/screenshot.jpg')
	speak("Your screenshot is saved in the home directory of your device.")
	
def sendEmail(to,content):
	server.smtplib.SMTP('smtp.gmail.com',587)		#587 is port for gmail
	server.elho()		#helps in identifying ourselves to smtp server
	server.starttls();		#puts connection to smtp server into the tls module
	#use low security in your sender mail
	server.login("karthikavula32@gmail.com","***********");
	server.sendmail('karthikavula32@gmail.com',to,content)
	server.close()


def browser(query) :
	query = query.replace("browse", "")
	query = query.replace(" ", "%20")
	URL = ('https://www.google.com/search?q='+query)
	query = ('firefox ' + URL)
	print(query)
	os.system(query)




def youtube(query) :
	try:
		query = query.replace("play", "")
		query = query.replace("video", "")
	except: 
		print("Something wrong")
	query = query.replace(" ", "%20")
	query = str ( 'firefox -new-window https://www.youtube.com/results?search_query=' + query)
	os.system(  query   )

def kitchen(query):
	print("🔪🔪🔪🔪🔪🔪🔪🔪🔪🔪\n\tKitchen\n🔪🔪🔪🔪🔪🔪🔪🔪🔪🔪")
	with open("Kitchen.csv", 'r') as file:
		csv_file = csv.DictReader(file)
		for row in csv_file:
			if (query == row['name']):
				print("Reciepe = ", row['name'], "\n\nIngredients = ",row['ingredients'],"\n\nProcedure = ",row['procedure'])


def calculate(audio):
	if 'addition' in q:
		a=int(input("Enter first number:"))
		b=int(input("Enter second number:"))
		print("sum is",a+b)
	elif 'subtraction' in q:
		a=int(input("Enter first number:"))
		b=int(input("Enter second number:"))
		print("result is  ",a-b)
	elif 'multiplication' in q:
		a=int(input("Enter first number:"))
		b=int(input("Enter second number:"))
		print("multiplication of two numbers is  ",a*b)
	elif 'division' in q:
		a=int(input("Enter first number:"))
		b=int(input("Enter second number:"))
		print("division of given two numbers is",a/b)
	elif 'modulus' in q:
		a=int(input("Enter first number:"))
		b=int(input("Enter second number:"))
		print("modulus og given numbers is ",a%b)
	elif 'power' in q:
		a=int(input("Enter first number:"))
		b=int(input("Enter second number:"))
		print("result is",pow(a,b))
def image_to_sketch():
	img=input("Enter the location of the image\n")
	image=cv2.imread(img)
	gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	inverted=255-gray_image
	blurred=cv2.GaussianBlur(inverted,(21,21),0)
	invertedblur=255-blurred
	pencilsketch=cv2.divide(gray_image,invertedblur,scale=256.0)
	cv2.imwrite("/home/karthik/Desktop/sketch.jpeg",pencilsketch)
	speak("Your sketch is saved on to the Desktop")
		
def story():
	f=open("story.txt","r")
	lines=f.readlines()
	r=random.randint(1,20)
	a=print(lines[r])
	speak(lines[r])
	f.close()
if __name__=='__main__':
	greet()
	while True:
		query=takeCommand().lower()
		if 'time' in query:		
			time()
		elif 'date' in query:		
			date()
		elif 'wikipedia' in query:
			try:
				speak("searching..")
				query=query.replace('wikipedia','')
				result=wikipedia.summary(query,sentences=3)
				speak("According to wikipedia")
				print(result)
				speak(result)
			except:
				speak("Say Wikipedia Something!!!") 
		elif 'go offline' in query:
			speak("Going offline, See you soon")
			quit()
		elif 'stop listening' in query:
			speak("For how many seconds you want me to stop listening to your commands?")
			ans= int(takeCommand())
			time.sleep(ans)
			print(ans)
		elif 'make a note' in query:
			speak("What should i note?")
			notes= takeCommand()
			file = open('notes.txt','w')
			speak("Should i Include date and time")
			ans= takeCommand()
			if 'yes' in ans or 'sure' in ans:
				strTime= datetime.datetime.now().strftime("%H:%M:%S")
				file.write(strTime)
				file.write(':-')
				file.write(notes)
				speak("Done taking notes")
			else:
				file.write(notes)
				speak('Done')
		elif 'show note' in query:
			speak("Showing notes");
			file=open('notes.txt','r')
			f=file.read()
			print(f)
			speak(f)
		elif 'remember that' in query:
			speak("What should i remember")
			memory=takeCommand()
			speak("You asked me to remember"+memory)
			remember=open('memory.txt','w')
			remember.write(memory)
			remember.close()
		elif 'do you remember anything' in query:
			remember=open('memory.txt','r')
			speak("You asked me to remember that"+remember.read())
			
		elif 'where is' in query:			
			query= query.replace("where is","")
			location=query
			speak("you asked me to locate"+location)
			wb.open("https://www.google.com/maps/place/"+location)
			
		elif 'joke' in query:
			joke()
		elif 'read pdf' in query:
			print("Copy and past your pdf file location here..\n")
			filename = input("Enter location of filename:\n")
			read_pdf(filename)
			
		elif 'screenshot' in query:
			sleep(5)
			screenshot()
			speak("Done with screenshot. Now you can view your home directory for the image")
		elif 'send email' in query:
			try:
				print("Please Login to your gmail acc")
				sender_email = input("Enter sender email :")
				passwd = getpass.getpass(prompt = "Enter Password : ")
				rec_email = input("Enter receiver email : ")
				msg = input("Enter Msg : ")
				s = smtplib.SMTP('smtp.gmail.com', 587)
				s.starttls()
				s.login(sender_email, passwd)
				s.sendmail(sender_email, rec_email, msg)
				s.quit()
				print("Mail Sent Successfully")

			except Exception as e:
				print(e)
				speak('Unable to send email')
		elif 'news' in query:
			try:
				jsonObj=urlopen("http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=6a083818f882423189b01880d75f77f0")
				data=json.load(jsonObj)
				i=1
				speak("Here are some top headlines from the Business Field")
				print("===================="+"\n")
				for  item in data['articles']:
					print(str(i)+', '+item['title']+'\n')
					print(item['description']+'\n')
					speak(item['title'])
					i+=1
			except Exception as e:
					print(str(e))
		elif 'calculate' in query:
			print("speak out what operation you want to perform\n 1.Addition \n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus\n6.Power\n") 	
			q=takeCommand().lower()
			calculate(q)
		elif 'image to sketch' in query:
			image_to_sketch()
		elif 'story' in query:
			story()
		elif ( 'browse' or 'search' or 'search for' or 'browse for' ) in query :
			browser(query)
		elif ('play video' or 'video'  ) in query :
			youtube(query)
		elif ('play music' or 'music' or 'audio' or 'song' or 'audio song') in query:
			musicplayer()
		elif ('kitchen' or 'dish' or 'how to prepare') in query:
			query = query.replace("kitchen ","")
			query = query.replace("dish ","")
			query = query.replace("how to prepare ","")
			kitchen(query)
