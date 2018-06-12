import unittest, urllib.request, json

class TestMicroservice(unittest.TestCase):
    def test_connections(self):
        """
        This tests if the microservice is alive
        """
        try:
            # connect to microservice
            with urllib.request.urlopen("http://127.0.0.1:5000/test") as url:
                data = json.loads(url.read().decode())
                print(data)
        except Exception as e:
            self.fail("Could not communicate with the server.")


if __name__ == '__main__':
    unittest.main()