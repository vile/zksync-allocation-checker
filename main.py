import httpx
from httpx import Response
from typing import Final
from colorama import Fore, init
from os import name as os_name

WALLET_TXT_PATH: Final[str] = "./wallets.txt"
HTTPX_HEADERS: Final[dict[str, str]] = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "X-Api-Key": "46001d8f026d4a5bb85b33530120cd38",  # Public API key, not leaking anything
}


def main() -> None:
    init(
        convert=True if os_name == "nt" else False,
        autoreset=True,
    )

    wallets: list[str] = [wallet.strip() for wallet in load_wallets(WALLET_TXT_PATH)]
    print(wallets)
    get_allocations(wallets)


def load_wallets(path: str) -> list[str]:
    with open(path) as handle:
        wallets: list[str] = handle.read().split("\n")

    return wallets


def get_allocations(wallets: list[str]) -> None:
    total_airdrop_amount: int = 0

    for wallet in wallets:
        r: Response = httpx.get(
            f"https://api.zknation.io/eligibility?id={wallet}",
            headers=HTTPX_HEADERS,
        )

        if r.status_code != 200:
            print(
                f"{Fore.RED}There was an error reaching the zkSync API, is it offline? {r.status_code}, {r.reason_phrase}"
            )
            continue

        json: dict = r.json()

        if len(json["allocations"]) == 0:
            print(f"{Fore.YELLOW}This wallet doesn't have an airdrop :(")
            continue

        airdrop_amount: int = int(json["allocations"][0]["tokenAmount"]) / 1e18
        total_airdrop_amount += airdrop_amount
        print(f"{Fore.GREEN}{wallet}:{Fore.WHITE} {airdrop_amount}")

    print(f"{Fore.BLUE}Total Airdrop:{Fore.WHITE} {total_airdrop_amount}")


if __name__ == "__main__":
    main()
