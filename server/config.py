# 数据协议相关配置
REQUEST_LOGIN = '0001' # 登录请求
REQUEST_CHAT = '0002' # 聊天请求
RESPONSE_LOGIN_RESULT = '1001' # 登录相应
RESPONSE_CHAT = '1002' # chat response
DELIMITER = '|' # 分隔符
# server config
SERVER_IP = '127.0.0.1'
SERVER_PORT = 8888
MAX_CONNECTIONS = 128
# socket wrapper
RECV_BUFFER_SIZE = 512