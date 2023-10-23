import time
import requests
import asyncio

x = []
def num(x):
    time.sleep(1)
fist_time = time.time()
for i in range(100):
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    x.append(r)
second_time = time.time()
dif_time = second_time-fist_time
print(f"Время выполнения кода при запуске: {dif_time}")


start_time = time.time()
async def num():
    await asyncio.sleep(2)
    print("Прошло 2 секунды!")

if __name__ == '__main__':
     asyncio.run(num())
end_time =time.time()
diff_time = end_time-start_time
print(f"Время выполнения кода при запуске: {diff_time}")