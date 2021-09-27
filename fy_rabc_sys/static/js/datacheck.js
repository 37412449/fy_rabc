function validateIP(rule, value, callback) {
    if (value == '' || value == undefined || value == null) {
        callback();
    } else {
        const reg = /^(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])$/;
        if ((!reg.test(value)) && value != '') {
            callback(new Error('请输入正确的IP地址！'));
        } else {
            callback();
        }
    }
}

/* 是否手机号码或者固话*/
function validatePhoneTwo(rule, value, callback) {
    const reg = /^((0\d{2,3}-\d{7,8})|(1[34578]\d{9}))$/;
    ;
    if (value == '' || value == undefined || value == null) {
        callback();
    } else {
        if ((!reg.test(value)) && value != '') {
            callback(new Error('请输入正确的电话号码或者固话号码！'));
        } else {
            callback();
        }
    }
}

/* 是否固话 */
function validateTelphone(rule, value, callback) {
    const reg = /0\d{2}-\d{7,8}/;
    if (value == '' || value == undefined || value == null) {
        callback();
    } else {
        if ((!reg.test(value)) && value != '') {
            callback(new Error('请输入正确的固话（格式：区号+号码,如010-1234567）！'));
        } else {
            callback();
        }
    }
}

/* 是否手机号码*/
function validatePhone(rule, value, callback) {
    const reg = /^[1][3,4,5,7,8][0-9]{9}$/;
    if (value == '' || value == undefined || value == null) {
        callback();
    } else {
        if ((!reg.test(value)) && value != '') {
            callback(new Error('请输入正确的电话号码！'));
        } else {
            callback();
        }
    }
}

/* 是否身份证号码*/
function validateIdNo(rule, value, callback) {
    const reg = /^(^[1-9]\d{7}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}$)|(^[1-9]\d{5}[1-9]\d{3}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])((\d{4})|\d{3}[X])$)$/;
    if (value == '' || value == undefined || value == null) {
        callback();
    } else {
        if ((!reg.test(value)) && value != '') {
            callback(new Error('请输入正确的身份证号码！'));
        } else {
            callback();
        }
    }
}

/*不是身份证号码*/
function validateIdNoNot(rule, value, callback) {
    const reg = /^(^[1-9]\d{7}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}$)|(^[1-9]\d{5}[1-9]\d{3}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])((\d{4})|\d{3}[X])$)$/;
    if (value == '' || value == undefined || value == null) {
        callback();
    } else {
        if ((reg.test(value)) && value != '') {
            callback(new Error('请不要填写身份证号码！'));
        } else {
            callback();
        }
    }
}

/* 是否邮箱*/
function validateEMail(rule, value, callback) {
    const reg = /^([a-zA-Z0-9]+[-_\.]?)+@[a-zA-Z0-9]+\.[a-z]+$/;
    if (value == '' || value == undefined || value == null) {
        callback();
    } else {
        if (!reg.test(value)) {
            callback(new Error('请输入正确的邮箱地址！'));
        } else {
            callback();
        }
    }
}

/* 合法uri*/
function validateURL(textval) {
    const urlregex = /^(https?|ftp):\/\/([a-zA-Z0-9.-]+(:[a-zA-Z0-9.&%$-]+)*@)*((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}|([a-zA-Z0-9-]+\.)*[a-zA-Z0-9-]+\.(com|edu|gov|int|mil|net|org|biz|arpa|info|name|pro|aero|coop|museum|[a-zA-Z]{2}))(:[0-9]+)*(\/($|[a-zA-Z0-9.,?'\\+&%$#=~_-]+))*$/;
    return urlregex.test(textval);
}

/*验证内容是否英文数字以及下划线*/
function isPassword(rule, value, callback) {
    const reg = /^[_a-zA-Z0-9]+$/;
    if (value == '' || value == undefined || value == null) {
        callback();
    } else {
        if (!reg.test(value)) {
            callback(new Error('账号、密码仅由英文字母，数字以及下划线组成！'));
        } else {
            callback();
        }
    }
}

/*验证内容只能输入整数和两位小数*/
function isDecimalsAndNumbers(rule, value, callback) {
    const reg = /^[0-9]+(\.[0-9]{1,2})?$/;
    if (value == '' || value == undefined || value == null) {
        callback();
    } else {
        if (!reg.test(value)) {
            callback(new Error('只能输入整数和两位小数！'));
        } else {
            callback();
        }
    }
}

/*自动检验数值的范围*/
function checkMax20000(rule, value, callback) {
    if (value == '' || value == undefined || value == null) {
        callback();
    } else if (!Number(value)) {
        callback(new Error('请输入[1,20000]之间的数字！'));
    } else if (value < 1 || value > 20000) {
        callback(new Error('请输入[1,20000]之间的数字！'));
    } else {
        callback();
    }
}

//验证数字输入框最大数值,32767
function checkMaxVal(rule, value, callback) {
    if (value < 0 || value > 32767) {
        callback(new Error('请输入[0,32767]之间的数字！'));
    } else {
        callback();
    }
}

//验证是否1-99之间
function isOneToNinetyNine(rule, value, callback) {
    if (!value) {
        return callback(new Error('输入不可以为空！'));
    }
    setTimeout(() => {
        if (!Number(value)) {
            callback(new Error('请输入正整数！'));
        } else {
            const re = /^[1-9][0-9]{0,1}$/;
            const rsCheck = re.test(value);
            if (!rsCheck) {
                callback(new Error('请输入正整数，值为【1,99】！'));
            } else {
                callback();
            }
        }
    }, 0);
}

// 验证是否整数
function isInteger(rule, value, callback) {
    if (!value) {
        return callback(new Error('输入不可以为空！'));
    }
    setTimeout(() => {
        if (!Number(value)) {
            callback(new Error('请输入正整数'));
        } else {
            const re = /^[0-9]*[1-9][0-9]*$/;
            const rsCheck = re.test(value);
            if (!rsCheck) {
                callback(new Error('请输入正整数！'));
            } else {
                callback();
            }
        }
    }, 0);
}

// 验证是否整数,非必填
function isIntegerNotMust(rule, value, callback) {
    if (!value) {
        callback();
    }
    setTimeout(() => {
        if (!Number(value)) {
            callback(new Error('请输入正整数！'));
        } else {
            const re = /^[0-9]*[1-9][0-9]*$/;
            const rsCheck = re.test(value);
            if (!rsCheck) {
                callback(new Error('请输入正整数！'));
            } else {
                callback();
            }
        }
    }, 1000);
}

// 验证是否是[0-1]的小数
function isDecimal(rule, value, callback) {
    if (!value) {
        return callback(new Error('输入不可以为空！'));
    }
    setTimeout(() => {
        if (!Number(value)) {
            callback(new Error('请输入[0,1]之间的数字！'));
        } else {
            if (value < 0 || value > 1) {
                callback(new Error('请输入[0,1]之间的数字！'));
            } else {
                callback();
            }
        }
    }, 100);
}

// 验证是否是[1-10]的小数,即不可以等于0
function isBtnOneToTen(rule, value, callback) {
    if (typeof value == 'undefined') {
        return callback(new Error('输入不可以为空！'));
    }
    setTimeout(() => {
        if (!Number(value)) {
            callback(new Error('请输入正整数，值为[1,10]！'));
        } else {
            if (!(value == '1' || value == '2' || value == '3' || value == '4' || value == '5' || value == '6' || value == '7' || value == '8' || value == '9' || value == '10')) {
                callback(new Error('请输入正整数，值为[1,10]！'));
            } else {
                callback();
            }
        }
    }, 100);
}

// 验证是否是[1-100]的小数,即不可以等于0
function isBtnOneToHundred(rule, value, callback) {
    if (!value) {
        return callback(new Error('输入不可以为空！'));
    }
    setTimeout(() => {
        if (!Number(value)) {
            callback(new Error('请输入整数，值为[1,100]！'));
        } else {
            if (value < 1 || value > 100) {
                callback(new Error('请输入整数，值为[1,100]！'));
            } else {
                callback();
            }
        }
    }, 100);
}

//验证银行卡号
function isBankCount(rule, bankno, callback) {
    var lastNum = bankno.substr(bankno.length - 1, 1); //取出最后一位（与luhn进行比较）
    var first15Num = bankno.substr(0, bankno.length - 1); //前15或18位
    var newArr = new Array();
    for (var i = first15Num.length - 1; i > -1; i--) { //前15或18位倒序存进数组
        newArr.push(first15Num.substr(i, 1));
    }
    var arrJiShu = new Array(); //奇数位*2的积 <9
    var arrJiShu2 = new Array(); //奇数位*2的积 >9
    var arrOuShu = new Array(); //偶数位数组
    for (var j = 0; j < newArr.length; j++) {
        if ((j + 1) % 2 == 1) { //奇数位
            if (parseInt(newArr[j]) * 2 < 9) arrJiShu.push(parseInt(newArr[j]) * 2);
            else arrJiShu2.push(parseInt(newArr[j]) * 2);
        } else //偶数位
            arrOuShu.push(newArr[j]);
    }

    var jishu_child1 = new Array(); //奇数位*2 >9 的分割之后的数组个位数
    var jishu_child2 = new Array(); //奇数位*2 >9 的分割之后的数组十位数
    for (var h = 0; h < arrJiShu2.length; h++) {
        jishu_child1.push(parseInt(arrJiShu2[h]) % 10);
        jishu_child2.push(parseInt(arrJiShu2[h]) / 10);
    }

    var sumJiShu = 0; //奇数位*2 < 9 的数组之和
    var sumOuShu = 0; //偶数位数组之和
    var sumJiShuChild1 = 0; //奇数位*2 >9 的分割之后的数组个位数之和
    var sumJiShuChild2 = 0; //奇数位*2 >9 的分割之后的数组十位数之和
    var sumTotal = 0;
    for (var m = 0; m < arrJiShu.length; m++) {
        sumJiShu = sumJiShu + parseInt(arrJiShu[m]);
    }

    for (var n = 0; n < arrOuShu.length; n++) {
        sumOuShu = sumOuShu + parseInt(arrOuShu[n]);
    }

    for (var p = 0; p < jishu_child1.length; p++) {
        sumJiShuChild1 = sumJiShuChild1 + parseInt(jishu_child1[p]);
        sumJiShuChild2 = sumJiShuChild2 + parseInt(jishu_child2[p]);
    }
    //计算总和
    sumTotal = parseInt(sumJiShu) + parseInt(sumOuShu) + parseInt(sumJiShuChild1) + parseInt(sumJiShuChild2);

    //计算luhn值
    var k = parseInt(sumTotal) % 10 == 0 ? 10 : parseInt(sumTotal) % 10;
    var luhn = 10 - k;

    if (lastNum == luhn) {
        callback();
    } else {
        callback(new Error('银行卡号必须符合luhn校验！'));
    }

}

// 验证是否是[0-100]的小数
function isBtnZeroToHundred(rule, value, callback) {
    if (!value) {
        return callback(new Error('输入不可以为空！'));
    }
    setTimeout(() => {
        if (!Number(value)) {
            callback(new Error('请输入[1,100]之间的数字！'));
        } else {
            if (value < 0 || value > 100) {
                callback(new Error('请输入[1,100]之间的数字！'));
            } else {
                callback();
            }
        }
    }, 100);
}

// 验证端口是否在[0,65535]之间
function isPort(rule, value, callback) {
    if (!value) {
        return callback(new Error('输入不可以为空！'));
    }
    setTimeout(() => {
        if (value == '' || typeof (value) == undefined) {
            callback(new Error('请输入端口值！'));
        } else {
            const re = /^([0-9]|[1-9]\d|[1-9]\d{2}|[1-9]\d{3}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5])$/;
            const rsCheck = re.test(value);
            if (!rsCheck) {
                callback(new Error('请输入在[0-65535]之间的端口值！'));
            } else {
                callback();
            }
        }
    }, 100);
}

// 验证端口是否在[0,65535]之间，非必填,isMust表示是否必填
function isCheckPort(rule, value, callback) {
    if (!value) {
        callback();
    }
    setTimeout(() => {
        if (value == '' || typeof (value) == undefined) {
            //callback(new Error('请输入端口值'));
        } else {
            const re = /^([0-9]|[1-9]\d|[1-9]\d{2}|[1-9]\d{3}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5])$/;
            const rsCheck = re.test(value);
            if (!rsCheck) {
                callback(new Error('请输入在[0-65535]之间的端口值！'));
            } else {
                callback();
            }
        }
    }, 100);
}

//验证邮编
function validateZipCode(rule, value, callback) {
    if (!value) {
        return callback(new Error('输入不可以为空！'));
    }
    setTimeout(() => {
        const re = /^[0-8][0-7]\d{4}$/
        const rsCheck = re.test(value);
        if (!rsCheck) {
            callback(new Error('邮政编码格式不正确！'));
        } else {
            callback();
        }
    }, 100);
}

//不判断是否为空
function validateZipCode2(rule, value, callback) {
    if (!value) {
        callback();
    }
    setTimeout(() => {
        const re = /^[0-8][0-7]\d{4}$/
        const rsCheck = re.test(value);
        if (!rsCheck) {
            callback(new Error('邮政编码格式不正确！'));
        } else {
            callback();
        }
    }, 100);
}


/* 小写字母*/
function validateLowerCase(str) {
    const reg = /^[a-z]+$/;
    return reg.test(str);
}

/*保留2为小数*/
function validatetoFixedNew(str) {
    return str;
}

/* 验证key*/
//  function validateKey(str) {
//     var reg = /^[a-z_\-:]+$/;
//     return reg.test(str);
// }

/* 大写字母*/
function validateUpperCase(str) {
    const reg = /^[A-Z]+$/;
    return reg.test(str);
}

/* 大小写字母*/
function validatAlphabets(str) {
    const reg = /^[A-Za-z]+$/;
    return reg.test(str);
}
