# Środowisko

## Stwórz nowe środowisko dzięki Streamlit

1. Przejdź do folderu swojego projektu:

```bash
cd myproject
```

2. Utwórz nowe środowisko wirtualne w tym folderze i aktywuj to środowisko:

```bash
python -m venv .venv
```

3. Po uruchomieniu powyższego polecenia katalog o nazwie `.venv` pojawi się w `myproject/`.                                                              W tym katalogu jest instalowane środowisko wirtualne i jego zależności.
4. Zainstaluj Streamlit w swoim środowisku:

```bash
pip install streamlit
```

5. Sprawdź, czy instalacja działała:

```bash
streamlit hello
```

Aplikacja Hello firmy Streamlit powinna pojawić się w nowej karcie w Twojej przeglądarce internetowej!

---

## Użyj swojego nowego środowiska

1. Za każdym razem, gdy chcesz użyć nowego środowiska, musisz najpierw przejść do folderu projektu                              (gdzie `.venv` znajduje się katalog) i uruchomić:

```bash
source .venv/bin/activate
```

2. Teraz możesz normalnie używać Pythona i Streamlit:

```bash
streamlit run myfile.py
```

3. Aby zatrzymać serwer Streamlit, naciśnij `ctrl-C`
4. Kiedy skończysz korzystać z tego środowiska, wpisz, `deactivate` aby powrócić do normalnej powłoki.
   ```
   (.venv) PS E:\Py_GitHub\Streamlit_test> deactivate
   ```

Teraz, po zainstalowaniu Streamlit, poświęć kilka minut na przeczytanie [głównych pojęć](https://docs.streamlit.io/library/get-started/main-concepts) , aby zrozumieć model przepływu danych Streamlit.

---

# Praca z Streamlitem

[https://docs.streamlit.io/library/get-started/main-concepts](https://docs.streamlit.io/library/get-started/main-concepts)

Najpierw wsypujesz kilka poleceń Streamlit do normalnego skryptu Pythona, a następnie uruchamiasz go za pomocą `streamlit run`

```
streamlit run your_script.py [-- script args]
```

Gdy tylko uruchomisz skrypt, jak pokazano powyżej, uruchomi się lokalny serwer Streamlit, a Twoja aplikacja otworzy się w nowej karcie w domyślnej przeglądarce internetowej. Ta aplikacja to Twoje płótno, na którym możesz rysować wykresy, tekst, widżety, tabele i nie tylko.

To, co zostanie narysowane w aplikacji, zależy od Ciebie. Na przykład [`st.text`](https://docs.streamlit.io/library/api-reference/text/st.text) zapisuje nieprzetworzony tekst do Twojej aplikacji i [`st.line_chart`](https://docs.streamlit.io/library/api-reference/charts/st.line_chart) rysuje — jak zgadłeś — wykres liniowy. Zapoznaj się z naszą [dokumentacją interfejsu API](https://docs.streamlit.io/library/api-reference) , aby zobaczyć wszystkie dostępne polecenia.

#### Uwaga

Podczas przekazywania skryptowi niektórych niestandardowych argumentów należy je przekazać po dwóch myślnikach. W przeciwnym razie argumenty zostaną zinterpretowane jako argumenty samego Streamlit.

Innym sposobem uruchomienia Streamlit jest uruchomienie go jako modułu Pythona. Może to być przydatne podczas konfigurowania IDE, takiego jak PyCharm, do pracy ze Streamlitem:

```
# Działanie
python -m streamlit run your_script.py
# jest równa:
streamlit run your_script.py
```

#### Wskazówka

Możesz także przekazać adres URL do `streamlit run` ! Jest to świetne w połączeniu z GitHub Gists. 

Na przykład:

```
streamlit run https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/streamlit_app.py
```

Za każdym razem, gdy chcesz zaktualizować aplikację, zapisz plik źródłowy. Kiedy to zrobisz, Streamlit wykryje, czy nastąpiła zmiana i zapyta, czy chcesz ponownie uruchomić aplikację. Wybierz „Zawsze uruchamiaj ponownie” w prawym górnym rogu ekranu, aby automatycznie aktualizować aplikację za każdym razem, gdy zmienisz jej kod źródłowy.

Pozwala to na pracę w szybkiej interaktywnej pętli: wpisujesz kod, zapisujesz go, wypróbowujesz na żywo, następnie wpisujesz trochę więcej kodu, zapisujesz go, wypróbujesz i tak dalej, aż będziesz zadowolony z wyników. Ta ciasna pętla między kodowaniem a przeglądaniem wyników na żywo jest jednym ze sposobów, w jaki Streamlit ułatwia życie.

#### Wskazówka

Podczas opracowywania aplikacji Streamlit zaleca się rozmieszczenie okien edytora i przeglądarki obok siebie, aby kod i aplikacja były widoczne w tym samym czasie. Spróbuj!

---

# Wyświetlaj i stylizuj dane

### Użyj magii

Możesz także pisać do swojej aplikacji bez wywoływania metod Streamlit. Streamlit obsługuje „ [magiczne polecenia](https://docs.streamlit.io/library/api-reference/write-magic/magic) ”, co oznacza, że nie musisz ich [`st.write()`](https://docs.streamlit.io/library/api-reference/write-magic/st.write) w ogóle używać! Aby zobaczyć to w akcji, wypróbuj ten fragment:

```
# Tabela
import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
});
df
```

### Napisz ramkę danych

Wraz z [magicznymi komendami](https://docs.streamlit.io/library/api-reference/write-magic/magic) jest [`st.write()`](https://docs.streamlit.io/library/api-reference/write-magic/st.write) „szwajcarski scyzoryk” firmy Streamlit. Możesz przekazać prawie wszystko do [`st.write()`](https://docs.streamlit.io/library/api-reference/write-magic/st.write) : tekstu, danych, wykresów Matplotlib, wykresów Altair i innych. Nie martw się, Streamlit to rozgryzie i wyrenderuje wszystko we właściwy sposób.

```
import streamlit as st
import pandas as pd
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
```

Istnieją inne funkcje specyficzne dla danych, takie jak [`st.dataframe()`](https://docs.streamlit.io/library/api-reference/data/st.dataframe) i [`st.table()`](https://docs.streamlit.io/library/api-reference/data/st.table) których można również używać do wyświetlania danych. Dowiedzmy się, kiedy używać tych funkcji oraz jak dodawać kolory i style do ramek danych.

Być może zadajesz sobie pytanie: „dlaczego nie zawsze miałbym używać `st.write()` ?” Jest kilka powodów:

1. *Magia* i [`st.write()`](https://docs.streamlit.io/library/api-reference/write-magic/st.write) sprawdź typ przekazanych danych, a następnie zdecyduj, jak najlepiej renderować je w aplikacji. Czasami chcesz narysować to w inny sposób. Na przykład zamiast rysować ramkę danych jako interaktywną tabelę, możesz narysować ją jako tabelę statyczną za pomocą `st.table(df)`.
2. Drugim powodem jest to, że inne metody zwracają obiekt, którego można używać i modyfikować, dodając do niego dane lub je zastępując.
3. Wreszcie, jeśli używasz bardziej szczegółowej metody Streamlit, możesz przekazać dodatkowe argumenty, aby dostosować jej zachowanie.

Na przykład utwórzmy ramkę danych i zmieńmy jej formatowanie za pomocą `Styler` obiektu Pandas. W tym przykładzie użyjesz Numpy do wygenerowania losowej próbki i [`st.dataframe()`](https://docs.streamlit.io/library/api-reference/data/st.dataframe) metody do narysowania interaktywnej tabeli.

#### Notatka

W tym przykładzie użyto Numpy do wygenerowania losowej próbki, ale można użyć Pandas DataFrames, tablic Numpy lub zwykłych tablic Pythona.

```
import streamlit as st
import numpy as np

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)
```

Rozwińmy pierwszy przykład, używając `Styler` obiektu Pandas, aby wyróżnić niektóre elementy w interaktywnej tabeli.

```
import streamlit as st
import numpy as np
import pandas as pd

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))
```

Streamlit ma również metodę generowania statycznej tabeli: [`st.table()`](https://docs.streamlit.io/library/api-reference/data/st.table)

```

import streamlit as st
import numpy as np
import pandas as pd

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.table(dataframe)
```

### Rysuj wykresy i mapy

Streamlit obsługuje kilka popularnych bibliotek wykresów danych, takich jak [Matplotlib, Altair, deck.gl i inne](https://docs.streamlit.io/library/api-reference#chart-elements) . 

W tej sekcji dodasz do swojej aplikacji wykres słupkowy, wykres liniowy i mapę.

#### Narysuj wykres liniowy

Możesz łatwo dodać wykres liniowy do swojej aplikacji za pomocą [`st.line_chart()`](https://docs.streamlit.io/library/api-reference/charts/st.line_chart). Wygenerujemy losową próbkę za pomocą Numpy, a następnie przedstawimy ją na wykresie.

```
import streamlit as st
import numpy as np
import pandas as pd

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
```

#### Narysuj mapę

Za [`st.map()`](https://docs.streamlit.io/library/api-reference/charts/st.map) pomocą można wyświetlać punkty danych na mapie. Użyjmy Numpy do wygenerowania przykładowych danych i naniesienia ich na mapę San Francisco.

```
import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
```

---

# Widżety

Gdy doprowadzisz dane lub model do stanu, który chcesz eksplorować, możesz dodać widżety, takie jak [`st.slider()`](https://docs.streamlit.io/library/api-reference/widgets/st.slider), [`st.button()`](https://docs.streamlit.io/library/api-reference/widgets/st.button) lub [`st.selectbox()`](https://docs.streamlit.io/library/api-reference/widgets/st.selectbox). To naprawdę proste — traktuj widżety jak zmienne:

```
import streamlit as st
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)
```

Przy pierwszym uruchomieniu powyższa aplikacja powinna wyświetlić tekst „0 do kwadratu to 0”. Następnie za każdym razem, gdy użytkownik wchodzi w interakcję z widżetem, Streamlit po prostu ponownie uruchamia skrypt od góry do dołu, przypisując bieżący stan widżetu do zmiennej w procesie.

Na przykład, jeśli użytkownik przesunie suwak do pozycji `10`, Streamlit ponownie uruchomi powyższy kod i odpowiednio `x`go ustawi. `10` Teraz powinieneś zobaczyć tekst „10 do kwadratu to 100”.

Dostęp do widżetów można również uzyskać za pomocą klucza, jeśli zdecydujesz się określić ciąg, który będzie używany jako unikalny klucz dla widżetu:

```
import streamlit as st
st.text_input("Your name", key="name")

# You can access the value at any point with:

st.session_state.name
```

Każdy widżet z kluczem jest automatycznie dodawany do stanu sesji. Aby uzyskać więcej informacji o stanie sesji, jego powiązaniu ze stanem widżetu i jego ograniczeniach, zobacz [Przewodnik po interfejsie API stanu sesji](https://docs.streamlit.io/library/api-reference/session-state) .

---

# Użyj pól wyboru, aby pokazać/ukryć dane

Jednym z przypadków użycia pól wyboru jest ukrycie lub pokazanie określonego wykresu lub sekcji w aplikacji. [`st.checkbox()`](https://docs.streamlit.io/library/api-reference/widgets/st.checkbox) przyjmuje jeden argument, którym jest etykieta widżetu. W tym przykładzie pole wyboru służy do przełączania instrukcji warunkowych.

```
import streamlit as st
import numpy as np
import pandas as pd

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])  

chart_data
```

---

# Użyj pola wyboru dla opcji

Użyj [`st.selectbox`](https://docs.streamlit.io/library/api-reference/widgets/st.selectbox) , aby wybrać z serii. Możesz wpisać żądane opcje lub przejść przez tablicę lub kolumnę ramki danych.

Użyjmy `df` utworzonej wcześniej ramki danych.

```

import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })
option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option
```

---

# Układ

Streamlit ułatwia organizowanie widżetów na pasku bocznym lewego panelu za pomocą [`st.sidebar`](https://docs.streamlit.io/library/api-reference/layout/st.sidebar). Każdy przekazywany element [`st.sidebar`](https://docs.streamlit.io/library/api-reference/layout/st.sidebar) jest przypinany z lewej strony, dzięki czemu użytkownicy mogą skupić się na zawartości aplikacji, mając jednocześnie dostęp do elementów sterujących interfejsu użytkownika.

Na przykład, jeśli chcesz dodać pole wyboru i suwak do paska bocznego, użyj `st.sidebar.slider` i `st.sidebar.selectbox`zamiast `st.slider` i `st.selectbox` :

```
import streamlit as st
# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)
Add a slider to the sidebar:add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)
```

Oprócz paska bocznego Streamlit oferuje kilka innych sposobów kontrolowania układu aplikacji. [`st.columns`](https://docs.streamlit.io/library/api-reference/layout/st.columns) pozwala umieszczać widżety obok siebie i [`st.expander`](https://docs.streamlit.io/library/api-reference/layout/st.expander) pozwala oszczędzać miejsce, ukrywając dużą zawartość.

```
import streamlit as st

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")
```

#### Notatka

`st.echo` i `st.spinner` nie są obecnie obsługiwane na pasku bocznym ani w opcjach układu. Zapewniamy jednak, że obecnie pracujemy nad dodaniem obsługi również dla nich!

---

# Pokaż postęp

Podczas dodawania długotrwałych obliczeń do aplikacji można użyć [`st.progress()`](https://docs.streamlit.io/library/api-reference/status/st.progress) do wyświetlania stanu w czasie rzeczywistym.

Najpierw zaimportujmy czas. Zamierzamy użyć tej `time.sleep()` metody do symulacji długotrwałych obliczeń:

```
import time
```

Teraz utwórzmy pasek postępu:

```
import streamlit as st
import time'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
# Update the progress bar with each iteration.  
latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'
```

---

# Motywy

Streamlit obsługuje jasne i ciemne motywy po wyjęciu z pudełka. 

Streamlit najpierw sprawdzi, czy użytkownik przeglądający aplikację ma preferencje trybu jasnego lub ciemnego ustawione przez jego system operacyjny i przeglądarkę. Jeśli tak, to ta preferencja zostanie użyta. W przeciwnym razie domyślnie stosowany jest motyw Jasny.

Możesz także zmienić aktywny motyw z „☰” → „Ustawienia”.

Foto: [https://docs.streamlit.io/images/change_theme.gif](https://docs.streamlit.io/images/change_theme.gif)

Chcesz dodać własny motyw do aplikacji? Menu „Ustawienia” zawiera edytor motywów dostępny po kliknięciu „Edytuj aktywny motyw”. Możesz użyć tego edytora, aby wypróbować różne kolory i zobaczyć aktualizację aplikacji na żywo.

Foto: [https://docs.streamlit.io/images/edit_theme.gif](https://docs.streamlit.io/images/edit_theme.gif)

Gdy jesteś zadowolony ze swojej pracy, motywy można zapisać, [ustawiając opcje konfiguracji](https://docs.streamlit.io/library/advanced-features/configuration#set-configuration-options) w `[theme]` sekcji konfiguracji. Po zdefiniowaniu motywu dla aplikacji pojawi się on w selektorze motywów jako „Motyw niestandardowy” i zostanie zastosowany domyślnie zamiast dołączonych jasnych i ciemnych motywów.

Więcej informacji o opcjach dostępnych podczas definiowania motywu można znaleźć w [dokumentacji opcji motywu](https://docs.streamlit.io/library/advanced-features/theming) .

#### Notatka

Menu edytora motywów jest dostępne tylko w wersji lokalnej. Jeśli wdrożyłeś swoją aplikację za pomocą Streamlit Community Cloud, przycisk „Edytuj aktywny motyw” nie będzie już wyświetlany w menu „Ustawienia”.

#### Wskazówka

Innym sposobem eksperymentowania z różnymi kolorami motywu jest włączenie opcji „Uruchom przy zapisywaniu”, edytowanie pliku config.toml i obserwowanie, jak aplikacja uruchamia się ponownie z zastosowanymi nowymi kolorami motywu.

---

# Buforowanie

Pamięć podręczna Streamlit pozwala Twojej aplikacji zachować wydajność nawet podczas ładowania danych z sieci, manipulowania dużymi zbiorami danych lub wykonywania kosztownych obliczeń.

Podstawową ideą buforowania jest przechowywanie wyników kosztownych wywołań funkcji i zwracanie buforowanego wyniku, gdy te same dane wejściowe wystąpią ponownie, zamiast wywoływania funkcji przy kolejnych uruchomieniach.

Aby buforować funkcję w Streamlit, musisz ozdobić ją jednym z dwóch dekoratorów ( `st.cache_data` i `st.cache_resource` ):

```
@st.cache_data
def long_running_function(param1, param2):
    return …
```

W tym przykładzie dekorowanie `long_running_function` za pomocą `@st.cache_data` mówi Streamlitowi, że za każdym razem, gdy funkcja jest wywoływana, sprawdza dwie rzeczy:

1. Wartości parametrów wejściowych (w tym przypadku `param1` i `param2` ).
2. Kod wewnątrz funkcji.

Jeśli po raz pierwszy Streamlit widzi te wartości parametrów i kod funkcji, uruchamia funkcję i przechowuje zwracaną wartość w pamięci podręcznej. Następnym razem, gdy funkcja zostanie wywołana z tymi samymi parametrami i kodem (np. gdy użytkownik wchodzi w interakcję z aplikacją), Streamlit całkowicie pominie wykonanie funkcji i zamiast tego zwróci wartość z pamięci podręcznej. Podczas opracowywania pamięć podręczna aktualizuje się automatycznie wraz ze zmianami kodu funkcji, zapewniając odzwierciedlenie najnowszych zmian w pamięci podręcznej.

Jak wspomniano, istnieją dwa dekoratory buforujące:

* `st.cache_data` to zalecany sposób buforowania obliczeń, które zwracają dane: ładowanie DataFrame z pliku CSV, przekształcanie tablicy NumPy, wysyłanie zapytań do API lub dowolna inna funkcja, która zwraca możliwy do serializacji obiekt danych (str, int, float, DataFrame, array, list, … ). Tworzy nową kopię danych przy każdym wywołaniu funkcji, zabezpieczając ją przed [mutacjami i warunkami wyścigu](https://docs.streamlit.io/library/advanced-features/caching#mutation-and-concurrency-issues) . Zachowanie `st.cache_data` jest tym, czego chcesz w większości przypadków — więc jeśli nie masz pewności, zacznij od tego  `st.cache_data` i sprawdź, czy to działa!
* `st.cache_resource` to zalecany sposób buforowania zasobów globalnych, takich jak modele ML lub połączenia z bazami danych — obiekty, których nie można serializować, a których nie chcesz ładować wiele razy. Korzystając z niej, możesz udostępniać te zasoby we wszystkich powtórkach i sesjach aplikacji bez kopiowania lub powielania. Zauważ, że wszelkie mutacje wartości zwracanej w pamięci podręcznej bezpośrednio mutują obiekt w pamięci podręcznej (więcej szczegółów poniżej).

---

# Strony

Gdy aplikacje stają się duże, przydatne staje się zorganizowanie ich na wielu stronach. Ułatwia to zarządzanie aplikacją jako deweloperowi i łatwiejszą nawigację jako użytkownikowi. Streamlit zapewnia bezproblemowy sposób tworzenia aplikacji wielostronicowych.

Zaprojektowaliśmy tę funkcję tak, aby tworzenie aplikacji wielostronicowych było tak proste, jak tworzenie aplikacji jednostronicowych! Po prostu dodaj więcej stron do istniejącej aplikacji w następujący sposób:

1. W folderze zawierającym główny skrypt utwórz nowy `pages` folder. Załóżmy, że twój główny skrypt nazywa się `main_page.py`.
2. Dodaj nowe `.py` pliki do `pages` folderu, aby dodać więcej stron do swojej aplikacji.
3. Biegnij `streamlit run main_page.py` jak zwykle.

Otóż to! Skrypt `main_page.py` będzie teraz odpowiadał stronie głównej Twojej aplikacji. Zobaczysz inne skrypty z `pages` folderu w selektorze stron na pasku bocznym.

 Na przykład:

###### main_page.py

```
import streamlit as st
st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")
```

###### pages/page_2.py

```
import streamlit as st
st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")
```

###### pages/page_3.py

```
import streamlit as st
st.markdown("# Page 3 🎉")
st.sidebar.markdown("# Page 3 🎉")
```

Teraz uruchom `streamlit run main_page.py` i zobacz swoją nową, błyszczącą aplikację wielostronicową!

Foto: [https://docs.streamlit.io/images/mpa-main-concepts.gif](https://docs.streamlit.io/images/mpa-main-concepts.gif)

Nasza dokumentacja dotycząca [aplikacji wielostronicowych](https://docs.streamlit.io/library/get-started/multipage-apps) zawiera instrukcje dodawania stron do aplikacji, w tym definiowania stron, tworzenia struktury i uruchamiania aplikacji wielostronicowych oraz nawigowania między stronami. Gdy zrozumiesz podstawy, [utwórz swoją pierwszą aplikację wielostronicową](https://docs.streamlit.io/library/get-started/multipage-apps/create-a-multipage-app) !

---

# Model aplikacji

Teraz, gdy wiesz już trochę więcej o poszczególnych elementach, zamknijmy pętlę i sprawdźmy, jak to działa razem:

1. Usprawnione aplikacje to skrypty Pythona, które działają od góry do dołu
2. Za każdym razem, gdy użytkownik otworzy kartę przeglądarki wskazującą na Twoją aplikację, skrypt jest ponownie wykonywany
3. Podczas wykonywania skryptu Streamlit rysuje swoje dane wyjściowe na żywo w przeglądarce
4. Skrypty używają pamięci podręcznej Streamlit, aby uniknąć ponownego obliczania kosztownych funkcji, dzięki czemu aktualizacje następują bardzo szybko
5. Za każdym razem, gdy użytkownik wchodzi w interakcję z widżetem, skrypt jest ponownie wykonywany, a wartość wyjściowa tego widżetu jest ustawiana na nową wartość podczas tego uruchomienia.
6. Aplikacje Streamlit mogą zawierać wiele stron, które są zdefiniowane w osobnych `.py` plikach w `pages` folderze.

Foto: [https://docs.streamlit.io/images/app_model.png](https://docs.streamlit.io/images/app_model.png)

---

# Ściągawka

[https://docs.streamlit.io/library/cheatsheet](https://docs.streamlit.io/library/cheatsheet)

---

# Utwórz aplikację

[https://docs.streamlit.io/library/get-started/create-an-app](https://docs.streamlit.io/library/get-started/create-an-app)

---

# Aplikacje wielostronicowe

[https://docs.streamlit.io/library/get-started/multipage-apps](https://docs.streamlit.io/library/get-started/multipage-apps)

---

# Utwórz aplikację wielostronicową

[https://docs.streamlit.io/library/get-started/multipage-apps/create-a-multipage-app](https://docs.streamlit.io/library/get-started/multipage-apps/create-a-multipage-app)

# Odniesienie do interfejsu API

[https://docs.streamlit.io/library/api-reference](https://docs.streamlit.io/library/api-reference)

Streamlit ułatwia wizualizację, mutację i udostępnianie danych. Odwołanie do interfejsu API jest uporządkowane według typu działania, takiego jak wyświetlanie danych lub optymalizacja wydajności. Każda sekcja zawiera metody skojarzone z typem działania, w tym przykłady.

Przejrzyj nasz interfejs API poniżej i kliknij, aby dowiedzieć się więcej o dowolnym z naszych dostępnych poleceń! 🎈

---

# Zaawansowane funkcje

Ta sekcja zawiera podstawowe informacje na temat działania różnych części Streamlit.

[https://docs.streamlit.io/library/advanced-features](https://docs.streamlit.io/library/advanced-features)

---

# Komponenty niestandardowe

Komponenty to moduły Python innych firm, które rozszerzają możliwości Streamlit.

### Jak korzystać z komponentu

[https://docs.streamlit.io/library/components](https://docs.streamlit.io/library/components)

---

# Dokumentacja interfejsu API komponentów

[https://docs.streamlit.io/library/components/components-api](https://docs.streamlit.io/library/components/components-api)

### Utwórz komponent

### Opublikuj komponent

### Galeria komponentów

[https://streamlit.io/components](https://streamlit.io/components)

### Mapa drogowa

[https://roadmap.streamlit.app/](https://roadmap.streamlit.app/)

---

# Lista zmian

[https://docs.streamlit.io/library/changelog](https://docs.streamlit.io/library/changelog)

#### Wskazówka

Aby zaktualizować do najnowszej wersji Streamlit, uruchom:

```
pip install --upgrade streamlit
```

---

# Samouczki

[https://docs.streamlit.io/knowledge-base/tutorials](https://docs.streamlit.io/knowledge-base/tutorials)

Nasze samouczki zawierają przykłady krok po kroku tworzenia różnych typów aplikacji w Streamlit.

* [Połącz się ze źródłami danych](https://docs.streamlit.io/knowledge-base/tutorials/databases)
* [Podstawy stanu sesji](https://docs.streamlit.io/knowledge-base/tutorials/session-state)
* [Wdróż aplikacje Streamlit](https://docs.streamlit.io/knowledge-base/tutorials/deploy)
* [Twórz aplikacje konwersacyjne](https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps)

---

# Korzystanie ze Streamlita

[https://docs.streamlit.io/knowledge-base/using-streamlit](https://docs.streamlit.io/knowledge-base/using-streamlit)

Oto kilka często zadawanych pytań dotyczących korzystania ze Streamlit. Jeśli uważasz, że brakuje czegoś ważnego, o czym wszyscy powinni wiedzieć, [otwórz problem](https://github.com/streamlit/docs/issues) lub [prześlij prośbę o ściągnięcie](https://github.com/streamlit/docs/pulls) , a my z przyjemnością to sprawdzimy!

* [Kontrole poczytalności](https://docs.streamlit.io/knowledge-base/using-streamlit/sanity-checks)
* [Elementy wsadowe i widżety wejściowe za pomocą `st.form`](https://docs.streamlit.io/knowledge-base/using-streamlit/batch-elements-input-widgets-form)
* [Jak uruchomić mój skrypt Streamlit?](https://docs.streamlit.io/knowledge-base/using-streamlit/how-do-i-run-my-streamlit-script)
* [Jak sprawić, by Streamlit obserwował zmiany w innych modułach, które importuję w mojej aplikacji?](https://docs.streamlit.io/knowledge-base/using-streamlit/streamlit-watch-changes-other-modules-importing-app)
* [Jakie przeglądarki obsługuje Streamlit?](https://docs.streamlit.io/knowledge-base/using-streamlit/supported-browsers)
* [Jaka jest ścieżka do `config.tom `pliku Streamlit?](https://docs.streamlit.io/knowledge-base/using-streamlit/path-streamlit-config-toml)
* [Gdzie st.file_uploader przechowuje przesłane pliki i kiedy są one usuwane?](https://docs.streamlit.io/knowledge-base/using-streamlit/where-file-uploader-store-when-deleted)
* [Jak pobrać nazwę pliku przesłanego za pomocą st.file_uploader?](https://docs.streamlit.io/knowledge-base/using-streamlit/retrieve-filename-uploaded)
* [Jak usunąć „· Streamlit” z tytułu aplikacji?](https://docs.streamlit.io/knowledge-base/using-streamlit/remove-streamlit-app-title)
* [Jak pobrać plik w Streamlit?](https://docs.streamlit.io/knowledge-base/using-streamlit/how-download-file-streamlit)
* [Jak pobrać Pandas DataFrame jako plik CSV?](https://docs.streamlit.io/knowledge-base/using-streamlit/how-download-pandas-dataframe-csv)
* [Jak mogę `st.pydeck_chart `użyć niestandardowych stylów Mapbox?](https://docs.streamlit.io/knowledge-base/using-streamlit/pydeck-chart-custom-mapbox-styles)
* [Jak wstawić elementy nie po kolei?](https://docs.streamlit.io/knowledge-base/using-streamlit/insert-elements-out-of-order)
* [Jak animować elementy?](https://docs.streamlit.io/knowledge-base/using-streamlit/animate-elements)
* [Dołącz dane do tabeli lub wykresu](https://docs.streamlit.io/knowledge-base/using-streamlit/append-data-table-chart)
* [Ukryj indeksy wierszy podczas wyświetlania ramki danych](https://docs.streamlit.io/knowledge-base/using-streamlit/hide-row-indices-displaying-dataframe)
* [Jak nagrać screencast?](https://docs.streamlit.io/knowledge-base/using-streamlit/record-screencast)
* [Jak uaktualnić do najnowszej wersji Streamlit?](https://docs.streamlit.io/knowledge-base/using-streamlit/how-upgrade-latest-version-streamlit)
* [Jak ukryć menu hamburgerów w mojej aplikacji?](https://docs.streamlit.io/knowledge-base/using-streamlit/how-hide-hamburger-menu-app)
* [Aktualizacja widżetu dla co drugiego wejścia podczas korzystania ze stanu sesji](https://docs.streamlit.io/knowledge-base/using-streamlit/widget-updating-session-state)
* [Jak utworzyć łącze kotwicy?](https://docs.streamlit.io/knowledge-base/using-streamlit/create-anchor-link)
* [Jak włączyć dostęp do kamery?](https://docs.streamlit.io/knowledge-base/using-streamlit/enable-camera)
* [Dlaczego Streamlit ogranicza zagnieżdżanie `st.columns`?](https://docs.streamlit.io/knowledge-base/using-streamlit/why-streamlit-restrict-nested-columns)
* [Jak hostować pliki statyczne w Streamlit?](https://docs.streamlit.io/library/advanced-features/static-file-serving)
* [Co to jest serializowalny stan sesji?](https://docs.streamlit.io/knowledge-base/using-streamlit/serializable-session-state)

---

# Usprawnione komponenty

[https://docs.streamlit.io/knowledge-base/components](https://docs.streamlit.io/knowledge-base/components)

Poniżej znajdują się wybrane pytania, które otrzymaliśmy na temat Streamlit Components. Jeśli nie znajdziesz tutaj swojego pytania, zajrzyj na forum społeczności Streamlit za pomocą [tagu Components](https://discuss.streamlit.io/tag/custom-components) .

* [Czym Streamlit Components różni się od funkcjonalności zapewnianej w podstawowym pakiecie Streamlit?](https://docs.streamlit.io/knowledge-base/components/how-streamlit-components-differ-base-package)
* [Jakie rodzaje rzeczy **nie są możliwe** dzięki Streamlit Components?](https://docs.streamlit.io/knowledge-base/components/not-possibe-streamlit-components)
* [Jak dodać komponent do paska bocznego?](https://docs.streamlit.io/knowledge-base/components/add-component-sidebar)
* [Mój komponent wydaje się migać/zacinać się... jak to naprawić?](https://docs.streamlit.io/knowledge-base/components/component-blinking-stuttering-fix)

---

# Instalowanie zależności

[https://docs.streamlit.io/knowledge-base/dependencies](https://docs.streamlit.io/knowledge-base/dependencies)

* [ModuleNotFoundError: Brak modułu o nazwie](https://docs.streamlit.io/knowledge-base/dependencies/module-not-found-error)
* [ImportError: libGL.so.1: nie można otworzyć udostępnionego pliku obiektu: Brak takiego pliku lub katalogu](https://docs.streamlit.io/knowledge-base/dependencies/libgl)
* [BŁĄD: Nie znaleziono pasującej dystrybucji dla](https://docs.streamlit.io/knowledge-base/dependencies/no-matching-distribution)
* [Jak zainstalować pakiet nie na PyPI/Conda, ale dostępny na GitHub](https://docs.streamlit.io/knowledge-base/dependencies/install-package-not-pypi-conda-available-github)
* [Zainstaluj Snowflake Connector dla Pythona w Streamlit Community Cloud](https://docs.streamlit.io/knowledge-base/dependencies/snowflake-connector-python-streamlit-cloud)

---

# Pytania i błędy związane z wdrażaniem

[https://docs.streamlit.io/knowledge-base/deploy](https://docs.streamlit.io/knowledge-base/deploy)

* [Jak wdrożyć Streamlit w domenie, aby działał na zwykłym porcie (tj. porcie 80)?](https://docs.streamlit.io/knowledge-base/deploy/deploy-streamlit-domain-port-80)
* [Jak mogę wdrożyć wiele aplikacji Streamlit w różnych subdomenach?](https://docs.streamlit.io/knowledge-base/deploy/deploy-multiple-streamlit-apps-different-subdomains)
* [Jak wdrożyć Streamlit na Heroku, AWS, Google Cloud itp.?](https://docs.streamlit.io/knowledge-base/deploy/deploy-streamlit-heroku-aws-google-cloud)
* [Wywoływanie podprocesu języka Python we wdrożonej aplikacji Streamlit](https://docs.streamlit.io/knowledge-base/deploy/invoking-python-subprocess-deployed-streamlit-app)
* [Czy Streamlit obsługuje protokół WSGI? (alias Czy mogę wdrożyć Streamlit za pomocą gunicorn?)](https://docs.streamlit.io/knowledge-base/deploy/does-streamlit-support-wsgi-protocol)
* [argh. Ta aplikacja przekroczyła swoje limity zasobów.](https://docs.streamlit.io/knowledge-base/deploy/resource-limits)
* [Aplikacja nie ładuje się podczas pracy zdalnej](https://docs.streamlit.io/knowledge-base/deploy/remote-start)
* [Uwierzytelnianie bez logowania jednokrotnego](https://docs.streamlit.io/knowledge-base/deploy/authentication-without-sso)
* [Nie mam GitHuba ani G Suite. Jak zalogować się do Streamlit Community Cloud?](https://docs.streamlit.io/knowledge-base/deploy/sign-in-without-sso)
* [Jak udostępniać aplikacje przeglądającym spoza mojej organizacji?](https://docs.streamlit.io/knowledge-base/deploy/share-apps-with-viewers-outside-organization)
* [Uaktualnij wersję Streamlit swojej aplikacji w Streamlit Community Cloud](https://docs.streamlit.io/knowledge-base/deploy/upgrade-streamlit-version-on-streamlit-cloud)
* [Porządkowanie aplikacji za pomocą obszarów roboczych w Streamlit Community Cloud](https://docs.streamlit.io/knowledge-base/deploy/organizing-apps-workspaces-streamlit-cloud)
* [Jak zwiększyć limit wysyłania w usłudze `st.file_uploader`Streamlit Community Cloud?](https://docs.streamlit.io/knowledge-base/deploy/increase-file-uploader-limit-streamlit-cloud)
* [Jak dostosować subdomenę mojej aplikacji?](https://docs.streamlit.io/knowledge-base/deploy/custom-subdomains)
* [Jak zaktualizować ustawienia administratora konta w Streamlit Community Cloud?](https://docs.streamlit.io/knowledge-base/deploy/how-to-update-account-admin-settings-on-streamlit-community-cloud)
* [Nie można edytować ani usuwać aplikacji w Streamlit Community Cloud po zmodyfikowaniu nazwy użytkownika GitHub](https://docs.streamlit.io/knowledge-base/deploy/unable-to-edit-or-delete-apps-in-streamlit-community-cloud-after-modifying-github-username)
* [huh. To nie powinno się zdarzyć komunikat po próbie zalogowania](https://docs.streamlit.io/knowledge-base/deploy/huh-this-isnt-supposed-to-happen-message-after-trying-to-log-in)
* [huh. To nie powinno się zdarzyć. Brak prawidłowego połączenia SSO dla domeny](https://docs.streamlit.io/knowledge-base/deploy/huh-this-isnt-supposed-to-happen-no-valid-sso-connection-for-domain)
* [Dostęp tylko do wyświetlania do aplikacji po zmianie nazwy użytkownika GitHub lub nazwy repozytorium](https://docs.streamlit.io/knowledge-base/deploy/view-only-access-to-app-after-changing-github-username-or-repository-name)
* [Próba zalogowania się do Streamlit Community Cloud kończy się niepowodzeniem z błędem 403](https://docs.streamlit.io/knowledge-base/deploy/login-attempt-to-streamlit-community-cloud-fails-with-error-403)
* [Jak przesłać zgłoszenie do pomocy technicznej dla usługi Streamlit Community Cloud](https://docs.streamlit.io/knowledge-base/deploy/how-to-submit-a-support-case-for-streamlit-community-cloud)
* [Jak usunąć konto Streamlit Community Cloud](https://docs.streamlit.io/knowledge-base/deploy/how-to-delete-your-streamlit-community-cloud-account)

---
