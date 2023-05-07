import streamlit as st
import requests
from bs4 import BeautifulSoup
URL=st.session_state['url']
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
videolist=[]
for line in soup.find_all('iframe'):
    video2=line.get('src')
    j=video2.index('trembed')
    #video2=video2[:38]+'3'+video2[39:]
for i in range(10) :
    videolist.append(video2[:38]+str(i)+video2[39:])
for i in videolist :
    page = requests.get(i)
    soup = BeautifulSoup(page.content, "html.parser")
    for line in soup.find_all('iframe'):
        video=line.get('src')
    st.write(video)
    if 'filepress' not in video :
        if 'srt' not in video :
            if video is not None :
                if video!='' :
                    st.write(
                            f'<iframe width="100%" height="500" src="'+video+'" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
                            unsafe_allow_html=True,
                        )
