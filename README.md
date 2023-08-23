# Overview

This repo allows you to bridge USDT from BSC to Harmony using Harmony Bridge from LayerZero for multiple wallets.

# Instructions

1. Make sure to have python, pip and git installed.

2. Clone this repo:
```sh
git clone https://github.com/VolodymyrVozniak/layer0-harmony-bridge.git
```

3. Go to a directory:
```sh
cd layer0-harmony-bridge
```

4. Add your private keys to `data/wallets.txt` (paste private keys, each from the new line, press Ctrl+O, Enter and Ctrl+X):
```sh
nano data/wallets.txt
```

5. Create virtual environment (can skip this step):
```sh
python -m venv env
```

6. Activate virtual environment (must run every time you connect to a server):
```sh
source env/bin/activate
```

7. Install python requirements (install only once):
```sh
pip install -r requirements.txt
```

8. Run the script to use Aptos Bridge:
```sh
python main.py
```

9. You can modify the following parameters in `main.py`:
    * `SLEEP_FROM`: The lowest value to sleep between wallets in seconds;
    * `SLEEP_TO`: The highest value to sleep between wallets in seconds;
    * `AMOUNT_FROM`: The lowest value to bridge in USDT;
    * `AMOUNT_TO`: The highest value to bridge in USDT;
    * `RANDOM_WALLETS`: Rather to shuffle wallets;
    * `WALLETS_PATH`: Path for file with private keys (each private key from new line).

-----

</br>
</br>

This repo was created for "STD" group.

Donation: `0x34Ec371BA620e6C67A115a6794D44FED038Cc78C`
