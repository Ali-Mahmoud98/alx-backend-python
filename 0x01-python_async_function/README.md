# 0x01. Python - Async

## Resources
* [Async IO in Python: A Complete Walkthrough]()
* [asyncio - Asynchronous I/O]()
* [random.uniform]()

## Learning Objectives
* `async` and `await` syntax
* How to execute an async program with `asyncio`
* How to run concurrent coroutines
* How to create `asyncio` tasks
* How to use the `random` module

## basic concepts and components of `asyncio`
`asyncio` is a Python library used to write concurrent code using the `async`/`await` syntax. It provides a foundation for asynchronous programming, which allows you to manage multiple tasks simultaneously, making your code more efficient, especially when dealing with I/O-bound operations like network requests, file handling, or database queries.

### 1. **Asynchronous Programming**
   - **Synchronous** code runs sequentially, meaning each task must finish before the next one starts.
   - **Asynchronous** code, on the other hand, allows tasks to be run concurrently. This doesn't mean that tasks are literally running at the same time, but rather, they are managed in a way that allows them to be paused and resumed, making better use of time, especially when waiting for I/O operations.

### 2. **Event Loop**
   - The **event loop** is the core of any asyncio program. It runs asynchronous tasks and callbacks, performs network I/O operations, and schedules them to run. 
   - You can think of the event loop as a manager that knows when a task is ready to run and when it should be paused.

   ```python
   import asyncio

   async def main():
       print('Hello')
       await asyncio.sleep(1)
       print('World')

   asyncio.run(main())
   ```

   In this example, `asyncio.run(main())` starts the event loop and runs the `main()` function until it completes.

### 3. **Coroutines**
   - A **coroutine** is a special function in Python defined with `async def`. 
   - When called, a coroutine does not execute immediately but returns a coroutine object that can be awaited.
   - You can pause a coroutine using `await`, which allows other tasks to run.

   ```python
   async def greet():
       print('Hello')
       await asyncio.sleep(1)
       print('World')
   ```

   Here, `await asyncio.sleep(1)` pauses the coroutine for 1 second, allowing other tasks to run during that time.

### 4. **Tasks**
   - **Tasks** are used to schedule coroutines concurrently. When you create a task, it is added to the event loop, which will run it as soon as possible.
   - You can create a task using `asyncio.create_task()`.

   ```python
   async def say_hello():
       print('Hello')
       await asyncio.sleep(1)
       print('Goodbye')

   async def main():
       task = asyncio.create_task(say_hello())
       await task

   asyncio.run(main())
   ```

   In this example, `say_hello()` is scheduled to run concurrently within the `main()` coroutine.

### 5. **Await**
   - The `await` keyword is used to pause the execution of a coroutine until the awaited task is completed. 
   - You can await another coroutine, a Task, or any object that implements the `__await__()` method.

   ```python
   async def main():
       print('Waiting...')
       await asyncio.sleep(2)
       print('Done!')

   asyncio.run(main())
   ```

   Here, `await asyncio.sleep(2)` pauses `main()` for 2 seconds.

### 6. **Future**
   - A **Future** represents a result that is initially unknown but will be available at some point in the future.
   - You generally don't create Future objects directly; instead, they're used internally by tasks and coroutines.

### 7. **Async I/O Bound Operations**
   - `asyncio` excels in I/O-bound tasks where you spend a lot of time waiting for external resources (like network data, files, etc.).
   - Example: fetching data from the internet using `aiohttp`.

   ```python
   import aiohttp

   async def fetch_data(url):
       async with aiohttp.ClientSession() as session:
           async with session.get(url) as response:
               return await response.text()

   asyncio.run(fetch_data('https://example.com'))
   ```

### Important words:
- **`async`/`await`**: Key syntax for writing asynchronous code.
- **Event loop**: Manages and runs asynchronous tasks.
- **Coroutines**: Functions that can be paused and resumed.
- **Tasks**: Concurrently executed coroutines.
- **Await**: Pauses coroutine execution until the awaited task is complete.

`asyncio` allows you to write highly concurrent programs in Python with relative ease, making it a powerful tool for handling I/O-bound and event-driven programming tasks.

## 0. The basics of async
Write an asynchronous coroutine that takes in an integer argument (`max_delay`, with a default value of 10) named `wait_random` that waits for a random delay between 0 and `max_delay` (included and float value) seconds and eventually returns it.

Use the `random` module.
```
bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))

bob@dylan:~$ ./0-main.py
9.034261504534394
1.6216525464615306
10.634589756751769
```

## 1. Let's execute multiple coroutines at the same time with async
Import `wait_random` from the previous python file that you’ve written and write an async routine called `wait_n` that takes in 2 int arguments (in this order): `n` and `max_delay`. You will spawn `wait_random` `n` times with the specified max_delay.

`wait_n` should return the list of all the delays (float values). The list of the delays should be in ascending order without using `sort()` because of concurrency.
```
bob@dylan:~$ cat 1-main.py
#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n

print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))

bob@dylan:~$ ./1-main.py
[0.9693881173832269, 1.0264573845731002, 1.7992690129519855, 3.641373003434587, 4.500011569340617]
[0.07256214141415429, 1.518551245602588, 3.355762808432721, 3.7032593997182923, 3.7796178143655546, 4.744537840582318, 5.50781365463315, 5.758942587637626, 6.109707751654879, 6.831351588271327]
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
```
The output for your answers might look a little different and that’s okay.

## 2. Measure the runtime
From the previous file, import `wait_n` into `2-measure_runtime.py`.

Create a `measure_time` function with integers `n` and `max_delay` as arguments that measures the total execution time for `wait_n(n, max_delay)`, and returns `total_time / n`. Your function should return a float.

Use the `time` module to measure an approximate elapsed time.
```
bob@dylan:~$ cat 2-main.py
#!/usr/bin/env python3

measure_time = __import__('2-measure_runtime').measure_time

n = 5
max_delay = 9

print(measure_time(n, max_delay))

bob@dylan:~$ ./2-main.py
1.759705400466919
```

## 3. Tasks
Import `wait_random` from `0-basic_async_syntax`.

Write a function (do not create an async function, use the regular function syntax to do this) `task_wait_random` that takes an integer `max_delay` and returns a `asyncio.Task`.
```
bob@dylan:~$ cat 3-main.py
#!/usr/bin/env python3

import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def test(max_delay: int) -> float:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))

bob@dylan:~$ ./3-main.py
<class '_asyncio.Task'>
```

## 4. Tasks
Take the code from `wait_n` and alter it into a new function `task_wait_n`. The code is nearly identical to `wait_n` except `task_wait_random` is being called.
```
bob@dylan:~$ cat 4-main.py
#!/usr/bin/env python3

import asyncio

task_wait_n = __import__('4-tasks').task_wait_n

n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))

bob@dylan:~$ ./4-main.py
[0.2261658205652346, 1.1942770588220557, 1.8410422186086628, 2.1457353803430523, 4.002505454641153]
```
