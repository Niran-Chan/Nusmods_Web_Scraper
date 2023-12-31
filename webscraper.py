import chromedriver_autoinstaller
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

def scrape(courses,file_name):
    url = "https://nusmods.com/courses/"
    f = open(file_name,"w")
    year,sem = 1,1;
    missing_modules=[]
    for yr in courses:
        
        f.write("Year"+ str(year)+ "\tSemester: " + str(sem) + "\n")
        year = year + 1 if sem == 2 else year
        sem = 1 if sem == 2 else 2
        course_cnt = 1
        for course in yr:
            URL = url + course
            print("[+] Trying " + URL)
            detail_tag = ""
            retry_cnt=0
            f.write(str(course_cnt) + " " + course + ", ")
            #100 Tries
            for i in range(100):
                try:
                    driver.get(URL)
                    html = driver.page_source
                    soup = BeautifulSoup(html, 'html.parser')
                    #tags= soup.find_all('p',string=lambda text: text and 'This module' in text)
                    #print(soup.prettify())
                    detail_tag = soup.find('div',id="details")
                    if(detail_tag is None):
                        raise("[-] Required div is not found.Trying again...")
                    title = detail_tag.find('h1').contents[1]
                    print(title)
                    f.write(title + ", ")
                    break;

                except:
                    print("[-] Retrying ",i)
                    retry_cnt+=1
                    sleep(1)
            
            if(retry_cnt == 100):
                print( "[-]"+ course + " is not on NUSMods")
                missing_modules.append(course)
                continue

            
    #print(detail_tag.prettify())
            try:
                units = detail_tag.find('p').find('span',string=lambda a:a and 'Units' in a).text
                f.write(str(units) + "\n")
            except:
                print("[-] No Modular Units scraped. Check the link: ",URL)  

            final_content = detail_tag.find('section').find('p').text
            f.write(final_content + "\n")
            course_cnt +=1

        f.write("\n")
    f.close()
    print(50*"-" + "\n" + "SUMMARY OF MISSING MODULES" + "\n" + 50*"-")
    for i in missing_modules:
        print(i)

def test(URL):
    print(50*"-" + "\nTEST FUNCTION\n" + 50*"-" + "\n")
    driver.get(URL)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    detail_tag = soup.find('div',id="details")
    #print(detail_tag.prettify())
    units = detail_tag.find('p').find('span',string=lambda a:a and 'Units' in a).text
    print(units)
    print("\n\n\nFinal\n\n\n")
    #print(p_tags[2].find_all('span'))
    content = detail_tag.find('section').find('p').text
    print(content)
def units_calculator(courses):
    for yr in courses:
        year,sem = 0,0
         
if __name__ == '__main__':
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    Y1S1=['CS1010E','MA1505','MA1512','ME1102','GER1000','UTW1001E'] 
    Y1S2=['EG1311','EG2310','MA1513','ME2104','UTC1702E']
    Y2S1=['CFG1002','CP2106','EE2211','ME2102','ME2112','MLE1010','UTC2706']
    Y2S2=['CFG2002I','CS2040C','CS2107','ME2134','ME2162','UTS2709','UTW2001R']
    Y3S1=['EG3611A','ME3163']
    Y3S2=[]
    Y4S1=['LAF1201','ME2115','ME2121','ME2142','ME3242','ME4101A']
    Y4S2=[]
    Y5S1=[]
    Y5S2=[]
    #For custom semesters, ensure to line them up according to their year and sem,
    scrape([[],[],[],[],[Y3S1],[],[Y4S1]],"modulecontext.txt")
    #scrape([Y1S1,Y1S2,Y2S1,Y2S2,Y3S1,Y3S2,Y4S1,Y4S2,Y5S1,Y5S2],"modulecontext.txt")
    #test("https://nusmods.com/courses/ME2121")