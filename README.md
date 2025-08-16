# All_About_PDF

## 📝 Opis

All_About_PDF to internetowa aplikacja do kompleksowej pracy z plikami PDF, zbudowana przy użyciu Pythona i frameworka Streamlit. Aplikacja umożliwia wykonywanie różnych operacji na plikach PDF, takich jak wyodrębnianie tekstu, obrazów, metadanych, szyfrowanie plików hasłem oraz funkcję ChatPDF wykorzystującą technologie OpenAI i LangChain do interakcji z plikami PDF za pomocą przetwarzania języka naturalnego.

Motywacją stojącą za All_About_PDF było stworzenie prostego, przyjaznego dla użytkownika narzędzia do pracy z plikami PDF. Chociaż w Internecie dostępnych jest wiele narzędzi związanych z plikami PDF, wiele z nich jest skomplikowanych i trudnych w użyciu. All_About_PDF ma na celu zapewnienie łatwej w użyciu alternatywy, z której może korzystać każdy, niezależnie od wiedzy technicznej.

## ✨ Funkcje

- **Wyodrębnianie tekstu** 📄 - Ekstrakcja tekstu z plików PDF
- **Wyodrębnianie obrazów** 🖼️ - Ekstrakcja obrazów z plików PDF
- **Wyodrębnianie linków** 🔗 - Ekstrakcja linków z plików PDF
- **Wyodrębnianie metadanych** 📂 - Ekstrakcja metadanych z plików PDF
- **Adnotacje PDF** 📝 - Przeglądanie adnotacji w plikach PDF
- **Szyfrowanie PDF** 🔐 - Zabezpieczanie plików PDF hasłem
- **ChatPDF** 💬 - Interaktywna rozmowa z plikiem PDF przy użyciu OpenAI i LangChain

## 🚀 Instalacja

### Wymagania wstępne

- Python 3.11 lub nowszy
- Pip (menedżer pakietów Pythona)

### Kroki instalacji

1. Sklonuj repozytorium:

   ```bash
   git clone https://github.com/twoj-username/All_About_PDF.git
   cd All_About_PDF
   ```
2. Utwórz i aktywuj wirtualne środowisko (opcjonalnie, ale zalecane):

   ```bash
   # Używając venv
   python -m venv .venv
   # W Windows
   .venv\Scripts\activate
   # W Linux/MacOS
   source .venv/bin/activate
   ```
3. Zainstaluj wymagane zależności:

```bash
pip install -r requirements.txt

```

## 📋 Użycie

1. Uruchom aplikację za pomocą Streamlit:

   ```bash
   streamlit run app_pdf.py
   ```
2. Otwórz przeglądarkę internetową i przejdź pod adres: `http://localhost:8501`
3. Prześlij plik PDF za pomocą interfejsu użytkownika.
4. Wybierz operację, którą chcesz wykonać na pliku PDF:

   * Wyodrębnianie metadanych
   * Wyodrębnianie tekstu
   * Wyodrębnianie linków
   * Wyodrębnianie obrazów
   * Adnotacje PDF
   * Szyfrowanie PDF hasłem
   * ChatPDF

### Przykład użycia ChatPDF:

1. Prześlij plik PDF
2. Wybierz opcję "Chat_PDF 💬"
3. Wprowadź klucz API OpenAI
4. Zadaj pytanie dotyczące zawartości pliku PDF
5. Otrzymaj odpowiedź wygenerowaną na podstawie zawartości pliku

## 🛠️ Technologie

* **Python** - Główny język programowania
* **Streamlit** - Framework do tworzenia aplikacji webowych
* **PyPDF2** - Biblioteka do manipulacji plikami PDF
* **LangChain** - Framework do tworzenia aplikacji wykorzystujących LLM
* **OpenAI API** - Wykorzystywane do funkcji ChatPDF
* **FAISS** - Biblioteka do efektywnego wyszukiwania podobieństw
* **Tiktoken** - Tokenizer używany przez modele OpenAI

## 🤝 Współpraca

Zachęcamy do współpracy przy rozwoju projektu All_About_PDF! Oto jak możesz pomóc:

1. Forkuj repozytorium
2. Utwórz nową gałąź (`git checkout -b feature/amazing-feature`)
3. Zatwierdź swoje zmiany (`git commit -m 'Dodano nową funkcję'`)
4. Wypchnij do gałęzi (`git push origin feature/amazing-feature`)
5. Otwórz Pull Request

### Propozycje rozwoju

* Dodanie funkcji konwersji PDF do innych formatów (DOCX, JPEG, PNG)
* Implementacja funkcji łączenia wielu plików PDF
* Dodanie możliwości edycji tekstu w plikach PDF
* Rozszerzenie funkcji ChatPDF o obsługę większych dokumentów
* Dodanie wsparcia dla innych języków

## 📄 Licencja

Ten projekt jest udostępniany na licencji MIT. Szczegółowe informacje można znaleźć w pliku [LICENSE](vscode-webview://1qd8v1tula0u43gou3ukfl0snpfh7dthaabr622qdvjsb150mmrk/LICENSE).

![Licencja MIT](https://img.shields.io/badge/Licencja-MIT-blue.svg)

## 📞 Kontakt





---
