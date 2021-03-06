# coding: utf-8

"""
    DFC

    DFC is a scalable object-storage based caching system with Amazon and Google Cloud backends.  # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: dfcdev@exchange.nvidia.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient


class DaemonApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get(self, what, **kwargs):  # noqa: E501
        """Get daemon related details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get(what, async=True)
        >>> result = thread.get()

        :param async bool
        :param GetWhat what: Daemon details which needs to be fetched (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_with_http_info(what, **kwargs)  # noqa: E501
        else:
            (data) = self.get_with_http_info(what, **kwargs)  # noqa: E501
            return data

    def get_with_http_info(self, what, **kwargs):  # noqa: E501
        """Get daemon related details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_with_http_info(what, async=True)
        >>> result = thread.get()

        :param async bool
        :param GetWhat what: Daemon details which needs to be fetched (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['what']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'what' is set
        if ('what' not in params or
                params['what'] is None):
            raise ValueError("Missing the required parameter `what` when calling `get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'what' in params:
            query_params.append(('what', params['what']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json''text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/daemon/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def perform_operation(self, input_parameters, **kwargs):  # noqa: E501
        """Perform operations such as setting config value, shutting down proxy/target etc. on a DFC daemon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.perform_operation(input_parameters, async=True)
        >>> result = thread.get()

        :param async bool
        :param InputParameters input_parameters: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.perform_operation_with_http_info(input_parameters, **kwargs)  # noqa: E501
        else:
            (data) = self.perform_operation_with_http_info(input_parameters, **kwargs)  # noqa: E501
            return data

    def perform_operation_with_http_info(self, input_parameters, **kwargs):  # noqa: E501
        """Perform operations such as setting config value, shutting down proxy/target etc. on a DFC daemon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.perform_operation_with_http_info(input_parameters, async=True)
        >>> result = thread.get()

        :param async bool
        :param InputParameters input_parameters: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['input_parameters']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method perform_operation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'input_parameters' is set
        if ('input_parameters' not in params or
                params['input_parameters'] is None):
            raise ValueError("Missing the required parameter `input_parameters` when calling `perform_operation`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'input_parameters' in params:
            body_params = params['input_parameters']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/daemon/', 'PUT',
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
