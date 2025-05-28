from web3 import Web3
import json

RPC_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"

wallets = [
    # Masukkan alamat wallet yang ingin dipantau
    "0xWalletAddress1",
    "0xWalletAddress2",
    # ...
]

def get_eth_balance(web3, address):
    return web3.fromWei(web3.eth.get_balance(address), 'ether')

def main():
    web3 = Web3(Web3.HTTPProvider(RPC_URL))
    if not web3.isConnected():
        print("❌ Gagal koneksi ke node")
        return

    for w in wallets:
        try:
            balance = get_eth_balance(web3, w)
            print(f"Wallet {w} saldo ETH: {balance} ETH")
            # Bisa ditambah fitur histori transaksi via API (Etherscan dll) nanti
        except Exception as e:
            print(f"Gagal cek wallet {w}: {e}")

if __name__ == "__main__":
    main()
