import argparse
from bot.orders import place_order
from bot.validators import validate_side, validate_order

parser = argparse.ArgumentParser(
    description="Binance Futures Testnet Trading Bot"
)

parser.add_argument(
    "--symbol",
    required=True,
    help="Trading pair (e.g., BTCUSDT)"
)

parser.add_argument(
    "--side",
    required=True,
    help="BUY or SELL"
)

parser.add_argument(
    "--type",
    required=True,
    help="MARKET or LIMIT"
)

parser.add_argument(
    "--quantity",
    required=True,
    type=float,
    help="Order quantity"
)

parser.add_argument(
    "--price",
    type=float,
    help="Limit price (required for LIMIT orders)"
)

args = parser.parse_args()

try:
    side = validate_side(args.side)
    order_type = validate_order(args.type)

    if args.quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")

    if order_type == "LIMIT":
        if args.price is None:
            raise ValueError("Price is required for LIMIT orders.")
        if args.price <= 0:
            raise ValueError("Price must be greater than 0.")

    print("\n" + "=" * 40)
    print("        ORDER SUMMARY")
    print("=" * 40)

    print(f"Symbol      : {args.symbol.upper()}")
    print(f"Side        : {side}")
    print(f"Order Type  : {order_type}")
    print(f"Quantity    : {args.quantity}")

    if args.price:
        print(f"Price       : {args.price}")

    print("=" * 40)

    print("\nPlacing order...\n")

    response = place_order(
        symbol=args.symbol.upper(),
        side=side,
        order_type=order_type,
        quantity=args.quantity,
        price=args.price
    )

    print("=" * 40)
    print("       ORDER RESPONSE")
    print("=" * 40)

    print(f"Order ID      : {response.get('orderId')}")
    print(f"Status        : {response.get('status')}")
    print(f"Executed Qty  : {response.get('executedQty')}")
    print(f"Average Price : {response.get('avgPrice', 'N/A')}")

    print("\n✅ Order placed successfully!")

except Exception as e:
    print("\n❌ Order Failed")
    print(f"Reason: {e}")