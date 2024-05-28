# goit-algo-fp

# Висновки щодо правильності розрахунків Задачі #7

## Порівняння отриманих за допомогою методу Монте-Карло результатів та результатів аналітичних розрахунків

Симуляція кидків двох кубиків методом Монте-Карло була виконана для 100000 кидків. Нижче надано порівняння отриманих ймовірностей та теоретичних ймовірностей:

# Ймовірності за допомогою Методу Монте-Карло:
Сума    Імовірність
2       2.81% (2813/100000)
3       5.48% (5478/100000)
4       8.36% (8361/100000)
5       11.09% (11088/100000)
6       13.90% (13901/100000)
7       16.76% (16756/100000)
8       13.96% (13958/100000)
9       11.16% (11164/100000)
10      8.31% (8313/100000)
11      5.52% (5516/100000)
12      2.65% (2650/100000)


### Аналітічні ймовірності:

Аналітичні ймовірності:
Сума    Імовірність
2       2.78%
3       5.56%
4       8.33%
5       11.11%
6       13.89%
7       16.67%
8       13.89%
9       11.11%
10      8.33%
11      5.56%
12      2.78%

# Висновок
На основі порівняння симуляційних результатів та аналітичних ймовірностей можна зробити висновок, що метод Монте-Карло ефективно моделює ймовірності подій. Чим більше кидків симулюється, тим ближчими до аналітичних стають результати симуляції, підтверджуючи правильність аналітичних розрахунків.
