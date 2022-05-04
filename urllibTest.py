# urllib3
# pip install urllib3
import urllib3
import urllib.request
# Get HTML or API Call
r = urllib3.PoolManager()
response = r.request('GET', 'http://www.example.com')
print(response.status)
print(response.data)
# Mutliple API Call
r = urllib3.PoolManager(num_pools=2)
response1 = r.request('GET', 'http://www.example1.com')
response2 = r.request('GET', 'http://www.example2.com')
# Download Images/videos and Files
# r = urllib.request.urlretrieve("video url", 'video_name.mp4')