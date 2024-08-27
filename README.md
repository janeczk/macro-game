# Opis narzędzia do automatyzacji rozgrywki

## Podstawowe założenia i cele
- Projekt w swoim zamyśle ma na celu być jak najbezpieczniejszym narzędziem do automatyzacji rozgrywki, dalej zwany botem, macro. Poprzez zastosowanie rozwiązań opierających się na naśladowaniu gracza, tj. klikania myszką i klawiaturą, zachowujemy się bardziej jak człowiek, niż jak bot, co zmniejsza naszą szanse na wykrycie niepożądanych inputów przez grę. Większość botów korzysta z wyciągania informacji bezpośrednio ze strony (co zwiększa podejrzany traffic na stronie) i na tej podstawie podejmuje działania, ten projekt natomiast opiera się na tym co widzi na ekranie. <br>
- Bot ma na celu zdobywanie przedmiotów poprzez pokonywanie przeciwników, a następnie sprzedanie ich u handlarza i powtarzórzenie cyklu.


```python
from func import *
from const import *
from visualization import *
```

## Czas pomiędzy akcjami gracza
Funckja wait() ma naśladować czas z jakim gracz średnio wykonuje swoje akcje. Zastosowany został rozkład normalny w odpowiednich proporcjach. Wykres reprezentuje rozkład czasu dla miliona prób. Jak widać około 90% wyników mieści się między 0.1-0.8 sekundy, przez co w rzeczywisty sposób odzwierciedla czas pomiędzy akcjami gracza. W programie te czasy są traktowane wektorowo tzn. można je mnożyć oraz dzielić przez określone stałe w celu usprawnienia działania konkretnych części programu. 


```python
def wait():
    x = np.random.normal(0.5,0.3,1)
    if x < 0 :  return float(-x + random.randrange(0,200)/1000)
    if x < 0.1 :return float(x + random.randrange(50,200)/1000) 
    if x > 1.2 : return float(x - random.randrange(0,500)/1000)
    return float(x)
```


```python
create_hist(1000000) #using function wait() for milion times and visualization
```


    
![png](jpgs/output_4_0.png)
    


## Algorytm wyszukiwania i pokonywania przeciwników
### Z tą mapą pracujemy, zacznijmy od opisania co jest czym.
- Biały kwadrat - gracz
- Czerwony diament - przeciwnik
- Niebieskie koło - przejścia między mapami
![mapa_bot.png](jpgs/6b47062f-0231-4dfb-9f0a-e47709b0958b.png)<br>
Algorytm pamięta ostatnią pozycję gracza i na jej podstawie wyznacza najbliższą trasę do przeciwnika, następnie klika na niego myszką i czeka aż dookoła niego pojawi się gracz. W momencie zauważenia gracza klika przycisk 'e' odpowiadający zaatakowniu, odczekuje chwile i powtarza cykl. W momencie pozbycia się wszystkich przeciwników z mapy, idzie do predefiniowanej pozycji przejścia na następną mapę i ponownie się powtarza. Z każdym przejściem mapy aktualizowana jest jej nazwa do której przypisane są kluczowe wartości, pozwalające na działanie programu.

## Struktury danych i problemy napotkane po drodze
Dzięki zastowaniu słownika który na kluczu przyjmuje unikalne nazwy map, możliwe było w wygodny sposób zapisywać ich właściwości, ponieważ każda rózni się pozycjami przeciwników, wymiarami, przejściami itd. 


```python
print(map_data["Gvar Hamryd"].printMapProperties())
```

    startMiniMap:  [142, 118]
    endMiniMap:  [685, 931]
    mapSize:  [64, 96]
    transitions:  [[63, 42], [63, 41], [11, 0], [12, 0], [0, 79], [0, 80]]
    mob_locations:  [[25, 15], [52, 43], [53, 36], [54, 23], [46, 19], [44, 42], [39, 46], [42, 54], [45, 52], [55, 53], [53, 60], [48, 67], [40, 68], [38, 75], [32, 73], [31, 80], [37, 85], [45, 86], [22, 88], [12, 89], [17, 82], [8, 79], [15, 72], [16, 63], [12, 69], [48, 83], [35, 77], [33, 61], [34, 49], [26, 42], [20, 49], [3, 59], [4, 68], [9, 67], [14, 47], [44, 66], [17, 51], [6, 43], [19, 32], [8, 30], [16, 24], [8, 17], [17, 14], [13, 5], [30, 47], [59, 42], [55, 28], [53, 17], [50, 51], [38, 51], [37, 57], [38, 63], [29, 64], [23, 73], [49, 77], [23, 83], [3, 80], [7, 62], [12, 58], [11, 53], [25, 46], [28, 37], [24, 33], [12, 28], [12, 13], [19, 4], [56, 34]]
    nextMapCoords:  [0, 79]
    None
    

Również w zmiennej game_state zapisane są informacje, na których podstawie są podejmowane decyzje.


```python
game_state = const.GameState()
game_state.setGameState({"map_name": "Gvar Hamryd",})
print(game_state.getGameState())
```

    {'map_name': 'Gvar Hamryd', 'player_coords': [62, 42], 'mob_coords': [0, 0], 'start_mini_map': [142, 118], 'end_mini_map': [685, 931], 'map_size': [64, 96], 'step_x': 8.484375, 'step_y': 8.46875}
    

Głównym problemem była zamiana pozycji pikseli na ekranie, na koordynaty w grze, temu służą zmienne step_x i step_y, które odpowiadają jednemu koordynatowi na mapie w danej osi. Do zamiany koordynatów na piksele służy funkcja transfer_coords_to_pixels_XY(coords,game_state).


```python
print(transfer_coords_to_pixels_XY([20,20],game_state))
```

    (315.9296875, 291.609375)
    

Oznacza to, że koordynaty [20,20] na mapie "Gvar Hamryd" , są na pikselach (315.9296875, 291.609375). Wyniki te będą się róznić w zależności od rozdzielczości monitora oraz przybliżenia na stronie (alt + scroll). Niestety ta część nie jest uniwersalna i musiałaby być zmieniana w zależności od użytkownika. Do poprawnego działania programu potrzebne są wymiary mini mapy, w zmiennej start_mini_map i end_mini_map.

## Dalsze perspektywy rozwoju projektu
Głównym atrybutem jest uniwersalność kodu i zawarcie wszystkich niezbędnych informacji w jednym miejscu. Dzięki zastosowaniu klas oraz wszyskich danych w jednej zmiennej najbardziej czasochłonnym problemem przy dodawaniu kolejnych map, byłoby ręczne mapowanie przeciwników, nie pisanie kodu. <br>
Kolejną funkcją mogłoby być automatyczne wyszukiwanie herosów, którzy charakteryzują się stałymi miejscami pojawiania się, ale na dużej ilości map. Wymagałoby to zmapowania pojedynczych respów oraz "pomierzenia" dużej ilości map. 


```python

```
