from loguru import logger
from tortoise import Tortoise, run_async
import asyncio
from dataclasses import dataclass
from aiohttp import ClientSession
import models


async def init():
    # Here we create connection to PostgresQL database
    #  also specify the app name of "models"
    #  which contain models from "models"
    await Tortoise.init(
        db_url='sqlite://db.sqlite1',
        modules={'models': ['models']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()


@dataclass
class Service:
    name: str
    url: str


SERVICE = [
    Service("users", "https://jsonplaceholder.typicode.com/users"),
    Service("posts", "https://jsonplaceholder.typicode.com/posts"),
    Service("todos", "https://jsonplaceholder.typicode.com/todos"),
]


async def fetch(session: ClientSession, url: str) -> dict:
    """
    :param session:
    :param url:
    :return:
    """
    async with session.get(url) as response:
        return await response.json()


async def fetch_url(service: Service) -> tuple:
    """
    :param source:
    :return:
    """
    async with ClientSession() as session:
        result = await fetch(session, service.url)
    logger.info("Добавлено {} данных {} ", len(result), service.url)
    return service.name, result


async def get_users():
    await init()
    coros = [fetch_url(s) for s in SERVICE]
    done, pending = await asyncio.wait(
        coros,
        timeout=5,
        return_when=asyncio.ALL_COMPLETED,
    )

    db_user = await db_write(done, name='users', adding_func=user_add)
    logger.info("Добавлен users")
    db_post = await db_write(done, name='posts', adding_func=post_add)
    logger.info("Добавлен posts")
    db_todos = await db_write(done, name='todos', adding_func=todos_add)
    logger.info('Добавлен todos')


async def db_write(done: set, name: str, adding_func):
    for s in done:
        if s.result()[0] == name:
            await adding_func(s.result()[1])



async def write_data():
    await init()
    welcome = []
    coros = [fetch_url(s) for s in SERVICE]
    welcome.append(coros)


async def user_add(S: list):
    for i in S:
        await models.User.create(
            id=i['id'],
            name=i['name'],
            email=i['email'],
        )


async def post_add(S: list):
    for i in S:
        await models.Post.create(
            id=i['id'],
            title=i['title'],
            body=i['body'],
        )


async def todos_add(S: list):
    for i in S:
        await models.Todos.create(
            id=i['id'],
            title=i['title'],
        )


if __name__ == '__main__':
    run_async(init())
    run_async(get_users())
    print("Великая асинхронщина в деле!")