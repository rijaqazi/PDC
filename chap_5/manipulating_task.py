import asyncio

async def factorial(number):
    f = 1
    for i in range(2, number + 1):
        print("Asyncio.Task: Compute factorial(%s)" % (i))
        await asyncio.sleep(1)  # Use await for asynchronous operations
        f *= i
    print("Asyncio.Task - factorial(%s) = %s" % (number, f))

async def fibonacci(number):  # Define the fibonacci function
    a, b = 0, 1
    for i in range(number):
        print("Asyncio.Task: Compute fibonacci (%s)" % (i))
        await asyncio.sleep(1)
        a, b = b, a + b
    print("Asyncio.Task - fibonacci(%s) = %s" % (number, a))

# ... (optional) define binomial_coefficient if needed

if __name__ == '__main__':
    loop = asyncio.get_event_loop()  # Get the event loop
    task_list = [
        loop.create_task(factorial(10)),
        loop.create_task(fibonacci(10)),
        # loop.create_task(binomial_coefficient(20, 10))  # Add if needed
    ]
    loop.run_until_complete(asyncio.wait(task_list))  # Run tasks in the loop
    loop.close()