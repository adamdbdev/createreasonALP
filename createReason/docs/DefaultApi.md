# swagger_client.DefaultApi

All URIs are relative to *https://apim-nd.azure-api.net/calculator*

Method | HTTP request | Description
------------- | ------------- | -------------
[**5b5b2152dfc9bc0c2ce743a7**](DefaultApi.md#5b5b2152dfc9bc0c2ce743a7) | **GET** /add | Add two integers
[**5b5b2152dfc9bc0c2ce743a8**](DefaultApi.md#5b5b2152dfc9bc0c2ce743a8) | **GET** /sub | Subtract two integers
[**5b5b2152dfc9bc0c2ce743a9**](DefaultApi.md#5b5b2152dfc9bc0c2ce743a9) | **GET** /mul | Multiply two integers
[**5b5b2152dfc9bc0c2ce743aa**](DefaultApi.md#5b5b2152dfc9bc0c2ce743aa) | **GET** /div | Divide two integers


# **5b5b2152dfc9bc0c2ce743a7**
> 5b5b2152dfc9bc0c2ce743a7(a, b)

Add two integers

Produces a sum of two numbers.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
a = '51' # str | First operand. Default value is <code>51</code>. (default to 51)
b = '49' # str | Second operand. Default value is <code>49</code>. (default to 49)

try:
    # Add two integers
    api_instance.5b5b2152dfc9bc0c2ce743a7(a, b)
except ApiException as e:
    print("Exception when calling DefaultApi->5b5b2152dfc9bc0c2ce743a7: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **a** | **str**| First operand. Default value is &lt;code&gt;51&lt;/code&gt;. | [default to 51]
 **b** | **str**| Second operand. Default value is &lt;code&gt;49&lt;/code&gt;. | [default to 49]

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **5b5b2152dfc9bc0c2ce743a8**
> 5b5b2152dfc9bc0c2ce743a8(a, b)

Subtract two integers

Produces a difference between two numbers.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
a = '51' # str | First operand. Default value is <code>51</code>. (default to 51)
b = '49' # str | Second operand. Default value is <code>49</code>. (default to 49)

try:
    # Subtract two integers
    api_instance.5b5b2152dfc9bc0c2ce743a8(a, b)
except ApiException as e:
    print("Exception when calling DefaultApi->5b5b2152dfc9bc0c2ce743a8: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **a** | **str**| First operand. Default value is &lt;code&gt;51&lt;/code&gt;. | [default to 51]
 **b** | **str**| Second operand. Default value is &lt;code&gt;49&lt;/code&gt;. | [default to 49]

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **5b5b2152dfc9bc0c2ce743a9**
> 5b5b2152dfc9bc0c2ce743a9(a, b)

Multiply two integers

Produces a product of two numbers.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
a = '51' # str | First operand. Default value is <code>51</code>. (default to 51)
b = '49' # str | Second operand. Default value is <code>49</code>. (default to 49)

try:
    # Multiply two integers
    api_instance.5b5b2152dfc9bc0c2ce743a9(a, b)
except ApiException as e:
    print("Exception when calling DefaultApi->5b5b2152dfc9bc0c2ce743a9: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **a** | **str**| First operand. Default value is &lt;code&gt;51&lt;/code&gt;. | [default to 51]
 **b** | **str**| Second operand. Default value is &lt;code&gt;49&lt;/code&gt;. | [default to 49]

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **5b5b2152dfc9bc0c2ce743aa**
> 5b5b2152dfc9bc0c2ce743aa(a, b)

Divide two integers

Produces a quotient of two numbers.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
a = '51' # str | First operand. Default value is <code>51</code>. (default to 51)
b = '49' # str | Second operand. Default value is <code>49</code>. (default to 49)

try:
    # Divide two integers
    api_instance.5b5b2152dfc9bc0c2ce743aa(a, b)
except ApiException as e:
    print("Exception when calling DefaultApi->5b5b2152dfc9bc0c2ce743aa: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **a** | **str**| First operand. Default value is &lt;code&gt;51&lt;/code&gt;. | [default to 51]
 **b** | **str**| Second operand. Default value is &lt;code&gt;49&lt;/code&gt;. | [default to 49]

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

