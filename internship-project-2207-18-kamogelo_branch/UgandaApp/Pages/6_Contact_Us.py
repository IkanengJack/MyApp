import streamlit as st 

options = {
    "Contact Us": lambda: contact_us()
}

def contact_us():
    st.image("Ab.jpg", width=450)
    st.header(" Get in touch with us 📩 ")
    contact_form = """
    <form action="https://formsubmit.co/ereshiagabier@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name"required>
        <input type="email" name="email" placeholder="Your email"required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("style/style.css")
    st.image("Thank you.jpg", width=700)

selection = "Contact Us"
options.get(selection, lambda: None)()
