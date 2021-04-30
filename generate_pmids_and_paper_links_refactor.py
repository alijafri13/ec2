# import sqlite3
# conn = sqlite3.connect('pmid.db')
from tqdm import tqdm
import ../dynamodb
#conn.execute('''DROP TABLE PMIDS''')
# conn.execute('''CREATE TABLE PMIDS
#          (DOI STRING PRIMARY KEY     NOT NULL);''')

# keep in stage 1
# import sqlite3
# conn = sqlite3.connect('pmid.db')

new_links = open("new_links.txt","w")
DOI_text = open("DOI.txt","w")

# def INSERT_IF_NOT_EXIST_AND_RETURN_FLAG(doi):
#     c = conn.cursor()
#     vars_ = c.execute("SELECT * FROM PMIDS WHERE DOI = (?)", (doi,))
#     li = [row for row in vars_]
#     if li == []:
#         c = conn.cursor()
#         c.execute("INSERT INTO PMIDS (DOI) VALUES (?)", (doi,));
#         conn.commit()
#         return False

#     return True

import requests
from bs4 import BeautifulSoup

Base = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
URL = 'https://scihubtw.tw/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
summary = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id="
end_summary = "&retmode=json&tool=my_tool&email=pholur@nextnet.com"

def modify_search_term(search_term):
    return search_term.replace(" ","+")


def get_DOI(search_term, NumResults=100):
    modified_search_term = modify_search_term(search_term)
    eSearch = "esearch.fcgi?db=pubmed&term=" + modified_search_term
    QueryURL = Base + eSearch + "&retmax=" + str(NumResults) + "&format=json"
    result = requests.get(QueryURL).json()["esearchresult"]["idlist"]
    doi_res = []

    for res in result:
        try:
            doids = requests.get(summary + res + end_summary).json()["result"][res]["articleids"]
            for id_ in doids:
                if id_["idtype"] == "doi":
                    doi_res.append(id_["value"])
        except:
            continue
    return doi_res


def pull_pdf_from_scihub(list_of_DOIs):
    print('Fetching URLs...')
    all_links = []
    for DOI in tqdm(list_of_DOIs):

        if write_DOI(DOI):
            continue

        response = requests.post(URL, data = {'request': DOI}, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        if "not found" not in soup:
            try:
                link = soup.find_all('iframe')[0]['src'].lstrip('//')
                if "#view=FitH" in link:
                    link = link[:-10]
                    all_links.append(link)
                    new_links.write(str(link) + "\n")
                    DOI_text.write(str(DOI)+ "\n")
#                     print(link)

            except:
                continue
    return all_links

read = open('test.txt','r')
term = read.readlines()
# print(term)
term_fix = term[0]
print('search term = ' + term_fix)
doi = get_DOI(term_fix)
print(doi)
print(pull_pdf_from_scihub(doi))
