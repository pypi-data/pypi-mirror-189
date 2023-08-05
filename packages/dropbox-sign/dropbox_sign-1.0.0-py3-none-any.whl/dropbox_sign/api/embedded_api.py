"""
    Dropbox Sign API

    Dropbox Sign v3 API  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Contact: apisupport@hellosign.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
import re  # noqa: F401
import sys  # noqa: F401

from dropbox_sign.api_client import ApiClient, ApiException, Endpoint as _Endpoint
from dropbox_sign.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from dropbox_sign.model.embedded_edit_url_request import EmbeddedEditUrlRequest
from dropbox_sign.model.embedded_edit_url_response import EmbeddedEditUrlResponse
from dropbox_sign.model.embedded_sign_url_response import EmbeddedSignUrlResponse
from dropbox_sign.model.error_response import ErrorResponse


class EmbeddedApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.embedded_edit_url_endpoint = _Endpoint(
            settings={
                'response_type': (EmbeddedEditUrlResponse,),
                'auth': [
                    'api_key',
                    'oauth2'
                ],
                'endpoint_path': '/embedded/edit_url/{template_id}',
                'operation_id': 'embedded_edit_url',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'template_id',
                    'embedded_edit_url_request',
                ],
                'required': [
                    'template_id',
                    'embedded_edit_url_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'template_id':
                        (str,),
                    'embedded_edit_url_request':
                        (EmbeddedEditUrlRequest,),
                },
                'attribute_map': {
                    'template_id': 'template_id',
                },
                'location_map': {
                    'template_id': 'path',
                    'embedded_edit_url_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.embedded_sign_url_endpoint = _Endpoint(
            settings={
                'response_type': (EmbeddedSignUrlResponse,),
                'auth': [
                    'api_key',
                    'oauth2'
                ],
                'endpoint_path': '/embedded/sign_url/{signature_id}',
                'operation_id': 'embedded_sign_url',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'signature_id',
                ],
                'required': [
                    'signature_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'signature_id':
                        (str,),
                },
                'attribute_map': {
                    'signature_id': 'signature_id',
                },
                'location_map': {
                    'signature_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def embedded_edit_url(
        self,
        template_id,
        embedded_edit_url_request,
        **kwargs
    ) -> EmbeddedEditUrlResponse:
        """Get Embedded Template Edit URL  # noqa: E501

        Retrieves an embedded object containing a template url that can be opened in an iFrame. Note that only templates created via the embedded template process are available to be edited with this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.embedded_edit_url(template_id, embedded_edit_url_request, async_req=True)
        >>> result = thread.get()

        Args:
            template_id (str): The id of the template to edit.
            embedded_edit_url_request (EmbeddedEditUrlRequest):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            EmbeddedEditUrlResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['template_id'] = \
            template_id
        kwargs['embedded_edit_url_request'] = \
            embedded_edit_url_request
        try:
            return self.embedded_edit_url_endpoint.call_with_http_info(**kwargs)
        except ApiException as e:
            if e.status == 200:
                e.body = self.api_client.deserialize(
                    response=type('obj_dict', (object,), {'data': e.body}),
                    response_type=[EmbeddedEditUrlResponse],
                    _check_type=True,
                )

                raise e
            range_code = "4XX"[0]
            range_code_left = int(f"{range_code}00")
            range_code_right = int(f"{range_code}99")

            if range_code_left <= e.status <= range_code_right:
                e.body = self.api_client.deserialize(
                    response=type('obj_dict', (object,), {'data': e.body}),
                    response_type=[ErrorResponse],
                    _check_type=True,
                )

                raise e

    def embedded_sign_url(
        self,
        signature_id,
        **kwargs
    ) -> EmbeddedSignUrlResponse:
        """Get Embedded Sign URL  # noqa: E501

        Retrieves an embedded object containing a signature url that can be opened in an iFrame. Note that templates created via the embedded template process will only be accessible through the API.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.embedded_sign_url(signature_id, async_req=True)
        >>> result = thread.get()

        Args:
            signature_id (str): The id of the signature to get a signature url for.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            EmbeddedSignUrlResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['signature_id'] = \
            signature_id
        try:
            return self.embedded_sign_url_endpoint.call_with_http_info(**kwargs)
        except ApiException as e:
            if e.status == 200:
                e.body = self.api_client.deserialize(
                    response=type('obj_dict', (object,), {'data': e.body}),
                    response_type=[EmbeddedSignUrlResponse],
                    _check_type=True,
                )

                raise e
            range_code = "4XX"[0]
            range_code_left = int(f"{range_code}00")
            range_code_right = int(f"{range_code}99")

            if range_code_left <= e.status <= range_code_right:
                e.body = self.api_client.deserialize(
                    response=type('obj_dict', (object,), {'data': e.body}),
                    response_type=[ErrorResponse],
                    _check_type=True,
                )

                raise e

