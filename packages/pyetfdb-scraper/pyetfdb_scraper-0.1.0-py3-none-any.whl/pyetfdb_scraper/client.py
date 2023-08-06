if __name__ == "__main__":
    import requests
    from pyetfdb_scraper.etf import ETF
    from bs4 import BeautifulSoup

    base_url: str = "https://etfdb.com/etf/"
    ticker: str = "VGLT"

    request_headers: dict = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0",
        "Accept": "application/json",
    }

    response: requests.Response = requests.get(
        f"{base_url}/{ticker}", headers=request_headers
    )

    if response.status_code == 200:
        soup: BeautifulSoup = BeautifulSoup(response.text)

    for ticker in ["IAU", "GLD", "VYM", "VTI", "VTV"]:
        etf = ETF(ticker)
        end_sep = "\n\n"

        print(etf.to_dict(), end=end_sep)
