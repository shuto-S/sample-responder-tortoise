from tortoise import Tortoise, run_async


async def migrate():
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",
        modules={"models": ["models"]}
    )
    await Tortoise.generate_schemas()

    print("Success migration!!")


run_async(migrate())
