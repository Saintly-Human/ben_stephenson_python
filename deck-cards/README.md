# 🃏 Card Dealing Simulation (Python)

A Python implementation of a standard card deck creation, Fisher-Yates shuffling algorithm, and round-robin card dealing process. 

This project solves Exercise 126 from *The Python Workbook* (Ben Stephenson), building upon the deck creation and shuffling logic developed in Exercise 125.

---

## Task Description

### 📝 Original Task (Russian)
> Во многих карточных играх после процедуры тасования колоды каждый игрок получает на руки определенное количество карт. Напишите функцию deal, принимающую на вход три параметра: количество игроков, количество раздаваемых каждому из них карт и саму колоду. Функция должна возвращать список рук, которые были розданы игрокам. При этом каждая рука, в свою очередь, тоже является списком из входящих в нее карт. Во время раздачи карт игрокам функция параллельно должна удалять розданные карты из переданной ей третьим параметром колоды. Также принято раздавать карты каждому игроку по одной строго по очереди. Придерживайтесь этих принципов и при написании своей функции. Воспользуйтесь своими наработками из упражнения 125 при построении структуры основной программы. Вам необходимо создать колоду карт, перетасовать ее и раздать четырем игрокам по пять карт. Выведите на экран карманные карты всех игроков, находящихся в раздаче, а также оставшиеся в колоде карты.

### 📝 English Translation
> In many card games, each player receives a number of cards after the deck has been shuffled. Write a function named deal that takes three parameters: the number of players, the number of cards per player, and the deck. The function should return a list of hands (where each hand is a list of cards). As cards are dealt, the function must remove them from the deck. Cards must be dealt one at a time sequentially to each player in order.

---

## 📌 Features

* **Custom Deck Generation (`create_deck`)**: Generates a standard 52-card deck combining 13 ranks (`2-10`, `J`, `Q`, `K`, `A`) and 4 suits (`s`, `h`, `d`, `c`).
* **Fisher-Yates Shuffle (`shuffle`)**: Implements an in-place deck shuffling algorithm without relying on `random.shuffle()`.
* **Sequential Card Dealing (`deal`)**: Simulates real-life card distribution where players take turns receiving one card at a time. Karten are removed directly from the main deck in-place.
* **Input Validation & Safety**: Handles invalid user input and prevents dealing more cards than available in the deck.

---

## 🛠️ How It Works

1. **Deck Creation**: Creates a list of strings representing 52 unique playing cards.
2. **Shuffling**: Reorders the cards randomly using the Fisher-Yates algorithm.
3. **Dealing**: 
   * Accepts three parameters: `number_of_players`, `cards_per_player`, and `deck`.
   * Deals **one card per player per round** until everyone receives the required amount.
   * Mutates the original `deck` parameter by removing dealt cards (`pop(0)`).
   * Returns a list of lists representing each player's hand.

---

## 🚀 Getting Started

### Prerequisites

* Python 3.6+ installed.

### ⚙️ Execution

1. **Clone the repository & navigate to this exercise:**:
```bash
git clone https://github.com/Saintly_Human/ben_stephenson_python.git
cd ben_stephenson_python/deck-cards
```

2. Run the application:

```bash
python main.py
```

## 🖥️ **Example Usage & Output:**

```plaintext
How many folks are playing? (integer ONLY): 4
How many cards for each person? (integer ONLY): 5

THE GAME IS STARTING !!!
4 players with 5 cards per person

1 player has these cards:
10h, Kd, 3s, 7c, Qh

2 player has these cards:
4s, As, Jd, 2c, 8h

3 player has these cards:
6d, 9h, Ks, 5c, 10c

4 player has these cards:
7d, Jh, Ac, 2s, 4c

32 left in deck: 5s, 8d, Qs, 3c, 9c, ...
```
