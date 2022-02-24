from terra_sdk.core.slashing.msgs import MsgUnjail


def test_deserializes_msg_unjail_examples(load_msg_examples):
    examples = load_msg_examples(MsgUnjail.type_url, "./MsgUnjail.data.json")
    for example in examples:
        assert MsgUnjail.from_data(example).to_data() == example
