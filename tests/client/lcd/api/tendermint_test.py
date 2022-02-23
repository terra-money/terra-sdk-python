from terra_sdk.client.lcd import LCDClient

terra = LCDClient(
    url="https://bombay-lcd.terra.dev/",
    chain_id="bombay-12",
)


def test_validator_set():
    result = terra.tendermint.validator_set()
    print(result)


def test_validator_set_with_height():
    result = terra.tendermint.validator_set(6740000)
    print(result)


def test_node_info():
    result = terra.tendermint.node_info()
    print(result)


def test_block_info():
    result = terra.tendermint.block_info()
    print(result)


def test_block_info_with_height():
    result = terra.tendermint.block_info(6740000)
    print(result)


def test_syncing():
    result = terra.tendermint.syncing()
    print(result)
