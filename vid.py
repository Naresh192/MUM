import requests
from bs4 import BeautifulSoup
import streamlit as st
def switch_page(page_name: str):
    from streamlit import _RerunData, _RerunException
    from streamlit.source_util import get_pages

    def standardize_name(name: str) -> str:
        return name.lower().replace("_", " ")
    
    page_name = standardize_name(page_name)
    
    pages = get_pages("vid.py")  # OR whatever your main page is called
    print(pages)
    for page_hash, config in pages.items():
        if standardize_name(config["page_name"]) == page_name:
            raise _RerunException(
                _RerunData(
                    page_script_hash=page_hash,
                    page_name=page_name,
                )
            )

    page_names = [standardize_name(config["page_name"]) for config in pages.values()]

    raise ValueError(f"Could not find page {page_name}. Must be one of {page_names}")
st.set_page_config(layout="wide")
if 'url' in st.session_state :
    st.session_state['url']
MGIName=st.text_input("Enter Mobie Name")

URL = "https://www.bolly2tolly.wiki/?s="+ MGIName
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
for line in soup.find_all('a'):
    try :
            if st.button(line.get('href'),key=line.get('href')) :
                    st.session_state['url']=line.get('href')
                    st.write("switc2h")
                    switch_page('vid')
                    st.write('done')
    except :
        pass
    

