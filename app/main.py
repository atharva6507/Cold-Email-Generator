import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from chains import Chain
from portfolio import Portfolio
from utils import clean_text

def create_streamlit_app(chain_instance, portfolio_instance, text_cleaner):
    st.title("📧 Cold Mail Generator")
    url_input = st.text_input("Enter a URL:")
    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = text_cleaner(loader.load().pop().page_content)
            portfolio_instance.load_portfolio()
            jobs = chain_instance.extract_jobs(data)
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio_instance.query_links(skills)
                email = chain_instance.write_mail(job, links)
                st.code(email, language='markdown')
        except Exception as e:
            st.error(f"An Error Occurred: {e}")


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)
