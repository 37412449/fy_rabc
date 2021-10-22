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
        url: '/sys/rol_all_usr',
        data: JSON.stringify({'rolecode': rolcode, 'optype': 'view'}),
        headers: {'Content-Type': 'application/json'},
        error: function (xhr, err) {
            _action.msg = err;
        },
        success: function (data) {
            if (data['code'] == 1) {
                _action.$refs.eltree.setCheckedKeys(data['usrs']);
            } else {
                _action.$refs.eltree.setCheckedKeys([]);
            }
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            _action.disSave = true;
            _action.disCancle = true;
            window.location.replace('/admin/login/');
        }
    });
    _selRoleValue = rolcode;
};

var fun_getAllRoles = function (roles) {
    $.ajax({
        type: "post",
        dataType: "json",
        async: false,
        url: '/sys/rol_all',
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
            _action.disSave = true;
            _action.disCancle = true;
            window.location.replace('/admin/login/');
        }
    });
    roles.length = 0;
    _allRoles.forEach((rol, i) => {
        roles.push({rolname: rol.name, rolcode: rol.code});

    });
};

var fun_getUsrTree = function () {
    $.ajax({
        type: "post",
        dataType: "json",
        async: false,
        url: '/sys/rol_usr_tree',
        data: JSON.stringify({'optype': 'view'}),
        headers: {'Content-Type': 'application/json'},
        error: function (xhr, err) {
            _action.msg = '请求失败，请检查，' + err + '!';
        },
        success: function (data) {
            if (data['code'] == 1) {
                _usrTreeData = data['usrtree'];
            }
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            _action.disSave = true;
            _action.disCancle = true;
            window.location.replace('/admin/login/');
        }
    });
};

var _action = new Vue({
    el: '.actions',
    data: {
        usrnodevalue: '',
        props: {
            label: 'usrname',
            children: 'chilusr'
        },
        treedata: _usrTreeData,
        expKeys: [],

        disCancle: true,
        disSave: true,
        msg: '',

        rolsea: '',
        roles: [],
        activateCode: '',
    },
    created() {
        if (_usrTreeData.length > 0 && _usrTreeData[0].chilusr.length > 0) {
            exArr = []
            for (var i = 0; i < _usrTreeData[0].chilusr.length; i++) {
                exArr.push(_usrTreeData[0].chilusr[i].id)
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
            fun_getUsrTree();
            this.treedata = _usrTreeData;
            this.disSave = true;
        },
        orgsave() {
            if (_selRoleValue == null) {
                return;
            }
            this.$confirm('确定要要修改吗？', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(() => {
                // -------------------------------
                axios({
                    method: 'POST',
                    url: '/sys/rol_save_usr',
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

                // -----------------------------
            }).catch(() => {
                fun_selRole(_selRoleValue);
                this.$message({
                    type: 'info',
                    message: '已取修改!'
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
    lisUsr = [];
    arrSel = _action.$refs.eltree.getCheckedNodes(true, true)
    arrSel.forEach((r, i) => {
        if (r.usrtype == 'U') {
            lisUsr.push(r.user_code);
        }
    });
    return {role_code: _selRoleValue, users: lisUsr};
};