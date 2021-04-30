import requests
import sys
import os


# url='https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5283695/pdf/nihms829208.pdf'
file_with_urls = sys.argv[1] # of batch length
file_with_DOI = sys.argv[2]
folder_to_files = sys.argv[3]

#folder_to_files = "/Users/pholur/Desktop/to_ali/"

urls = open(file_with_urls, 'r')
urls_lines = urls.readlines()
fail_rate = 0
DOIs = open(file_with_DOI, 'r')
DOIs = DOIs.readlines()
# urls_lines = ['https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5283695/pdf/nihms829208.pdf']
for i, (url, DOI) in enumerate(zip(urls_lines, DOIs)):
    if url[-1] == "\n":
        url = url[:-1]
#         print(url)
        if url[0:5] != "https":
                url = "https://" + url
#                 print(url)

    if url == "":
        print("CORRUPT URLs FILE! ABORT.", file=sys.stderr)
        exit(-1)

    try:
#         # add headers to spoof website
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
#         # we can store the url in the name
        with open(folder_to_files + 'Pavan'+ str(DOI.replace("/","ALI").replace('\n',"").replace('.','DOT').replace('-','DASH'))  + ".pdf", 'wb') as f:
            f.write(r.content)
        print(url + ' downloaded')

    except:
        print("Url: " + str(url) + " failed to download", file=sys.stderr)
        fail_rate += 1
print("Fail Rate: ", fail_rate / float(len(urls_lines)))
