from config import *

class ResponseProtocol(object):
    """server response protocal farmat string handle"""

    """
    generate user login result string format
    @param result: login result, 0: failed, 1: successs 
    @param nickname: user nickname
    @param username: user username
    @return: string
    """
    @staticmethod
    def response_login_result(result, nickname, username) -> str:
        return DELIMITER.join([RESPONSE_LOGIN_RESULT, result, nickname, username])

    """
    generate chat message string format
    @param nickname: sender
    @param message: chat message
    @return: string
    """
    @staticmethod
    def response_chat(sender_nickname, message) -> str:
        return DELIMITER.join([RESPONSE_CHAT, sender_nickname, message])