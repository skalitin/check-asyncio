import asyncio

def log(func):
    print("just returning it")
    if asyncio.iscoroutinefunction(func):
        async def log_func(*x,**k):
            try:
                print("calling coroutine ...")
                return await func(*x,**k)
            except Exception:
                print("Ups! Got an error")
    else:
        def log_func(*x, **k):
            try:
                print("calling function...")
                return func(*x, **k)
            except Exception:
                print("Ups! Got an error")
    return log_func

@log
def sum(x,y):
    raise Exception("Wow!")
    return x + y

@log
async def error():

    print("I am here!")
    raise Exception("it is an error")

async def check():
    await error()

def run_check():

    loop = asyncio.new_event_loop()
    loop.run_until_complete(check())

    loop.close()

def main():

    sum(2,5) # exception is caught
    run_check() # exception is not caught

if __name__ == '__main__':
    main()