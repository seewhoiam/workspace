#!/usr/bin/env python

import sys
import re


def checkUrlReq(url):
    """
    """
    ReqFileTypes = ('png', 'jpeg', 'bmp', 'jpg', 'js', 'css')

    url = url.strip()

    for types in ReqFileTypes:
        if types in url:
            return 1
        else:
            continue

    return 0

def cleansUrl(url):
    '''过滤掉不符合要求的url，去掉url携带的参数。

    去掉包含 png、jpeg、bmp、jpg、js、css等文件格式请求，以及去掉url中携带的参数。

    Args:
        url: 需要处理的url
    Returns:
        处理后的url
    Raises:
        列出所有异常
    '''
    
    if checkUrlReq(url) == 1:
        pass
    

for line in open("data.txt"):

    line = line.strip()

    pattern = re.compile(r"[\w\.\/\:\+\&\=\?\-]+")

    words = pattern.findall(line)

    print(cleansUrl(words[6]))

    # data format
    # 127.0.0.1 - - [26/Oct/2017:15:02:57 +0800] "POST /commonApi/service.php/Dispatch/putOn HTTP/1.1" 200 46
    
    # print data
    # if words:
    #     print("%s\t%s\t%s\t%s\t" %
    #           (words[0], words[3], words[5], cleansUrl(words[6])))
    
    # break   


    
    
    
    
if __name__ == "__main__":
    print("main")
