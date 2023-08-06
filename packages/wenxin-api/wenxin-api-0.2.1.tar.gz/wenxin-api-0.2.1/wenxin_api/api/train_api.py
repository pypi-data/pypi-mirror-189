# !/usr/bin/env python3
""" train api """
import json
from wenxin_api import requestor, error
from wenxin_api.api import (APIBaseObject, 
                            CreatableAPIObject, 
                            ListableAPIObject, 
                            StopableAPIObject, 
                            RetrievalableAPIObject)
from wenxin_api.base_object import BaseObject
from wenxin_api.const import CMD_DO_TRAIN, CMD_QUERY_TASK, CMD_STOP_TASK
from wenxin_api.const import TRAIN_TASK
from wenxin_api.error import MissingRequestArgumentError, IllegalRequestArgumentError

class Train(ListableAPIObject, CreatableAPIObject, StopableAPIObject, RetrievalableAPIObject):
    OBJECT_NAME = "fine-tunes"
    training_api_type = 10

    @classmethod
    def create(cls, train_datasets=[], dev_datasets=[], **params):
        if not isinstance(train_datasets, list):
            raise IllegalRequestArgumentError("train_datasets should be a list")
        if not isinstance(dev_datasets, list):
            raise IllegalRequestArgumentError("dev_datasets should be a list")
        if len(train_datasets) == 0:
            raise IllegalRequestArgumentError("train datasets shouldn't be null")

        train_data_ids = [dataset.id for dataset in train_datasets]
        if len(dev_datasets) > 0:
            dev_data_ids = [dataset.id for dataset in dev_datasets]
        else:
            dev_data_ids = []

        request_id = CMD_DO_TRAIN
        params["type"] = "task"
        # api_type 10 for training
        api_type = params.pop("api_type", cls.training_api_type)
        resp = super().create(request_id=request_id, 
                              api_type=api_type,
                              train_data_ids=train_data_ids, 
                              dev_data_ids=dev_data_ids, 
                              **params)
        resp.update()
        return resp

    @classmethod
    def list(cls, *args, **params):
        """ list """
        request_id = CMD_QUERY_TASK
        api_type = params.pop("api_type", cls.training_api_type)
        params["type"] = "task"
        resps = super().list(request_id=request_id, 
                             api_type=api_type,
                             **params)
        filtered_resps = [resp for resp in resps \
                            if resp.status >= 200 and \
                               resp.status < 300]
        return filtered_resps

    @classmethod
    def retrieve(cls, *args, **params):
        """ retrieve """
        request_id = CMD_QUERY_TASK
        api_type = params.pop("api_type", cls.training_api_type)
        params["type"] = "task"
        if "task_id" not in params:
            raise MissingRequestArgumentError("task_id is not provided")
        resp = super().retrieve(request_id=request_id, 
                                api_type=api_type,
                                **params)
        return resp

    def stop(self, *args, **params) -> BaseObject:
        request_id = CMD_STOP_TASK
        params["type"] = "task"
        params["task_type"] = TRAIN_TASK
        params["task_id"] = self.id
        if self.id is None:
            raise IllegalRequestArgumentError("illegal task_id")
        super().stop(request_id=request_id, 
                     api_type=self.api_type,
                     **params)
        self.update()

    def update(self, *args, **params):
        """ update """
        request_id = CMD_QUERY_TASK
        params["type"] = "task"
        task = super().retrieve(task_id=self.id, 
                                request_id=request_id, 
                                api_type=self.api_type,
                                **params)
        self.refresh_from(task)

    def __str__(self):
        return "Task {}:{}".format(
                        id(self),
                        json.dumps({"id": self.id, 
                                    "status": self.status,
                                    "api_type": self.api_type,
                                    "base_model": self.base_model,
                                    "job_id": self.job_id,
                                    "type": self.type
                                   }, ensure_ascii=False)
        )

    def __repr__(self):
        return self.__str__()

