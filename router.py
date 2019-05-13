import responder

from controllers.account import Account


def add_routers(api: responder.API):
    api.add_route("/accounts", Account)
