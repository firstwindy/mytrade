import logging
from logging.handlers import TimedRotatingFileHandler

def logger_DEV(name=None):
    #1 logger instance를 만든다.
    logger = logging.getLogger(name)

    #2 logger의 level을 가장 낮은 수준인 DEBUG로 설정해둔다.
    logger.setLevel(logging.DEBUG)

    #3 formatter 지정
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    
    #4 handler instance 생성
    console = logging.StreamHandler()
    file_handler = logging.FileHandler(filename="test.log")
 
    #5 handler 별로 다른 level 설정
    console.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)

    #6 handler 출력 format 지정
    console.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    #7 logger에 handler 추가
    logger.addHandler(console)
    logger.addHandler(file_handler)

    return logger


def hi() :
    print("hi")

def logger_File(name=None):

    #1 logger instance를 만든다.
    logger = logging.getLogger(name)

    #2 logger의 level을 가장 낮은 수준인 DEBUG로 설정해둔다.
    logger.setLevel(logging.DEBUG)

    #3 formatter 지정
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # TimedRotatingFileHandler 설정 (일별로 로그 파일을 회전)
    handler = TimedRotatingFileHandler(filename="trade.log", when="midnight", interval=1, backupCount=7)
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    logger.addHandler(handler)


    return logger



def logger_DEBUG(name=None):
    #1 logger instance를 만든다.
    logger = logging.getLogger(name)

    #2 logger의 level을 가장 낮은 수준인 DEBUG로 설정해둔다.
    logger.setLevel(logging.DEBUG)

    #3 formatter 지정
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # TimedRotatingFileHandler 설정 (일별로 로그 파일을 회전)
    handler = TimedRotatingFileHandler(filename="trade.log", when="midnight", interval=1, backupCount=7)
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    handlerD = TimedRotatingFileHandler(filename="tradeDEBUG.log", when="midnight", interval=1, backupCount=7)
    handlerD.setLevel(logging.DEBUG)
    handlerD.setFormatter(formatter)
    logger.addHandler(handlerD)

    return logger


def logger_console(name=None):
    #1 logger instance를 만든다.
    logger = logging.getLogger(name)

    #2 logger의 level을 가장 낮은 수준인 DEBUG로 설정해둔다.
    logger.setLevel(logging.DEBUG)

    #3 formatter 지정
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    
    #4 handler instance 생성
    console = logging.StreamHandler()
 
    #5 handler 별로 다른 level 설정
    console.setLevel(logging.INFO)

    #6 handler 출력 format 지정
    console.setFormatter(formatter)

    #7 logger에 handler 추가
    logger.addHandler(console)

    return logger