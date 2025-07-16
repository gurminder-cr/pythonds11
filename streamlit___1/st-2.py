import streamlit as st
from streamlit_option_menu import option_menu

import base64
# pip install streamlit-option-menu
st.set_page_config('APP')

# st.header('Sidebar')

# with st.sidebar:
#     st.header("Sidebar code")
#     st.subheader("Subheader")

# st.sidebar.header("Sidebar header")

# with st.sidebar:
#     # state= st.selectbox('Select State', options=['Punjab','Gujrat','MP','HP','UP'])
#     # if st.button('submit'):
#     #     st.write(state)
    
#     # opt= st.radio('Menu',options=['Home','About','Contact'])
#     opt= option_menu("Menu",options=['Home','About','Contact'], icons=['house-fill','info-square-fill','phone-fill'])
    
# opt= option_menu("",options=['Home','About','Contact'], icons=['house-fill','info-square-fill','phone-fill'],orientation='horizontal')
   
# if opt=="Home":
#     st.header("Home page")
# elif opt=="About":
#     st.header("About page")
# elif opt=="Contact":
#     st.header("Contact Page")
        
        
# st.image('img-1.jpg')
# st.video('')
# st.audio('')


with open('img-1.jpg','rb') as f:
    data= f.read()

img= base64.b64encode(data).decode()

css=f"""
    <style>
    [data-testid="stAppViewContainer"]{{
        background-image:url('data:image/png;base64,{img}');
        background-size:cover
        
    }}
    </style>
"""
st.markdown(css, unsafe_allow_html=True)

st.header("Helo")