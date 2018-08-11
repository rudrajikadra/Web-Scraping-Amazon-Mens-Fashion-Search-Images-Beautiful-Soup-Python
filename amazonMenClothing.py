#https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Dfashion-mens-clothing&field-keywords=

#Import all the libraries needed
import os
import urllib
import urllib.request
from bs4 import BeautifulSoup
from random import randint

#this function will create a soup and retuens which is the parsed html format for extracting html tags of the webpage
def makeSoup(url):
	#This will load the webpage for the given url
	page = urllib.request.urlopen(url) 
	#this BeautifulSoup below will parse the html file
	soup = BeautifulSoup(page, "html.parser")
	return soup



#This function will be called every new keyword line is encountered and will start scraping the amazon web page of the search result according to the text mention in the keywords text file
def perfromScraping(urlReceived, folderName, breakPointNumber):
	breaki = 1
	url = urlReceived #This will hold the url addres
	soup = makeSoup(url)
	print("Folder Name is ", folderName)

	i = 1
	for image in soup.findAll('img', {"class" : "cfMarker"}):
		if(breaki <= breakPointNumber): #This statement checks the number of images that were restricted to which were supposed to be downloaded
			#print(image)
			print("Image number ", i ," : \n", image.get('src'), "\n")
			i = i+1
			breaki = breaki + 1

			nameOfFile = image.get('alt')
			nameOfFile = nameOfFile.replace('/','-')
			img = image.get('src')
			tempCheck = img.split('.')
			check = str(tempCheck[len(tempCheck) - 1])
			ImageType = ".jpeg"
			if (check == "jpg" or check == "jpeg" or check == "png"):

				if check == "jpg" or check == "jpeg":
					ImageType = ".jpeg"
				else:
					ImageType = ".png"

				filename = nameOfFile
				folderIndividualName = "AmazonImages/" + folderName + "/" #Creates the path where the images will be stored

				#Create The folder according to search name
				if not os.path.exists(folderIndividualName):
					os.makedirs(folderIndividualName)
				imageFile = open(folderIndividualName + filename + ImageType, 'wb')
				imageFile.write(urllib.request.urlopen(img).read()) #This will read the image file from the link and download it and save it in the folder mentioned all at the same time
				imageFile.close()


#This function returns the folder name removing the number of images range from they line of keywords file
def getFolderName(wholeName):
	tempArray = wholeName.split(" ")
	nameTemp = ""
	for i in range(1, len(tempArray)):
		nameTemp = nameTemp + " " + tempArray[i]

	return nameTemp



breakNumber = -1
standardUrl = "https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Dfashion-mens&field-keywords="

# Open the file with read only permit
file = open('keywords.txt', "r")
# use readlines to read all lines in the file
# The variable "lines" is a list containing all lines in the file
lines = file.readlines()
# close the file after reading the lines.


#The File stores Input data as "<Number Of Images Required><<SPACE>><Search Text With Spaces>"
for i in range(0,len(lines)):
	keys = lines[i]
	keys = keys.replace('\n', '')
	print(keys)
	folderName = getFolderName(keys)

	keywords = keys.split(" ")
	keyLen = len(keywords)

	breakNumber = int(keywords[0])

	keyUrl = standardUrl
	for j in range(1, keyLen):

		if (keyUrl == standardUrl):
			keyUrl = keyUrl + keywords[j]
		else:
			keyUrl = keyUrl + "+" + keywords[j]

	print(keyUrl)

	perfromScraping(keyUrl, folderName, breakNumber)

file.close()