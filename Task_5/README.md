В одной из предыдущих задач требовалось вывести перевернутую матрицу, теперь задача усложняется:
При этом поворот необходимо осуществлять in−place, т.е. без выделения дополнительной памяти. 

Для этого вместо результирующей матрицы необходимо вывести последовательность операций. 
За одну операцию можно обменять местами два элемента матрицы.

Вам дана матрица n×n, а так же указано, надо ли повернуть изображение по часовой R или против часовой L стрелки. 
Выведите последовательность операций, чтобы исходная матрица повернулась на 90 градусов в указанном направлении.
Заметьте, что необязательно переставлять элементы в том порядке, в котором происходил бы поворот, главное чтобы в 
результате матрица соответствовала повороту на 90 градусов. Также необязательно, чтобы количество операций было минимальным, нужно только вписаться в ограничения.

#### Формат входных данных 
Первая строка содержит одно натуральное число n (1≤n≤103) и указание направления поворота — символ R или L. 

Следующие n строк содержат описание матрицы, по n целых неотрицательных чисел, не превосходящих 

#### Формат выходных данных
В первой строке выведите число k — необходимое количество операций, при этом это число не должно превосходить. 

В последующих k строках выведите по две пары чисел — координаты (x1,y1) и (x2,y2) ячеек, между которыми необходимо обменять элементы матрицы.

#### Замечание
Обратите внимание, что нумерация строк и столбцов матрицы ведётся с 0, а не с 1.

### Пример
#### Входные данные:
```azure
2 L # размер и направление поворота матрицы
0 0 
0 1
```


#### Выходные данные:
```azure
1 
1 1 0 1
```