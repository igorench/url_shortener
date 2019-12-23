import requests
from bs4 import BeautifulSoup
from django.template import engines
from .сonstants import TEXT_DELIMITER


def parse_page(url):
    try:
        page = requests.get(url)
    except requests.exceptions.ConnectionError:
        print("This url doen't exist", flush=True)
        return ''
    text = ""

    if page.status_code == 200:
        soup = BeautifulSoup(page.content, "html.parser")
        tags = ["p", "span", "h1", "h2", "h3", "h4", "h5", "h6"]

        for tag in tags:
            text += get_text_by_tag(soup, tag) + "\n"

        return modify_text_icon(text, TEXT_DELIMITER)

    return text


def get_text_by_tag(soup, tag):
    tag = soup.find_all(tag)

    if len(tag):
        return "{} ".format(tag[0].text)

    return ""


def modify_text_icon(text, icon):
    for char in text: 
        if char in "\n":
             text = text.replace(char,'') 

    texts = text.split(" ")
    modify_texts = []

    for text in texts:
        if len(text) == 6 and text.isalpha() and text[-1] != "," and text[-1] != '.' and text[-1] != '!' and text[-1] != '?':
            modify_texts.append("{}{}".format(text, icon))
        elif (len(text) == 7) and text.isalpha() and (text[-1] == "," or text[-1] == '.' or text[-1] == '!' or text[-1] == '?'):
            text = text[:-1] + TEXT_DELIMITER + text[-1:]
            modify_texts.append("{}".format(text))
        else:
            modify_texts.append("{}".format(text))

    modify_texts = " ".join(modify_texts)

    return modify_texts
