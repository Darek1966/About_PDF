---
description: Repository Information Overview
alwaysApply: true
---

# All_About_PDF - Informacje o Projekcie

## Podsumowanie

All_About_PDF to internetowa aplikacja do pracy z plikami PDF, zbudowana przy użyciu Pythona i frameworka Streamlit. Aplikacja umożliwia wykonywanie różnych operacji na plikach PDF, takich jak wyodrębnianie tekstu, obrazów, metadanych, szyfrowanie plików hasłem oraz funkcję ChatPDF wykorzystującą technologie OpenAI i LangChain do interakcji z plikami PDF za pomocą przetwarzania języka naturalnego.

## Struktura

- **app_pdf.py**: Główny plik aplikacji zawierający logikę biznesową
- **requirements.txt**: Lista zależności projektu
- **index.html**: Strona HTML do uruchamiania aplikacji w oknie przeglądarki
- **Pliki .md**: Dokumentacja projektu (README.md, Streamlit.md, Szablony.md, Środowisko.md, Rozszerzenie.md)
- **.venv**: Wirtualne środowisko Pythona
- **.vscode**: Konfiguracja VSCode do uruchamiania aplikacji Streamlit

## Język i Środowisko Uruchomieniowe

**Język**: Python
**Wersja**: 3.11.4
**System Budowania**: Brak dedykowanego systemu budowania
**Menedżer Pakietów**: pip

## Zależności

**Główne Zależności**:

- streamlit: Framework do tworzenia aplikacji webowych w Pythonie
- PyPDF2: Biblioteka do manipulacji plikami PDF
- langchain: Framework do tworzenia aplikacji wykorzystujących LLM
- openai: Klient API OpenAI
- faiss-cpu: Biblioteka do efektywnego wyszukiwania podobieństw
- tiktoken: Tokenizer używany przez modele OpenAI

## Instalacja i Uruchomienie

```bash
# Instalacja zależności
pip install -r requirements.txt

# Uruchomienie aplikacji
streamlit run app_pdf.py
```

## Główne Funkcje Aplikacji

- **Wyodrębnianie tekstu**: Ekstrakcja tekstu z plików PDF
- **Wyodrębnianie obrazów**: Ekstrakcja obrazów z plików PDF
- **Wyodrębnianie metadanych**: Ekstrakcja metadanych z plików PDF
- **Szyfrowanie PDF**: Zabezpieczanie plików PDF hasłem
- **ChatPDF**: Interaktywna rozmowa z plikiem PDF przy użyciu OpenAI i LangChain

## Punkty Wejściowe

- **app_pdf.py**: Główny plik aplikacji zawierający funkcję `main()` jako punkt wejściowy
- **ChatPDF()**: Funkcja obsługująca interaktywną rozmowę z plikiem PDF
- **main()**: Funkcja inicjalizująca interfejs użytkownika Streamlit

## Konfiguracja VSCode

Projekt zawiera konfigurację VSCode do uruchamiania aplikacji Streamlit bezpośrednio z edytora:

- **launch.json**: Konfiguracja uruchamiania modułu streamlit z argumentami `run ${file}`
