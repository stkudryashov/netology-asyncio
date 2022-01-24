import asyncio
import aiosqlite

import os

from aiosmtplib import SMTP
from email.message import EmailMessage


EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')


async def send_message(email_to: str):
    message = EmailMessage()
    message["From"] = EMAIL
    message["To"] = email_to
    message["Subject"] = "Благодарность за использование!"

    smtp_client = SMTP('smtp.gmail.com', 587)

    await smtp_client.connect()
    await smtp_client.starttls()
    await smtp_client.login(EMAIL, PASSWORD)

    content = f'Уважаемый {email_to}!\nСпасибо, что пользуетесь нашим сервисом объявлений!'
    message.set_content(content)

    await smtp_client.sendmail(EMAIL, email_to, message.as_string())


async def start_mailing():
    db = await aiosqlite.connect('contacts.db')
    cursor = await db.execute('SELECT email FROM contacts')
    rows = await cursor.fetchall()

    tasks = []

    for email in rows:
        task = asyncio.create_task(send_message(email[0]))
        tasks.append(task)

    await asyncio.gather(*tasks)
    await cursor.close()
    await db.close()
