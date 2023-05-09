import streamlit as st



#st.write('The current movie title is', title)



opt = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'LinkedIn'))

if(opt=="Email"):
    st.write("deepak2004sakthi@gmail.com")
else:
    st.write("https://www.linkedin.com/in/deepaksakthi-v-k-2085a81ab/")



title = st.text_input('FeedBack', '')
if len(title)>0:
    st.caption("Thank you for your Feedback")
    st.balloons()