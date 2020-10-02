from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import shutil
from os import system, name
import urllib.request
from selenium.webdriver.support.ui import WebDriverWait


class img:
    name=""

    def __init__(self,name):
        self.name=name



def google():

    print('...........................google.........................................')
    driver = webdriver.Firefox()

    driver.get("https://image.google.com")

    query = driver.find_element_by_name('q')
    driver.implicitly_wait(5)

    query.send_keys(image.name + Keys.ENTER)

    time.sleep(3)

    #images = driver.find_elements_by_xpath('//img[@class="rg_i Q4LuWd"]')

    img=[]
    for _ in range(15):
        z=''
        try: 
            driver.find_element_by_xpath('//input[@class="mye4qd"]').click()
            time.sleep(7)
            continue
            z=driver.find_element_by_xpath("//div[@class='OuJzKb Yu2Dnd']/div")
            if len(z)>0:
                break
                    
        except:
            pass
        
        driver.execute_script("window.scrollTo(0, 50000)")
        time.sleep(3)
        continue
    wait = WebDriverWait(driver, 10)
    driver.implicitly_wait(10)
    time.sleep(4)
    images = driver.find_elements_by_xpath('//img[@class="rg_i Q4LuWd"]')
    driver.implicitly_wait(10)

    for i in images:
        img.append(i.get_attribute('src'))
    count=len(img)
    print('total links:',count)
    duplicate=dict()
    for i in img:
        if i in duplicate:
            duplicate[i]+=1
        else:
            duplicate[i]=1

    for key,items in duplicate.items():
        if items>1:
            print('duplicates',items)

    print('total distinct images are:',len(duplicate))



    fh=open(image.name+'.txt','w')

    for key,item in duplicate.items():
        fh.write(str(key))
        fh.write('\n')

    fh.close()


                



    driver.close()


def yahoo():

    print('......................................yahoo............................................')

    driver = webdriver.Firefox()

    driver.get("https://in.images.search.yahoo.com/")

    query = driver.find_element_by_name('p')
    driver.implicitly_wait(5)

    query.send_keys(image.name+ Keys.ENTER)

    time.sleep(3)

    #images = driver.find_elements_by_xpath('//img[@class="rg_i Q4LuWd"]')

    img=[]
    for _ in range(15):
        z=''
        try: 
            driver.find_element_by_xpath('//button[@class="ygbt more-res"]').click()#show more
            time.sleep(7)
            continue
            z=driver.find_element_by_xpath("//div[@class='OuJzKb Yu2Dnd']/div")# end
            if len(z)>0:
                break
                    
        except:
            pass
        
        driver.execute_script("window.scrollTo(0, 50000)")
        time.sleep(3)
        continue
    wait = WebDriverWait(driver, 10)
    driver.implicitly_wait(10)
    time.sleep(4)
    images = driver.find_elements_by_xpath('//img')#img
    driver.implicitly_wait(10)

    for i in images:
        img.append(i.get_attribute('src'))
    count=len(img)
    print('total links:',count)
    duplicate=dict()
    for i in img:
        if i in duplicate:
            duplicate[i]+=1
        else:
            duplicate[i]=1

    for key,items in duplicate.items():
        if items>1:
            print('duplicates',items)

    print('total distinct images are:',len(duplicate))



    fh=open(image.name+'.txt','a')
    fh.write('\n')
    for key,item in duplicate.items():
        fh.write(str(key))
        fh.write('\n')

    fh.close()


                



    driver.close()


def bing():
    print('..................bing.........................')
    driver = webdriver.Firefox()

    driver.get("https://www.bing.com/images/trending?FORM=ILPTRD")

    query = driver.find_element_by_name('q')
    driver.implicitly_wait(5)

    query.send_keys(image.name + Keys.ENTER)

    time.sleep(3)

    #images = driver.find_elements_by_xpath('//img[@class="rg_i Q4LuWd"]')

    img=[]
    for _ in range(15):
        z=''
        try: 
            driver.find_element_by_xpath("//a[@class='btn_seemore cbtn mBtn']").click()
            time.sleep(7)
            continue
            z=driver.find_element_by_xpath("//div[@class='OuJzKb Yu2Dnd']/div")
            if len(z)>0:
                break
                    
        except:
            pass
        
        driver.execute_script("window.scrollTo(0, 50000)")
        time.sleep(3)
        continue
    wait = WebDriverWait(driver, 10)
    driver.implicitly_wait(10)
    time.sleep(15)
    images = driver.find_elements_by_xpath("//img")
    driver.implicitly_wait(10)

    for i in images:
        img.append(i.get_attribute('src'))
    count=len(img)
    print('total links:',count)
    duplicate=dict()
    for i in img:
        if i in duplicate:
            duplicate[i]+=1
        else:
            duplicate[i]=1

    for key,items in duplicate.items():
        if items>1:
            print('duplicates',items)

    print('total distinct images are:',len(duplicate))



    fh=open(image.name+'.txt','a')
    fh.write('\n')
    for key,item in duplicate.items():
        fh.write(str(key))
        fh.write('\n')

    fh.close()


                



    driver.close()


def downloader():
    print('...................Downloading......................................./')
    
    cwd = os.getcwd()
    dir = os.path.join(cwd,image.name)
    os.mkdir(dir)
    source = cwd + "\\" + image.name +".txt"
    dest = dir + "\\" + image.name + ".txt"
    shutil.copyfile(source,dest)
    os.remove(source)

    os.chdir(dir)

    
    fh=open(image.name+'.txt','r')
    l=list()
    c=0
    for i in fh:
        if i == '\n':
            continue
        l.append(i)

    print("\ntotal images are " + str(len(l)))

    fh.close()

    os.remove(dest)

    count=0
    for j in l:
        try:
            count+=1
            urllib.request.urlretrieve(j, image.name+"{}.jpg".format(0+count)) 
        except:
            continue       

    
if __name__ == "__main__":
    x = input("Enter name of which image you want to download: ")

    image = img(x)

    

    google()
    yahoo()
    bing()
    downloader()  
