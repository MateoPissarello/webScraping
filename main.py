import requests
from bs4 import BeautifulSoup

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
    if type == "viewRanks":
        a = soup.find("a")
        data = {
            "url": "https://classcentral.com"+a["href"],
            "text": a.find("span", attrs={"class":"text-1 weight-semi icon-chevron-right-charcoal icon-right-small color-charcoal"}).text
        }
        list_elements.append(data)
    if type == "imgs":
        imgs = soup.find_all("li")
        for i in imgs:
            data = {
                "svg" : i.find("svg"),
                "img_src": i.find("svg").find_all("path")
            }
            list_elements.append(data)
    if type == "article":
        elements = soup.find("ul", attrs={"class":xpath}).find_all("li")
        for ele in elements:
            a = ele.find("a")
            data = {
                "url": "https://classcentral.com"+a["href"],
                "name": a.text,
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
    viewRanks = soup.find("div", attrs={"class":"text-center margin-bottom-xlarge"})
    findRanks = get_full_data(viewRanks,"text-center margin-bottom-xlarge","viewRanks")
    get_articles = get_full_data(articles,"row list-no-style","article")

    data = {
        "universities": universities,
        "providers": providers,
        "institutions": institutions,
        "ranks": ranks,
        "viewRanks": viewRanks,
        "findRanks": findRanks
        }
    return data
    #images_as_seen_in = soup.find("section", attrs={"class":"padding-vert-xxlarge large-down-padding-horz-medium margin-bottom-large border-box"})
    #img_seen_in = get_full_data(images_as_seen_in,"width-1-2 large-up-width-1-3 border-box padding-horz-small padding-vert-xsmall","imgs")
    #TODO svg to png


# def get_full_data_nav(soup, xpath):
#     elemets = soup.find("div", attrs={"class":"xpath"})
#     pass
# def get_data_nav(soup):
#     nav = soup.find('nav', attrs = {"class":"cmpt-nav row nowrap vert-align-middle absolute width-100 padding-horz-medium border-box"})
#     linksnav = get_full_data_nav(nav,"margin-right-small large-up-margin-right-medium")
#     #pass



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
print(scrap)

