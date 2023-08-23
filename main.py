"""Bridge USDT from BSC to Harmony using Harmony Bridge"""

import random

from src import harmony_bridge, sleeping


# In seconds
SLEEP_FROM = 100
SLEEP_TO   = 200

# All values in USDT
AMOUNT_FROM = 0.1
AMOUNT_TO   = 0.3

RANDOM_WALLETS = True  # Shuffle wallets
WALLETS_PATH   = "data/wallets.txt"  # Path for file with private keys


if __name__ == "__main__":
    with open(WALLETS_PATH, "r") as f:
        wallets = [row.strip() for row in f]

    if RANDOM_WALLETS:
        random.shuffle(wallets)

    for i, wallet in enumerate(wallets):
        harmony_bridge(
            name=str(i),
            private_key=wallet,
            from_chain="BSC",
            amount=random.uniform(AMOUNT_FROM, AMOUNT_TO),
            max_gas=0.0014,   # ~0.3$ for BSC fees
            max_value=0.0046  # ~1.1$ for Layer0 fees
        )

        sleeping(SLEEP_FROM, SLEEP_TO)
