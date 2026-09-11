"""
Stock Portfolio Tracker
------------------------
Calculates total investment value based on manually entered stock
quantities and a hardcoded price dictionary. Optionally saves the
result to a .txt or .csv file.
"""

import csv

# Hardcoded stock prices (per share)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 145,
    "NFLX": 600,
}


def get_portfolio():
    """Ask the user for stock names and quantities, return as a dict."""
    portfolio = {}

    print("Available stocks and prices:")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: ${price}")
    print()

    while True:
        symbol = input("Enter stock symbol (or 'done' to finish): ").upper().strip()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"'{symbol}' is not in the price list. Try again.\n")
            continue

        qty_input = input(f"Enter quantity of {symbol}: ").strip()
        try:
            quantity = int(qty_input)
            if quantity <= 0:
                print("Quantity must be a positive number.\n")
                continue
        except ValueError:
            print("Please enter a valid whole number.\n")
            continue

        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        print(f"Added {quantity} share(s) of {symbol}.\n")

    return portfolio


def calculate_total(portfolio):
    """Return total investment value and a per-stock breakdown list."""
    breakdown = []
    total = 0

    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        total += value
        breakdown.append((symbol, quantity, price, value))

    return total, breakdown


def display_summary(breakdown, total):
    """Print a formatted summary of the portfolio."""
    print("\n" + "=" * 40)
    print("PORTFOLIO SUMMARY")
    print("=" * 40)
    print(f"{'Symbol':<10}{'Qty':<8}{'Price':<10}{'Value':<10}")
    print("-" * 40)

    for symbol, quantity, price, value in breakdown:
        print(f"{symbol:<10}{quantity:<8}${price:<9}${value:<9}")

    print("-" * 40)
    print(f"Total Investment: ${total}")
    print("=" * 40)


def save_to_txt(breakdown, total, filename="portfolio.txt"):
    """Save the portfolio summary to a .txt file."""
    with open(filename, "w") as f:
        f.write("PORTFOLIO SUMMARY\n")
        f.write("=" * 40 + "\n")
        f.write(f"{'Symbol':<10}{'Qty':<8}{'Price':<10}{'Value':<10}\n")
        f.write("-" * 40 + "\n")
        for symbol, quantity, price, value in breakdown:
            f.write(f"{symbol:<10}{quantity:<8}${price:<9}${value:<9}\n")
        f.write("-" * 40 + "\n")
        f.write(f"Total Investment: ${total}\n")
    print(f"Saved summary to {filename}")


def save_to_csv(breakdown, total, filename="portfolio.csv"):
    """Save the portfolio summary to a .csv file."""
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Symbol", "Quantity", "Price", "Value"])
        for symbol, quantity, price, value in breakdown:
            writer.writerow([symbol, quantity, price, value])
        writer.writerow([])
        writer.writerow(["Total Investment", "", "", total])
    print(f"Saved summary to {filename}")


def main():
    print("Welcome to the Stock Portfolio Tracker!\n")

    portfolio = get_portfolio()

    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    total, breakdown = calculate_total(portfolio)
    display_summary(breakdown, total)

    choice = input(
        "\nSave results? Enter 'txt', 'csv', or press Enter to skip: "
    ).lower().strip()

    if choice == "txt":
        save_to_txt(breakdown, total)
    elif choice == "csv":
        save_to_csv(breakdown, total)
    else:
        print("Results not saved.")


if __name__ == "__main__":
    main()