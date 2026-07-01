from bot.client import client
from bot.logging_config import logger

def place_order(
    symbol,
    side,
    order_type,
    quantity,
    price=None
):

    try:

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        logger.info(f"Request: {params}")

        response = client.futures_create_order(**params)

        logger.info(f"Response: {response}")

        return response

    except Exception as e:

        logger.error(str(e))
        raise