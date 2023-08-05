# bacalhau_apiclient.HealthApi

All URIs are relative to *http://bootstrap.production.bacalhau.org:1234*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_serverdebug**](HealthApi.md#api_serverdebug) | **GET** /debug | Returns debug information on what the current node is doing.
[**pkgrequesterdebug**](HealthApi.md#pkgrequesterdebug) | **GET** /requester/debug | Returns debug information on what the current node is doing.


# **api_serverdebug**
> str api_serverdebug()

Returns debug information on what the current node is doing.

### Example
```python
from __future__ import print_function
import time
import bacalhau_apiclient
from bacalhau_apiclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = bacalhau_apiclient.HealthApi()

try:
    # Returns debug information on what the current node is doing.
    api_response = api_instance.api_serverdebug()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthApi->api_serverdebug: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pkgrequesterdebug**
> str pkgrequesterdebug()

Returns debug information on what the current node is doing.

### Example
```python
from __future__ import print_function
import time
import bacalhau_apiclient
from bacalhau_apiclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = bacalhau_apiclient.HealthApi()

try:
    # Returns debug information on what the current node is doing.
    api_response = api_instance.pkgrequesterdebug()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthApi->pkgrequesterdebug: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

