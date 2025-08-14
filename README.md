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

<div style="display: flex; align-items: center; gap: 15px;">
  <img src="logo.png" alt="Icon" width="70">
  <div style="display: flex; align-items: center; gap: 10px;">
    <span>netdark_1966</span>
    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
      <path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>
    </svg>
    <a href="mailto:netdark_1966@op.pl">netdark_1966</a>
    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
      <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
    </svg>
    <a href="https://github.com/Darek1966">GitHub — Darek1966</a>
  </div>
</div>

---
