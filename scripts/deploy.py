from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def deploy_fund_me():
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config(
            ["networks"][network.show_active()]["eth_usd_price_feed"]
        )

    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"]["development"].get("verify"),
    )
    print(
        f"Contract deployed to {fund_me.address} on the {network.show_active()} network"
    )
    return fund_me


def main():
    deploy_fund_me()
