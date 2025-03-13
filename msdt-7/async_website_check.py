import asyncio
import aiohttp  # Используем aiohttp для асинхронных HTTP-запросов

# Асинхронно проверяет статус веб-сайта
async def check_website_status(session, url):
    try:
        async with session.get(url) as response:
            status = response.status
            print(f"Сайт {url}: Статус {status}")
            return url, status
    except aiohttp.ClientError as e:
        print(f"Ошибка при подключении к {url}: {e}")
        return url, None  # Или какой-то другой индикатор ошибки

# Собирает и запускает задачи для проверки статуса сайтов
async def main():

    urls = [
        "https://www.google.com",
        "https://ssau.ru",
        "https://vk.com",
        "https://nonexistent-website.com",  # Пример сайта, который не существует
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [check_website_status(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

    print("\nРезультаты проверки:")
    for url, status in results:
        print(f"{url}: {status}")

if __name__ == "__main__":
    asyncio.run(main())
