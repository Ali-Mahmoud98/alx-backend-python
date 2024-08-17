#!/usr/bin/env python3
import time
import asyncio

async def perform_task(name, delay):
    await asyncio.sleep(delay)
    print(f"Task {name} completed with delay {delay}")

async def main(): # will take 3 seconds
    start_time = time.time()  # Record the start time
    tasks = [
        asyncio.create_task(perform_task("A", 2)),
        asyncio.create_task(perform_task("B", 1)),
        asyncio.create_task(perform_task("C", 3)),
    ]
    
    print("All tasks started.")
    
    await asyncio.gather(*tasks)
    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time    
    print(f"All tasks completed in {elapsed_time:.2f} seconds.")

async def main2(): # will take 6 seconds
    start_time = time.time()  # Record the start time
    await perform_task("A", 2)
    await perform_task("B", 1)
    await perform_task("C", 3)
    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time    
    print(f"All tasks completed in {elapsed_time:.2f} seconds.")

async def main3(): # will take 3 seconds
    # this is same as `main`
    start_time = time.time()  # Record the start time
    await asyncio.gather(perform_task("A", 2), perform_task("B", 1), perform_task("C", 3))
    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time    
    print(f"All tasks completed in {elapsed_time:.2f} seconds.")

asyncio.run(main())
print("start main2")
asyncio.run(main2())
print("start main3")
asyncio.run(main3())
