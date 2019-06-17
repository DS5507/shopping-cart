# shopping-cart

[Project Description](https://github.com/prof-rossetti/nyu-info-2335-201905/blob/master/projects/shopping-cart/README.md)

## Installation
Clone or download from [GitHub source](https://github.com/DS5507/shopping-cart), then navigate into the project repo.

```sh
cd ~\shopping-cart
```

## App Credentials
Create a copy of ".env.example" and rename it ".env".  Insert sendgrid API key and Email address into the template and save.

## Create Virtual Environment
```sh
conda create -n shopping-env #first time only
conda activate shopping-env
```

## Install Requirements
```sh
pip install python-dotenv
pip install sendgrid==5.6.0
```

## Usage
Run the program:
```sh
python shopping_cart.py
```