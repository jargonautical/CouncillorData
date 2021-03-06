import os
import errno
import requests

base_urls = open('urls.txt')

mgWebService_ops = ['GetMeetings','GetAttachment','GetAttachmentByPath']

for url in base_urls:
    for op in mgWebService_ops:
        url = url.strip().replace('http://', '').replace('https://', '')
        req_url_base = "{0}/mgWebService.asmx/{1}".format(url,op)

        print(req_url_base)
        try:
            req = requests.get("http://{0}".format(req_url_base))
        except:
            req = requests.get("https://{0}".format(req_url_base))
        path = os.path.join(
        
            os.path.abspath('.'),
            'data',
            url.replace('http://', '')\
            .replace('www.', '')\
            .replace('applications.', '')\
            .replace('democracy.', '')\
            .split('/')[0]\
            .replace('moderngov.', '')\
            .replace('ww5.', '')
        )
        out_filder = os.makedirs(path, exist_ok=True)
        out_file_name = "{0}.xml".format(op.replace('Get',''))
        out_file = open(os.path.join(path,out_file_name), 'wb')
        out_file.write(req.content)