# [263. Ugly Number](https://leetcode.com/problems/ugly-number/)

**Main Idea**  
Take advantage of the fact that if a is divisible by b, then there's no remainder.

**Algorithm**  
Divide the number by 2 as many times as you can, then 3 as many times as you can, then 5 as many times as you can. If the orignal number has only 2, 3, and/or 5 as prime factors, then the number will become 1 after all of the divisions.

```python
def isUgly(n: int) -> bool:
    if n <= 0:
        return False

    for factor in [2, 3, 5]:
        while n % factor == 0:
            n = n / factor

    return n == 1
```

**Time complexity**  
$O(\log n)$ since we are repeatedly dividing $n$

**Space complexity**  
$O(1)$ since the array we use is constant size
