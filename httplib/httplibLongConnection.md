## [python中httplib实现长连接](http://blog.csdn.net/ustclu/article/details/3326624)   
工作需要，通过长连接的方式测试程序的性能，于是做了以下的测试。这里的代码是一个单元测试，给目标post指定数据。  
其中 在headers中添加 "Connection":"Keep-Alive" 即可使服务器不主动断开此连接。当然也要注意，每次请求后，调用read()方法（否则不能进行下一次发送，httplib中第2次发送数据时，必须保证上一次数据被读取，否则会抛出异常）。  
```
import urllib,unittest
class PressureTest(unittest.TestCase):
    times=100
	data='''
        <?xml version="1.0" encoding="UTF-8"?>
        <message >
        </message>
	'''
    
    def testSend(self):
        import httplib
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain","Connection":"Keep-Alive"}
        conn = httplib.HTTPConnection("192.168.54.138",6040)
        for i in range(self.times):
            conn.request("POST", "/index.html", self.data, headers)
            response = conn.getresponse()
            response.read()
        conn.close()
if __name__ == "__main__":
    unittest.main()
```
