import pytest

all_tokens = pytest.mark.parametrize(
    "token",
    (
        "eth",
        "test_token",
        # "proxy_token",  # TODO: Fix local proxies
    ),
)


@pytest.fixture(scope="module", autouse=True)
def ensure_token_deployed(token_contract):
    _ = token_contract


@all_tokens
def test_get_balance(tokens, account, token_initial_supply, token):
    if token == "eth":
        # Likely spent fees
        assert tokens.get_balance(account)
    else:
        assert tokens.get_balance(account, token=token) == token_initial_supply


@all_tokens
def test_transfer(tokens, account, second_account, token):
    initial_balance = tokens.get_balance(second_account.address, token=token)
    tokens.transfer(account.address, second_account.address, 10, token=token)
    actual = tokens.get_balance(second_account.address, token=token)
    expected = initial_balance + 10
    assert actual == expected


@all_tokens
def test_transfer_providing_a_struct(tokens, account, second_account, token):
    amount = {"low": 10, "high": 0}  # == Uint256(10, 0) == 10
    initial_balance = tokens.get_balance(second_account, token=token)
    tokens.transfer(account, second_account, amount, token=token)
    assert tokens.get_balance(second_account, token=token) == initial_balance + 10


def test_large_transfer(tokens, account, second_account):
    initial_balance = tokens.get_balance(second_account.address, token="test_token")

    # Value large enough to properly test Uint256 logic
    balance_to_transfer = 2**128 + 1
    tokens.transfer(
        account.address, second_account.address, balance_to_transfer, token="test_token"
    )
    actual = tokens.get_balance(second_account.address, token="test_token")
    expected = initial_balance + balance_to_transfer
    assert actual == expected


@all_tokens
def test_is_token(tokens, token):
    # Ensure it's recognized as a token
    assert tokens.is_token(tokens[token])


def test_is_not_token(contract, tokens):
    assert not tokens.is_token(contract.address)
