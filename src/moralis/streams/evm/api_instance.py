import openapi_streams
from openapi_streams.apis.tags import evm_api
from ..utilities import get_common_headers


def get_api_instance(api_key):
    configuration = openapi_streams.Configuration()
    configuration.api_key['x-api-key'] = api_key
    api_client = openapi_streams.ApiClient(configuration)
    headers = get_common_headers()
    for header in headers:
        api_client.default_headers[header] = headers[header]
    api_instance = evm_api.EvmApi(api_client)
    api_client.close()

    return api_instance

