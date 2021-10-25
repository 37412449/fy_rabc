_operationType = null;
var _hiVue = new Vue({
    el: '#divHidden',
    data: {
        resnodevalue: '',
        dialogVisible: false,
        infos: '值不能为空！'
    },
    methods: {
        handleClose(done) {
            this.$confirm('确定关闭吗？').then(_ => {
                done();
            }).catch(_ => {
            });
        }
    }
});

var _resTree = new Vue({
    el: '#resTree',
    data: {
        props: {
            label: 'resname',
            children: 'chilres'
        },
        treedata: _resTreeData,
        expKeys: [],
    },
    created() {
        if (_resTreeData.length > 0 && _resTreeData[0].chilres.length > 0) {
            exArr = []
            for (var i = 0; i < _resTreeData[0].chilres.length; i++) {
                exArr.push(_resTreeData[0].chilres[i].id)
            }
            this.expKeys = exArr;
        }
    },
    methods: {
        handleNodeClick(data) {
            // console.log(data);
            setResValue(data);
        }
    }
});

var setSelNodes = function () {
    if (_resTreeData.length > 0 && _resTreeData[0].chilres.length > 0) {
        exArr = []
        for (var i = 0; i < _resTreeData[0].chilres.length; i++) {
            exArr.push(_resTreeData[0].chilres[i].id)
        }
        _resTree.expKeys = exArr;
    }
};

var _action = new Vue({
    el: '.actions',
    data: {
        form: {
            'resname': '',
            'resvalue': '',
            'id': -1,
            'restypes':
                [{id: 'M', name: '菜单'}, {id: 'A', name: '操作'}],
            resselected: '',
            'resstatus': [{id: 1, name: '有效'}, {id: 0, name: '无效'}],
            staselected: 1,
            resremark: '',
            disResType: true,
        },
        'disAdd': true,
        'disUpdate': true,
        'disDelete': true,
        'disCancle': true,
        'disSave': true,
        'disForm': true,
        msg: '',
        restaurants: [],

        rules: {
            resselected: [{required: true, message: '请选择类型！', trigger: 'change'}],
            resname: [{required: true, message: '名称不能为空！', trigger: 'change'},
                {min: 2, max: 20, message: '长度需在2到20个字符间！', trigger: 'blur'}],
        },
    },
    created() {
        // this.form.resselected = this.form.restypes[0].id;
        this.form.staselected = this.form.resstatus[0].id;
    },
    methods: {
        getResSelected() {

            //获取选中项
            if (this.form.resselected == 'A' && (_hiVue.resnodevalue.resvalue == '' || _hiVue.resnodevalue.resvalue.trim() == '')) {
                _hiVue.infos = '父节点的值不能为空（菜单路径），请先修改！';
                _hiVue.dialogVisible = true;
                this.disSave = true;
                return;
            }
        },
        getStatSelected() {
            // console.log(this.form.staselected);
        },
        deleteRes() {
            this.$confirm('确定要删除吗？', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(() => {
                // ----------------------------------
                axios({
                    method: 'POST',
                    url: '/sys/res_del',
                    // headers: {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
                    headers: {'Content-Type': 'application/json'},

                    // 在请求之前对data传参进行格式转换
                    transformRequest: [function (data) {
                        data = JSON.stringify(data)
                        return data;
                    }],
                    params: {},

                    // 传递的参数
                    data: {'optype': 'delete', 'id': _hiVue.resnodevalue.id},
                }).then((res) => {
                    if (res.data['code'] == 1) {
                        disabledBtn();
                        _resTree.treedata = res.data['restree'];
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
        ressave() {
            this.$refs.myForm.validate(valid => {
                if (!valid) {
                    this.msg = '输入验证未通过，请正确输入！';
                } else {

                    // 判断输入是否正确
                    if (this.form.resselected == 'A' && (this.form.resvalue == '' || this.form.resvalue.trim() == '')) {
                        _hiVue.infos = '值不能为空！'
                        _hiVue.dialogVisible = true;
                        this.$refs.txtResValue.focus();
                        return;
                    }
                    if (this.form.resselected == 'A' && (_hiVue.resnodevalue.resvalue == '' || _hiVue.resnodevalue.resvalue.trim() == '')) {
                        _hiVue.infos = '父节点的值不能为空（菜单路径），请先修改！';
                        _hiVue.dialogVisible = true;
                        this.disSave = true;
                        return;
                    }
                    axios({
                        method: 'POST',
                        url: '/sys/res_save',
                        // headers: {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
                        headers: {'Content-Type': 'application/json'},

                        // 在请求之前对data传参进行格式转换
                        transformRequest: [function (data) {
                            data = JSON.stringify(data)
                            return data
                        }],
                        params: {},

                        // 传递的参数
                        data: getDicRes(),
                    }).then((res) => {

                        if (res.data['code'] == 1) {
                            _resTree.treedata = res.data['restree'];
                            //  _resTree.$refs.eltree.setCurrentKey(res.data['curid']);
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
        querySearch(queryString, cb) {
            if (this.form.resselected != 'A') {
                this.$refs.txtResName.close();
                return;
            }
            var restaurants = this.restaurants;
            var results = queryString ? restaurants.filter(this.createFilter(queryString)) : restaurants;
            // 调用 callback 返回建议列表的数据
            cb(results);
        },
        createFilter(queryString) {
            return (restaurant) => {
                return (restaurant.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0);
            };
        },
        loadAll() {
            return _resActions;
        },
        handleSelect(item) {
            //console.log(item);
            this.form.resvalue = item['action']
        }
    },
    mounted() {
        this.restaurants = this.loadAll();
    }
});

var disabledBtn = function () {
    _action.disAdd = true;
    _action.disUpdate = true;
    _action.disCancle = true;
    _action.disSave = true;
    _action.disForm = true;
    _action.disDelete = true;
};

var getDicRes = function () {
    id = _action.form.id;
    resname = _action.form.resname;
    restype = _action.form.resselected;
    resvalue = _action.form.resvalue;
    status = _action.form.staselected;
    remark = _action.form.resremark;
    return {
        "optype": _operationType,
        "id": id,
        "resname": resname,
        "resvalue": resvalue,
        "restype": restype,
        "status": status,
        "remark": remark
    };
};

var setResValue = function (nodeData) {
    _action.form.id = nodeData.id;
    _action.form.resname = nodeData.resname;
    _action.form.resvalue = nodeData.resvalue;
    _action.form.resselected = nodeData.restype;
    _action.form.staselected = nodeData.status;
    _action.form.resremark = nodeData.remark;
    _action.disForm = true;
    if (nodeData.restype == 'A') {
        _action.disAdd = true;
        _action.form.disResType = true;
    } else {
        _action.disAdd = false;
        _action.form.disResType = false;
        // console.log(_action.form.disResType);
    }
    if (nodeData.restype == 'S') {
        _action.disUpdate = true;
    } else {
        _action.disUpdate = false;
    }
    _action.disCancle = false;
    _action.disSave = true;
    _operationType = null;
    _action.msg = '';

    // 保存原始值
    _hiVue.resnodevalue = nodeData;
    _action.$refs['myForm'].clearValidate();

    // 检查该节点是否可以删除
    if (nodeData.orgtype != 'S') {
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
    _action.form.resname = _hiVue.resnodevalue.resname;
    _action.form.resvalue = _hiVue.resnodevalue.resvalue;
    _action.form.resselected = _hiVue.resnodevalue.restype;
    _action.form.staselected = _hiVue.resnodevalue.status;
    _action.form.resremark = _hiVue.resnodevalue.remark;
    _action.disForm = true;

    if (_hiVue.resnodevalue.restype == 'A') {
        _action.disAdd = true;
    } else {
        _action.disAdd = false;
    }
    if (_hiVue.resnodevalue.restype == 'S') {
        _action.disUpdate = true;
    } else {
        _action.disUpdate = false;
    }
    _action.disSave = true;
    _operationType = null;
    _action.msg = '';
    _action.$refs['myForm'].clearValidate();
};
var addControl = function () {
    _action.form.resname = '';
    _action.form.resvalue = '';
    _action.disAdd = true;
    _action.disUpdate = true;
    _action.disCancle = false;
    _action.disSave = false;
    _action.form.resremark = '';
    _operationType = 'add';
    if (_hiVue.resnodevalue.restype == 'S') {
        _action.form.resselected = 'M';
    } else if (_hiVue.resnodevalue.restype == 'M') {
        _action.form.resselected = 'A';
    } else if (_hiVue.resnodevalue.restype == 'A') {
        _action.form.resselected = '';
    }
    _action.disForm = false;
};
var updateControl = function () {
    _action.disAdd = true;
    _action.disUpdate = true;
    _action.disCancle = false;
    _action.disSave = false;
    _operationType = 'update';
    _action.disForm = false;
};

var checkNodeDel = function (nodeId) {
    var reFlag = -1;
    $.ajax({
        type: "post",
        dataType: "json",
        async: false,
        url: '/sys/res_check',
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