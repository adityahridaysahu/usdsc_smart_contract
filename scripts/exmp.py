from brownie import config


def main():
    print(config(["networks"]))
