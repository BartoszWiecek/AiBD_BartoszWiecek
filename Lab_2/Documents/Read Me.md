# Operacje wykonane na danych   
Aby powtórzyć operacje wykonane przeze mnie doczas analizy danych należy uruchomić kod znajdujący się w pliku 'zad_1.ipynb'. 
Plik ten można znaleźć w katalogu 'Command Files'. Kod napisany jest w języku pyhon, a do jego uruchomienia niezbędne jest posiadanie ninlioteki 'pandas'.
Uruchomienie kodu powoduje pobranie oryginalnych danych z pliku 'tb.csv' znajdującego się w katalogu 'Original Data'.
Następnie nagłówki kolumn zostają zmienione na bardziej czytelne. Kolejno wykonany zostaje proces meltingu który zmienia tabelę do postaci w której składa się ona z 4 kolumn.
Pierwsza zawiera kraj, druga rok, trzecia informację o płci i wieku chorych a czwarta - liczbę chorych. Następnie z tabeli zostają usunięte wszystkie niekompletne wiersze (czyli takie które zawierają co najmniej jedną pustą komórkę).
Po wyczyszczeniu tabeli z nikompletnych wierszy kolumna informująca o wieku i płci chorych zostaje rozdzielona na dwie osobne kolumny (jedna zawiera informacje o płci, a druga o wieku).
Proces ten realizuje zasadę 'tidy data'. Na koniec, tak uporządkowane dane zostają zapisane do pliku 'processed_tb.csv', który znajduje się w katalogu 'Analysis Data'.