# Sprawdzanie i uzupełnianie kodu

## IntelliCode 👍

### [Dostosuj zachowanie IntelliSense](https://code.visualstudio.com/docs/python/editing#_customize-intellisense-behavior)

Domyślne włączenie pełnego zestawu funkcji IntelliSense może spowodować, że środowisko programistyczne będzie wolniejsze, dlatego rozszerzenie języka Python udostępnia minimalny zestaw funkcji, które umożliwiają produktywność przy jednoczesnym zapewnieniu wydajności. Można jednak dostosować zachowanie silnika analitycznego do własnych upodobań za pomocą wielu ustawień.

### [Włącz funkcję IntelliSense dla niestandardowych lokalizacji pakietów](https://code.visualstudio.com/docs/python/editing#_enable-intellisense-for-custom-package-locations)

Aby włączyć funkcję IntelliSense dla pakietów zainstalowanych w niestandardowych lokalizacjach, dodaj te lokalizacje do kolekcji `python.analysis.extraPaths` w `settings.json` pliku (domyślna kolekcja jest pusta). Na przykład możesz mieć zainstalowany Google App Engine w niestandardowych lokalizacjach, określonych w `app.yaml` rzypadku korzystania z Flask. W takim przypadku należy określić te lokalizacje w następujący sposób:

**Windows:**

```
"python.analysis.extraPaths": [
"C:/Program Files (x86)/Google/google_appengine",
"C:/Program Files (x86)/Google/google_appengine/lib/flask-0.12"]
```

Pełną listę dostępnych formantów IntelliSense można znaleźć w [ustawieniach analizy kodu](https://code.visualstudio.com/docs/python/settings-reference#_code-analysis-settings) rozszerzenia języka Python i [ustawieniach autouzupełniania](https://code.visualstudio.com/docs/python/settings-reference#_autocomplete-settings) .

Możesz również dostosować ogólne zachowanie autouzupełniania i funkcji IntelliSense, a nawet całkowicie wyłączyć te funkcje. Więcej informacji można znaleźć w [temacie Dostosowywanie technologii IntelliSense](https://code.visualstudio.com/docs/editor/intellisense#_customizing-intellisense) .

---

# Emoji

[https://emojipedia.org/](https://emojipedia.org/)

## :emojisense: 💯💬

skrót: Ctrl + i

---

# Automatyczne importy

## Pylance  ✏️

### [Włącz automatyczne importy](https://code.visualstudio.com/docs/python/editing#_enable-auto-imports)

[Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) oferuje sugestie dotyczące automatycznego importu modułów w Twoim obszarze roboczym i/lub pakietów, które zainstalowałeś w swoim środowisku. Umożliwia to automatyczne dodawanie instrukcji importu podczas pisania. Automatyczne importowanie jest domyślnie wyłączone, ale możesz je włączyć, ustawiając `python.analysis.autoImportCompletions` opcję `true` w ustawieniach.

Domyślnie sugerowane jest automatyczne importowanie tylko symboli/pakietów najwyższego poziomu. Na przykład możesz zobaczyć `import matplotlib` jako sugestię, ale nie `import matplotlib.pyplot` domyślnie. Możesz jednak dostosować to zachowanie za pomocą `python.analysis.packageIndexDepths` ustawienia (zapoznaj się z [dokumentacją ustawień IntelliSense](https://code.visualstudio.com/docs/python/settings-reference#_pylance-language-server) , aby dowiedzieć się więcej). Symbole zdefiniowane przez użytkownika (te, które nie pochodzą z zainstalowanych pakietów lub bibliotek) są automatycznie importowane tylko wtedy, gdy zostały już użyte w plikach otwieranych w edytorze. W przeciwnym razie będą one dostępne tylko za pośrednictwem funkcji [Add Imports Quick Fix](https://code.visualstudio.com/docs/python/editing#_quick-fixes) .

[Rozwiązywanie problemów z technologią IntelliSense](https://code.visualstudio.com/docs/python/editing#_troubleshooting-intellisense)

---

# Formatowanie i błędy zapisu

Linting podkreśla problemy składniowe i stylistyczne w kodzie źródłowym Pythona, co często pomaga zidentyfikować i poprawić subtelne błędy programistyczne lub niekonwencjonalne praktyki kodowania, które mogą prowadzić do błędów.

## Flake8 (płatek8)

Firma Microsoft publikuje następujące rozszerzenia linting:

| Lintera  | Rozszerzenie                                                                                                                                                    |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pilint   | [https://marketplace.visualstudio.com/items?itemName=ms-python.pylint](https://marketplace.visualstudio.com/items?itemName=ms-python.pylint)                       |
| płatek8 | [https://marketplace.visualstudio.com/items?itemName=ms-python.flake8](https://marketplace.visualstudio.com/items?itemName=ms-python.flake8)                       |
| mypy     | [https://marketplace.visualstudio.com/items?itemName=ms-python.mypy-type-checker](https://marketplace.visualstudio.com/items?itemName=ms-python.mypy-type-checker) |

Rozszerzenia Linting oferowane przez społeczność:

| Lintera  | Rozszerzenie                                                                                                                                  |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Batalion | [https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff) |
| mypy     | [https://marketplace.visualstudio.com/items?itemName=matangover.mypy](https://marketplace.visualstudio.com/items?itemName=matangover.mypy)       |

---
