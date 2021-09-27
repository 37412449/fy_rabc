//去除字符串头尾空格或指定字符
String.prototype.Trim = function (c) {
    if (c == null || c == "") {
        var str = this.replace(/^s*/, '');
        var rg = /s/;
        var i = str.length;
        while (rg.test(str.charAt(--i))) ;
        return str.slice(0, i + 1);
    } else {
        var rg = new RegExp("^" + c + "*");
        var str = this.replace(rg, '');
        rg = new RegExp(c);
        var i = str.length;
        while (rg.test(str.charAt(--i))) ;
        return str.slice(0, i + 1);
    }
}
//去除字符串头部空格或指定字符
String.prototype.TrimStart = function (c) {
    if (c == null || c == "") {
        var str = this.replace(/^s*/, '');
        return str;
    } else {
        var rg = new RegExp("^" + c + "*");
        var str = this.replace(rg, '');
        return str;
    }
}

//去除字符串尾部空格或指定字符
String.prototype.TrimEnd = function (c) {
    if (c == null || c == "") {
        var str = this;
        var rg = /s/;
        var i = str.length;
        while (rg.test(str.charAt(--i))) ;
        return str.slice(0, i + 1);
    } else {
        var str = this;
        var rg = new RegExp(c);
        var i = str.length;
        while (rg.test(str.charAt(--i))) ;
        return str.slice(0, i + 1);
    }
}
String.prototype.EndWith = function (str) {
    var reg = new RegExp(str + "$");
    return reg.test(this);
}

// 前端获取url参数
function getURLParValue(parName) {
    var url = location.search; //获取url中"?"符后的字串
    var theRequest = new Object();
    if (url.indexOf("?") != -1) {
        var str = url.substr(1);
        strs = str.split("&");
        for (var i = 0; i < strs.length; i++) {
            theRequest[strs[i].split("=")[0]] = (strs[i].split("=")[1]);
        }
    }
    if (theRequest[parName] != null && theRequest[parName] != undefined) {
        return theRequest[parName].replace('%2F', '/');
    } else {
        return null;
    }
}

// 将有网址地址的的字串，识别成链接<a>的html代码
String.prototype.httpHtml = function () {
    var reg = /(http:\/\/|https:\/\/)((\w|=|\?|\.|\/|&|-|#|:)+)/g;
    return this.replace(reg, '<a href="$1$2" target="_blank">$1$2</a>');
};


// 获取当前日期（单数补'0'）
function getNowFormatDate() {
    var day = new Date();
    var Year = 0;
    var Month = 0;
    var Day = 0;
    var CurrentDate = "";
    //初始化时间
    //Year       = day.getYear();//有火狐下2008年显示108的bug
    Year = day.getFullYear();//ie火狐下都可以
    Month = day.getMonth() + 1;
    Day = day.getDate();
    CurrentDate += Year + "-";
    if (Month >= 10) {
        CurrentDate += Month + "-";
    } else {
        CurrentDate += "0" + Month + "-";
    }
    if (Day >= 10) {
        CurrentDate += Day;
    } else {
        CurrentDate += "0" + Day;
    }
    return CurrentDate;
}

// 获取页面cookie值
function getCookie(name) {
    var arr, reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");
    if (arr = document.cookie.match(reg))
        return unescape(arr[2]);
    else
        return null;
}

//s20是代表20秒
//h是指小时，如12小时则是：h12
//d是天数，30天则：d30
function setCookie(name, value, time) {
    var strsec = getsec(time);
    var exp = new Date();
    exp.setTime(exp.getTime() + strsec * 1);
    document.cookie = name + "=" + escape(value) + ";expires=" + exp.toGMTString();
}

function getsec(str) {
    var str1 = str.substring(1, str.length) * 1;
    var str2 = str.substring(0, 1);
    if (str2 == "s") {
        return str1 * 1000;
    } else if (str2 == "h") {
        return str1 * 60 * 60 * 1000;
    } else if (str2 == "d") {
        return str1 * 24 * 60 * 60 * 1000;
    }
}

function setCSRF() {
    var csrftoken = $.cookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

}

function getReqHeader(postUrl) {
    setCSRF();
    var reHead = null;
    $.ajax({
        type: "post",
        dataType: "json",
        async: false,
        url: postUrl + 'comm',
        data: JSON.stringify({
            'data': 'fun_gettoken',
        }),
        headers: {'Content-Type': 'application/json'},
        error: function (xhr, err) {
            alert('请求失败，请检查，' + err + '!');
        },
        complete: function (data) {
            if (data == null || data == undefined) {
                reHead = null;
            } else {
                message = JSON.parse(data['responseText']).result;
                if (message == null || message == undefined) {
                    reHead = null;
                } else {
                    reHead = {"Authorization": "Token " + message, "Content-Type": "application/json"}

                }
            }
        }
    });
    return reHead;
}

// 获取cookie值
var getCookies = function (postUrl) {

    var clientId = getCookie('ai_cs_clientId');
    if (clientId != null && clientId != undefined && clientId != 'undefined') {
        return;
    }
    setCSRF();
    $.ajax({
        type: "post",
        dataType: "json",
        async: false,
        url: postUrl + 'comm',
        data: JSON.stringify({
            'data': 'fun_getclientid',
        }),
        headers: {'Content-Type': 'application/json'},
        error: function (xhr, err) {
            alert('请求失败，请检查，' + err + '!');
        },
        complete: function (data) {
            message = JSON.parse(data['responseText']).result;
            setCookie("ai_cs_clientId", message, "d2");
            document.cookie = '"ai_cs_clientId":"' + message + '"';
        }
    });
};

function createJC(link) {
    var len = link.length;
    var n = 0;
    start();

    function start() {
        var jc = null;
        var dataT = new Date().getTime();
        if (link[n].EndWith('.js')) {
            jc = document.createElement('script');
            jc.type = 'text/javascript';
            jc.src = '/static/' + link[n] + '?t=' + dataT;
            document.body.appendChild(jc);
        } else if (link[n].EndWith('.css')) {
            jc = document.createElement('link');
            jc.rel = 'stylesheet';
            jc.href = '/static/' + link[n] + '?t=' + dataT;
            document.getElementsByTagName("head")[0].appendChild(jc);
        }

        jc.onload = function () {
            n++;
            if (n < len) {
                start();
            }
        }
    }
}