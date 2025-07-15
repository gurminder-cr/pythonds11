import streamlit as st

st.set_page_config('First Lecture', page_icon="🏠")

# st.header('Hello Class')
st.header('Registration :red[form] :writing_hand:')
# st.subheader('Hello this is subheader')

# st.write('hello how are you')

# naam=st.text_input('Name',placeholder='Enter your name here....')
# age= st.number_input('Age', min_value=5, max_value=50)

# # btn= st.button("Submit")
# if st.button("Submit"):
#     st.write(naam, age)


with st.form(key='key'):
    col1, col2, col3= st.columns((1,1,1))
    with col1:
        first_naam= st.text_input('First Name')
        age= st.number_input("Age")
    with col2:
        mid_naam= st.text_input('Middle Name')
        gender= st.radio('Gender', options=['Male','Female'],horizontal=True)
    with col3:
        last_naam= st.text_input('Last Name')
        dob= st.date_input("Enter DOB")
        
    check=st.checkbox('Terms and conditions')
    # st.camera_input("Image")
    
        
        
    if st.form_submit_button():
        st.success("Registered successfully")
        # st.error("Registered successfully")
        st.balloons()
        
        
    
# for bold use ** text ** 

st.write("this is **boldtext**")
st.write("this is _itallic_")