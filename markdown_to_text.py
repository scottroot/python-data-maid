from bs4 import BeautifulSoup
from markdown import markdown

def markdown_to_text(markdown_string):
    """ Converts a markdown string to plaintext """

    # md -> html -> text since BeautifulSoup can extract text cleanly
    html = markdown(markdown_string)
    # extract text
    soup = BeautifulSoup(html, "html.parser")
    # remove code snippets
    [s.extract() for s in soup(["iframe", "script", "pre", "code"])]
    
    text = ''.join(soup.findAll(text=True))

    # print(text)
    return text
