import platform
import sys
import asyncio
import aiohttp
import datetime

class ExchangeRateService:
    API_URL = 'https://api.privatbank.ua/p24api/exchange_rates?json&date={date}'
    CURRENCY_CODES = ['USD', 'EUR']

    async def get_exchange_rates(self, days):
        days = min(days, 10)
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_exchange_rate(session, days_ago) for days_ago in range(1, days + 1)]
            results = await asyncio.gather(*tasks)
            return results

    async def fetch_exchange_rate(self, session, days_ago):
        date = datetime.date.today() - datetime.timedelta(days=days_ago)
        date_str = date.strftime('%d.%m.%Y')
        url = self.API_URL.format(date=date_str)
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                exchange_rates = data.get('exchangeRate', [])
                exchange_rate = {}
                for currency_code in self.CURRENCY_CODES:
                    rate = self.find_exchange_rate(exchange_rates, currency_code)
                    result = await rate
                    exchange_rate[currency_code] = result
                exchange_rate['date'] = date_str
                return exchange_rate
            else:
                return {'date': date_str, 'error': 'Failed to fetch exchange rate'}

    async def find_exchange_rate(self, exchange_rates, currency_code):
        for rate in exchange_rates:
            if rate.get('currency') == currency_code:
                return rate.get('saleRateNB')
        # Return None if the exchange rate for the currency was not found
        return None

async def main():
    try:
        days = int(sys.argv[1])
    except (ValueError, IndexError):
        print("Please provide a valid integer argument for the number of days to retrieve exchange rates for")
        return
    exchange_rate_service = ExchangeRateService()
    exchange_rates = await exchange_rate_service.get_exchange_rates(days)
    for exchange_rate in exchange_rates:
        # Check if the exchange rate is not None before printing it
        usd_rate = exchange_rate.get('USD')
        eur_rate = exchange_rate.get('EUR')
        if usd_rate is not None and eur_rate is not None:
            print(f"{exchange_rate['date']}: USD={usd_rate}, EUR={eur_rate}")
        else:
            print(f"{exchange_rate['date']}: exchange rate not found")

if __name__ == '__main__':
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())





