# Streamlit

## Skonfiguruj VSCode do uruchamiania aplikacji Streamlit

[https://medium.com/codefile/how-to-run-your-streamlit-apps-in-vscode-3417da669fc](https://medium.com/codefile/how-to-run-your-streamlit-apps-in-vscode-3417da669fc)

Najpierw utwórz aplikację — zrobi to coś prostego, takiego jak to:

```
import streamlit as st
st.write("Hello from Streamlit")
```

Kiedy po raz pierwszy to utworzysz i zapiszesz jako, na przykład, `myapp.py` VSCode myśli, że to zwykły plik Pythona, a jeśli spróbujesz uruchomić go z menu Uruchom, niewiele to da.

---



### Musimy powiedzieć VSCode, jak go uruchomić. 

Aby to zrobić, kliknij ikonę ***uruchamiania/debugowania*** po lewej stronie okna. 

Spowoduje to wyświetlenie okienka Uruchom/Debuguj, w którym zobaczysz kilka opcji. 

Ten, który nas interesuje, to ***utworzenie pliku launch.json*** .

Foto: [https://miro.medium.com/v2/resize:fit:1400/format:webp/1*S8LyCLS003Xx02rNujD0uw.png](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*S8LyCLS003Xx02rNujD0uw.png)

Kliknij na to, a pojawi się monit o wybranie konfiguracji, jak na poniższym obrazku. Wybierz opcję, którą zaznaczyłem na żółto ***Moduł Debuguj moduł Pythona**, wywołując go za pomocą „**-m**”.*

Foto: [https://miro.medium.com/v2/resize:fit:720/format:webp/1*0Sc-64g8N4mcMy6fevib6w.png](https://miro.medium.com/v2/resize:fit:720/format:webp/1*0Sc-64g8N4mcMy6fevib6w.png)

Następnie musisz podać nazwę modułu, który ma być ***streamlitowany*** .

Foto: [https://miro.medium.com/v2/resize:fit:720/format:webp/1*e_m95ONEVEK71vswgi9ydA.png](https://miro.medium.com/v2/resize:fit:720/format:webp/1*e_m95ONEVEK71vswgi9ydA.png)

Spowoduje to utworzenie pliku o nazwie** *launch.json*** , który zawiera konfigurację uruchamiania. Plik będzie wyglądał jak ten poniżej (ale musimy go trochę zmienić).

Foto: [https://miro.medium.com/v2/resize:fit:720/format:webp/1*gW4XrelL6-71KYp4S3O5mA.png](https://miro.medium.com/v2/resize:fit:720/format:webp/1*gW4XrelL6-71KYp4S3O5mA.png)

Domyślna konfiguracja zakłada brak parametrów, ale musimy podać dwa: słowo ***uruchom*** i nazwę pliku, który zamierzamy uruchomić. Robimy to, dodając listę ***argumentów*** , jak widać poniżej.

Foto: [https://miro.medium.com/v2/resize:fit:720/format:webp/1*jKfUheaW7aAIUT-gbFJqSw.png](https://miro.medium.com/v2/resize:fit:720/format:webp/1*jKfUheaW7aAIUT-gbFJqSw.png)

Tak więc lista argumentów to `"args": ["run", "${file}"]` — gdzie druga to zmienna VSCode, która odnosi się do aktualnie otwartego pliku.


**I nie zapomnij dodać przecinka na końcu poprzedniego wiersza!**

Zapisz plik uruchamiania i wróć do swojej aplikacji.

Teraz, gdy wybierzesz Uruchom z menu Uruchom, oto co się stanie:

Foto: [https://miro.medium.com/v2/resize:fit:720/format:webp/1*cqGEVmIs_IHJ3TMobeMYVA.png](https://miro.medium.com/v2/resize:fit:720/format:webp/1*cqGEVmIs_IHJ3TMobeMYVA.png)

Rzeczywiste wykonywane polecenie to:

```
python -m streamlit run myapp.py
```

I to jest odpowiednik tego, co normalnie uruchamiałbyś w oknie terminala.

W rezultacie ta urocza aplikacja działa w Twojej przeglądarce (jestem pewien, że możesz zrobić to lepiej!).

Foto:[ https://miro.medium.com/v2/resize:fit:720/format:webp/1*QT8OIT_TJ9DhBIuRZESONg.png](https://miro.medium.com/v2/resize:fit:720/format:webp/1*QT8OIT_TJ9DhBIuRZESONg.png)

---



Teraz każdy plik znajdujący się w tym samym katalogu co nowy `launch.json` będzie uruchamiany jako plik **Streamlit**.

Zadanie wykonane!
