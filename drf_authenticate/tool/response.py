from rest_framework.response import Response
from rest_framework import status

class CustomizeResponse(Response):

    def __init__(self, data_status=status.HTTP_200_OK, data_message=None, results=None,
                 http_status=None, headers=None, exception=False, **kwargs):
        # 定义响应回去的数据
        data = {
            "status": data_status,
            "message": data_message,
        }

        # 判断results是否有结果
        if results is not None:
            data['results'] = results

        # 如果还需要传递自定义的参数  使用kwargs接收
        # 如果kwargs有值则将值添加到 data中  如果没值则不作任何操作
        data.update(kwargs)

        # 获取一个response对象  将自定义的response响应回去
        super().__init__(data=data, status=http_status, headers=headers, exception=exception)
