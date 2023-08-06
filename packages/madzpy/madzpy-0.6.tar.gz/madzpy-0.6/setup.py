from distutils.core import setup
from pathlib import Path

readme = Path(__file__).parent
readme = (readme / "README.md").read_text()

setup(
    name = "madzpy",
    packages = ["madzpy"],
    version = "0.6",
    license= "MIT",
    description = "Madzcoin RPC Client",
    long_description = readme,
    long_description_content_type = "text/markdown",
    author = "Bastel Pichi",
    author_email = "pichi@pichisdns.com",
    url = "https://github.com/MadzCoin/madz-py/",
    download_url = "https://github.com/MadzCoin/madz-py/archive/refs/heads/main.zip",
    keywords = ["Madzcoin", "Crypto", "RPC"],
    install_requires = [
        "web3",
        "eth-account",
        "requests"
    ],
)
