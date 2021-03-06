# coding: utf-8

"""
    Basic Calculator

    Arithmetics is just a call away!  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class DefaultApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def 5b5b2152dfc9bc0c2ce743a7(self, a, b, **kwargs):  # noqa: E501
        """Add two integers  # noqa: E501

        Produces a sum of two numbers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.5b5b2152dfc9bc0c2ce743a7(a, b, async=True)
        >>> result = thread.get()

        :param async bool
        :param str a: First operand. Default value is <code>51</code>. (required)
        :param str b: Second operand. Default value is <code>49</code>. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.5b5b2152dfc9bc0c2ce743a7_with_http_info(a, b, **kwargs)  # noqa: E501
        else:
            (data) = self.5b5b2152dfc9bc0c2ce743a7_with_http_info(a, b, **kwargs)  # noqa: E501
            return data

    def 5b5b2152dfc9bc0c2ce743a7_with_http_info(self, a, b, **kwargs):  # noqa: E501
        """Add two integers  # noqa: E501

        Produces a sum of two numbers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.5b5b2152dfc9bc0c2ce743a7_with_http_info(a, b, async=True)
        >>> result = thread.get()

        :param async bool
        :param str a: First operand. Default value is <code>51</code>. (required)
        :param str b: Second operand. Default value is <code>49</code>. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['a', 'b']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method 5b5b2152dfc9bc0c2ce743a7" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'a' is set
        if ('a' not in params or
                params['a'] is None):
            raise ValueError("Missing the required parameter `a` when calling `5b5b2152dfc9bc0c2ce743a7`")  # noqa: E501
        # verify the required parameter 'b' is set
        if ('b' not in params or
                params['b'] is None):
            raise ValueError("Missing the required parameter `b` when calling `5b5b2152dfc9bc0c2ce743a7`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'a' in params:
            query_params.append(('a', params['a']))  # noqa: E501
        if 'b' in params:
            query_params.append(('b', params['b']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apiKeyHeader', 'apiKeyQuery']  # noqa: E501

        return self.api_client.call_api(
            '/add', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def 5b5b2152dfc9bc0c2ce743a8(self, a, b, **kwargs):  # noqa: E501
        """Subtract two integers  # noqa: E501

        Produces a difference between two numbers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.5b5b2152dfc9bc0c2ce743a8(a, b, async=True)
        >>> result = thread.get()

        :param async bool
        :param str a: First operand. Default value is <code>51</code>. (required)
        :param str b: Second operand. Default value is <code>49</code>. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.5b5b2152dfc9bc0c2ce743a8_with_http_info(a, b, **kwargs)  # noqa: E501
        else:
            (data) = self.5b5b2152dfc9bc0c2ce743a8_with_http_info(a, b, **kwargs)  # noqa: E501
            return data

    def 5b5b2152dfc9bc0c2ce743a8_with_http_info(self, a, b, **kwargs):  # noqa: E501
        """Subtract two integers  # noqa: E501

        Produces a difference between two numbers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.5b5b2152dfc9bc0c2ce743a8_with_http_info(a, b, async=True)
        >>> result = thread.get()

        :param async bool
        :param str a: First operand. Default value is <code>51</code>. (required)
        :param str b: Second operand. Default value is <code>49</code>. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['a', 'b']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method 5b5b2152dfc9bc0c2ce743a8" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'a' is set
        if ('a' not in params or
                params['a'] is None):
            raise ValueError("Missing the required parameter `a` when calling `5b5b2152dfc9bc0c2ce743a8`")  # noqa: E501
        # verify the required parameter 'b' is set
        if ('b' not in params or
                params['b'] is None):
            raise ValueError("Missing the required parameter `b` when calling `5b5b2152dfc9bc0c2ce743a8`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'a' in params:
            query_params.append(('a', params['a']))  # noqa: E501
        if 'b' in params:
            query_params.append(('b', params['b']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apiKeyHeader', 'apiKeyQuery']  # noqa: E501

        return self.api_client.call_api(
            '/sub', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def 5b5b2152dfc9bc0c2ce743a9(self, a, b, **kwargs):  # noqa: E501
        """Multiply two integers  # noqa: E501

        Produces a product of two numbers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.5b5b2152dfc9bc0c2ce743a9(a, b, async=True)
        >>> result = thread.get()

        :param async bool
        :param str a: First operand. Default value is <code>51</code>. (required)
        :param str b: Second operand. Default value is <code>49</code>. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.5b5b2152dfc9bc0c2ce743a9_with_http_info(a, b, **kwargs)  # noqa: E501
        else:
            (data) = self.5b5b2152dfc9bc0c2ce743a9_with_http_info(a, b, **kwargs)  # noqa: E501
            return data

    def 5b5b2152dfc9bc0c2ce743a9_with_http_info(self, a, b, **kwargs):  # noqa: E501
        """Multiply two integers  # noqa: E501

        Produces a product of two numbers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.5b5b2152dfc9bc0c2ce743a9_with_http_info(a, b, async=True)
        >>> result = thread.get()

        :param async bool
        :param str a: First operand. Default value is <code>51</code>. (required)
        :param str b: Second operand. Default value is <code>49</code>. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['a', 'b']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method 5b5b2152dfc9bc0c2ce743a9" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'a' is set
        if ('a' not in params or
                params['a'] is None):
            raise ValueError("Missing the required parameter `a` when calling `5b5b2152dfc9bc0c2ce743a9`")  # noqa: E501
        # verify the required parameter 'b' is set
        if ('b' not in params or
                params['b'] is None):
            raise ValueError("Missing the required parameter `b` when calling `5b5b2152dfc9bc0c2ce743a9`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'a' in params:
            query_params.append(('a', params['a']))  # noqa: E501
        if 'b' in params:
            query_params.append(('b', params['b']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apiKeyHeader', 'apiKeyQuery']  # noqa: E501

        return self.api_client.call_api(
            '/mul', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def 5b5b2152dfc9bc0c2ce743aa(self, a, b, **kwargs):  # noqa: E501
        """Divide two integers  # noqa: E501

        Produces a quotient of two numbers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.5b5b2152dfc9bc0c2ce743aa(a, b, async=True)
        >>> result = thread.get()

        :param async bool
        :param str a: First operand. Default value is <code>51</code>. (required)
        :param str b: Second operand. Default value is <code>49</code>. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.5b5b2152dfc9bc0c2ce743aa_with_http_info(a, b, **kwargs)  # noqa: E501
        else:
            (data) = self.5b5b2152dfc9bc0c2ce743aa_with_http_info(a, b, **kwargs)  # noqa: E501
            return data

    def 5b5b2152dfc9bc0c2ce743aa_with_http_info(self, a, b, **kwargs):  # noqa: E501
        """Divide two integers  # noqa: E501

        Produces a quotient of two numbers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.5b5b2152dfc9bc0c2ce743aa_with_http_info(a, b, async=True)
        >>> result = thread.get()

        :param async bool
        :param str a: First operand. Default value is <code>51</code>. (required)
        :param str b: Second operand. Default value is <code>49</code>. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['a', 'b']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method 5b5b2152dfc9bc0c2ce743aa" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'a' is set
        if ('a' not in params or
                params['a'] is None):
            raise ValueError("Missing the required parameter `a` when calling `5b5b2152dfc9bc0c2ce743aa`")  # noqa: E501
        # verify the required parameter 'b' is set
        if ('b' not in params or
                params['b'] is None):
            raise ValueError("Missing the required parameter `b` when calling `5b5b2152dfc9bc0c2ce743aa`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'a' in params:
            query_params.append(('a', params['a']))  # noqa: E501
        if 'b' in params:
            query_params.append(('b', params['b']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apiKeyHeader', 'apiKeyQuery']  # noqa: E501

        return self.api_client.call_api(
            '/div', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
