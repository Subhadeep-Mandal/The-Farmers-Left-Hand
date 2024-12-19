import streamlit as st
# Home page
def home_page():
    st.markdown("<h1 style='text-align:center;'>DISEASE RECOGNITION SYSTEM🔍</h1>", unsafe_allow_html=True)
    st.markdown("---")
    image1 = "https://img.freepik.com/premium-photo/flower-pot-with-face-face-it_910054-7476.jpg"
    image2 = "https://static.vecteezy.com/system/resources/previews/007/506/342/non_2x/cute-jade-plant-illustration-cute-plant-pot-free-vector.jpg"
    col, col1 = st.columns(2)

    # CSS to make images circular
    st.markdown(
        """
        <style>
        .circle-img {
            border-radius: 30%;
            width: 100%;
            height: auto;
            padding: 30px;
        }
        .center-caption {
            font-weight: bold;
            margin-left: 180px;
        }
        .left-align {
            text-align: justify;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    with col1:
        st.markdown(f"<img src='{image2}' class='circle-img' alt='PLANTS'>", unsafe_allow_html=True)
        st.markdown("<div class='center-caption'>--- LOVE PLANTS ---</div>", unsafe_allow_html=True)
    
    with col:
        st.markdown(f"<img src='{image1}' class='circle-img' alt='ANIMALS'>", unsafe_allow_html=True)
        st.markdown("<div class='center-caption'>--- CURE PLANTS ---</div>", unsafe_allow_html=True)

    # Markdown text for the Home page
    st.header(" 🦠 WELCOME TO OUR DISEASE DETECTOR ")
    st.markdown("""
    ---
    ## Empowering You with Disease Detection
    Welcome to our innovative platform designed to help you identify diseases in plants and animals through image recognition. Our mission is to provide you with accurate and timely information to ensure the health and well-being of your plants and animals.
    """
    )
    st.markdown("""
                ---
    ### How It Works

    1. **Upload an Image**: Start by uploading a clear image of the diseased plant or animal you want to diagnose.
    2. **Analyze**: Our advanced machine learning models analyze the image to detect any signs of disease.
    3. **Get Results**: Receive a detailed report with the most probable diseases and recommended actions.
    ---
    ### Why Choose Us?

    - **Accuracy**: Our models are trained on extensive datasets to provide reliable predictions.
    - **Privacy**: Your data is secure with us. We prioritize your privacy and ensure that your information is protected.
    - **Ease of Use**: Our platform is designed to be intuitive and easy to navigate, making it accessible for everyone.
    ---
    ### Our Mission

    We believe in empowering individuals with knowledge about the health of their plants and animals. Our goal is to make disease detection more accessible and proactive, helping you take control of their well-being.
    
    ---
    ### Contact Us

    If you have any questions or need further assistance, please don't hesitate to contact us.

    ---

    Thank you for choosing our platform. We are here to support you in maintaining the health of your plants and animals.
    """
    )