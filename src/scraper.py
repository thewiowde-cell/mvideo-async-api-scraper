import json
import random
import asyncio
import aiohttp
import aiofiles
from pathlib import Path
from config import api_url, headers, cookies, json_data


async def collect_data(session):
    folder = Path(__file__).resolve().parent.parent

    (folder / 'data').mkdir(parents=True, exist_ok=True)

    json_path = folder / 'data' / 'products.json'

    limit = json_data['limit']
    cursorId = 0
    products_list = []
    while True:
        if cursorId == 180:
            break

        json_data['cursorId'] = str(cursorId)

        await asyncio.sleep(random.uniform(2, 5))
        async with session.post(url=api_url, headers=headers, cookies=cookies, json=json_data) as response:
            if response.status != 200:
                print(f"Request error. Status code: {response.status}")
                break

            data = await response.json()

        products = data.get('body', {}).get('items', [])

        if not products:
            break

        for product in products:
            name = product.get('name', 'no name')
            slug = product.get('slug', '')
            url = f"https://www.mvideo.ru{slug}" if slug else 'no link'
            price_key = product.get('price')
            discount_price = price_key.get(
                'salePrice') if price_key else 'no discount price'
            old_price = price_key.get(
                'basePrice') if price_key else 'no price'
            discount = f"{price_key.get('discount')} %" if price_key else 'no discount'

            products_list.append(
                {
                    "name product": name,
                    "product link": url,
                    "discount price": discount_price,
                    "old price": old_price,
                    "discount": discount,
                }
            )

        if len(products) < limit:
            break

        cursorId += limit
        await asyncio.sleep(random.uniform(2, 5))

    if products_list:
        async with aiofiles.open(json_path, 'w', encoding='utf-8') as file:
            json_string = json.dumps(
                products_list, indent=4, ensure_ascii=False)
            await file.write(json_string)


async def main():
    async with aiohttp.ClientSession() as session:
        await collect_data(session=session)

if __name__ == '__main__':
    asyncio.run(main())
