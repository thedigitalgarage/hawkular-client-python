import unittest
import uuid
from metrics import *

class TestMetricFunctionsBase(unittest.TestCase):

    def setUp(self):
        self.test_tenant = 'sample'
        self.client = HawkularMetricsClient(tenant_id=self.test_tenant, port=8443)

class MetricsTestCase(TestMetricFunctionsBase):
    """
    Test metric functionality, both adding definition and querying for definition,
    as well as adding new gauge and availability metrics.

    Metric definition creation should also test fetching the definition, while
    metric inserts should test also fetching the metric data.
    """

    def test_query_options(self):
        # Create metric with two values
        t = time_millis()
        v1 = create_datapoint(float(1.45), t)
        v2 = create_datapoint(float(2.00), (t - 2000))

        m = create_metric(MetricType.Gauge, 'test.query.gauge.1', [v1, v2])
        print m
        #self.client.put(m)

        t = self.client.query_tenants()
        print "Tenants ", t

        # Query first without limitations
        d = self.client.query_metric(MetricType.Gauge, 'test.query.gauge.1')
        self.assertEqual(2, len(d))

        # Query for data which has start time limitation
        d = self.client.query_metric(MetricType.Gauge, 'test.query.gauge.1', start=(t-1000))
        self.assertEqual(1, len(d))


if __name__ == '__main__':
    unittest.main()
