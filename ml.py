import numpy as np
import streamlit as st
from PIL import Image

#from forms import dl, intelli, du, dv, evaluation, ExData, DFrame, FEngineering, pProfile
#from forms import dl, DFrame, FEngineering, ExData, pProfile, machine_learning, ModelBuild, home
from forms import dl, DFrame, FEngineering, ExData, machine_learning, ModelBuild, home
from mp import MP

# create page title
st.set_page_config(
    layout="wide",
    page_title="MatFlow: Materials Design System",
    page_icon="๐จโ๐ป",
)
st.markdown("""
<h3 class="title" style='text-align: center; background-color: lightblue; font-family: "Lucida Console", "Courier New", monospace;'>
        Knowledgebased Materials Design System Using Machine Learning</h3>
""", unsafe_allow_html=True)
# instance of our system
ml = MP()
display = Image.open('banner.png')
display = np.array(display)
st.image(display)

hide_streamlit_style = """ 
 <style>
     #MainMenu {visibility:hidden}
     footer{visibility:hidden}
    </style>
"""
# Remove Streamlit footer note and repository notes
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Add all my application pages here
ml.connect("Start", home.load_view)
ml.connect("๐๏ธUpload Dataset", dl.main)
ml.connect("โ๏ธTraining", ModelBuild.main)
ml.connect("๐ก Best Fit", machine_learning.main)
#ml.connect("โ Change Metadata", du.main)
ml.connect("๐ฅ Statistical Data", DFrame.main)
ml.connect("๐ Exploratory Data Analysis", ExData.main)
ml.connect("โ๏ธ Feature Engineering", FEngineering.main)
#ml.connect("๐ Data Analysis", dv.main)
#ml.connect("๐ Optimization and Evaluation", evaluation.main)
#ml.connect("๐ฉ๐ปโ๐ปPandas Auto Profiling", pProfile.main)

# The main app
ml.start()
