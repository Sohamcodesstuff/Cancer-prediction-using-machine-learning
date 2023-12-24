#core packages
import streamlit as st
import time


#database system
import predictor


def main():
    st.title("Breast Cancer Prediction System")
    menu = ["Predict","About"]
    st.sidebar.image("Streamlit_ui_refactor/b_cancer.png",width=200)
    choice = st.sidebar.selectbox("Menu",menu)
    params = []
    prediction = None

    
    if choice=="Predict":
        st.subheader("Input Biopsy Parameters")
        p1 = st.number_input("Texture Mean", min_value=9.71, max_value=39.2, value=9.71)
        p2 = st.number_input("Area Mean", min_value=143.5, max_value=2501.00, value=143.5)
        p3 = st.number_input("Concavity Mean", min_value=0.00, max_value=0.43, value=0.00)
        p4 = st.number_input("Area SE", min_value=6.80, max_value=542.20, value=6.80)
        p5 = st.number_input("Concavity SE", min_value=0.00, max_value=0.40, value=0.00)
        p6 = st.number_input("Fractal Dimension SE", min_value=0.00, max_value=0.03, value=0.00)
        p7 = st.number_input("Smoothness Worst", min_value=0.07, max_value=0.22, value=0.07)
        p8 = st.number_input("Concavity Worst", min_value=0.00, max_value=1.25, value=0.00)
        p9 = st.number_input("Symmetry Worst", min_value=0.16, max_value=0.67, value=0.16)
        p10 = st.number_input("Fractal Dimension Worst", min_value=0.06, max_value=0.21, value=0.06)

        params = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]

        st.empty()

        if st.button("Predict Tumour type"):

            progress_text = "Processing data"
            prediction = predictor.predict(parameters=params)
            my_bar = st.progress(0, text=progress_text)

            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1, text=progress_text)
            time.sleep(1)
            my_bar.empty()
            if(prediction[0]==0):
                st.success("The patient is likely to have a benign tumour")
            else:
                st.error("The patient is likely to have a malignant tumour")

    elif choice=="About":
        st.subheader("About this app")
        st.text("Created By Soham Chakraborty")
        st.text("Linkedin:-")
        st.link_button("Linkedin","https://www.linkedin.com/in/soham-chakraborty-a07b471b0/")
        st.text("Github:-")
        st.link_button("Github","https://github.com/Sohamcodesstuff/Cancer-prediction-using-machine-learning")
        st.text("Version:- 2.0")



    
    pass





if __name__=="__main__":
    main()
