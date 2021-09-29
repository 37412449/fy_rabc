var _allRoles = [];
var _selRoleValue = null;
var fun_selRole = function (rolcode) {
    _action.msg = '';
    _action.disSave = false;
    _action.disCancle = false;
    $.ajax({
        type: "post",
        dataType: "json",
        async: true,
        url: '/sys/r2r_all_res',
        data: JSON.stringify({'rolecode': rolcode, 'optype': 'view'}),
        headers: {'Content-Type': 'application/json'},
        error: function (xhr, err) {
            _action.msg = err;
        },
        success: function (data) {
            if (data['code'] == 1) {
                _action.$refs.eltree.setCheckedKeys(data['ress']);
            } else {
                _action.$refs.eltree.setCheckedKeys([]);
            }
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            alert('获取角色资源异常！');
            _action.disSave = true;
            _action.disCancle = true;
        }
    });
    _selRoleValue = rolcode;

};

var fun_getAllRoles = function (roles) {
    $.ajax({
        type: "post",
        dataType: "json",
        async: false,
        url: '/sys/r2rs',
        data: JSON.stringify({'optype': 'view'}),
        headers: {'Content-Type': 'application/json'},
        error: function (xhr, err) {
            _action.msg = '请求失败，请检查，' + err + '!';
        },
        success: function (data) {
            if (data['code'] == 1) {
                _allRoles = data['roles'];
            }
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            alert('获取所有角色异常！');
            _action.disSave = true;
            _action.disCancle = true;
        }
    });
    roles.length = 0;
    _allRoles.forEach((rol, i) => {
        roles.push({rolname: rol.name, rolcode: rol.code});

    });
};

var fun_getResTree = function () {
    $.ajax({
        type: "post",
        dataType: "json",
        async: false,
        url: '/sys/r2r_res_tree',
        data: JSON.stringify({'optype': 'view'}),
        headers: {'Content-Type': 'application/json'},
        error: function (xhr, err) {
            _action.msg = '请求失败，请检查，' + err + '!';
        },
        success: function (data) {
            if (data['code'] == 1) {
                _resTreeData = data['restree'];
            }
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            alert('获取资源树异常！');
            _action.disSave = true;
            _action.disCancle = true;
        }
    });
};

var _action = new Vue({
    el: '.actions',
    data: {
        props: {
            label: 'resname',
            children: 'chilres'
        },
        treedata: _resTreeData,
        expKeys: [],

        disCancle: true,
        disSave: true,
        msg: '',

        rolsea: '',
        roles: [],
        activateCode: '',
    },
    created() {
        if (_resTreeData.length > 0 && _resTreeData[0].chilres.length > 0) {
            exArr = []
            for (var i = 0; i < _resTreeData[0].chilres.length; i++) {
                exArr.push(_resTreeData[0].chilres[i].id)
            }
            this.expKeys = exArr;
        }
        fun_getAllRoles(this.roles);
    },
    methods: {
        handleNodeClick(data) {
            // console.log(data);
        },
        freshRoles() {
            this.rolsea = '';
            fun_getAllRoles(this.roles);
            fun_getResTree();
            this.treedata = _resTreeData;
            this.disSave = true;
        },
        ressave() {
            if (_selRoleValue == null) {
                return;
            }

            this.$confirm('确定要修改吗？', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(() => {
                // ----------------------------------
                axios({
                    method: 'POST',
                    url: '/sys/r2r_save_res',
                    // headers: {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
                    headers: {'Content-Type': 'application/json'},

                    // 在请求之前对data传参进行格式转换
                    transformRequest: [function (data) {
                        data = JSON.stringify(data)
                        return data;
                    }],
                    params: {},

                    // 传递的参数
                    data: getDicUsr(),
                }).then((res) => {
                    if (res.data['code'] == 1) {
                        this.disSave = true;
                    }
                    this.msg = res.data['msg'];
                }).catch(function (err) {
                    this.msg = err;
                });

                // --------------------------
            }).catch(() => {
                fun_selRole(_selRoleValue);
                this.$message({
                    type: 'info',
                    message: '已取消修改!'
                });
            });


        },
        setSelNode(e, rolcode) {
            fun_selRole(rolcode);
            this.activateCode = rolcode;
        },
        cancleSetValue() {
            if (_selRoleValue == null) {
                _action.$refs.eltree.setCheckedKeys([]);
            } else {
                fun_selRole(_selRoleValue);
            }
            this.msg = '';
        },
        searitem() {
            this.roles = [];
            if (this.rolsea.trim() == '') {
                _allRoles.forEach((rol, i) => {
                    this.roles.push({rolname: rol.name, rolcode: rol.code});
                });
            } else {
                _allRoles.forEach((rol, i) => {
                    if (rol.name.indexOf(this.rolsea.trim()) > -1) {
                        this.roles.push({rolname: rol.name, rolcode: rol.code});
                    }
                });
            }
        }
    },
    mounted() {
    },
});

var getDicUsr = function () {
    lisRes = [];
    arrSel = _action.$refs.eltree.getCheckedNodes(true, true);
    arrSel.forEach((r, i) => {
        if (r.restype == 'A') {
            lisRes.push(r.rescode);
        }
    });
    return {role_code: _selRoleValue, ress: lisRes};
};