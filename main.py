from pprint import pprint
from bs4 import BeautifulSoup
from PRTO import PRTO, Antenna, BaseStation
from rutermextract import TermExtractor

term_extractor = TermExtractor()
ext_text = []



if __name__ == '__main__':
    with open('test/data1.html', 'r') as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')
        for child in soup.recursiveChildGenerator():       
            if child.name == 'p':            
                ext_text.append(child.text)

    for i in ext_text:
        pprint (i)
        #for term in term_extractor(i):
            #print (i, term.normalized, term.count)
        
    SZZ_title = ext_text[1]
    SZZ_text = ext_text[2]