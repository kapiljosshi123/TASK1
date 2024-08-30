import mysql.connector,csv,time,os,codecs
from bs4 import BeautifulSoup
from selenium import webdriver

#First of all, download Python in your system and install this library which I have imported.


#This code will create a folder named Htmlfile in your folder where these files will be stored.

foldername ='HtmlFiles'

directory = os.getcwd()+f'\{foldername}'
if not os.path.isdir(directory):os.makedirs(directory) 

#.....


#If you want to insert your data into the database then create a database name.
#This code connect your database.
#And if you don't need it, you can comment it and select this part use control+? .

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password='',
    database="dnb_dat_aus"
)

cursor = connection.cursor()
#.....

#This is driver install
driver = webdriver.Chrome()
#...

#This function csv create code

def write_output(data):
    with open('dnb_data.csv', mode='a', newline='',encoding='utf-8') as output_file:
        writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(data)
    output_file.close()
write_output(["Company_Name", "Address", "Revenue"])
#....

#my code starts from here

for i in range (1,21):

    #I have given the range from 1 to 21 which will go to 20 pages because I went to the website and saw the pagination, so I fixed it by giving the range.

    url = f"https://www.dnb.com/business-directory/company-information.manufacturing.au.victoria.html?page={i}"
    
    print('Page Number: ',i)

    #or this code, it will see the page in your folder, if it is taken to that place, it will go to else or it will get it from the driver, it will save the page or it will give the result.

    filename =  directory+'\\'+f'Pagenumber_{i}'+'.html'
    
    if os.path.isfile(f"{filename}"):
        f = codecs.open(filename, "r", "utf-8")
        soup = BeautifulSoup(f,'lxml')
        all_locations =soup.find('div',{'id':'companyResults'}).find_all('div',{'class':'col-md-12 data'})

    else:

        driver.get(url)
        if i == 1:
            time.sleep(13)
        else:
            time.sleep(2)
        soup = BeautifulSoup(driver.page_source,'lxml')

        try:all_locations =soup.find('div',{'id':'companyResults'}).find_all('div',{'class':'col-md-12 data'})
        except:
            time.sleep(13)
            soup = BeautifulSoup(driver.page_source,'lxml')
            all_locations =soup.find('div',{'id':'companyResults'}).find_all('div',{'class':'col-md-12 data'})
        f = codecs.open(filename, "w", "utf-8")
        f.write(driver.page_source)


    for loc in all_locations:
        
        Company_Name = loc.find('div',{'class':'col-md-6'}).text.strip()
        
        Address      = loc.find('div',{'class':'col-md-4'}).text.replace(' ','').replace('\n\n\n',' ').replace('\n\n',' ').replace('Country:','').strip()
        
        Revenue      = loc.find('div',{'class':'col-md-2 last'}).text.replace(' ','').replace('\n\n\n',' ').replace('\n\n',' ').replace('SalesRevenue($M):','').strip()

        print('Company_Name:',Company_Name,' ,','Address:',Address,' ,','Revenue:',Revenue)

        #This info part will write the result in the form.

        info =[Company_Name,Address,Revenue]
        write_output(info)
        #....

        #This part will insert the result into the database
        #And if you don't need it, you can comment it and select this part use control+?
        val=(Company_Name,Address,Revenue)
        cursor.execute('INSERT IGNORE INTO tbl_dnb_data (Company_Name,Address,Revenue) VALUES (%s,%s,%s)',val)
        connection.commit()

