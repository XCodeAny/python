# coding = utf-8

'''
@author = super_fazai
@File    : logging_demo.py
@Time    : 2017/8/14 09:26
@connect : superonesfazai@gmail.com
'''

'''
对于代码量较大的工程，建议使用logging模块进行输出。
该模块是线程安全的，可将日志信息输出到控制台、写入文件、使用TCP/UDP协议发送到网络等等。

默认情况下logging模块将日志输出到控制台(标准出错)，
且只显示大于或等于设置的日志级别的日志。
日志级别由高到低为CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET，默认级别为WARNING。
'''

# 以下示例将日志信息分别输出到控制台和写入文件：

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] at %(filename)s, %(lineno)d: %(message)s',
    datefmt='%Y-%m-%d(%a)%H:%M:%S',
    filename='out.txt',
    filemode='w'
)

# 将大于或等于INFO级别的日志信息输出到StreamHandler(默认为标准错误)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('[%(levelname)-8s] %(message)s')  # 屏显实时查看, 无需时间
console.setFormatter(formatter)
logging.getLogger().addHandler(console)

logging.debug('gubed')
logging.info('ofni')
logging.critical('lacitirc')