import httplib
import unittest


class PressureTest(unittest.TestCase):
    times = 100
    data = '''
          <?xml version="1.0" encoding="UTF-8"?>
          <message >
          </message>
          '''

    def testSend(self):
        headers = {"Content-type": "application/x-www-form-urlencoded"}
        conn = httplib.HTTPConnection("10.64.79.66", 5000)
        for i in range(self.times):
            conn.request("GET", "/", self.data, headers)
            response = conn.getresponse()
            response.read()
        conn.close()
if __name__ == "__main__":
    unittest.main()
