import requests
from bs4 import BeautifulSoup

#step 1:get article url
def get_wikipeida_url(topic):
    url=f"https://en.wikipedia.org/wiki/{topic.replace(' ','_')}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response=requests.get(url, headers=headers)
    if response.status_code==200:
      return response.text
    else:
      print(f"failed to retrive article. Status code: {response.status_code}.Check the topic and try again")
      return None

def get_article_title(soup):
  return soup.find('h1').text

def get_article_summary(soup):
  paragraphs = soup.find_all('p')
  for para in paragraphs:
    if para.text.strip():
      return para.text.strip()
  return "No Summary Found"

def get_headings(soup):
  headings=[heading.text.strip()  for heading in soup.find_all(['h2','h3','h4','h5','h6'])]
  return headings


def get_related_links(soup):
  links=[]
  for a_tag in soup.find_all('a',href=True):
    href=a_tag['href']
    if href.startswith('/wiki/') and ':' not in href:
      links.append(f"https://en.wikipedia.org{href}")
  return list(set(links))[:5]


def main():
  topic=input("Enter the topic for wikipedia article: ").strip()
  html_content=get_wikipeida_url(topic)
  if html_content:
    soup=BeautifulSoup(html_content,'html.parser')
    title=get_article_title(soup)
    summary=get_article_summary(soup)
    headings=get_headings(soup)
    related_links=get_related_links(soup)

    print(f"\n---Wikipedia Article---")
    print(f"Title: {title}")
    print(f"Summary: {summary}")
    print("\n---Headings---")
    for heading in headings[:6]:
      print(heading)
    print("\n---Related Links---")
    for link in related_links:
      print(link)

if __name__=='__main__':
  main()
