# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from TimeSeriesIoT.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_mean_sensor_id_get(self):
        """Test case for mean_sensor_id_get

        Renvoie la moyenne d'un capteur entre deux dates
        """
        query_string = [('startDate', 56),
                        ('endDate', 56)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1/mean/{sensor_id}'.format(sensor_id='sensor_id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
