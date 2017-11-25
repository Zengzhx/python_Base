import urllib
import urllib.request

def get_image(url):
    request = urllib.request.Request(url) #构建服务器请求
    response= urllib.request.urlopen(request) #获取服务器响应
    get_img = response.read()
    with open('001.jpg','wb') as img:
        img.write(get_img)
        print('success')
        return

url = 'http://upload-images.jianshu.io/upload_images/2917634-7667382cc63b833d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240'
get_image(url)
