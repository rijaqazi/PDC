import asyncio
import sys

async def first_coroutine(future, num):
    count = 0
    for i in range(1, num + 1):
        count += i
        await asyncio.sleep(1)
    future.set_result(f'First coroutine (sum of N integers) result = {count}')

async def second_coroutine(future, num):
    count = 1
    for i in range(2, num + 1):
        count *= i
        await asyncio.sleep(2)
    future.set_result(f'Second coroutine (factorial) result = {count}')

def got_result(future):
    print(future.result())

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python your_script.py <num1> <num2>")
        sys.exit(1)
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    loop = asyncio.get_event_loop()
    future1 = asyncio.Future()
    future2 = asyncio.Future()

    tasks = [
        loop.create_task(first_coroutine(future1, num1)),
        loop.create_task(second_coroutine(future2, num2))
    ]

    future1.add_done_callback(got_result)
    future2.add_done_callback(got_result)

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()