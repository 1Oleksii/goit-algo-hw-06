## Висновки

У цьому завданні було реалізовано два алгоритми обходу графа — **DFS** (глибина у пріоритеті) та **BFS** (ширина у пріоритеті) — для графа, який моделює лінію Київського метро (червона гілка).

Граф є **лінійним** — тобто, станції з’єднані послідовно, без розгалужень або петель. Саме тому шлях від початкової станції **"Akademmistechko"** до кінцевої **"Teatralna"** однаковий для обох алгоритмів:

**DFS шлях**:  
`['Akademmistechko', 'Zhytomyrska', 'Sviatoshyn', 'Nyvky', 'Beresteiska', 'Shuliavska', 'Politekhnichnyi Instytut', 'Vokzalna', 'Universytet', 'Teatralna']`

**BFS шлях**:  
`['Akademmistechko', 'Zhytomyrska', 'Sviatoshyn', 'Nyvky', 'Beresteiska', 'Shuliavska', 'Politekhnichnyi Instytut', 'Vokzalna', 'Universytet', 'Teatralna']`

### Різниця між DFS та BFS

Попри однаковий результат у цьому конкретному випадку, в загальному:

- **DFS** заглиблюється у глибину шляху і може першим знайти довший або не найкоротший маршрут.
- **BFS** завжди знаходить **найкоротший шлях** у графах без ваг (як у нас).

Отже, для **деревовидних або складніших графів** результати алгоритмів можуть суттєво відрізнятись.