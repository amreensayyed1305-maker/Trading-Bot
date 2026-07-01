def validate_side(side):
    side = side.upper()

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    return side


def validate_order(order_type):
    order_type = order_type.upper()

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Invalid order type")

    return order_type