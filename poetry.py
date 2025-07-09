import streamlit as st

# Title of the page
st.title("কবিতার পাতা")

# Poetry post form
st.header("নতুন কবিতা পোস্ট করুন")
with st.form("poetry_form", clear_on_submit=True):
    author = st.text_input("আপনার নাম")
    poem_title = st.text_input("কবিতার শিরোনাম")
    poem_text = st.text_area("আপনার কবিতা")
    submitted = st.form_submit_button("পোস্ট করুন")
    if submitted and poem_text and author and poem_title:
        # Save poetry to session state (for demo; replace with database in real use)
        if "poems" not in st.session_state:
            st.session_state["poems"] = []
        st.session_state["poems"].insert(0, {
            "author": author,
            "title": poem_title,
            "text": poem_text
        })
        st.success("আপনার কবিতা পোস্ট হয়েছে!")

# Show all poems
st.header("সাম্প্রতিক কবিতাসমূহ")
if "poems" in st.session_state and st.session_state["poems"]:
    for poem in st.session_state["poems"]:
        st.subheader(poem["title"])
        st.write(poem["text"])
        st.markdown(f"_লিখেছেন: {poem['author']}_")
        st.markdown("---")
else:
    st.info("এখনো কোনো কবিতা পোস্ট হয়নি।")
