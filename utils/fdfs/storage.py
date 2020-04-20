from django.core.files.storage import Storage
from fdfs_client.client import Fdfs_client, get_tracker_conf
from django.conf import settings

class FDFSStorage(Storage):
    def __init__(self, client_conf = None, base_url=None):
        if client_conf is None:
            client_conf = settings.FDFS_CLIENT_CONF
        self.client_conf = client_conf

        if base_url is None:
            base_url = settings.FDFS_URL
        self.base_url = base_url


    def _open(self, name, mode='rb'):
        pass
    def _save(self, name, content):
        '''保存文件'''
        # name
        # 创建上传

        conf_path = get_tracker_conf(self.client_conf)
        client = Fdfs_client(conf_path)
        #
        print('*'*100)
        print(client)
        res = client.upload_by_buffer(content.read())
        print(res)

        if res.get('Status') != 'Upload successed.':
            raise Exception('上传文件到fasf dfs失败')
        filename = res.get('Remote file_id')

        return filename.decode()
    # 1.jpg
    def exists(self, name):
        '''Django判断文件名是否可用'''
        return False

    def url(self, name):
        '''返回访问文件的url路径'''
        #
        print(self.base_url+name)
        return self.base_url + name
        # return self.base_url + name