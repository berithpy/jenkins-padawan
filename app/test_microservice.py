import unittest

class TestMicroservice(unittest.TestCase):
    def test_connections(self):
        """
        This tests if the microservice is alive
        """
        try:
            # connect to microservice
            if isinstance(savitest_config,str):
                if "couldn't" in savitest_config:
                    self.fail(savitest_config)
                if "ROC configuration" in savitest_config:
                    self.fail(savitest_config)
        except Exception as e:
            self.fail("Could not get the zoho-config.")
        try:
            k8_config_provider.protodump(savitest_config.__dict__)
        except Exception as e:
            self.fail("Could not dump the zoho-config.")


if __name__ == '__main__':
    unittest.main()