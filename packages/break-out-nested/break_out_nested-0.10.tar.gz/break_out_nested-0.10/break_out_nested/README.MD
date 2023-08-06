# Break out of nested loops with max. 4 lines of code, no matter how deeply they are nested 


## The problem: breaking out of nested loops 

#### pip install break-out-nested 

```python
# Break out of nested loops - a pain in the ***
# How it is usually done:
done = False
for i in range(1, 6, 1):  # 1st loop
    print('i:', i)
    for j in range(1, 11, 2):  # 2nd loop
        print('   i, j:', i, j)
        for k in range(1, 21, 4):  # 3rd loop
            print('      i,j,k:', i, j, k)
            if i % 3 == 0 and j % 3 == 0 and k % 3 == 0:
                done = True
                break  # breaking from 3rd loop
        if done: break  # breaking from 2nd loop
    if done: break  # breaking from 1st loop
```



## The solution

```python
# Way easier
from break_out_nested import it, bol

# you need to create new variables as attributes of it,
# because break_out_nested has only access to these variables
it.i, it.j, it.k = 1, 1, 1


# the break condition
def cond(): return it.i % 3 == 0 and it.j % 3 == 0 and it.k % 3 == 0


# The condition will be checked in each loop
# The function that checks the condition has to be passed as the last argument. 
# You can pass as many iterables as you want to the function
for it.i, it.j, it.k in bol(range(1, 6, 1), range(1, 11, 2), range(1, 21, 4), cond):
    print(it.i, it.j, it.k)
```



## More examples

```python
# More examples
def cond(): return it.i + it.j + it.k == 777


it.i, it.j, it.k = 0, 0, 0
for it.i, it.j, it.k in bol(range(100), range(1000), range(10000), cond):
    print(it.i, it.j, it.k)


def cond(): return it.i + it.j + it.k >= 100000


it.i, it.j, it.k = 0, 0, 0
# you don't have to use it.i, it.j, it.k as the loop variables, you can
# use anything you want, but you have to update the variables somewhere
for i, j, k in bol(range(100), range(1000), range(10000), cond):
    it.i, it.j, it.k = i * 10, j * 100, k * 100
    print(it.i, it.j, it.k)
```

