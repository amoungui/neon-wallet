"""core"""


from typing import Any
from neon_wallet.wallet.coin_wallet import CoinWallet
from neon_wallet.wallet.e_wallet import EWallet

from neon_wallet.wallet.ether_wallet import EtherWallet


def wallet(symbol: str) -> Any:
    """Wallet"""

    # Condition multiple inheritance based on symbol
    if symbol == "ETH":
        return EtherWallet(symbol)
    elif symbol in ["BTC", "BCH", "LTC", "DASH", "ZEC", "BSV"]:
        return CoinWallet(symbol)
    elif symbol in ["EUR", "CFA", "USD", "YEN"]:
        return EWallet(symbol)