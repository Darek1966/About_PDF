import os
import streamlit as st
from PyPDF2 import PdfReader, PdfWriter 
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback

def ChatPDF(text):
# st.write(tekst)
    
# podzielić na kawałki
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function=len
    )

    chunks = text_splitter.split_text(text)
# st.write(kawałki)
# tworzenie osadzeń

    OPENAI_API_KEY = st.text_input("OPENAI API KEY", type = "password")
    if OPENAI_API_KEY:
        embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
# st.write("Utworzono osadzanie")
# st.write(osadzenia)
        knowledge_base = FAISS.from_texts(chunks, embeddings)
        st.write("Utworzono Bazę Wiedzy ")
# pokaż dane wprowadzone przez użytkownika

        def ask_question(i=0):
            user_question = st.text_input("Zadaj pytanie dotyczące pliku PDF?",key = i)
            if user_question:
                docs = knowledge_base.similarity_search(user_question)
# st.write(docs)

                llm = OpenAI(openai_api_key=OPENAI_API_KEY)
                chain = load_qa_chain(llm, chain_type="stuff")
                with get_openai_callback() as cb:
                    response = chain.run(input_documents=docs, question=user_question)
                    print(cb)
                st.write(response)
                ask_question(i+1)
                
        ask_question()

def main():
    st.set_page_config(page_title="Zapytaj o PDF",
                       page_icon="📄")

    hide_st_style = """
            <style>
            #mainMenue {visibility: hidden;}
            footer {visibility: hidden;}
            #header {visibility: hidden;}
            </style>
    """
    st.markdown(hide_st_style, unsafe_allow_html=True)

# st.write(st.set_page_config)
    st.header("Zapytaj swojego PDF_a 😎💭")
    
# przesyłanie pliku
    pdf = st.file_uploader("Prześlij plik PDF ", type="pdf")

# wyodrębnij tekst
    if pdf is not None:
        option = st.selectbox("Co chcesz zrobić z plikiem PDF 📜", [
            "Metadane 📂",
            "Wyodrębnij surowy tekst 📄",
            "Wyodrębnij linki 🔗",
            "Wyodrębnij obrazy 🖼️",
            "Zabezpiecz PDF hasłem 🔐",
            "Adnotacja PDF 📝",
            "Chat_PDF 💬"
            ])
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        if option == "Metadene 📂":
            st.write(pdf_reader.metadata)
        elif option == "Zabezpiecz PDF hasłem 🔐":
            pswd = st.text_input("Wprowadź hasło", type="password")
            if pswd:
                with st.spinner("Szyfrowanie..."):
                    pdf_writer = PdfWriter()
                    for page_num in range(len(pdf_reader.pages)):
                        pdf_writer.add_page(pdf_reader.pages[page_num])
                        
                    pdf_writer.encrypt(pswd)
                    with open(f"{pdf.name.split('.')[0]}_szyfrowany.pdf", "wb") as f:
                        pdf_writer.write(f)

                    st.success("Szyfrowano pomyślne!")
                    st.download_button(
                        label="Pobierz zaszyfrowany plik PDF",
                        data=open(f"{pdf.name.split('.')[0]}_szyfrowany.pdf", "rb").read(),
                        file_name=f"{pdf.name.split('.')[0]}_szyfrowany.pdf",
                        mime="application/octet-stream",
                    )
                    try:
                        os.remove(f"{pdf.name.split('.')[0]}_szyfrowany.pdf")
                    except: pass
        elif option == "Wyodrębnij surowy tekst 📄":
            st.write(text)
        elif option == "Wyodrębnij linki 🔗":
            for page in pdf_reader.pages:
                if "/Annots" in page:
                    for annot in page["/Annots"]:
                        subtype = annot.get_object()["/Subtype"]
                        if subtype == "/Link":
                            try:
                                st.write(annot.get_object()["/A"]["/URI"])
                            except: pass
        elif option == "Wyodrębnij obrazy 🖼️":
            for page in pdf_reader.pages:
                try:
                    for img in page.images:
                        st.write(img.name)
                        st.image(img.data)
                except: pass
        elif option == "Adnotacja PDF 📝":
            for page in pdf_reader.pages:
                if "/Annots" in page:
                    for annot in page["/Annots"]:
                        obj = annot.get_object()
                        st.write(obj)
                        st.write("***********")
                        annotation = {"subtype": obj["/Subtype"], "location": obj["/Rect"]}
                        st.write(annotation)
        elif option == "Chat_PDF 💬":
            ChatPDF(text)
    

if __name__ == "__main__":
    main()
# https://emojipedia.org/ 😎
