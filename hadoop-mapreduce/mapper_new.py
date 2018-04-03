#!/usr/bin/env python

import sys
import re


def checkUrlReq(url):
    """校验是否为文件请求
    Args:
        url: 需要校验的url
    Returns:
        True / False
    """
    ReqFileTypes = ('.png', '.jpeg', '.bmp', '.jpg', '.js', '.css')

    url = url.strip()

    for types in ReqFileTypes:
        if types in url:
            return True
        else:
            continue

    return False


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
    res = None

    if checkUrlReq(url) is True:
        pass
    elif "?" in url:

        # /Invite/?Vid=105&Aid=103&MoCode=460060766536
        pos = url.index("?")

        res = url[:pos]

    elif ".php" in url:
        # 要处理 /.../index.php/controller/action/paramer/data ...
        pattern = re.compile(r".*/.*\.php/\w+/\w+")

        res = pattern.findall(url)

    else:
        res = url

    return res


if __name__ == "__main__":
    for line in sys.stdin:

        feature = line.strip()

        pattern = re.compile(r"[\w\.\/\:\+\&\=\?\-]+")

        words = pattern.findall(feature)

        urlLink = cleansUrl(words[6])
        if urlLink:
            print("%s\t%s\t%s" % words[0], urlLink, 1)