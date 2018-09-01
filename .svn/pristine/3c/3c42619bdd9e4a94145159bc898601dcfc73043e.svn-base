var serverAddress = 'localhost:5000';

(function($, owner) {

	//JSON对象转GET请求字符串
	owner.JSON2Url = function (json) {
		var result = '?';
		for (key in json) {
			result = result + key + '=' + json[key] + '&';
		}
		//移除最后一个字符(如果json为空则刚好移除空格)
		result = result.Substring(0, result.Length - 1);
		return result;
	}

	//将JSON对象填充至form表单
	owner.JSON2Form = function(json, form) {
		if (!form) {
			return;
		}
		for (var x = 0; x < form.children.length; x++) {
			obj = form.children[x];
			for (key in json) {
				if (obj.name == key) {
					if (obj.localName == 'input') {
						obj.value = json[key];
					}
					if (obj.localName == 'select') {
						for (var y = 0; y < obj.children.length; y++) {
							option = obj.children[y];
							if (option.value == json[key]) {
								option.setAttribute('selected', 'selected');
							} else {
								if (option.getAttribute('selected')) {
									$(option).removeAttr("selected");
								}
							}
						}
					}
				}
			}
			//递归
			this.JSON2Form(json, obj);
		}
	}

	owner.getQueryString = function(name) {
		var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)");
		var r = window.location.search.substr(1).match(reg);
		if (r != null) {
			return  unescape(r[2]);
		}
		return null;
	}

	owner.getQueryStringDecodeURI = function(name) {
		var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)");
		var r = decodeURI(window.location.search).substr(1).match(reg);
		if (r != null) {
			return  unescape(r[2]);
		}
		return null;
	}
}($, window.app = {}))