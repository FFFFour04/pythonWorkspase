import requests

# get
payload = {'key1': 'value1', 'key2': 'value2'}
resp1 = requests.get('https://api.github.com/events')
print(resp1.text)
resp1 = requests.get("http://httpbin.org/get", params=payload)
print(resp1.url)
# post
resp2 = requests.post('http://httpbin.org/post', data={'key': 'value'})
#
resp3 = requests.put('http://httpbin.org/put', data={'key': 'value'})
resp4 = requests.delete('http://httpbin.org/delete')
resp5 = requests.head('http://httpbin.org/get')
resp6 = requests.options('http://httpbin.org/get')


# 直接运行文件以下代码块会运行，import导入不运行
if __name__ == '__main__':
    target='http://gitbook.cn/'
    req = requests.get(url=target)
    print(req.text) 