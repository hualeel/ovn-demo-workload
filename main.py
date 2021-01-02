# -*- coding:utf-8 -*-
"""
Author:
名称：kubeovn demo
功能描述：
"""

from flask import Flask, current_app, redirect, url_for
from flask_cors import *
import socket
import os

app = Flask(__name__,
            static_url_path='/python',  # 访问静态资源的url前缀，默认值是static
            static_folder='static',  # 静态文件目录，默认就是static
            template_folder='templates',  # 模板文件的目录，默认是templates
            )


@app.route('/get-pod', methods=["GET"])
@cross_origin()
def get_self_name_ip():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print "Host name: %s" % host_name
    print "IP address: %s" % ip_address
    return "Host name: %s" % host_name + "<br>" + "IP address: %s" % ip_address


if __name__ == '__main__':
    # 通过url_map可以查看整个flask中的路由信息
    print (app.url_map)

    # 启动flask程序
    service_port = os.getenv("SERVICE_PORT")
    app.run(host="0.0.0.0", port=service_port)
