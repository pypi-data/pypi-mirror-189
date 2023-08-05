from ape import plugins
from ape.api.networks import LOCAL_NETWORK_NAME, NetworkAPI, create_network_type
from ape.types import AddressType

from ape_starknet.accounts import StarknetAccountContainer, StarknetKeyfileAccount
from ape_starknet.config import StarknetConfig
from ape_starknet.conversion import StarknetAccountConverter, StarknetAddressConverter
from ape_starknet.ecosystems import Starknet
from ape_starknet.explorer import StarknetExplorer
from ape_starknet.provider import StarknetDevnetProvider, StarknetProvider
from ape_starknet.tokens import tokens
from ape_starknet.utils import NETWORKS, PLUGIN_NAME

network_names = [LOCAL_NETWORK_NAME] + list(NETWORKS.keys())


@plugins.register(plugins.ConversionPlugin)
def converters():
    yield AddressType, StarknetAddressConverter
    yield int, StarknetAccountConverter


@plugins.register(plugins.Config)
def config_class():
    return StarknetConfig


@plugins.register(plugins.EcosystemPlugin)
def ecosystems():
    yield Starknet


@plugins.register(plugins.NetworkPlugin)
def networks():
    for network_name, network_params in NETWORKS.items():
        yield PLUGIN_NAME, network_name, create_network_type(*network_params)

    # NOTE: This works for development providers, as they get chain_id from themselves
    yield PLUGIN_NAME, LOCAL_NETWORK_NAME, NetworkAPI


@plugins.register(plugins.ProviderPlugin)
def providers():
    for network_name in list(NETWORKS.keys()):
        yield PLUGIN_NAME, network_name, StarknetProvider

    yield PLUGIN_NAME, LOCAL_NETWORK_NAME, StarknetDevnetProvider


@plugins.register(plugins.AccountPlugin)
def account_types():
    return StarknetAccountContainer, StarknetKeyfileAccount


@plugins.register(plugins.ExplorerPlugin)
def explorers():
    for network_name in network_names:
        yield PLUGIN_NAME, network_name, StarknetExplorer


__all__ = [
    "tokens",
]
