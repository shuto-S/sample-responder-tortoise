from models import User


class Account:
    async def on_get(self, req, resp):
        # await User.create(name="Test User")
        user = await User.first()
        resp.text = f"Hello, {user.name}"
