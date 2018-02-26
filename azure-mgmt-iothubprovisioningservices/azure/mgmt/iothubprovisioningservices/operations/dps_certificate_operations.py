# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class DpsCertificateOperations(object):
    """DpsCertificateOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: The version of the API. Constant value: "2018-01-22".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2018-01-22"

        self.config = config

    def get(
            self, certificate_name, resource_group_name, provisioning_service_name, if_match=None, custom_headers=None, raw=False, **operation_config):
        """Get the certificate from the provisioning service.

        :param certificate_name: Name of the certificate to retrieve.
        :type certificate_name: str
        :param resource_group_name: Resource group identifier.
        :type resource_group_name: str
        :param provisioning_service_name: Name of the provisioning service the
         certificate is associated with.
        :type provisioning_service_name: str
        :param if_match: ETag of the certificate.
        :type if_match: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: CertificateResponse or ClientRawResponse if raw=true
        :rtype:
         ~azure.mgmt.iothubprovisioningservices.models.CertificateResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorDetailsException<azure.mgmt.iothubprovisioningservices.models.ErrorDetailsException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'certificateName': self._serialize.url("certificate_name", certificate_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'provisioningServiceName': self._serialize.url("provisioning_service_name", provisioning_service_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorDetailsException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('CertificateResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/provisioningServices/{provisioningServiceName}/certificates/{certificateName}'}

    def create_or_update(
            self, resource_group_name, provisioning_service_name, certificate_name, if_match=None, certificate=None, custom_headers=None, raw=False, **operation_config):
        """Upload the certificate to the provisioning service.

        Add new certificate or update an existing certificate.

        :param resource_group_name: Resource group identifier.
        :type resource_group_name: str
        :param provisioning_service_name: The name of the provisioning
         service.
        :type provisioning_service_name: str
        :param certificate_name: The name of the certificate create or update.
        :type certificate_name: str
        :param if_match: ETag of the certificate. This is required to update
         an existing certificate, and ignored while creating a brand new
         certificate.
        :type if_match: str
        :param certificate: Base-64 representation of the X509 leaf
         certificate .cer file or just .pem file content.
        :type certificate: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: CertificateResponse or ClientRawResponse if raw=true
        :rtype:
         ~azure.mgmt.iothubprovisioningservices.models.CertificateResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorDetailsException<azure.mgmt.iothubprovisioningservices.models.ErrorDetailsException>`
        """
        certificate_description = models.CertificateBodyDescription(certificate=certificate)

        # Construct URL
        url = self.create_or_update.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'provisioningServiceName': self._serialize.url("provisioning_service_name", provisioning_service_name, 'str'),
            'certificateName': self._serialize.url("certificate_name", certificate_name, 'str', max_length=256)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(certificate_description, 'CertificateBodyDescription')

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorDetailsException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('CertificateResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/provisioningServices/{provisioningServiceName}/certificates/{certificateName}'}

    def delete(
            self, resource_group_name, if_match, provisioning_service_name, certificate_name, certificatename=None, certificateraw_bytes=None, certificateis_verified=None, certificatepurpose=None, certificatecreated=None, certificatelast_updated=None, certificatehas_private_key=None, certificatenonce=None, custom_headers=None, raw=False, **operation_config):
        """Delete the Provisioning Service Certificate.

        Deletes the specified certificate assosciated with the Provisioning
        Service.

        :param resource_group_name: Resource group identifier.
        :type resource_group_name: str
        :param if_match: ETag of the certificate
        :type if_match: str
        :param provisioning_service_name: The name of the provisioning
         service.
        :type provisioning_service_name: str
        :param certificate_name: This is a mandatory field, and is the logical
         name of the certificate that the provisioning service will access by.
        :type certificate_name: str
        :param certificatename: This is optional, and it is the Common Name of
         the certificate.
        :type certificatename: str
        :param certificateraw_bytes: Raw data within the certificate.
        :type certificateraw_bytes: bytearray
        :param certificateis_verified: Indicates if certificate has been
         verified by owner of the private key.
        :type certificateis_verified: bool
        :param certificatepurpose: A description that mentions the purpose of
         the certificate. Possible values include: 'clientAuthentication',
         'serverAuthentication'
        :type certificatepurpose: str or
         ~azure.mgmt.iothubprovisioningservices.models.CertificatePurpose
        :param certificatecreated: Time the certificate is created.
        :type certificatecreated: datetime
        :param certificatelast_updated: Time the certificate is last updated.
        :type certificatelast_updated: datetime
        :param certificatehas_private_key: Indicates if the certificate
         contains a private key.
        :type certificatehas_private_key: bool
        :param certificatenonce: Random number generated to indicate Proof of
         Possession.
        :type certificatenonce: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorDetailsException<azure.mgmt.iothubprovisioningservices.models.ErrorDetailsException>`
        """
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'provisioningServiceName': self._serialize.url("provisioning_service_name", provisioning_service_name, 'str'),
            'certificateName': self._serialize.url("certificate_name", certificate_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if certificatename is not None:
            query_parameters['certificate.name'] = self._serialize.query("certificatename", certificatename, 'str')
        if certificateraw_bytes is not None:
            query_parameters['certificate.rawBytes'] = self._serialize.query("certificateraw_bytes", certificateraw_bytes, 'bytearray')
        if certificateis_verified is not None:
            query_parameters['certificate.isVerified'] = self._serialize.query("certificateis_verified", certificateis_verified, 'bool')
        if certificatepurpose is not None:
            query_parameters['certificate.purpose'] = self._serialize.query("certificatepurpose", certificatepurpose, 'str')
        if certificatecreated is not None:
            query_parameters['certificate.created'] = self._serialize.query("certificatecreated", certificatecreated, 'iso-8601')
        if certificatelast_updated is not None:
            query_parameters['certificate.lastUpdated'] = self._serialize.query("certificatelast_updated", certificatelast_updated, 'iso-8601')
        if certificatehas_private_key is not None:
            query_parameters['certificate.hasPrivateKey'] = self._serialize.query("certificatehas_private_key", certificatehas_private_key, 'bool')
        if certificatenonce is not None:
            query_parameters['certificate.nonce'] = self._serialize.query("certificatenonce", certificatenonce, 'str')
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 204]:
            raise models.ErrorDetailsException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/provisioningServices/{provisioningServiceName}/certificates/{certificateName}'}

    def generate_verification_code(
            self, certificate_name, if_match, resource_group_name, provisioning_service_name, certificatename=None, certificateraw_bytes=None, certificateis_verified=None, certificatepurpose=None, certificatecreated=None, certificatelast_updated=None, certificatehas_private_key=None, certificatenonce=None, custom_headers=None, raw=False, **operation_config):
        """Generate verification code for Proof of Possession.

        :param certificate_name: The mandatory logical name of the
         certificate, that the provisioning service uses to access.
        :type certificate_name: str
        :param if_match: ETag of the certificate. This is required to update
         an existing certificate, and ignored while creating a brand new
         certificate.
        :type if_match: str
        :param resource_group_name: name of resource group.
        :type resource_group_name: str
        :param provisioning_service_name: Name of provisioning service.
        :type provisioning_service_name: str
        :param certificatename: Common Name for the certificate.
        :type certificatename: str
        :param certificateraw_bytes: Raw data of certificate.
        :type certificateraw_bytes: bytearray
        :param certificateis_verified: Indicates if the certificate has been
         verified by owner of the private key.
        :type certificateis_verified: bool
        :param certificatepurpose: Description mentioning the purpose of the
         certificate. Possible values include: 'clientAuthentication',
         'serverAuthentication'
        :type certificatepurpose: str or
         ~azure.mgmt.iothubprovisioningservices.models.CertificatePurpose
        :param certificatecreated: Certificate creation time.
        :type certificatecreated: datetime
        :param certificatelast_updated: Certificate last updated time.
        :type certificatelast_updated: datetime
        :param certificatehas_private_key: Indicates if the certificate
         contains private key.
        :type certificatehas_private_key: bool
        :param certificatenonce: Random number generated to indicate Proof of
         Possession.
        :type certificatenonce: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: VerificationCodeResponse or ClientRawResponse if raw=true
        :rtype:
         ~azure.mgmt.iothubprovisioningservices.models.VerificationCodeResponse
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorDetailsException<azure.mgmt.iothubprovisioningservices.models.ErrorDetailsException>`
        """
        # Construct URL
        url = self.generate_verification_code.metadata['url']
        path_format_arguments = {
            'certificateName': self._serialize.url("certificate_name", certificate_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'provisioningServiceName': self._serialize.url("provisioning_service_name", provisioning_service_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if certificatename is not None:
            query_parameters['certificate.name'] = self._serialize.query("certificatename", certificatename, 'str')
        if certificateraw_bytes is not None:
            query_parameters['certificate.rawBytes'] = self._serialize.query("certificateraw_bytes", certificateraw_bytes, 'bytearray')
        if certificateis_verified is not None:
            query_parameters['certificate.isVerified'] = self._serialize.query("certificateis_verified", certificateis_verified, 'bool')
        if certificatepurpose is not None:
            query_parameters['certificate.purpose'] = self._serialize.query("certificatepurpose", certificatepurpose, 'str')
        if certificatecreated is not None:
            query_parameters['certificate.created'] = self._serialize.query("certificatecreated", certificatecreated, 'iso-8601')
        if certificatelast_updated is not None:
            query_parameters['certificate.lastUpdated'] = self._serialize.query("certificatelast_updated", certificatelast_updated, 'iso-8601')
        if certificatehas_private_key is not None:
            query_parameters['certificate.hasPrivateKey'] = self._serialize.query("certificatehas_private_key", certificatehas_private_key, 'bool')
        if certificatenonce is not None:
            query_parameters['certificate.nonce'] = self._serialize.query("certificatenonce", certificatenonce, 'str')
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorDetailsException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('VerificationCodeResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    generate_verification_code.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/provisioningServices/{provisioningServiceName}/certificates/{certificateName}/generateVerificationCode'}

    def verify_certificate(
            self, certificate_name, if_match, resource_group_name, provisioning_service_name, certificatename=None, certificateraw_bytes=None, certificateis_verified=None, certificatepurpose=None, certificatecreated=None, certificatelast_updated=None, certificatehas_private_key=None, certificatenonce=None, certificate=None, custom_headers=None, raw=False, **operation_config):
        """Verify certificate's private key possession.

        Verifies the certificate's private key possession by providing the leaf
        cert issued by the verifying pre uploaded certificate.

        :param certificate_name: The mandatory logical name of the
         certificate, that the provisioning service uses to access.
        :type certificate_name: str
        :param if_match: ETag of the certificate.
        :type if_match: str
        :param resource_group_name: Resource group name.
        :type resource_group_name: str
        :param provisioning_service_name: Provisioning service name.
        :type provisioning_service_name: str
        :param certificatename: Common Name for the certificate.
        :type certificatename: str
        :param certificateraw_bytes: Raw data of certificate.
        :type certificateraw_bytes: bytearray
        :param certificateis_verified: Indicates if the certificate has been
         verified by owner of the private key.
        :type certificateis_verified: bool
        :param certificatepurpose: Describe the purpose of the certificate.
         Possible values include: 'clientAuthentication',
         'serverAuthentication'
        :type certificatepurpose: str or
         ~azure.mgmt.iothubprovisioningservices.models.CertificatePurpose
        :param certificatecreated: Certificate creation time.
        :type certificatecreated: datetime
        :param certificatelast_updated: Certificate last updated time.
        :type certificatelast_updated: datetime
        :param certificatehas_private_key: Indicates if the certificate
         contains private key.
        :type certificatehas_private_key: bool
        :param certificatenonce: Random number generated to indicate Proof of
         Possession.
        :type certificatenonce: str
        :param certificate: base-64 representation of X509 certificate .cer
         file or just .pem file content.
        :type certificate: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: CertificateResponse or ClientRawResponse if raw=true
        :rtype:
         ~azure.mgmt.iothubprovisioningservices.models.CertificateResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorDetailsException<azure.mgmt.iothubprovisioningservices.models.ErrorDetailsException>`
        """
        request = models.VerificationCodeRequest(certificate=certificate)

        # Construct URL
        url = self.verify_certificate.metadata['url']
        path_format_arguments = {
            'certificateName': self._serialize.url("certificate_name", certificate_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'provisioningServiceName': self._serialize.url("provisioning_service_name", provisioning_service_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if certificatename is not None:
            query_parameters['certificate.name'] = self._serialize.query("certificatename", certificatename, 'str')
        if certificateraw_bytes is not None:
            query_parameters['certificate.rawBytes'] = self._serialize.query("certificateraw_bytes", certificateraw_bytes, 'bytearray')
        if certificateis_verified is not None:
            query_parameters['certificate.isVerified'] = self._serialize.query("certificateis_verified", certificateis_verified, 'bool')
        if certificatepurpose is not None:
            query_parameters['certificate.purpose'] = self._serialize.query("certificatepurpose", certificatepurpose, 'str')
        if certificatecreated is not None:
            query_parameters['certificate.created'] = self._serialize.query("certificatecreated", certificatecreated, 'iso-8601')
        if certificatelast_updated is not None:
            query_parameters['certificate.lastUpdated'] = self._serialize.query("certificatelast_updated", certificatelast_updated, 'iso-8601')
        if certificatehas_private_key is not None:
            query_parameters['certificate.hasPrivateKey'] = self._serialize.query("certificatehas_private_key", certificatehas_private_key, 'bool')
        if certificatenonce is not None:
            query_parameters['certificate.nonce'] = self._serialize.query("certificatenonce", certificatenonce, 'str')
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(request, 'VerificationCodeRequest')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorDetailsException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('CertificateResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    verify_certificate.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/provisioningServices/{provisioningServiceName}/certificates/{certificateName}/verify'}
