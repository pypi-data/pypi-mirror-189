# coding: utf-8

"""
    Workspace Data Service

    This page lists both current and proposed APIs. The proposed APIs which have not yet been implemented are marked as deprecated. This is incongruous, but by using the deprecated flag, we can force swagger-ui to display those endpoints differently.  Error codes and responses for proposed APIs are likely to change as we gain more clarity on their implementation.  As of v0.2, all APIs are subject to change without notice.   # noqa: E501

    The version of the OpenAPI document: v0.2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import wds_client
from wds_client.models.record_query_response import RecordQueryResponse  # noqa: E501
from wds_client.rest import ApiException

class TestRecordQueryResponse(unittest.TestCase):
    """RecordQueryResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RecordQueryResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = wds_client.models.record_query_response.RecordQueryResponse()  # noqa: E501
        if include_optional :
            return RecordQueryResponse(
                search_request = wds_client.models.search_request.SearchRequest(
                    offset = 0, 
                    limit = 0, 
                    sort = 'asc', 
                    sort_attribute = '0', ), 
                total_records = 56, 
                records = [
                    wds_client.models.record_response.RecordResponse(
                        id = '0', 
                        type = '0', 
                        attributes = {
  "stringAttr": "string",
  "numericAttr": 123,
  "booleanAttr": true,
  "relationAttr": "terra-wds:/target-type/target-id",
  "arrayString": ["green", "red"],
  "arrayBoolean": [true, false],
  "arrayNumber": [12821.112, 0.12121211, 11],
  "arrayDate": ["2022-11-03"],
  "arrayDateTime": ["2022-11-03T04:36:20"]
}
, )
                    ]
            )
        else :
            return RecordQueryResponse(
                search_request = wds_client.models.search_request.SearchRequest(
                    offset = 0, 
                    limit = 0, 
                    sort = 'asc', 
                    sort_attribute = '0', ),
                total_records = 56,
                records = [
                    wds_client.models.record_response.RecordResponse(
                        id = '0', 
                        type = '0', 
                        attributes = {
  "stringAttr": "string",
  "numericAttr": 123,
  "booleanAttr": true,
  "relationAttr": "terra-wds:/target-type/target-id",
  "arrayString": ["green", "red"],
  "arrayBoolean": [true, false],
  "arrayNumber": [12821.112, 0.12121211, 11],
  "arrayDate": ["2022-11-03"],
  "arrayDateTime": ["2022-11-03T04:36:20"]
}
, )
                    ],
        )

    def testRecordQueryResponse(self):
        """Test RecordQueryResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
