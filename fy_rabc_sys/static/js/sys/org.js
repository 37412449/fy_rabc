_operationType = null;
var _hiVue = new Vue({
    el: '#divHidden',
    data: {
        orgnodevalue: '',
    },
    methods: {}
});
var _orgTree = new Vue({
    el: '#orgTree',
    data: {
        props: {
            label: 'orgname',
            children: 'chilorg'
        },
        treedata: _orgTreeData,
        expKeys: [],
    },
    created() {
        if (_orgTreeData.length > 0 && _orgTreeData[0].chilorg.length > 0) {
            exArr = []
            for (var i = 0; i < _orgTreeData[0].chilorg.length; i++) {
                exArr.push(_orgTreeData[0].chilorg[i].id)
            }
            this.expKeys = exArr;
        }
    },
    methods: {
        handleNodeClick(data) {
            // console.log(data);
            setOrgValue(data);
        },
        handleNodeExpand(data, node, e) {
        },
    }
});

var _action = new Vue({
    el: '.actions',
    data: {
        form: {
            'orgname': '',
            'id': -1,
            'orgtypes':
                [{id: 'D', name: '部门'}, {id: 'G', name: '组'}, {id: 'P', name: '岗位'},
                    {id: 'C', name: '公司', 'disabled': true}],
            orgselected: '',
            'orgstatus': [{id: 1, name: '有效'}, {id: 0, name: '无效'}],
            staselected: 1,
            orgremark: '',
            disOrgType: true,
        },
        disForm: true,
        'disAdd': true,
        'disUpdate': true,
        'disCancle': true,
        'disDelete': true,
        'disSave': true,
        msg: '',

        rules: {
            orgname: [{required: true, message: '名称不能为空！', trigger: 'blur'},
                {min: 2, max: 20, message: '长度需在2到20个字符间！', trigger: 'blur'}],
            orgselected: [{required: true, message: '请选择类型！', trigger: 'change'}],
        },
    },
    created() {
        // this.form.orgselected = this.form.orgtypes[0].id;
        this.form.staselected = this.form.orgstatus[0].id;
    },
    methods: {
        getOrgSelected() {

            //获取选中的优惠券
            console.log(this.form.orgselected);
        },
        getStatSelected() {
            console.log(this.staselected);
        },
        deleteOrg() {

            this.$confirm('确定要删除吗？', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(() => {
                // ----------------------------------
                axios({
                    method: 'POST',
                    url: '/sys/org_del',
                    // headers: {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
                    headers: {'Content-Type': 'application/json'},

                    // 在请求之前对data传参进行格式转换
                    transformRequest: [function (data) {
                        data = JSON.stringify(data)
                        return data;
                    }],
                    params: {},

                    // 传递的参数
                    data: {'optype': 'delete', 'id': _hiVue.orgnodevalue.id},
                }).then((res) => {
                    if (res.data['code'] == 1) {
                        disabledBtn();
                        _orgTree.treedata = res.data['orgtree'];
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
        orgsave() {
            // 判断输入是否正确
            this.$refs.myForm.validate(valid => {
                if (!valid) {
                    this.msg = '输入验证未通过，请正确输入！';
                } else {
                    axios({
                        method: 'POST',
                        url: '/sys/org_save',
                        // headers: {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
                        headers: {'Content-Type': 'application/json'},

                        // 在请求之前对data传参进行格式转换
                        transformRequest: [function (data) {
                            data = JSON.stringify(data)
                            return data
                        }],
                        params: {},

                        // 传递的参数
                        data: getDicOrg(),
                    }).then((res) => {

                        if (res.data['code'] == 1) {
                            _orgTree.treedata = res.data['orgtree'];
                            //  _orgTree.$refs.eltree.setCurrentKey(res.data['curid']);
                        }
                        this.msg = res.data['msg'];
                        disabledBtn();
                    }).catch(function (err) {
                        this.msg = err;
                        disabledBtn();
                    });
                }
            });
        }
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

var getDicOrg = function () {
    id = _action.form.id;
    orgname = _action.form.orgname;
    orgtype = _action.form.orgselected;
    status = _action.form.staselected;
    remark = _action.form.orgremark;
    return {
        "optype": _operationType,
        "id": id,
        "orgname": orgname,
        "orgtype": orgtype,
        "status": status,
        "remark": remark
    };
};

var setOrgValue = function (nodeData) {
    _action.disForm = true;
    _action.form.id = nodeData.id;
    _action.form.orgname = nodeData.orgname;
    _action.form.orgselected = nodeData.orgtype;
    _action.form.staselected = nodeData.status;
    _action.form.orgremark = nodeData.remark;

    if (nodeData.orgtype == 'C') {
        _action.disUpdate = true;
        _action.disAdd = false;
        _action.form.disOrgType = false;

    } else if (nodeData.orgtype == 'D') {
        _action.disUpdate = false;
        _action.disAdd = false;
        _action.form.disOrgType = false;
    } else if (nodeData.orgtype == 'G') {
        _action.disUpdate = false;
        _action.disAdd = false;
        _action.form.disOrgType = false;
    } else if (nodeData.orgtype == 'P') {
        _action.disUpdate = false;
        _action.disAdd = true;
        _action.form.disOrgType = true;
    }
    _action.disCancle = false;
    _action.disSave = true;
    _operationType = null;
    _action.msg = '';

    // 保存原始值
    _hiVue.orgnodevalue = nodeData;
    _action.$refs['myForm'].clearValidate();

    // 检查该节点是否可以删除
    if (nodeData.orgtype != 'C') {
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
    _action.disForm = true;
    _action.form.orgname = _hiVue.orgnodevalue.orgname;
    _action.form.orgselected = _hiVue.orgnodevalue.orgtype;
    _action.form.staselected = _hiVue.orgnodevalue.status;
    _action.form.orgremark = _hiVue.orgnodevalue.remark;

    if (_hiVue.orgnodevalue.orgtype == 'P') {
        _action.disAdd = true;
        _action.disUpdate = false
    }
    if (_hiVue.orgnodevalue.orgtype == 'C') {
        _action.disUpdate = true;
        _action.disAdd = false;
    }
    if (_hiVue.orgnodevalue.orgtype == 'D' || _hiVue.orgnodevalue.orgtype == 'G') {
        _action.disUpdate = false;
        _action.disAdd = false;
    }

    _action.disSave = true;
    _operationType = null;
    _action.msg = '';
    _action.$refs['myForm'].clearValidate();

    // 检查该节点是否可以删除
    if (_hiVue.orgnodevalue.orgtype != 'C') {
        var tmpFlag = checkNodeDel(_hiVue.orgnodevalue.id);
        if (tmpFlag == 0) {
            _action.disDelete = false;
        } else {
            _action.disDelete = true;
        }
    } else {
        _action.disDelete = true;
    }
};
var addControl = function () {
    _action.disForm = false;
    _action.disAdd = true;
    _action.disUpdate = true;
    _action.disCancle = false;
    _action.disSave = false;
    _action.form.orgname = '';
    _action.form.orgremark = '';

    _operationType = 'add';
    if (_hiVue.orgnodevalue.orgtype == 'P') {
        _action.form.orgselected = '';
    } else if (_hiVue.orgnodevalue.orgtype == 'C') {
        _action.form.orgselected = 'D';
    } else if (_hiVue.orgnodevalue.orgtype == 'D') {
        _action.form.orgselected = 'G';
    } else if (_hiVue.orgnodevalue.orgtype == 'G') {
        _action.form.orgselected = 'P';
    }

};
var updateControl = function () {
    _action.disForm = false;
    _action.disAdd = true;
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
        url: '/sys/org_check',
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
}


// 设置节点颜色（节点状态为非有效的）
var nodeIndex = 0;

function getChilNodeIndex(nodes, lisNode) {
    for (var j = 0; j < nodes.length; j++) {
        var temNode = _orgTree.$refs.eltree.getNode(nodes[j].id);
        if (temNode && temNode.data.status == 0) {
            lisNode.push({index: nodeIndex, id: nodes[j].id});
        }
        nodeIndex++;
        if (nodes[j].chilorg && nodes[j].chilorg.length > 0) {

            if (temNode && temNode.expanded) {
                getChilNodeIndex(nodes[j].chilorg, lisNode);
            }
        }
    }
}

function getTreeNodeIndex() {
    var lisNode = [];
    var tree = _orgTree.$refs.eltree;
    for (var i = 0; i < tree.children.length; i++) {
        var temNode = tree.getNode(tree.children[i].id);
        if (temNode && temNode.data.status == 0) {
            lisNode.push({index: nodeIndex, id: tree.children[i].id});
        }
        nodeIndex++;
        if (tree.children[i].chilorg && tree.children[i].chilorg.length > 0) {

            if (temNode && temNode.expanded) {
                getChilNodeIndex(tree.children[i].chilorg, lisNode, nodeIndex);
            }
        }
    }
    return lisNode;
}

function setNodeColor() {
    var nodes = getTreeNodeIndex();
    for (var t = 0; t < nodes.length; t++) {
        _orgTree.$refs.eltree.treeItems[nodes[t].index].style.color = '#1516ff';
    }
}

// setNodeColor();