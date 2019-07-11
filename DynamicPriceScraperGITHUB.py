from bs4 import BeautifulSoup
from selenium import webdriver
import smtplib
import os


class item:
    def __init__(self,URL,prePrice = 1000000.00):                                                       #sets the price exceptionally high so it will drop to normal levels when it first is made
        self.URL = URL.strip()                                                                          #url info
        self.prePrice = float(prePrice)                                                                 #the price of the item if it already exist, defualts to 1000000000
        self.headersINFO = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}                         #user agent info 
        self.checkPrice()                                                                               #call the check price method

    def checkPrice(self):

       
        driver.get(self.URL)        #accesses URL

        soup = BeautifulSoup(driver.page_source, 'html.parser')     #HTML parses 

        self.title = (soup.find(id = "productTitle").get_text()).strip()     #grabs the item based on id attributes
        
        try:
            self.Price = soup.find(id = "price_inside_buybox").get_text().strip()        #get the price based on id if one type of layout
        except:
            self.Price = soup.find(id = "priceblock_ourprice").get_text().strip()        #get the price based on id if another type of layout

        #improve here for pther type of layout?
        
        
        self.Price = float(self.Price[1:])                                              #turns the price from a string to flaot

        if self.Price < self.prePrice:                                                 #if the price is less than the price before 
            self.Price == self.prePrice                                                 #set the new low price
            self.send_Email()                                                           #send email method
            self.update_Price()

    
    def send_Email(self):
        server =  smtplib.SMTP('smtp.gmail.com',587)                    #sets conncetion to google servers --- password?
        server.ehlo()                                                   #google it
        server.starttls()                                               #start connection
        server.ehlo()                                                   #do it again

        #server.login('#YOUR EMAIL HERE', 'YOUR APP PASSWORD HERE')    #logs into google using 'app passwords'

        subject =("PRICE FELL", self.title)                                              #subject line for email
        body= ("Check the link at " ,self.URL)                                          #body line for email

        msg = f"Subject: {subject}\n\n{body}"                                    #construct email msg

        server.sendmail(                                                        #sending email
            #'YOUR EMAIL HERE',                                     #from 
            #'RECEIVING EMAIL',                                     #to
            msg                                                                 #message
        )

        print("email SENT")                                             

        server.quit()                                                           #close conncetion

    def update_Price(self):
        NewFile.write("{0}  {1} \n" .format(self.URL, self.Price))                #writes to new file


    


if __name__ == "__main__":
    driver = webdriver.Chrome() #useing chrome calls PATH variable
    #FrontFile = open("INPUT FILE LOCATION","r")                  #put input file.txt here
    BackFile = open("F:\\Scrapers\\DynamicAmazonScraper\\ScraperData.txt","r")                          #linked to assocatied file
    NewFile = open("F:\\Scrapers\\DynamicAmazonScraper\\NewFiles.txt","a")                              #link to new file
    
    frontFile_Data = FrontFile.readlines()                                                              #read input file and input each line into an list
    Backfile_Data = BackFile.readlines()                                                                #read assoicated file and input each line into an list

    for i in range(len(frontFile_Data)):                                                                #for every line in the front file
        found = False                                                                                   #we have not found the current line in the back file
        for j in range(len(Backfile_Data)):                                                             #scan the back file
            if ((frontFile_Data[i].strip() in Backfile_Data[j].strip()) and (found == False)):          #if we find matching lines in the front and back file and havnt found it before meaning the item already exist
                found = True                                                                            #we found it
                item(frontFile_Data[i],(Backfile_Data[j].strip()[(len(frontFile_Data[i].strip())):]).strip())     #grab url and cost of item and run it into the class construstion method
        if found == False:                                                                              #if true it is not found in the back file and is a new item
            item(frontFile_Data[i])                                                                     #send url to class construction




    driver.quit()                                     #becasue we are a good person

    BackFile.close()                             #becasue we are a good person
    FrontFile.close()                            #becasue we are a good person
    NewFile.close()                               #becasue we are a good person
    
    os.remove("F:\\Scrapers\\DynamicAmazonScraper\\ScraperData.txt")          #remove old file 
    os.rename("F:\\Scrapers\\DynamicAmazonScraper\\NewFiles.txt","F:\\Scrapers\\DynamicAmazonScraper\\ScraperData.txt")    #rename extra file to new file



    

            