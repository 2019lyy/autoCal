from flask import Blueprint
import json

bp = Blueprint('logger', __name__, url_prefix='/logger')

logger = ['我是logger，我也是服务器启动的第一条信息']

#前台接口，获取当前log
@bp.route('/get_logger')
def get_logger():
	global logger
	copy = logger[:]
	logger.clear()
	return json.dumps(copy)