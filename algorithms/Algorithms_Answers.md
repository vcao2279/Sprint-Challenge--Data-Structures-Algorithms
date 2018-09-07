```
a)  a = 0
    while (a < n * n * n) 
      a = a + n * n
```
> In this while loop, a add n*n until a===n\*n\*n. n\*n\*n / n\*n = n, this means a needs to add nth times for the loop to stop. The number of operation will grow proportionally with n. This is O(n).

```
b)  sum = 0
    for (i = 0; i < n; i++)
      for (j = i + 1; j < n; j++)
        for (k = j + 1; k < n; k++)
          for (l = k + 1; l < 10 + k; l++)
            sum++
```
> The first 3 `for loops` depends on n. The 4th `for loop` depends on k, which depends on n. So the number of operation should be O(n<sup>4</sup>)

```
c)  bunnyEars = function(bunnies) {
      if (bunnies == 0) return 0
      return 2 + bunnyEars(bunnies-1)
    }
```
> This recursive function will run until `bunnies` reaches 0, hence the number of operation will grow proportionally with n. This is O(n)   

**Exercise II**
> I would try floor 51 first. If the eggs break then that mean _f_ is in the lower half. Then i try 26,now i can narrow down the _f_ within which 25 floors. Then down to 13, 7, 4, then 1. So it takes 6 tries.