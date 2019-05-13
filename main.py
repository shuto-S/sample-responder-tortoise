import responder
from tortoise import Tortoise

from router import add_routers

api = responder.API()


@api.on_event("startup")
async def start_db_connection():
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",
        modules={"models": ["models"]}
    )


@api.on_event("shutdown")
async def close_db_connection():
    await Tortoise.close_connections()


add_routers(api)


if __name__ == '__main__':
    api.run(debug=True)
