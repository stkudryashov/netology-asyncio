import asyncio

from datetime import datetime
from mailing import start_mailing


if __name__ == '__main__':
    time_start = datetime.now()
    asyncio.run(start_mailing())
    time_end = datetime.now()

    print(f'Выполнено за {time_end - time_start}')
