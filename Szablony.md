# Szablon dla rozszerzeń narzędzi Pythona VS Code

To jest repozytorium szablonów, które pomoże Ci rozpocząć tworzenie rozszerzenia VS Code dla Twojego ulubionego narzędzia Pythona. Może to być linter, formatter, analiza kodu lub wszystkie razem. Ten szablon zapewni Ci podstawowe elementy potrzebne do zbudowania dla niego rozszerzenia VS Code.

## Języki programowania i frameworki

Szablon rozszerzenia składa się z dwóch części, części rozszerzenia i części serwera języka. Część rozszerzenia jest napisana w TypeScript, a część serwera językowego jest napisana w Pythonie w bibliotece [pygls][pygls] (serwer języka Python).

Podczas korzystania z tego szablonu będziesz w większości pracował nad częścią kodu Pythona. Będziesz integrować swoje narzędzie z częścią rozszerzającą przy użyciu [Language Server Protocol](https://microsoft.github.io/language-server-protocol). [pygls][pygls] obecnie pracuje na [wersji 3.16 LSP](https://microsoft.github.io/language-server-protocol/specifications/specification-3-16/).

Część TypeScript obsługuje pracę z kodem VS i jego interfejsem użytkownika. Szablon rozszerzenia zawiera kilka wstępnie skonfigurowanych ustawień, z których może korzystać Twoje narzędzie. Jeśli chcesz dodać nowe ustawienia do obsługi swojego narzędzia, będziesz musiał trochę popracować nad TypeScriptem. Rozszerzenie zawiera przykłady kilku ustawień, które możesz śledzić. Możesz także spojrzeć na rozszerzenia opracowane przez nasz zespół dla niektórych popularnych narzędzi jako odniesienie.

## Wymagania

1. VS Code 1.64.0 lub nowszy
2. Python 3.7 lub nowszy
3. węzeł >= 14.19.0
4. npm >= 8.3.0 (`npm` jest instalowany z węzłem, sprawdź wersję npm, użyj `npm install -g npm@8.3.0` do aktualizacji)
5. Rozszerzenie Pythona dla VS Code

Powinieneś wiedzieć, jak tworzyć i pracować z wirtualnymi środowiskami Pythona.

## Pierwsze kroki

1. Użyj tego [szablonu, aby utworzyć repozytorium](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).
2. Sprawdź swoje repozytorium lokalnie na swojej maszynie programistycznej.
3. Utwórz i aktywuj wirtualne środowisko Pythona dla tego projektu w terminalu. Upewnij się, że używasz minimalnej wersji Pythona dla swojego narzędzia. Ten szablon został napisany do pracy z Pythonem 3.7 lub nowszym.
4. Zainstaluj `nox` w aktywowanym środowisku: `python -m pip install nox`.
5. Dodaj swoje ulubione narzędzie do `requirements.in`
6. Uruchom `nox --session setup`.
7. **Opcjonalnie** Zainstaluj zależności testowe `python -m pip install -r src/test/python_tests/requirements.txt`. Będziesz musiał je zainstalować, aby uruchomić testy z Eksploratora testów.
8. Otwórz `package.json`, poszukaj i zaktualizuj następujące rzeczy:
   1. Znajdź i zastąp `<pytool-module>` nazwą modułu swojego narzędzia. Będzie to używane wewnętrznie do tworzenia przestrzeni nazw ustawień, rejestrowania poleceń itp. Zaleca się używanie nazwy pisanej małymi literami, bez spacji, `-` jest ok. Na przykład zastąpienie `<pytool-module>` przez `pylint` spowoduje, że ustawienia będą wyglądały jak `pylint.args`. Inny przykład, zastąpienie `<pytool-module>` przez `black-formatter` sprawi, że ustawienia będą wyglądały jak `black-formatter.args`.
   2. Znajdź i zastąp `<pytool-display-name>` wyświetlaną nazwą swojego narzędzia. Jest to używane jako tytuł rozszerzenia na rynku, w widoku rozszerzeń, dziennikach wyjściowych itp. Na przykład dla rozszerzenia „czarnego” jest to „Czarny formater”.
9. Zainstaluj pakiety węzłów za pomocą `npm install`.

## Funkcje tego szablonu

Po zakończeniu części wprowadzającej ten szablon dodałby następujące elementy. Załóżmy, że `<pytool-module>` został zastąpiony przez `mytool`, a `<pytool-display-name>` przez `My Tool`:

1. Polecenie „Moje narzędzie: Uruchom ponownie serwer” (identyfikator polecenia: „mytool.restart”).
2. Następujące ustawienie:
   - `mytool.args`
   - `moja ścieżka.narzędzia`
   - `mytool.importStrategy`
   - `mytool.interpreter`
   - `mytool.showNotification`
3. Następujące wyzwalacze aktywacji rozszerzenia:
   - W języku `python`.
   - W pliku z rozszerzeniem `.py` znalezionym w otwartym obszarze roboczym.
4. Rejestrowane są następujące komendy:
   - `mytool.restart`: Ponownie uruchamia serwer językowy.
5. Kanał wyjściowy do logowania `Wyjście` > `Moje narzędzie`

## Dodawanie funkcji z Twojego narzędzia

Otwórz `bundled/tool/lsp_server.py`, tutaj dokonasz większości zmian. Poszukaj tam komentarzy `TODO`, aby uzyskać więcej informacji.

Szukaj też `TODO` w innych miejscach w całym szablonie:

- `bundled/tool/lsp_runner.py`: W niektórych szczególnych przypadkach może być konieczna aktualizacja.
- `src/test/python_tests/test_server.py` : Tutaj będziesz pisać testy. Na początek podano dwa niekompletne przykłady.
- Wszystkie pliki przeceny w tym szablonie mają pewne elementy „DO ZROBIENIA”, pamiętaj, aby je również sprawdzić. Obejmuje to aktualizację pliku LICENCJA, nawet jeśli chcesz zachować licencję MIT.

Odniesienia do innego rozszerzenia stworzonego przez nasz zespół przy użyciu szablonu:

- Odniesienie do protokołu: [https://microsoft.github.io/language-server-protocol/specifications/specification-3-16/](https://microsoft.github.io/language-server-protocol/specifications/specification -3-16/)
- Implementacja pokazująca, jak obsługiwać Linting na pliku `open`, `save` i `close`. [Pylint](https://github.com/microsoft/vscode-pylint/tree/main/bundled/tool)
- Implementacja pokazująca sposób obsługi formatowania. [Czarny formater](https://github.com/microsoft/vscode-black-formatter/tree/main/bundled/tool)
- Implementacja pokazująca, jak obsługiwać Code Actions. [isort](https://github.com/microsoft/vscode-isort/blob/main/bundled/tool)

## Budowanie i uruchamianie rozszerzenia

Uruchom konfigurację `Debug Extension and Python` z VS Code. To powinno zbudować i debugować rozszerzenie w oknie hosta.

Uwaga: jeśli chcesz tylko zbudować, możesz uruchomić zadanie kompilacji w kodzie VS (`ctrl`+`shift`+`B`)

## Debugowanie

Aby debugować zarówno kod TypeScript, jak i Python, użyj konfiguracji debugowania `Debug Extension and Python`. To jest zalecany sposób. Ponadto, zatrzymując się, pamiętaj o zatrzymaniu zarówno sesji debugowania TypeScript, jak i Pythona. W przeciwnym razie może nie połączyć się ponownie z sesją Pythona.

Aby debugować tylko kod TypeScript, użyj konfiguracji debugowania „Rozszerzenie debugowania”.

Aby debugować już działający serwer lub serwer produkcyjny, użyj `Python Attach` i wybierz proces, który uruchamia `lsp_server.py`.

## Rejestrowanie i dzienniki

Szablon tworzy kanał wyjściowy logowania, który można znaleźć w panelu `Wyjście` > `mytool`. Możesz kontrolować poziom dziennika, uruchamiając polecenie `Programista: Ustaw poziom dziennika...` z palety poleceń i wybierając rozszerzenie z listy. Powinien być wymieniony przy użyciu wyświetlanej nazwy narzędzia. Możesz także ustawić globalny poziom dziennika, który będzie miał zastosowanie do wszystkich rozszerzeń i edytora.

Jeśli potrzebujesz logów zawierających komunikaty pomiędzy Klientem Językowym a Serwerem Językowym, możesz ustawić `"mytool.server.trace": "verbose"`, aby uzyskać dzienniki komunikatów. Te dzienniki są również dostępne w panelu `Wyjście` > `mytool`.

## Dodawanie nowych ustawień lub poleceń

Możesz dodać nowe ustawienia, dodając szczegóły ustawień w pliku `package.json`. Aby przekazać tę konfigurację do serwera narzędzi Pythona (np. `lsp_server.py`), zaktualizuj plik `settings.ts` zgodnie z potrzebami. W tym pliku znajdują się przykłady różnych typów ustawień, na których można oprzeć nowe ustawienia.

Możesz śledzić, jak polecenie `restart` jest zaimplementowane w `package.json` i `extension.ts`, aby dowiedzieć się, jak dodawać polecenia. Możesz także przekazywać polecenia z Pythona za pośrednictwem protokołu serwera językowego.

## Testowanie

Zobacz `src\test\python_tests\test_server.py` dla punktu wyjścia. Zobacz inne projekty, o których mowa tutaj, do testowania różnych aspektów uruchamiania narzędzia przez LSP.

Jeśli zainstalowałeś wymagania testowe, powinieneś być w stanie zobaczyć testy w Eksploratorze testów.

Możesz także uruchomić wszystkie testy za pomocą polecenia `nox --session testing`.

## Strzępienie

Uruchom `nox --session lint`, aby uruchomić linting na kodzie Pythona i TypeScript. Zaktualizuj plik nox, jeśli chcesz użyć innego lintera i formatera.

## Pakowanie i publikowanie

1. Zaktualizuj różne pola w `package.json`. Przynajmniej sprawdź następujące pola i odpowiednio je zaktualizuj. Zobacz [odniesienie do manifestu rozszerzenia](https://code.visualstudio.com/api/references/extension-manifest), aby dodać więcej pól:
   - `"publisher"`: zaktualizuj to do swojego identyfikatora wydawcy z [https://marketplace.visualstudio.com/](https://marketplace.visualstudio.com/).
   - `"wersja"`: Zobacz [https://semver.org/](https://semver.org/) w celu uzyskania szczegółowych informacji o wymaganiach i ograniczeniach dotyczących tego pola.
   - `"licencja"`: Zaktualizuj licencję zgodnie z projektem. Domyślnie `MIT`.
   - `"słowa kluczowe"`: Zaktualizuj słowa kluczowe dla swojego projektu, będą one używane podczas wyszukiwania na rynku VS Code.
   - `"kategorie"`: Zaktualizuj kategorie dla swojego projektu, ułatwia filtrowanie na rynku VS Code.
   - `"homepage"`, `"repository"` i `"bugs"` : zaktualizuj adresy URL tych pól, aby wskazywały na Twój projekt.
   - **Opcjonalne** Dodaj pole „ikona” ze względną ścieżką do pliku obrazu, który będzie używany jako ikona w tym projekcie.
2. Sprawdź następujące pliki przeceny:
   - **WYMAGANE** Tylko za pierwszym razem: `CODE_OF_CONDUCT.md`, `LICENSE`, `SUPPORT.md`, `SECURITY.md`
   - Każde wydanie: `CHANGELOG.md`
3. Zbuduj pakiet używając `nox --session build_package`.
4. Weź wygenerowany plik `.vsix` i prześlij go na stronę zarządzania rozszerzeniami [https://marketplace.visualstudio.com/manage](https://marketplace.visualstudio.com/manage).

Aby to zrobić z wiersza poleceń, zobacz tutaj [https://code.visualstudio.com/api/working-with-extensions/publishing-extension](https://code.visualstudio.com/api/working-with-extensions /publikowanie-rozszerzenie)

## Aktualizowanie zależności

Dostarczono Dependabot yml, aby ułatwić konfigurację zależności aktualizacji w tym rozszerzeniu. Pamiętaj, aby dodać etykiety używane w Dependabocie do swojego repozytorium.

Aby ręcznie zaktualizować projekt lokalny:

1. Utwórz nowy oddział
2. Uruchom `npm update`, aby zaktualizować moduły węzła.
3. Uruchom `nox --session setup`, aby zaktualizować pakiety Pythona.

## Rozwiązywanie problemów

### Zmiana ścieżki lub nazwy pliku `lsp_server.py` na coś innego

Jeśli chcesz zmienić nazwę `lsp_server.py` na inną, możesz to zrobić. Pamiętaj o zaktualizowaniu plików `constants.ts` i `src\test\python_tests\lsp_test_client\session.py`.

Upewnij się również, że wstawione ścieżki w `lsp_server.py` wskazują odpowiednie foldery, aby pobrać zależne pakiety.

### Nie znaleziono modułu błędy

Może się to zdarzyć, jeśli `bundled/libs` jest puste. To jest folder, w którym umieścimy twoje narzędzie i inne zależności. Pamiętaj, aby wykonać kroki kompilacji potrzebne do tworzenia i łączenia wymaganych bibliotek.

Często spotykanym jest moduł [pygls][pygls], którego nie znaleziono.

---

# DO ZROBIENIA: Opiekun tego repozytorium nie edytował jeszcze tego pliku

**Właściciel repozytorium** Upewnij się, że to zaktualizujesz. Jako właściciel repozytorium będziesz musiał zaktualizować ten plik o szczegółowe instrukcje dla swojego rozszerzenia.

[[pygls]: https://github.com/openlawlibrary/pygls](https://github.com/openlawlibrary/pygls)

---
