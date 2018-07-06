# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.10.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library

from aiokubernetes.api_client import ApiClient


class AuthorizationV1Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client):
        self.api_client = api_client

    def create_namespaced_local_subject_access_review(self, namespace, body, **kwargs):  # noqa: E501
        """create_namespaced_local_subject_access_review  # noqa: E501

        create a LocalSubjectAccessReview  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_namespaced_local_subject_access_review(namespace, body, async=True)
        >>> result = thread.get()

        :param: async bool
        :param: str namespace: object name and auth scope, such as for teams and projects (required)
        :param: V1LocalSubjectAccessReview body: (required)
        :param: str pretty: If 'true', then the output is pretty printed.
        :return: V1LocalSubjectAccessReview
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_namespaced_local_subject_access_review_with_http_info(namespace, body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_namespaced_local_subject_access_review_with_http_info(namespace, body, **kwargs)  # noqa: E501
            return data

    def create_namespaced_local_subject_access_review_with_http_info(self, namespace, body, **kwargs):  # noqa: E501
        """create_namespaced_local_subject_access_review  # noqa: E501

        create a LocalSubjectAccessReview  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_namespaced_local_subject_access_review_with_http_info(namespace, body, async=True)
        >>> result = thread.get()

        :param: async bool
        :param: str namespace: object name and auth scope, such as for teams and projects (required)
        :param: V1LocalSubjectAccessReview body: (required)
        :param: str pretty: If 'true', then the output is pretty printed.
        :return: V1LocalSubjectAccessReview
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['namespace', 'body', 'pretty']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_namespaced_local_subject_access_review" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `create_namespaced_local_subject_access_review`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_namespaced_local_subject_access_review`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']  # noqa: E501

        query_params = []
        if 'pretty' in params:
            query_params.append(('pretty', params['pretty']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerToken']  # noqa: E501

        return self.api_client.call_api(
            '/apis/authorization.k8s.io/v1/namespaces/{namespace}/localsubjectaccessreviews', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1LocalSubjectAccessReview',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_self_subject_access_review(self, body, **kwargs):  # noqa: E501
        """create_self_subject_access_review  # noqa: E501

        create a SelfSubjectAccessReview  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_self_subject_access_review(body, async=True)
        >>> result = thread.get()

        :param: async bool
        :param: V1SelfSubjectAccessReview body: (required)
        :param: str pretty: If 'true', then the output is pretty printed.
        :return: V1SelfSubjectAccessReview
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_self_subject_access_review_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_self_subject_access_review_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_self_subject_access_review_with_http_info(self, body, **kwargs):  # noqa: E501
        """create_self_subject_access_review  # noqa: E501

        create a SelfSubjectAccessReview  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_self_subject_access_review_with_http_info(body, async=True)
        >>> result = thread.get()

        :param: async bool
        :param: V1SelfSubjectAccessReview body: (required)
        :param: str pretty: If 'true', then the output is pretty printed.
        :return: V1SelfSubjectAccessReview
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'pretty']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_self_subject_access_review" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_self_subject_access_review`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'pretty' in params:
            query_params.append(('pretty', params['pretty']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerToken']  # noqa: E501

        return self.api_client.call_api(
            '/apis/authorization.k8s.io/v1/selfsubjectaccessreviews', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1SelfSubjectAccessReview',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_self_subject_rules_review(self, body, **kwargs):  # noqa: E501
        """create_self_subject_rules_review  # noqa: E501

        create a SelfSubjectRulesReview  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_self_subject_rules_review(body, async=True)
        >>> result = thread.get()

        :param: async bool
        :param: V1SelfSubjectRulesReview body: (required)
        :param: str pretty: If 'true', then the output is pretty printed.
        :return: V1SelfSubjectRulesReview
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_self_subject_rules_review_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_self_subject_rules_review_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_self_subject_rules_review_with_http_info(self, body, **kwargs):  # noqa: E501
        """create_self_subject_rules_review  # noqa: E501

        create a SelfSubjectRulesReview  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_self_subject_rules_review_with_http_info(body, async=True)
        >>> result = thread.get()

        :param: async bool
        :param: V1SelfSubjectRulesReview body: (required)
        :param: str pretty: If 'true', then the output is pretty printed.
        :return: V1SelfSubjectRulesReview
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'pretty']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_self_subject_rules_review" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_self_subject_rules_review`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'pretty' in params:
            query_params.append(('pretty', params['pretty']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerToken']  # noqa: E501

        return self.api_client.call_api(
            '/apis/authorization.k8s.io/v1/selfsubjectrulesreviews', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1SelfSubjectRulesReview',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_subject_access_review(self, body, **kwargs):  # noqa: E501
        """create_subject_access_review  # noqa: E501

        create a SubjectAccessReview  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_subject_access_review(body, async=True)
        >>> result = thread.get()

        :param: async bool
        :param: V1SubjectAccessReview body: (required)
        :param: str pretty: If 'true', then the output is pretty printed.
        :return: V1SubjectAccessReview
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_subject_access_review_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_subject_access_review_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_subject_access_review_with_http_info(self, body, **kwargs):  # noqa: E501
        """create_subject_access_review  # noqa: E501

        create a SubjectAccessReview  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_subject_access_review_with_http_info(body, async=True)
        >>> result = thread.get()

        :param: async bool
        :param: V1SubjectAccessReview body: (required)
        :param: str pretty: If 'true', then the output is pretty printed.
        :return: V1SubjectAccessReview
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'pretty']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_subject_access_review" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_subject_access_review`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'pretty' in params:
            query_params.append(('pretty', params['pretty']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerToken']  # noqa: E501

        return self.api_client.call_api(
            '/apis/authorization.k8s.io/v1/subjectaccessreviews', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1SubjectAccessReview',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_api_resources(self, **kwargs):  # noqa: E501
        """get_api_resources  # noqa: E501

        get available resources  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_api_resources(async=True)
        >>> result = thread.get()

        :param: async bool
        :return: V1APIResourceList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_api_resources_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_api_resources_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_api_resources_with_http_info(self, **kwargs):  # noqa: E501
        """get_api_resources  # noqa: E501

        get available resources  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_api_resources_with_http_info(async=True)
        >>> result = thread.get()

        :param: async bool
        :return: V1APIResourceList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_api_resources" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerToken']  # noqa: E501

        return self.api_client.call_api(
            '/apis/authorization.k8s.io/v1/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1APIResourceList',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
