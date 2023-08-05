# coding: utf-8

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from flywheel.api_client import ApiClient
import flywheel.models

# NOTE: This file is auto generated by the swagger code generator program.
# Do not edit the class manually.

class BatchApi(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def cancel_batch(self, batch_id, **kwargs):  # noqa: E501
        """Cancel a Job

        Cancels jobs that are still pending, returns number of jobs cancelled. Moves a 'running' batch job to 'cancelled'. 
        This method makes a synchronous HTTP request by default.

        :param str batch_id: (required)
        :param bool async_: Perform the request asynchronously
        :return: BatchCancelOutput
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('async_'):
            return self.cancel_batch_with_http_info(batch_id, **kwargs)  # noqa: E501
        else:
            (data) = self.cancel_batch_with_http_info(batch_id, **kwargs)  # noqa: E501
            if data and hasattr(data, 'return_value'):
                return data.return_value()
            return data


    def cancel_batch_with_http_info(self, batch_id, **kwargs):  # noqa: E501
        """Cancel a Job

        Cancels jobs that are still pending, returns number of jobs cancelled. Moves a 'running' batch job to 'cancelled'. 
        This method makes a synchronous HTTP request by default.

        :param str batch_id: (required)
        :param bool async: Perform the request asynchronously
        :return: BatchCancelOutput
        """

        all_params = ['batch_id',]  # noqa: E501
        all_params.append('async_')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('_request_out')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_batch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'batch_id' is set
        if ('batch_id' not in params or
                params['batch_id'] is None):
            raise ValueError("Missing the required parameter `batch_id` when calling `cancel_batch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'batch_id' in params:
            path_params['BatchId'] = params['batch_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/batch/{BatchId}/cancel', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BatchCancelOutput',  # noqa: E501
            auth_settings=auth_settings,
            async_=params.get('async_'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            _request_out=params.get('_request_out'),
            collection_formats=collection_formats)

    def create_batch_job_from_jobs(self, body, **kwargs):  # noqa: E501
        """Create a batch job proposal from preconstructed jobs and insert it as &#x27;pending&#x27;.

        This method makes a synchronous HTTP request by default.

        :param BatchJobsProposalInput body: Set of jobs to be run as a batch (required)
        :param bool async_: Perform the request asynchronously
        :return: BatchProposal
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('async_'):
            return self.create_batch_job_from_jobs_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_batch_job_from_jobs_with_http_info(body, **kwargs)  # noqa: E501
            if data and hasattr(data, 'return_value'):
                return data.return_value()
            return data


    def create_batch_job_from_jobs_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a batch job proposal from preconstructed jobs and insert it as &#x27;pending&#x27;.

        This method makes a synchronous HTTP request by default.

        :param BatchJobsProposalInput body: Set of jobs to be run as a batch (required)
        :param bool async: Perform the request asynchronously
        :return: BatchProposal
        """

        all_params = ['body',]  # noqa: E501
        all_params.append('async_')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('_request_out')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_batch_job_from_jobs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_batch_job_from_jobs`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = flywheel.models.BatchJobsProposalInput.positional_to_model(params['body'])
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/batch/jobs', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BatchProposal',  # noqa: E501
            auth_settings=auth_settings,
            async_=params.get('async_'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            _request_out=params.get('_request_out'),
            collection_formats=collection_formats)

    def get_all_batches(self, **kwargs):  # noqa: E501
        """Get a list of batch jobs the user has created.

        Requires login.
        This method makes a synchronous HTTP request by default.

        :param bool async_: Perform the request asynchronously
        :return: list[Batch]
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('async_'):
            return self.get_all_batches_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_batches_with_http_info(**kwargs)  # noqa: E501
            if data and hasattr(data, 'return_value'):
                return data.return_value()
            return data


    def get_all_batches_with_http_info(self, **kwargs):  # noqa: E501
        """Get a list of batch jobs the user has created.

        Requires login.
        This method makes a synchronous HTTP request by default.

        :param bool async: Perform the request asynchronously
        :return: list[Batch]
        """

        all_params = []  # noqa: E501
        all_params.append('async_')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('_request_out')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_batches" % key
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
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/batch', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Batch]',  # noqa: E501
            auth_settings=auth_settings,
            async_=params.get('async_'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            _request_out=params.get('_request_out'),
            collection_formats=collection_formats)

    def get_batch(self, batch_id, **kwargs):  # noqa: E501
        """Get batch job details.

        This method makes a synchronous HTTP request by default.

        :param str batch_id: (required)
        :param bool jobs: If true, return job objects instead of job ids
        :param bool async_: Perform the request asynchronously
        :return: Batch
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('async_'):
            return self.get_batch_with_http_info(batch_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_batch_with_http_info(batch_id, **kwargs)  # noqa: E501
            if data and hasattr(data, 'return_value'):
                return data.return_value()
            return data


    def get_batch_with_http_info(self, batch_id, **kwargs):  # noqa: E501
        """Get batch job details.

        This method makes a synchronous HTTP request by default.

        :param str batch_id: (required)
        :param bool jobs: If true, return job objects instead of job ids
        :param bool async: Perform the request asynchronously
        :return: Batch
        """

        all_params = ['batch_id','jobs',]  # noqa: E501
        all_params.append('async_')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('_request_out')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_batch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'batch_id' is set
        if ('batch_id' not in params or
                params['batch_id'] is None):
            raise ValueError("Missing the required parameter `batch_id` when calling `get_batch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'batch_id' in params:
            path_params['BatchId'] = params['batch_id']  # noqa: E501

        query_params = []
        if 'jobs' in params:
            query_params.append(('jobs', params['jobs']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/batch/{BatchId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Batch',  # noqa: E501
            auth_settings=auth_settings,
            async_=params.get('async_'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            _request_out=params.get('_request_out'),
            collection_formats=collection_formats)

    def propose_batch(self, body, **kwargs):  # noqa: E501
        """Create a batch job proposal and insert it as &#x27;pending&#x27;.

        This method makes a synchronous HTTP request by default.

        :param BatchProposalInput body: The batch proposal (required)
        :param bool async_: Perform the request asynchronously
        :return: BatchProposal
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('async_'):
            return self.propose_batch_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.propose_batch_with_http_info(body, **kwargs)  # noqa: E501
            if data and hasattr(data, 'return_value'):
                return data.return_value()
            return data


    def propose_batch_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a batch job proposal and insert it as &#x27;pending&#x27;.

        This method makes a synchronous HTTP request by default.

        :param BatchProposalInput body: The batch proposal (required)
        :param bool async: Perform the request asynchronously
        :return: BatchProposal
        """

        all_params = ['body',]  # noqa: E501
        all_params.append('async_')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('_request_out')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method propose_batch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `propose_batch`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = flywheel.models.BatchProposalInput.positional_to_model(params['body'])
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/batch', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BatchProposal',  # noqa: E501
            auth_settings=auth_settings,
            async_=params.get('async_'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            _request_out=params.get('_request_out'),
            collection_formats=collection_formats)

    def start_batch(self, batch_id, **kwargs):  # noqa: E501
        """Launch a job.

        Creates jobs from proposed inputs, returns jobs enqueued. Moves 'pending' batch job to 'running'.
        This method makes a synchronous HTTP request by default.

        :param str batch_id: (required)
        :param bool async_: Perform the request asynchronously
        :return: list[JobOutput]
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('async_'):
            return self.start_batch_with_http_info(batch_id, **kwargs)  # noqa: E501
        else:
            (data) = self.start_batch_with_http_info(batch_id, **kwargs)  # noqa: E501
            if data and hasattr(data, 'return_value'):
                return data.return_value()
            return data


    def start_batch_with_http_info(self, batch_id, **kwargs):  # noqa: E501
        """Launch a job.

        Creates jobs from proposed inputs, returns jobs enqueued. Moves 'pending' batch job to 'running'.
        This method makes a synchronous HTTP request by default.

        :param str batch_id: (required)
        :param bool async: Perform the request asynchronously
        :return: list[JobOutput]
        """

        all_params = ['batch_id',]  # noqa: E501
        all_params.append('async_')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('_request_out')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method start_batch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'batch_id' is set
        if ('batch_id' not in params or
                params['batch_id'] is None):
            raise ValueError("Missing the required parameter `batch_id` when calling `start_batch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'batch_id' in params:
            path_params['batch_id'] = params['batch_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/batch/{batch_id}/run', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[JobOutput]',  # noqa: E501
            auth_settings=auth_settings,
            async_=params.get('async_'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            _request_out=params.get('_request_out'),
            collection_formats=collection_formats)
