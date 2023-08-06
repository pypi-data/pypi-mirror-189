# !/usr/bin/env python3
""" base api """
from typing import Optional
import wenxin_api
import wenxin_api.variable
from wenxin_api import requestor, error
from wenxin_api.base_object import BaseObject
from wenxin_api.const import ERNIE_1P5B_MODEL
from wenxin_api.error import IllegalRequestArgumentError, InvalidResponseValue

class APIBaseObject(BaseObject):
    wenxin_api.variable.API_REQUEST_URLS

    def __init__(self, 
                 ak=None, 
                 sk=None, 
                 api_type=None, 
                 base_model=ERNIE_1P5B_MODEL,
                 **params):
        super(APIBaseObject, self).__init__(**params)
        self.__setattr__("ak", ak)
        self.__setattr__("sk", sk)
        self.__setattr__("api_type", api_type)
        self.__setattr__("base_model", base_model)

    @classmethod
    def construct_from(cls, **values):
        instance = cls(**values)
        return instance

    @classmethod
    def default_request(
        cls,
        ak=None,
        sk=None,
        api_type=None,
        method="post",
        request_id=None,
        request_type=None,
        files=None,
        **params,
    ):
        if api_type is None:
            api_type = cls.api_type
        try:
            api_type = int(api_type)
            url = wenxin_api.variable.API_REQUEST_URLS[api_type]
        except:
            raise IllegalRequestArgumentError()
        if request_type is None:
            request_type = params.pop("type", None)

        http_requestor = requestor.HTTPRequestor(ak, sk, request_type)
        resp = http_requestor.request(url, method, files=files, request_id=request_id, **params)
        if not isinstance(resp, BaseObject) and isinstance(resp, list):
            InvalidResponseValue()
        return resp
    
    @classmethod
    def get_url(cls, api_type=None):
        try:
            if api_type is None:
                api_type = cls.api_type
            url = wenxin_api.variable.API_REQUEST_URLS[api_type]
        except:
            raise IllegalRequestArgumentError("api_type: {}".format(api_type))
        return url

class CreatableAPIObject(APIBaseObject):
    """ creatable api object """
    @classmethod
    def create(cls, ak=None, sk=None, api_type=None, request_id=None, **params):
        """ create """
        if isinstance(cls, APIBaseObject):
            raise ValueError(".create may only be called as a class method now.")
        request_type = params.pop("type", None)
        method = params.pop("method", "post")
        http_requestor = requestor.HTTPRequestor(ak, sk, request_type)
        url = cls.get_url(api_type)
        resp = http_requestor.request(url, method, request_id=request_id, **params)
        if not isinstance(resp, BaseObject):
            raise InvalidResponseValue("create method should returns BaseObject instance")
        return cls.construct_from(**resp, api_type=api_type)

class DeletableAPIObject(APIBaseObject):
    """ deletable api object """
    @classmethod
    def delete(cls, ak=None, sk=None, api_type=None, request_id=None, **params):
        if isinstance(cls, APIBaseObject):
            raise ValueError(".delete may only be called as a class method now.")
        request_type = params.pop("type", None)
        method = params.pop("method", "post")
        http_requestor = requestor.HTTPRequestor(ak, sk, request_type)
        url = cls.get_url(api_type)
        resp = http_requestor.request(url, method, request_id=request_id, **params)
        if not isinstance(resp, BaseObject):
            raise InvalidResponseValue("delete method should returns BaseObject instance")
        return cls.construct_from(api_type=api_type, **resp)

class StopableAPIObject(APIBaseObject):
    """ stopable api object """
    @classmethod
    def stop(cls, ak=None, sk=None, api_type=None, request_id=None, **params):
        request_type = params.pop("type", None)
        method = params.pop("method", "post")
        http_requestor = requestor.HTTPRequestor(ak, sk, request_type)
        url = cls.get_url(api_type)
        resp = http_requestor.request(url, method, request_id=request_id, **params)
        if not isinstance(resp, BaseObject):
            raise InvalidResponseValue("stop method should returns BaseObject instance")
        return cls.construct_from(api_type=api_type, **resp)

class ListableAPIObject(APIBaseObject):
    """ listable api object """
    @classmethod
    def list(cls, ak=None, sk=None, api_type=None, request_id=None, **params):
        request_type = params.pop("type", None)
        method = params.pop("method", "post")
        if request_type is None:
            raise IllegalRequestArgumentError("type is not provided")
        http_requestor = requestor.HTTPRequestor(ak, sk, request_type)
        url = cls.get_url(api_type)
        resps = http_requestor.request(url, method, request_id=request_id, **params)
        if isinstance(resps, BaseObject):
            return [cls.construct_from(**resps, api_type=api_type)]
        resp = [cls.construct_from(**r, api_type=api_type) for r in resps]
        return resp

class RetrievalableAPIObject(APIBaseObject):
    """ retrievalable api object """
    @classmethod
    def retrieve(cls, ak=None, sk=None, api_type=None, request_id=None, **params):
        if "type" not in params:
            raise IllegalRequestArgumentError("type is not provided")
        request_type = params.pop("type", None)
        http_requestor = requestor.HTTPRequestor(ak, sk, request_type)
        method = params.pop("method", "post")
        url = cls.get_url(api_type)
        resp = http_requestor.request(url, method, request_id=request_id, **params)
        if not isinstance(resp, BaseObject):
            raise InvalidResponseValue("retrieve method should returns BaseObject instance")
        return cls.construct_from(api_type=api_type, **resp)