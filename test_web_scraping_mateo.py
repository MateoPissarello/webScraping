import requests
from bs4 import BeautifulSoup
from pprint import pprint


def remove_space(string):
    return string.lstrip().rstrip().replace("\n", "")

def get_nav(soup):
    list_elements = []
    nav_bar = soup.find("nav", attrs = {"class": "cmpt-nav row nowrap vert-align-middle absolute width-100 padding-horz-medium border-box"})
    login_singup = nav_bar.find("div", attrs = {"class":"hidden xlarge-up-inline-block"}).find_all("a")
    for i in login_singup:
        text = i.text
        url = i["href"]
        data = {
            "text": text,
            "url": "http://classcentral.com"+url,
        }
        list_elements.append(data)
    return list_elements
def get_popularCourses(soup):
    list_elements = []
    popular_courses = soup.find("div", attrs = {"class":"width-100 medium-up-width-2-3 border-box medium-up-padding-left-large horz-align-right"})
    subject_university_learn_more = popular_courses.find_all("a", attrs = {"class":"link-gray-underline"})
    for i in subject_university_learn_more:
        text = i.text
        url = i["href"]
        data = {
            "text": text,
            "url": "http://classcentral.com"+url,
        }
        list_elements.append(data)
    li_popular_courses = popular_courses.find("ul", attrs = {"id": "home-subjects"}).find_all("li")
    for li in li_popular_courses:
        a = li.find("a")
        url = a["href"]
        try :
            img = li.find("a").find("img")["src"]
        except :
            img = "no image available"
        text = a.find("span").text
        data = {
            "url": url,
            "img" : img,
            "text" : text,
        }
        list_elements.append(data)
    return list_elements

def get_footer(soup):
    list_elements = []
    footer_div = soup.find("div", attrs = {"class":"width-page large-down-padding-horz-medium padding-vert-large border-box"})
    ul_footer1 = footer_div.find_all("ul", attrs = {"class":"list-no-style text-2"})
    ul_footer2 = footer_div.find_all("ul", attrs = {"class": "row list-no-style text-2"})
    names_footer = footer_div.find_all("a", attrs = {"class": "inline-block margin-bottom-xxsmall text-2 color-charcoal weight-bold border-bottom border-gray hover-no-underline"})
    name_browse_university=footer_div.find("a",attrs = {"class": "inline-block text-2 margin-bottom-xxsmall color-charcoal weight-bold border-bottom border-gray hover-no-underline"})
    div_about_us = footer_div.find("div", attrs = {"class":"width-100 medium-up-width-3-5 margin-bottom-medium"})
    text_about_us = "About class central:" + div_about_us.find("p").text
    list_elements.append(text_about_us)
    li_social_media = div_about_us.find("ul").find_all("li")
    for li in li_social_media:
        url = li.find("a")["href"]
        name = li.find("a").text
        data = {
            "url": url,
            "name_socialmedia": name,
        }
        list_elements.append(data)
    
    dataUniversity = {
        "name": remove_space(name_browse_university.text),
        "url": "http//classcentral.com" + name_browse_university["href"]
    }
    list_elements.append(dataUniversity)
    for name in names_footer:
        data = {
            "name":remove_space(name.text),
            "url": "http://classcentral.com" + name["href"]
        }
        list_elements.append(data)
    for ul in ul_footer1:
        li = ul.find_all("li")
        for i in li:
            url = i.find("a")["href"]
            name = i.find("a").text
            data = {
                "url": url,
                "name":name,
            }
            list_elements.append(data)
    for ul in ul_footer2:
        li = ul.find_all("li")
        for i in li:
            url = i.find("a")["href"]
            name = i.find("a").text
            data = {
                "url": url,
                "name":name,
            }
            list_elements.append(data)
    return list_elements


def get_all_collections(soup):
    list_elements = []
    collections = soup.find("ul", attrs = {"class":"list-no-style row wrap margin-bottom-xxlarge"}).find_all("li")

    for collection in collections:
        img = collection.find("a").find("img")["src"]
        url = collection.find("a")["href"]
        data = {
            "img": img,
            "url": "https://classcentral.com" + url,
        }
        list_elements.append(data)
    return list_elements
def get_all_buttons(soup):
    list_elements = []
    buttonsPurple = soup.find_all("a", attrs={"class":"btn-gradient-purple scale-on-hover"})
    orangeButtons = soup.find("a", attrs={"class":"btn-gradient-orange scale-on-hover"})
    blueButton = soup.find("a", attrs={"class":"btn-gradient-blue scale-on-hover"})
    greenButton = soup.find("a", attrs={"class":"btn-gradient scale-on-hover"})
    for ele in buttonsPurple:
        data = {
            "url": "https://classcentral.com"+ele["href"],
            "text": remove_space(ele.find("span", attrs={"class":"text-1 weight-semi icon-chevron-right-charcoal icon-right-small color-charcoal"}).text)
        }
        list_elements.append(data)
    dataOrange = {
        "url": "https://classcentral.com" + orangeButtons["href"],
        "text":  remove_space(orangeButtons.find("span", attrs={"class":"text-1 weight-semi icon-chevron-right-charcoal icon-right-small color-charcoal"}).text)   
        }
    list_elements.append(dataOrange)
    dataBlue = {
        "url": "https://classcentral.com" + blueButton["href"],
        "text":  remove_space(blueButton.find("span", attrs={"class":"text-1 weight-semi icon-chevron-right-charcoal icon-right-small color-charcoal"}).text)   
        }
    list_elements.append(dataBlue)
    dataGreen = {
        "url": "https://classcentral.com" + greenButton["href"],
        "text":  remove_space(greenButton.find("span", attrs={"class":"text-1 weight-semi icon-chevron-right-charcoal icon-right-small color-charcoal"}).text)   
        }            
    list_elements.append(dataGreen)
    return list_elements      

def get_data_courses_guides(soup):
    list_elements = []
    courses = soup.find("ul", attrs = {"class": "margin-bottom-xlarge list-no-style"}).find_all("li")
    for course in courses:
        img = course.find("div", attrs={"class":"width-100 medium-up-width-1-3 horz-align-left row"}).find("a").find("img")["src"]
        link = course.find("div", attrs={"class":"width-100 medium-up-width-1-3 horz-align-left row"}).find("a")["href"]
        author = course.find("div", attrs={"class":"border-box width-100 medium-up-width-2-3 medium-up-padding-left-medium"}).find("p").find("strong").text
        text = course.find("a", attrs = {"class":"head-3 medium-up-head-2 color-charcoal"}).text
        data = {
            "img_course": img,
            "link": link,
            "author": author,
            "text": remove_space(text)
        } 
        list_elements.append(data)
    return list_elements

def get_data_article(soup):
    list_elements = []
    articles = soup.find('ul',attrs={"id":"home-report-recent"}).find_all('li')
    for article in articles:
        arti = article.find('a',attrs={"class":"head-3 weight-semi line-tight color-charcoal"})
        author = article.find('div',attrs={"class":"row nowrap"})
        data = {
            "url_article": arti['href'],
            "title": remove_space(arti.text),
            "author_url": author.find('a')["href"],
            "author_name": remove_space(author.find('a').find('span').text),
            "publish":author.find('span',attrs={"class":"text-2 inline-block color-gray inline-block"}).text

        }
        list_elements.append(data)
    return list_elements

def get_full_data(soup, xpath, type=None, index=None):
    list_elements = []
    if type == "midpage":
        if index is None:
            elements = soup.find('li',attrs={"class":xpath}).find('ul').find_all('li')
        else:
            elements = soup.find_all('li',attrs={"class":xpath})[index].find('ul').find_all('li')
        for ele in elements:
            a = ele.find('a')
            data = {
                "url": "https://www.classcentral.com"+a['href'],
                "name": a.find('strong',attrs={"class":"margin-left-xsmall fill-space"}).text,
                "img": a.find('img')["src"]
            }
            list_elements.append(data)
    if type == "rankings":
        elements = soup.find_all("li", attrs={"class":xpath})
        for ele in elements:
            a = ele.find('a')
            data = {
                "url": "https://www.classcentral.com"+a['href'],
                "img": a.find('img')["src"],
            }
            list_elements.append(data)
    # if type == "viewRanks":
    #     a = soup.find("a")
    #     data = {
    #         "url": "https://classcentral.com"+a["href"],
    #         "text": a.find("span", attrs={"class":"text-1 weight-semi icon-chevron-right-charcoal icon-right-small color-charcoal"}).text
    #     }
    #    list_elements.append(data)
    if type == "imgs":
        imgs = soup.find_all("li")
        for i in imgs:
            data = {
                "svg" : i.find("svg"),
                "img_src": i.find("svg").find_all("path")
            }
            list_elements.append(data)


    return list_elements


def get_data_all(soup):
    down = soup.find('ul',attrs={"class":"list-no-style row large-up-nowrap"})
    rankings = soup.find('ul',attrs={"class":"max-850 width-centered list-no-style row large-up-nowrap margin-bottom-xxlarge"})
    articles = soup.find("div", attrs={"width-100 border-box large-up-padding-right-large large-up-width-1-2"})
    universities = get_full_data(down,"border-box width-100 large-up-width-3-7 padding-horz-small relative","midpage")
    providers = get_full_data(down,"medium-down-hidden decor-grid-line border-box width-100 large-up-width-2-7 padding-horz-small large-up-padding-horz-large relative","midpage",0)
    institutions = get_full_data(down,"medium-down-hidden decor-grid-line border-box width-100 large-up-width-2-7 padding-horz-small large-up-padding-horz-large relative","midpage",1)
    ranks = get_full_data(rankings,"width-100 border-box padding-small large-up-width-1-2 border-box","rankings")
    get_articles = get_data_article(soup)
    buttons = get_all_buttons(soup)
    courses = get_data_courses_guides(soup)
    collections = get_all_collections(soup)
    footer = get_footer(soup)
    popularCourses = get_popularCourses(soup)
    nav = get_nav(soup)

    data = {
        "universities": universities,
        "providers": providers,
        "institutions": institutions,
        "ranks": ranks,
        "articles": get_articles,
        "buttons": buttons,
        "courses": courses,
        "collections": collections,
        "footer": footer,
        "popularCourses": popularCourses,
        "nav": nav
        }
    return data
def get_data():
    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': 'youremail@domain.example'
    }
    r = requests.get('https://www.classcentral.com/',headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    x = get_data_all(soup)
    return x
    # get_data_nav(soup)
scrap = get_data()
pprint(scrap)