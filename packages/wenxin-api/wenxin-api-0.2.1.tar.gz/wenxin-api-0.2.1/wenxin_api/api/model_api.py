""" model api """
import json
from wenxin_api.api.base_api import APIBaseObject, ListableAPIObject, DeletableAPIObject, RetrievalableAPIObject
from wenxin_api.const import CMD_QUERY_MODEL, CMD_DELETE_MODEL, CMD_STOP_SERVER
from wenxin_api.error import MissingRequestArgumentError

class Model(ListableAPIObject, DeletableAPIObject, RetrievalableAPIObject):
    """ model class """
    OBJECT_NAME = "models"
    training_api_type = 10
    @classmethod
    def list(cls, *args, **params):
        """ list """
        request_id = CMD_QUERY_MODEL
        api_type = params.pop("api_type", cls.training_api_type)
        params["type"] = "model"
        resps = super().list(request_id=request_id, 
                             api_type=api_type,
                             *args, **params)
        return resps

    @classmethod
    def retrieve(cls, *args, **params):
        """ retrieve """
        request_id = CMD_QUERY_MODEL
        api_type = params.pop("api_type", cls.training_api_type)
        params["type"] = "model"
        if "model_id" not in params and "task_id" not in params:
            raise MissingRequestArgumentError("model_id or task_id is not provided")
        resp = super().retrieve(request_id=request_id, api_type=api_type, **params)
        return resp

    @classmethod
    def delete(cls, *args, **params):
        """ retrieve """
        request_id = CMD_DELETE_MODEL
        if not isinstance(cls, APIBaseObject):
            api_type = params.pop("api_type", cls.training_api_type)
        else:
            api_type = cls.api_type
        params["type"] = "model"
        if "model_id" not in params:
            raise MissingRequestArgumentError("model_id is not provided")
        resp = super().delete(request_id=request_id, api_type=api_type, **params)
        return resp

    def update(self, *args, **params):
        """ update """
        request_id = CMD_QUERY_MODEL
        params["type"] = "model"
        model = super().retrieve(model_id=self.id, request_id=request_id, api_type=self.api_type, **params)
        self.refresh_from(model)

    def stop(self, *args, **params):
        """ stop """
        request_id = CMD_STOP_SERVER
        params["type"] = "model"
        super().delete(model_id=self.id, request_id=request_id, api_type=self.api_type, **params)
        self.update()

    def __str__(self):
        return "Model {}:{}".format(
                        id(self),
                        json.dumps({"id": self.id, 
                                    "status": self.status,
                                    "api_type": self.api_type,
                                    "base_model": self.get("base_model", ""), 
                                    "is_public": self.get("is_public", ""),
                                    "name": self.get("model_name", ""),
                                    "type": self.type
                                   }, ensure_ascii=False)
        )

    def __repr__(self):
        return self.__str__()
