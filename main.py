from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import shutil
from os import system, name
import multiprocessing
from multiprocessing import Manager
import urllib.request
from selenium.webdriver.support.ui import WebDriverWait
import threading
import concurrent.futures


count = 0

def google(image,l):

    print('...........................google.........................................')
    driver = webdriver.Firefox()

    driver.get("https://image.google.com")

    query = driver.find_element_by_name('q')
    driver.implicitly_wait(5)

    

    query.send_keys(image + Keys.ENTER)

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



    

    for key,item in duplicate.items():
        l.append(key)
    


                



    driver.close()


def yahoo(image,l):

    print('......................................yahoo............................................')

    driver = webdriver.Firefox()

    driver.get("https://in.images.search.yahoo.com/")

    query = driver.find_element_by_name('p')
    driver.implicitly_wait(5)

    query.send_keys(image + Keys.ENTER)

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



    
    for key,item in duplicate.items():
        l.append(key)
    


                



    driver.close()


def bing(image,l):
    print('..................bing.........................')
    driver = webdriver.Firefox()

    driver.get("https://www.bing.com/images/trending?FORM=ILPTRD")

    query = driver.find_element_by_name('q')
    driver.implicitly_wait(5)

    query.send_keys(image + Keys.ENTER)

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



    
    for key,item in duplicate.items():
        l.append(key)
    


                



    driver.close()



def download_using_thread(j):

    global count
        
    try:
        count+=1
        
        urllib.request.urlretrieve(j,"{}.jpg".format(0+count)) 
    except:
        pass   




def downloader(l,image):
    print('...................Downloading......................................./')
    
    cwd = os.getcwd()
    dir = os.path.join(cwd,image)
    os.mkdir(dir)

    os.chdir(dir)

    print("\ntotal images are " + str(len(l)))

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_using_thread,l)

        

    
if __name__ == "__main__":
    imge = input("Enter name of which image you want to download: ")

    intial = time.time()
    manager = Manager()

    l = manager.list()

    p1 = multiprocessing.Process(target=google,args=[imge,l])
    p2 = multiprocessing.Process(target=yahoo,args=[imge,l])
    p3 = multiprocessing.Process(target=bing,args=[imge,l])

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print('\ntotal images from all search engines are:',len(l))

    downloader(l,imge)

    print("total time taken to complete the program:",time.time()-intial, ' seconds')  

    a=input()
