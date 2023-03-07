# -*- coding: utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_cors import CORS
from app.NlpTasks.apis import apis as api_blueprint
from app_logging import get_logger
logger = get_logger()


app = Flask(__name__, static_url_path='')
# load config from config.py
app.config.from_pyfile('config.py')
# 初始化定时任务
from app.NlpTasks.apis.total_tasks import scheduler
scheduler.init_app(app)
scheduler.start()
# # 修改调度器执行组件冗余日志级别
# logger.getLogger('apscheduler.executors.default').setLevel(logger.WARNING)
# 处理跨域问题
# 处理跨域问题
CORS(app)


@app.route('/')
def index():
    return "APIs Server"


app.register_blueprint(api_blueprint, url_prefix='/api/nlptasks/study')

if __name__ == '__main__':
    host = app.config.get('APP_HOST', '127.0.0.1')
    port = app.config.get('APP_PORT', 10000)

    # set web access log
    access = logging.getLogger('werkzeug')
    access_handler = RotatingFileHandler("log/access.log",
                                         maxBytes=500000, backupCount=2, encoding='UTF-8')
    access.addHandler(access_handler)
    logger.info('应用启动. ' + host + ':' + str(port))
    
    try:
        from werkzeug.contrib.fixers import ProxyFix
    except:
        from werkzeug.middleware.proxy_fix import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app)

    # app.run(host=host, port=port, threaded=True, debug=True)
    app.run(host=host, port=port, threaded=True)
