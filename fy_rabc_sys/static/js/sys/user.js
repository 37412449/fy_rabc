_operationType = null;
var _hiVue = new Vue({
    el: '#divHidden',
    data: {
        usrnodevalue: '',
    },
    methods: {}
});
var _usrTree = new Vue({
    el: '#usrTree',
    data: {
        props: {
            label: 'usrname',
            children: 'chilusr'
        },
        treedata: _usrTreeData,
        hisTreeData: _usrTreeData,
        expKeys: [],
    },
    created() {
        if (_usrTreeData.length > 0 && _usrTreeData[0].chilusr.length > 0) {
            exArr = []
            for (var i = 0; i < _usrTreeData[0].chilusr.length; i++) {
                exArr.push(_usrTreeData[0].chilusr[i].id)
            }
            this.expKeys = exArr;
        }

    },
    methods: {
        handleNodeClick(data) {
            // console.log(data);
            setUsrValue(data);
        },
        handleDragStart(node, ev) {
            //console.log('drag start', node);
        },
        handleDragEnter(draggingNode, dropNode, ev) {
            //console.log('tree drag enter: ', dropNode.label);
        },
        handleDragLeave(draggingNode, dropNode, ev) {
            //console.log('tree drag leave: ', dropNode.label);
        },
        handleDragOver(draggingNode, dropNode, ev) {
            //console.log('tree drag over: ', dropNode.label);
        },
        handleDragEnd(draggingNode, dropNode, dropType, ev) {
            //console.log('tree drag end: ', dropNode && dropNode.label, dropType);
            //console.log(draggingNode.data.org_code);
            //console.log(dropNode.data.id);
            if (draggingNode == undefined || draggingNode == null || dropNode == undefined || dropNode == null ||
                dropNode.data.org_code == draggingNode.data.org_code) {
                return;
            }
            this.$confirm('确定要调整该用户的组织架构吗？', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(() => {
                // -----------------接口调用开始
                axios({
                    method: 'POST',
                    url: '/sys/usr_chg_org',
                    headers: {'Content-Type': 'application/json'},

                    // 在请求之前对data传参进行格式转换
                    transformRequest: [function (data) {
                        data = JSON.stringify(data)
                        return data
                    }],
                    params: {},

                    // 传递的参数
                    data: {"optype": "update", "id": draggingNode.data.id, "org_code": dropNode.data.org_code},
                }).then((res) => {

                    if (res.data['code'] == 1) {
                        this.treedata = res.data['usrtree'];
                        this.hisTreeData = res.data['usrtree'];
                        //  _usrTree.$refs.eltree.setCurrentKey(res.data['curid']);
                    }
                    this.msg = res.data['msg'];
                    disabledBtn();
                }).catch(function (err) {
                    this.msg = err;
                    disabledBtn();
                });
                // -----------------接口调用结束
                this.$message({
                    type: 'success',
                    message: '组织架构已更改!'
                });
            }).catch(() => {
                this.treedata = this.hisTreeData;
                this.$message({
                    type: 'info',
                    message: '已取消组织架构更改!'
                });
            });
        },
        handleDrop(draggingNode, dropNode, dropType, ev) {
            //console.log('tree drop: ', dropNode.label, dropType);
        },

        // 拖拽时判定目标节点能否被放置。type 参数有三种情况：'prev'、'inner' 和 'next'，
        // 分别表示放置在目标节点前、插入至目标节点和放置在目标节点后
        allowDrop(draggingNode, dropNode, type) {
            if (dropNode.data.usrtype == 'P' && type == 'inner') {
                return true;
            } else {
                return false;
            }
        },

        // 判断节点能否被拖拽
        allowDrag(draggingNode) {
            // return draggingNode.data.label.indexOf('三级 3-2-2') === -1;
            return draggingNode.data.usrtype == 'U';
        }
    }

});

var _allRoles = [];
var fun_getAllRoles = function () {
    $.ajax({
        type: "post",
        dataType: "json",
        async: false,
        url: '/sys/usr_getroles',
        data: JSON.stringify({'id': 0}),
        headers: {'Content-Type': 'application/json'},
        error: function (xhr, err) {
            alert('请求失败，请检查（或重新登录），' + err + '!');
        },
        success: function (data) {
            if (data['code'] == 1) {
                _allRoles = data['roles'];
            }
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            _action.disSave = true;
            _action.disAdd = true;
            _action.disUpdate = true;
            _action.disCancle = true;
            window.location.replace('/admin/login/');
        }
    });
};

var fun_getUsrAllRols = function (usrcode) {
    var ownRols = []
    $.ajax({
        type: "post",
        dataType: "json",
        async: false,
        url: '/sys/usr_getselrol',
        data: JSON.stringify({'usercode': usrcode}),
        headers: {'Content-Type': 'application/json'},
        error: function (xhr, err) {
            alert('请求失败，请检查（或重新登录），' + err + '!');
        },
        success: function (data) {
            try {
                if (data['code'] == 1) {
                    ownRols = data['roles'];
                }
            } catch (e) {
                alert('身份校验失败，请重新登录!' + e);
            }
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            _action.disSave = true;
            _action.disAdd = true;
            _action.disUpdate = true;
            _action.disCancle = true;
            window.location.replace('/admin/login/');
        }
    });
    return ownRols;
};

function checkloginname(rule, value, callback) {
    if (value == '' || value == undefined || value == null || _operationType == 'update') {
        // console.log(callback);
        callback();
    } else {
        axios({
            method: 'POST',
            url: '/sys/usr_logname_exist',
            // headers: {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
            headers: {'Content-Type': 'application/json'},

            // 在请求之前对data传参进行格式转换
            transformRequest: [function (data) {
                data = JSON.stringify(data)
                return data
            }],
            params: {},

            // 传递的参数
            data: {'loginname': _action.form.login_name},
        }).then((res) => {
            if (res.data['code'] == 1) {
                callback(new Error('登录账号已经存在，请输入其它账号！'));
            } else {
                callback();
            }
        }).catch(function (err) {
            callback(new Error(err));
        });
    }
};

var _action = new Vue({
    el: '.actions',
    data:
        {
            form: {
                id: -1,
                org_code: '',
                user_code: '',
                user_name: '',
                nick_name: '',
                genders: [{id: 1, name: '男'}, {id: 0, name: '女'}],
                gender: '',
                id_num: '',
                tel: '',
                email: '',
                login_name: '',
                'usrstatus': [{id: 1, name: '有效'}, {id: 0, name: '无效'}],
                status: 1,
                remark: '',
            },
            disForm: true,
            'disAdd': true,
            'disUpdate': true,
            'disCancle': true,
            'disSave': true,
            'disDelete': true,
            disLogName: false,
            msg: '',
            activeName: 'usrDetail',
            accFlag: true,
            filValue: [],
            filData: [],

            rules: {
                user_name: [
                    {required: true, message: '用户名不能为空！', trigger: 'blur'},
                    {min: 2, max: 20, message: '长度需在2到20个字符间！', trigger: 'blur'}
                ],
                login_name: [{required: true, message: '登录名不能为空！', trigger: 'blur'},
                    {validator: checkloginname, trigger: 'blur'},
                    {min: 4, max: 20, message: '长度需在5到20个字符间！', trigger: 'blur'}],
                gender: [{required: true, message: '请选择性别！', trigger: 'change'}],
                id_num: [{validator: validateIdNo, trigger: 'blur'}],
                tel: [{validator: validatePhone, trigger: 'blur'}],
                email: [{validator: validateEMail, trigger: 'blur'}]
            },
        },
    created() {
        this.status = this.form.usrstatus[0].id;
        fun_getAllRoles();
    },
    methods: {
        getStatSelected() {
            console.log(this.form.status);
        },
        deleteUsr() {
            this.$confirm('确定要删除吗？', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(() => {
                // ----------------------------------
                axios({
                    method: 'POST',
                    url: '/sys/usr_del',
                    // headers: {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
                    headers: {'Content-Type': 'application/json'},

                    // 在请求之前对data传参进行格式转换
                    transformRequest: [function (data) {
                        data = JSON.stringify(data)
                        return data;
                    }],
                    params: {},

                    // 传递的参数
                    data: {'optype': 'delete', 'id': _hiVue.usrnodevalue.id},
                }).then((res) => {
                    if (res.data['code'] == 1) {
                        disabledBtn();
                        _usrTree.treedata = res.data['usrtree'];
                    }
                    this.msg = res.data['msg'];
                }).catch(function (err) {
                    this.msg = err;
                });

                // --------------------------
            }).catch(() => {
                this.$message({
                    type: 'info',
                    message: '取消删除!'
                });
            });
        },
        auto_change_py() {
            var py = changePY(this.form.user_name);
            this.form.login_name = py;
        },
        usrsave() {
            this.$refs.myForm.validate(valid => {
                if (!valid) {
                    this.msg = '输入验证未通过，请正确输入！';
                } else {

                    // 提交数据
                    axios({
                        method: 'POST',
                        url: '/sys/usr_save',
                        // headers: {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
                        headers: {'Content-Type': 'application/json'},

                        // 在请求之前对data传参进行格式转换
                        transformRequest: [function (data) {
                            data = JSON.stringify(data)
                            return data
                        }],
                        params: {},

                        // 传递的参数
                        data: getDicUsr(),
                    }).then((res) => {

                        if (res.data['code'] == 1) {
                            _usrTree.treedata = res.data['usrtree'];
                            _usrTree.hisTreeData = res.data['usrtree'];
                            //  _usrTree.$refs.eltree.setCurrentKey(res.data['curid']);
                        }
                        this.msg = res.data['msg'];
                        disabledBtn();
                    }).catch(function (err) {
                        this.msg = err;
                        disabledBtn();
                    });
                }
            });

        },
        generateData() {
            const data = [];
            const roles = _allRoles;
            const values = roles;
            roles.forEach((rol, index) => {
                data.push({
                    label: rol.name,
                    key: rol.code,
                    // rolcode: values[index]
                    rolcode: rol.name
                });
            });
            return data;
        },
        filterMethod(query, item) {
            return item.rolcode.indexOf(query) > -1;
        },
    }
});

var disabledBtn = function () {
    _action.disForm = true;
    _action.disAdd = true;
    _action.disUpdate = true;
    _action.disCancle = true;
    _action.disSave = true;
    _action.disDelete = true;
};

var getDicUsr = function () {
    user_roles = []
    if (_hiVue.usrnodevalue.usrtype == 'U' || _hiVue.usrnodevalue.usrtype == 'P') {
        user_roles = _action.filValue;
    } else {
        user_roles = []
    }
    return {
        "optype": _operationType,
        "id": _action.form.id,
        "user_name": _action.form.user_name.trim(),
        "org_code": _action.form.org_code,
        "user_code": _action.form.user_code,
        "nick_name": _action.form.nick_name.trim(),
        "gender": _action.form.gender,
        "id_num": _action.form.id_num.trim(),
        "tel": _action.form.tel.trim(),
        "email": _action.form.email.trim(),
        "login_name": _action.form.login_name.trim(),
        "status": _action.form.status,
        "remark": _action.form.remark.trim(),
        "user_roles": user_roles
    };
};

var setUsrValue = function (nodeData) {

    if (nodeData.usrtype == 'U') {
        _action.form.id = nodeData.id;
        _action.form.user_name = nodeData.usrname;
        _action.form.org_code = nodeData.org_code;
        _action.form.user_code = nodeData.user_code;
        _action.form.nick_name = nodeData.nick_name;
        _action.form.gender = nodeData.gender;
        _action.form.id_num = nodeData.id_num;
        _action.form.tel = nodeData.tel;
        _action.form.email = nodeData.email;
        _action.form.login_name = nodeData.login_name;
        _action.form.status = nodeData.status;
        _action.form.remark = nodeData.remark;
        _action.filData = _action.generateData();
        _action.disAdd = true;
        _action.disUpdate = false;
        _action.disCancle = false;
        _action.disLogName = true;
        tmpValues = fun_getUsrAllRols(nodeData.user_code);
        _action.filValue = tmpValues;
    } else {
        if (nodeData.usrtype == 'P') {
            _action.disAdd = false;
            _action.disUpdate = true;
        } else {
            _action.disAdd = true;
            _action.disUpdate = true;
        }

        _action.form.id = nodeData.id;
        _action.form.user_name = '';
        _action.form.user_code = '';
        _action.form.org_code = nodeData.org_code;
        _action.form.nick_name = '';
        _action.form.id_num = '';
        _action.form.tel = '';
        _action.form.email = '';
        _action.form.login_name = '';
        _action.form.remark = '';
        _action.filData = _action.generateData();
        _action.filValue = [];
    }
    _action.disForm = true;
    _action.disCancle = true;
    _action.disSave = true;
    _action.msg = '';
    _action.$refs['myForm'].clearValidate();

    // 保存原始值
    _hiVue.usrnodevalue = nodeData;

    // 检查该节点是否可以删除
    if (nodeData.usrtype == 'U') {
        var tmpFlag = checkNodeDel(nodeData.id);
        if (tmpFlag == 0) {
            _action.disDelete = false;
        } else {
            _action.disDelete = true;
        }
    } else {
        _action.disDelete = true;
    }
};
var cancleSetValue = function () {

    if (_hiVue.usrnodevalue.usrtype == 'U') {
        _action.form.id = _hiVue.usrnodevalue.id;
        _action.form.user_name = _hiVue.usrnodevalue.usrname;
        _action.form.org_code = _hiVue.usrnodevalue.org_code;
        _action.form.user_code = _hiVue.usrnodevalue.user_code;
        _action.form.nick_name = _hiVue.usrnodevalue.nick_name;
        _action.form.id_num = _hiVue.usrnodevalue.id_num;
        _action.form.tel = _hiVue.usrnodevalue.tel;
        _action.form.email = _hiVue.usrnodevalue.email;
        _action.form.login_name = _hiVue.usrnodevalue.login_name;
        _action.form.status = _hiVue.usrnodevalue.status;
        _action.form.remark = _hiVue.usrnodevalue.remark;
        _action.disAdd = true;
        _action.disUpdate = false;
        _action.filData = _action.generateData();
        tmpValues = fun_getUsrAllRols(_hiVue.usrnodevalue.user_code);
        _action.filValue = tmpValues;
        _action.disLogName = true;
    } else {
        if (_hiVue.usrnodevalue.usrtype == 'P') {
            _action.disAdd = false;
            _action.disUpdate = true;
            _action.disLogName = false;
            _action.filData = _action.generateData();
            _action.filValue = [];

        } else {
            _action.disAdd = true;
            _action.disUpdate = true;
        }
        _action.form.id = _hiVue.usrnodevalue.id;
        _action.form.org_code = _hiVue.usrnodevalue.org_code;
        _action.form.user_code = '';
        _action.form.user_name = '';
        _action.form.org_code = '';
        _action.form.nick_name = '';
        _action.form.id_num = '';
        _action.form.tel = '';
        _action.form.email = '';
        _action.form.login_name = '';
        _action.form.remark = '';
    }
    _action.disForm = true;
    _action.disSave = true;
    _operationType = null;
    _action.msg = '';
    _action.$refs['myForm'].clearValidate();
};
var addControl = function () {
    _action.disForm = false;
    _action.disAdd = true;
    _action.disUpdate = false;
    _action.disCancle = false;
    _action.disSave = false;
    _action.form.remark = '';
    _operationType = 'add';
    _action.filData = _action.generateData();
    _action.filValue = [];
    _action.disLogName = false;

};
var updateControl = function () {
    _action.disForm = false;
    _action.disAdd = false;
    _action.disUpdate = true;
    _action.disCancle = false;
    _action.disSave = false;
    _operationType = 'update';
};

var checkNodeDel = function (nodeId) {
    var reFlag = -1;
    $.ajax({
        type: "post",
        dataType: "json",
        async: false,
        url: '/sys/usr_check',
        data: JSON.stringify({'optype': 'delete', 'id': nodeId}),
        headers: {'Content-Type': 'application/json'},
        error: function (xhr, err) {
            _action.msg = '请求失败，请检查，' + err + '!';
        },
        success: function (data) {
            reFlag = data['code'];
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            window.location.replace('/admin/login/');
        }
    });
    return reFlag;
};


var changePY = function (chs) {
    var rePY = '';
    $.ajax({
        type: "post",
        dataType: "json",
        async: false,
        url: '/sys/comm_ch_py',
        data: JSON.stringify({'optype': 'view', 'data': chs}),
        headers: {'Content-Type': 'application/json'},
        error: function (xhr, err) {
            _action.msg = '请求失败，请检查，' + err + '!';
        },
        success: function (data) {
            if (data['code'] == 1) {
                rePY = data['data'];
            }
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
        }
    });
    return rePY;
};