//获取随机数
function randomString(len) {
　　len = len || 32;
　　var num = '1234567890';  
　　var maxPos = num.length;
　　var pwd = '';
　　for (i = 0; i < len; i++) {
　　　　pwd += num.charAt(Math.floor(Math.random() * maxPos));
　　}
　　return pwd;
}
// 172.26.146.35  康
// 172.26.146.29  潘
// 172.26.152.176 内网
// 14.23.175.36 外网
var loanUrl = '14.23.175.36';
var ZS_queryID;
var ZS_loanOrder;
var ZS_flag = true;  

//招商
// var ZS_saveData = {
//     "tradeBody": {
//         "entityInfo": {
//             "conFlg": "1",
//             "carPrice": "25",
//             "avgIncCod": "3000",
//             "houPrcCod": "10000000",
//             "houCtyCod": "0021",
//             "ctfNbr": "430581198806253552",     
//             "ptcFlg": "1",
//             "phoneNo": "15521211495",
//             "homCtyCod": "0871",
//             "carNo": "粤B88888",
//             "carInf": "Y",
//             "houInf": "Y",
//             "carCtyCod": "0020",
//             "custNam": "潘伦友",
//             "carDteCod": "1",
//             "offNam": "车巴巴测试",
//             "brandCode": "38"
//         }
//     },
//     "tradeHead": {
//         "mainCmd": "100219",            // 订单信息  固定100219
//         "requSeq": "1453085832637",     //自定义随机数字
//         "retnCode": "0",                //返回码 --0 
//         "retnDesc": "",                 //返回描述  --空
//         "servSeq": "1453085832637",     //自定义随机数字
//         "subCmd": "",      //空   
//         "tradeTime": "2016-03-15 16:10:07" //交易时间，格式：yyyy-MM-dd HH:mm:ss
//     }
// } 
// var ZS_queryDATA = {
//     "tradeBody": {
//         "entityInfo": {
//             "verification":"111111" ,    //验证码
//             "phoneNo": "15521211495",
//             "queryId":"",
//             "loanOrder":""
//         }
//     },
//     "tradeHead": {
//         "mainCmd": "100220",
//         "requSeq": 1453085832637,
//         "retnCode": "0",
//         "retnDesc": "",
//         "servSeq": 1453085832637,
//         "subCmd": "",
//         "token": "",
//         "tradeTime": '2016-03-15 16:10:07'
//     }
// }

// $.ajax({
//     url: 'http://'+loanUrl+':8080/open-service/api/dealsLoan/cmbSave',
//     type:'get',
//     dataType: 'jsonp',
//     data: {
//         data:JSON.stringify(ZS_saveData)
//     },
//     success:function(data){

//         var dataInfo = data.tradeBody.entityInfo;
//         var queryIdObj = JSON.parse(dataInfo.queryId);      //外层对象
//         var queryIdData = queryIdObj.Data;             //内层对象

//         var outReturnCode = queryIdObj.ReturnCode;   //外层状态
//         var outMessage = queryIdObj.ReturnMessage;     // 外层提示

//         var insideReturnCode = queryIdData.ReturnCode   //内层状态
//         var insideMessage = queryIdData.Message;        //内层提示

//         if(outReturnCode == '0000'){
//             if(insideReturnCode == '0000'){
//                 ZS_queryID = queryIdObj.Data.Data.queryId;  
//                 alert(ZS_queryID)
//             }else{
//                 //重新请求

//                 alert(insideMessage);
//             }
//         }else{
//             alert(outMessage)
//         }

//         ZS_queryDATA.tradeBody.entityInfo.queryId = ZS_queryID; 
//         ZS_queryDATA.tradeBody.entityInfo.loanOrder =  dataInfo.loanOrder; 

//         $.ajax({
//             url: 'http://'+loanUrl+':8080/open-service/api/dealsLoan/cmbQuery',
//             type:'get',
//             dataType: 'jsonp',
//             data: {
//                 data:JSON.stringify(ZS_queryDATA)
//             },
//             success:function(data){
//                 var dataInfo = JSON.parse(data.tradeBody.entityInfo);
//                 var outReturnCode = dataInfo.ReturnCode; // 外层状态
//                 var outMessage = dataInfo.Message;    //外层提示

//                 var insideReturnCode = dataInfo.Data.ReturnCode; //内层报错状态  E007
//                 var insideReturnEorrer = dataInfo.Data.Message; //内层报错提示  

//                 var insideMessage = dataInfo.Data.message;  //内层正确提示;
//                 var insideAmt = dataInfo.Data.maxAmt2;  //额度;

//                 console.log(insideReturnEorrer)
//                 console.log(insideReturnCode)

//                 if(outReturnCode == '0000'){

//                 }else{
//                     alert(outMessage)
//                 }

//                 if(insideReturnCode == "E007"){
//                     alert(insideReturnEorrer)
//                 }
//             }
//         })       
//     }
// })


//日产
// var RC_saveData = {
//     "tradeBody": {
//         "entityInfo": {
//             "A0209":"0",           //身份证
//             "A0401": "张三",
//             "A0402": "1",
//             "A0403": "身份证",
//             "A0404": "441424199108080310",
//             "A0410": "16",
//             "A0413": "网络/软件/信息技术服务/电子商务",
//             "A0414": "中层管理人员",
//             "A0418": "30000",
//             "A0420": "已婚",
//             "A0421": "抵押买房居住",
//             "A0422": "研究生及以上",
//             "A0423": "股份公司",
//             "dealer_id": "1143",
//             "model_id": "229",
//             "A0424": "13682224071",
//             "A0405": "广州",
//             "A0325": "广东",
//             "A0314": "12",
//             "A0318": "30",
//             "A0313": "0.00",       //利率
//             "A0315": "东风日产金融",    //产品名称
//             "financial_id ": "207"
//         }
//     },
//     "tradeHead": {
//         "mainCmd": "100223",
//         "requSeq": "1453085832637",
//         "retnCode": "",
//         "retnDesc": "",
//         "servSeq": "",
//         "subCmd": "",
//         "token": "",
//         "tradeTime": "2016-02-02 10:36:53"
//     }
// }

// var RC_query = {
//     "tradeBody": {
//         "entityInfo": {
//             "queryId": ""
//         }
//     },
//     "tradeHead": {
//         "mainCmd": "100221",
//         "requSeq": "1453085832637",
//         "retnCode": "",
//         "retnDesc": "",
//         "servSeq": "",
//         "subCmd": "",
//         "token": "",
//         "tradeTime": "2016-02-02 10:36:53"
//     }
// }

// $.ajax({
//     url: 'http://'+loanUrl+':8080/open-service/api/dealsLoan/save',
//     type: 'get',
//     dataType: 'jsonp',
//     data: {data: JSON.stringify(RC_saveData)},   
// })
// .done(function(data) {
//     var queryId = data.tradeBody.entityInfo.queryId;
//     RC_query.tradeBody.entityInfo.queryId = queryId;

//     $.ajax({
//         url: 'http://'+loanUrl+':8080/open-service/api/dealsLoan/query',
//         type: 'get',
//         dataType: 'jsonp',
//         data: {data: JSON.stringify(RC_query)},   
//     })
//     .done(function(data) {
//         // console.log("success");
//         // var dataInfo = data.tradeBody.entityInfo;
//         // var result = JSON.parse(dataInfo.result);
//         // var success = result.success;

//         if(success){
//             // console.log(success)
//         }else{

//         }
//     })    
// })

// RC_query.tradeBody.entityInfo.queryId = "ab867a7233245b46850b72806c48da29";
// $.ajax({
//     url: 'http://'+loanUrl+':8080/open-service/api/dealsLoan/query',
//     type: 'get',
//     dataType: 'jsonp',
//     data: {data: JSON.stringify(RC_query)},   
// })
// .done(function(data) {
//     data = JSON.parse(data.tradeBody.entityInfo.RESPONSE_DATA);
//     console.log(data)
//     console.log(data.R009)   //ROO9提示   R012金额

//     if(data.R009 && data.R012){
//         console.log('success')
//     }else{

//     }
// }) 

function resultInfo(){
    $('#J-result-type').text($('#J-type-id').val());
    $('#J-result-downpay').text($('input[name="pay_scale"]').val());
    $('#J-result-period').text($('input[name="loan_period"]').val());
    $('#J-result-dealer').text($('.J-dealer-name').text());
    $('#J-result-tel').text($('#J-service-tel').val());
    $('#J-result-address').text($('#J-dlr-adress').val());
    $('#J-result-series').text($('input[name="loan_series"]').val());
}

function getPrice(){
    var typeId = $('#J-type-id').attr('data-id') || 346;
    var dealerId = $('#J-dealer-id').val() || 1143;
    var val;
    //获取价格
    $.ajax({    
      url: pythonData.typePriceOps,
      type: 'get',
      dataType: 'json',   
      data: {dealer_id: dealerId,car_type_id:typeId},
    })
    .done(function(data) {
        val = data.result.price
        $('#J-type-price').val(val);
    })
}

//金融方案
function ajaxFinance(ops){
    $.ajax({
        url: ops.url,
        dataType: 'json',
        data: ops.param,
    })
    .done(function(data) {
        financialVm.array = data.result || [];
    })
}

//经销商
function ajaxDeaer(ops){
    setTimeout(function(){
        dealerVm.loading = false;
        loadingVm.flag = true; 
        $.ajax({
            url: ops.url,
            dataType: 'json',
            data: ops.param
        })
        .done(function(data) {
            var data = data.result.dealer_list;
            var _num = data.length;
            dealerVm.num = _num;
            dealerVm.array = data || []; 
            dealerVm.loading = true;
            loadingVm.flag = false;
        })     
    })           
}

//进度导航
function loanNav(){
    $('.J-loan-nav .active').removeClass('active').next().addClass('active');
}

//车型 
var typeVm = avalon.define({
    $id: "c-type",
    array:[]
})

//省列表
var proinceListVm = avalon.define({
    $id: "c-proinceList",
    proinceListName:pythonData.provinceName,
    proinceListId:pythonData.provinceId,
    array:[],
    click:function(){
        var _this = $(this);
        var _id = $(this).attr('data-id');
        var _name = $(this).text();

        proinceOps.param.province_id = _id
        $.ajax({
            url: proinceOps.url,
            dataType: 'json',
            data: proinceOps.param,
        })
        .done(function(data) {
            var data = data['result']['city_list'];
            _this.closest('.form-list').removeClass('valid');  

            proinceListVm.proinceListName=_name;
            proinceListVm.proinceListId=_id;

            //重置
            cityVm.cityName = '';
            cityVm.cityId = '';
            countyVm.countyName = '';
            countyVm.countyId = '';
            countyVm.array = []; 
            dealerVm.array = [];
            dealerVm.loading = false;

            cityVm.array = data || []; 
        })
    }
})

//城市
var cityVm = avalon.define({
    $id: "c-city", 
    cityName:pythonData.cityName,
    cityId:pythonData.cityId,
    array:pythonData.cityJson,
    click:function(){
        var _id = $(this).attr('data-id');
        var _name = $(this).text();
        var _this = $(this);

        cityOps.param.city_id = _id;
        dealerOps.param.city_id = _id;
        dealerOps.param.county_id = '';

        $.ajax({
            url: cityOps.url,
            dataType: 'json',
            data: cityOps.param,
        })
        .done(function(data) {
            var data = data['result']['county_list'];

            cityVm.cityName = _name;
            cityVm.cityId = _id;
            //重置
            countyVm.countyName = '';
            countyVm.countyId = '';

            ajaxDeaer(dealerOps)

            countyVm.array = data || []; 

            _this.closest('.form-list').removeClass('error').addClass('valid').find('.txt').text('');    
        })
    }
})
//区
var countyVm = avalon.define({
    $id: "c-county", 
    countyName:'',
    countyId:'',
    array:[],
    click:function(){
        var _id = $(this).attr('data-id');
        var _name = $(this).text();
        countyVm.countyName = _name;
        countyVm.countyId = _id;

        dealerOps.param.county_id = _id;

        ajaxDeaer(dealerOps)
    }
})
//首付比例
var downpayVm = avalon.define({
    $id: "c-downpay", 
    array:[]
})
//期数
var periodVm = avalon.define({
    $id: "c-period", 
    array:[]
})
//金融方案
var financialVm = avalon.define({
    $id: "c-financial", 
    price:'',
    downpay:'0.2',
    array:[]
})
//经销商
var dealerVm = avalon.define({
    $id: "c-dealer", 
    num:'',
    array:[],
    loading:false,
    dialogBool:false,
    change:function(){
        dealerVm.dialogBool = true;
    },
    sureBtn:function(){
        var _parentsLi = $('.select-dealer input[name="dealer_id"]:checked ').closest('li');
        var _dataId = $('.select-dealer input[name="dealer_id"]:checked ').val();
        var _dealerCode = $('.select-dealer input[name="dealer_id"]:checked ').attr('data-code');
        var _name = _parentsLi.find('.name').text();
        var _country = _parentsLi.find('.country').text();
        var _tel = _parentsLi.find('.hidden-tel').val();
        var _address = _parentsLi.find('.hidden-address').val();
        var _html = ''

        if(_dataId){
            $('.J-dealer-name').text(_name);
            $('.J-dealer-area').text(_country);
            $('#J-dealer-id').val(_dataId);
            $('#J-service-tel').val(_tel);
            $('#J-dlr-adress').val(_address);
            $('#J-dealer-code').val(_dealerCode)

            $('.J-dealer-list').removeClass('error').addClass('valid').find('.txt').text('');
            dealerVm.dialogBool = false;
        }else{
            $.errorAlert({content:'请选择经销商'})
        }
    },
    closeDialog:function(){
         dealerVm.dialogBool = false;
    }
})

var loadingVm = avalon.define({
    $id:'c-loading',
    flag:false 
})

//返回結果
var resultVm = avalon.define({
    $id:'c-result',
    priceBool:false,           //是否有价格
    sucessBool:false                //是否成功
})
 
$(function(){

    //下拉框
    $.cbbSelect();

    //loading
    $.lodingWin();
    //移除loading
    $('.u-wait-pop').hide();
    $('.m-mask').hide();

    //获取验证码
    $('#J-code-btn').on('click',function(){
        var that= $(this);
        var _mobile = $("input[name='loan_phone']").val();
        var _reg = /^(((13[0-9]{1})|(15[0-9]{1})|(18[0-9]{1}))+\d{8})$/;

         if (_reg.test(_mobile)) {
            mobileOps.param.csrfmiddlewaretoken =  $("input[name='csrfmiddlewaretoken']").val();
            mobileOps.param.mobile =  _mobile;

            $.ajax({
                url: mobileOps.url,
                type:'POST',
                dataType: 'json',
                data: mobileOps.param 
            })
            .done(function(data) {
                var data = data.result;
                if(data.retnCode == 0){
                    countDown(function() {
                        that.text('获取验证码').removeClass('disabled').prop('id','J-code-btn');
                    })

                    function countDown(callback) {
                        $('#J-code-btn').off('click');
                        var count = 120;

                        (function fcount() {
                            if(count < 0) return callback();
                            that.text('重新获取('+ count-- + ')');
                            that.addClass('disabled').prop('id','');;
                            setTimeout(fcount, 1000);
                        })();
                    }
                }else{
                    $.errorAlert({content:data.retnDesc});
                }
            })
         }else{
             $.errorAlert({content:'手机号码错误'});
         };
    });

    /* validate验证 */
    $('.next-btn').on('click',function(){  
        $(this).closest('form').submit();
    });
    //进度条上一步
    $('.J-prex-btn').on('click',function(){
        $('.J-loan-nav .active').removeClass('active').prev().addClass('active');
        $(this).closest('form').hide().prev().show();
        $('body').animate({scrollTop:"0"},200);
    })
    //招商上一步
    $('#J-zs-prex').on('click',function(){
        $('.J-loan-nav .active').removeClass('active').prev().addClass('active');
        $(this).closest('form').hide();
        $('#J-step-2').show();
        $('body').animate({scrollTop:"0"},200);  
    }) 
    //checkbox
    $('.J-checkbox').on('click',function(){
        var obj = $(this).closest('label');
        var hasActive = obj.hasClass('active');
        hasActive? obj.removeClass('active'): obj.addClass('active');
    })

    $('.J-btn-select').on('click',function(){
        $(this).addClass('active').siblings().removeClass('active');
    })
    
    $("#J-step-1").validate({
        rules: {
            loan_name: {
                required: true,
                minlength:2                       
            },
            loan_phone: {
                required: true,  
                isMobile:true                            
            },
            verify_code:{
                required: true,  
                remote: {
                    url: verifyMobile.url, 
                    type: "post",          
                    dataType: "json",      
                    data: {                
                        verify_code: function() {
                            return $("input[name='verify_code']").val();
                        },
                        mobile: function() {
                            return $("input[name='loan_phone']").val();
                        },
                        csrfmiddlewaretoken: function() {
                            return $("input[name='csrfmiddlewaretoken']").val();
                        }
                    }
                }
            },
            loan_series:{
                required: true, 
            },
            product_id:{
                required: true, 
            },
            loan_city:{
                required: true, 
            },
            agree:{
                required: true,   
            }
        },
        messages:{
            agree:'请接受车巴巴服务条款'
        },
        errorPlacement: function(error, element) {  
            error.appendTo(element.parents('.frame'));  
        },
        submitHandler:function() { 
            
            // decodeURI
            //资料保存
            var lead_key = CBB.getUrlParam("lead_key") || 'NV-Chebabanew-Pc-V3-TO-Le-PoC-Msg8-03-0000',     //key
                _name = $('#J-name').val(),                                 //姓名
                _sex = $('.J-sex:checked').val(),                           //性别
                _phone = $('#J-phone').val(),                               //手机
                _verifyCode = $('#J-verify-code').val(),                    //验证码
                _seriesId = $('#J-series-id').attr('data-id'),              //车系ID
                _typeId = $('#J-type-id').attr('data-id'),                  //车型ID
                _proinceId = $('#J-proince-id').attr('data-id'),            //省ID
                _cityID = $('#J-city-id').attr('data-id'),                  //市ID
                _countyId = $('#J-county-id').attr('data-id'),              //区ID
                _dealerId = $('#J-dealer-id').attr('data-id'),              //经销商ID
                _dealerCode = $('#J-dealer-code').val(),                    //经销商code
                _dealerAddress = $('#J-dlr-adress').val();

            var clueSaveData = {
                csrfmiddlewaretoken:$("input[name='csrfmiddlewaretoken']").val(),
                name: _name,
                sex: _sex,
                phone: _phone,
                dlrCode: _dealerCode,
                clueType: 8,
                source: 4,
                carTypeId: _typeId,
                carSeriesId: _seriesId,
                address: _dealerAddress,
                cityId: _cityID,
                countyId: _countyId,
                buyWayCode: 2,
                pageId:lead_key
            }

            //留资
            $.ajax({
                url: clueSave.url,
                dataType: 'json',
                data: clueSaveData
            })

            financialOps.param.dealer_id = $('#J-dealer-id').val();
            financialOps.param.car_type_id = $('#J-type-id').attr('data-id');

            //获取方案
            ajaxFinance(financialOps)

            //首付比例
            $.ajax({
                url:downpayOps.url,
                dataType:'json',
                data:downpayOps.param
            })
            .done(function(data){
                downpayVm.array = data.result || [];
                setTimeout(function(){
                    $('#J-downpay a').on('click',function(){
                        var _downpay = parseInt($(this).attr('data-id'));
                        financialOps.param.first_pay_percent = _downpay;
                        //获取方案
                        ajaxFinance(financialOps)
                    });
                },100)
            }) 

            //期数
            $.ajax({
                url:periodyOps.url,
                dataType:'json',
                data:periodyOps.param
            })
            .done(function(data){
                periodVm.array = data.result || [];
                setTimeout(function(){
                    $('#J-period a').on('click',function(){
                        var _period = $(this).attr('data-id');
                        financialOps.param.sku_item = _period;
                        //获取方案
                        ajaxFinance(financialOps)
                    });
                },100)
            }) 

            //获取车型价格
            getPrice();

            //下一步
            $("#J-step-1").hide().next().show();
            loanNav();
        }                           
    }); 

    $("#J-step-2").validate({                 
        errorPlacement: function(error, element) {  
            error.appendTo(element.parents('.frame'));  
        },
        submitHandler:function() { 
            $("#J-step-2").hide();
            var _corpId = $('.J-corp-id:checked').val();
            // 日产是261，招行是258
            if(_corpId == 261){
                $('#J-step-rc-3').show();
                loanNav();
            }else if(_corpId == 258){
                $('#J-step-zs-3').show();
                //手机号码
                var phoneFormat = $('#J-phone').val();
                // phoneFormat = CBB.phoneFormat(phoneFormat)
                $('#J-phone-format').text(phoneFormat);
                loanNav();
            }else{ 
                $("#J-step-2").show();
                $.errorAlert({content:'请选择金融方案'});
            }
        }                           
    });
    //日产
    $("#J-step-rc-3").validate({
        rules: {
            card_name: {
                required: true,            
            },
            card_number: {
                required: true,
                isIdCardNo:true                  
            },
            fangchan: {
                required: true,            
            },
            marry: {
                required: true,            
            },
            trade: {
                required: true,            
            },
            occupation: {
                required: true,            
            },
            company: {
                required: true,            
            },
            education: {
                required: true,            
            },
            working_years: {
                required: true,            
            },
            income: {
                required: true,            
            },
        },                   
        errorPlacement: function(error, element) {  
            error.appendTo(element.parents('.frame'));  
        },
        submitHandler:function() {
            var randomNum = randomString(13);
            var myDate=new Date();  
            myDate = myDate.Format("yyyy-MM-dd hh:mm:ss");

            var _name = $('#J-name').val(),                                 //姓名
                _sex = $('.J-sex:checked').val(),                           //性别
                _phone = $('#J-phone').val(),                               //手机
                _typeId = $('#J-type-id').attr('data-id'),                          //车型id
                _proinceName = $('#J-proince-id').val(),                      //省
                _cityName = $('#J-city-id').val(),                            //市
                _countyName = $('#J-county-id').val(),                        //区
                _dealerName = $('.J-dealer-name').text(),                   //经销商
                _dealerId = $('#J-dealer-id').val(),                   //经销商id
                //步骤2
                _firstPay = $('#J-first-pay').attr('data-id'),              //首付比例
                _skuItem = $('#J-sku-item').attr('data-id'),                 //期数
                //步骤3
                _cardType = $('#J-rc-card').val(),               //证件类型
                _cardNumber = $('#J-rc-card-number').val(),      //证件号
                _house = $('#J-rc-house').val(),                 //房产  
                _marry = $('#J-rc-marry').val(),                 //婚姻
                _trade = $('#J-rc-trade').val(),                 //所属行业
                _occupation = $('#J-rc-occupation').val(),       //职业
                _company = $('#J-rc-company').val(),             //公司性质
                _education = $('#J-rc-education').val(),         //学历情况
                _work = $('#J-rc-work').attr('data-id'),                   //工作年限
                _income = $('#J-rc-income').val(),               //月收入
                _financialId = $('.J-product.active').attr('data-productid');    //产品id
                _financialName = $('.J-product.active').attr('data-productname');    //产品name
                _rate = $('.J-product.active').attr('data-rate');    //利率

            //修改性别值
            if(_sex == 'M'){
                _sex = '1'
            }else{
                _sex = '0';
            }
            //保存资料
            var RC_saveData = {
                "tradeBody": {
                    "entityInfo": {
                        "A0209":"0",
                        "A0401": _name,
                        "A0402": _sex,
                        "A0403": _cardType,
                        "A0404": _cardNumber,
                        "A0410": _work,
                        "A0413": _trade,
                        "A0414": _occupation,
                        "A0418": _income,
                        "A0420": _marry,
                        "A0421": _house,
                        "A0422": _education,
                        "A0423": _company,
                        "dealer_id": _dealerId,
                        "model_id": _typeId,
                        "A0424": _phone,
                        "A0405": _cityName,
                        "A0325": _proinceName,
                        "A0314": _skuItem,
                        "A0318": _firstPay,
                        "A0313": _rate,       //利率
                        "A0315": _financialName,    //产品名称
                        "financial_id": _financialId
                    }
                },
                "tradeHead": {
                    "mainCmd": "100223",
                    "requSeq": randomNum,
                    "retnCode": "",
                    "retnDesc": "",
                    "servSeq": randomNum,
                    "subCmd": "",
                    "token": "",
                    "tradeTime": myDate
                }
            }

            var RC_query = {
                "tradeBody": {
                    "entityInfo": {
                        "queryId": ""
                    }
                },
                "tradeHead": {
                    "mainCmd": "100221",
                    "requSeq": randomNum,
                    "retnCode": "",
                    "retnDesc": "",
                    "servSeq": "",
                    "subCmd": "",
                    "token": "",
                    "tradeTime": ""
                }
            }

            $.ajax({
                url: 'http://'+loanUrl+':8080/open-service/api/dealsLoan/save',
                type: 'get',
                dataType: 'jsonp',
                data: {data: JSON.stringify(RC_saveData)},   
            })
            .done(function(data) {
                var myDate=new Date();  
                var queryId = data.tradeBody.entityInfo.queryId;

                RC_query.tradeBody.entityInfo.queryId = queryId;
                RC_query.tradeHead.tradeTime = myDate.Format("yyyy-MM-dd hh:mm:ss");

                $('#J-load-dialog').show();

                setTimeout(function(){
                    $.ajax({
                        url: 'http://'+loanUrl+':8080/open-service/api/dealsLoan/query',
                        type: 'get',
                        dataType: 'jsonp',
                        data: {data: JSON.stringify(RC_query)},
                    })
                    .done(function(data) {
                        var data = JSON.parse(data.tradeBody.entityInfo.RESPONSE_DATA);

                        if(data.R009 && data.R012){
                            resultVm.priceBool=true;
                            resultVm.sucessBool=true;
                            $('#J-result-limit .price').text(data.R012)
                        }else if(data.R009){
                            resultVm.priceBool=false;
                            resultVm.sucessBool=true;
                        }else{
                            resultVm.priceBool=false;
                            resultVm.sucessBool=false;
                        }
 
                        loanNav(); 
                        $('#J-query-message').text(data.R009);
                        $('#J-result-order').text(data.tradeBody.entityInfo.DEALSLOANORDEID);  //订单号
                        $('#J-load-dialog').hide();
                        resultInfo();
                        $('#J-step-rc-3').hide();
                        $('#J-result-wrap').show();
                    }) 
                },10000)   
            })            
        }                           
    }); 

    //招商
    $("#J-step-zs-3").validate({
        rules: {
            idCard: {
                required: true, 
                isIdCardNo:true            
            },
            homCtyCod:{
                required:true,
            },
            carCtyCod:{
                required:true,
            },
            offNam: {
                required: true,            
            },
            avgIncCod: {
                required: true,            
            },
            carDteCod: {
                required: true,            
            },
            houCtyCod: {
                required: true,            
            },
            houPrcCod: {
                required: true,            
            },
            carNo: {
                required: true,   
                minlength:6           
            },
            verify_code:{
                required: true,
                minlength:6  
            },
            agree: {
                required: true,            
            }
        },  
        messages:{
            agree:'请接受车巴巴服务条款'
        },
        errorPlacement: function(error, element) {  
            error.appendTo(element.parents('.frame'));  
        },
        submitHandler:function() {
            var randomNum = randomString(32);
            var myDate=new Date();  
            myDate = myDate.Format("yyyy-MM-dd hh:mm:ss");

            var _name = $('#J-name').val(),                                 //姓名
                _phone = $('#J-phone').val(),                               //手机
                _typeId = $('#J-type-id').val(),                          //车型
                _proinceId = $('#J-proince-id').val(),                      //省
                _cityID = $('#J-city-id').val(),                            //市
                _countyId = $('#J-county-id').val(),                        //区
                _dealerName = $('.J-dealer-name').text(),                   //经销商
                _brandId = $('#J-brand').val(),                             //品牌ID
                _typePrice = (parseInt($('#J-type-price').val())/10000).toFixed(2), //车型价格
                //步骤2
                _firstPay = $('#J-first-pay').attr('data-id'),              //首付比例
                _skuItem = $('#J-sku-item').attr('data-id'),                 //期数
                //步骤3
                _idCard = $('#J-idCard').val(),               //身份证号码
                _homCtyCod = $('#J-homCtyCod').attr('data-id'),      //户籍城市
                _carCtyCod = $('#J-carCtyCod').attr('data-id'),      //购车城市编码
                _offNam = $('#J-offNam').val(),      //工作单位
                _avgIncCod = $('#J-avgIncCod').attr('data-id'),      //月均收入
                _carDteCod = $('#J-carDteCod').attr('data-id'),      //预计购车时间
                _houCtyCod = $('#J-houCtyCod').attr('data-id'),      //房产所在城市
                _houPrcCod = $('#J-houPrcCod').attr('data-id'),      //房产当前市值
                _carInf = $('.J-carInf.active').attr('data-id'),      //是否有车
                _conFlg = $('.J-conFlg.active').attr('data-id'),    //是否愿意客户经理与您联系
                _house = $('.J-house.active').attr('data-id'),    //房屋所有情况
                _carNo = $('#J-carNo-1').val()+$('#J-carNo-2').val();      //车牌号码

            //保存
            var ZS_saveData = {
                "tradeBody": {
                    "entityInfo": {
                        "conFlg": _conFlg,
                        "carPrice": _typePrice,
                        "avgIncCod": _avgIncCod,
                        "houPrcCod": _houPrcCod,
                        "houCtyCod": _houCtyCod,
                        "ctfNbr": _idCard,     
                        "ptcFlg": "1",
                        "phoneNo": _phone,
                        "homCtyCod": _homCtyCod,
                        "carNo": _carNo,
                        "carInf": _carInf,
                        "houInf": _house,
                        "carCtyCod": _carCtyCod,
                        "custNam": _name,
                        "carDteCod": _carDteCod,
                        "offNam": _offNam,
                        "brandCode": "38"
                    }
                },
                "tradeHead": {
                    "mainCmd": "100219",            // 订单信息  固定100219
                    "requSeq": randomNum,     //自定义随机数字
                    "retnCode": "0",                //返回码 --0 
                    "retnDesc": "",                 //返回描述  --空
                    "servSeq": randomNum,     //自定义随机数字
                    "subCmd": "",      //空   
                    "token": "",       //空
                    "tradeTime": myDate //交易时间，格式：yyyy-MM-dd HH:mm:ss
                }
            }

            //查询         
            var ZS_queryDATA = {
                "tradeBody": {
                    "entityInfo": {
                        "verification":"" ,    //验证码
                        "phoneNo": _phone,
                        "queryId":"",
                        "loanOrder":""
                    }
                },
                "tradeHead": {
                    "mainCmd": "100220",
                    "requSeq": randomNum,
                    "retnCode": "0",
                    "retnDesc": "",
                    "servSeq": randomNum,
                    "subCmd": "",
                    "token": "",
                    "tradeTime": myDate
                }
            }

            if(ZS_flag){
                $('.u-wait-pop').show();
                $('.m-mask').show();
                $.ajax({
                    url: 'http://'+loanUrl+':8080/open-service/api/dealsLoan/cmbSave',
                    type:'GET',
                    dataType: 'jsonp',
                    data: {
                        data:JSON.stringify(ZS_saveData)
                    }
                })
                .done(function(data){
                    //移除loading
                    $('.u-wait-pop').hide();
                    $('.m-mask').hide();

                    var dataInfo = data.tradeBody.entityInfo;
                    var queryIdObj = JSON.parse(dataInfo.queryId);      //外层对象
                    var queryIdData = queryIdObj.Data;             //内层对象 

                    var outReturnCode = queryIdObj.ReturnCode||'';   //外层状态
                    var outMessage = queryIdObj.ReturnMessage||'';     // 外层提示

                    var insideReturnCode = queryIdData.ReturnCode||'';   //内层状态
                    var insideMessage = queryIdData.Message||'';        //内层提示

                    if(outReturnCode == '0000'){
                        if(insideReturnCode == '0000'){

                            ZS_queryID = queryIdObj.Data.Data.queryId;
                            ZS_loanOrder = dataInfo.loanOrder;
                            //显示填写验证码
                            $('#J-zs-code-frame').show();
                            $('#J-zs-next').text('立即提交');
                            ZS_flag = false;

                        }else{
                            //重新请求
                            // $('#J-zs-next').trigger('click');
                            $.errorAlert({content:'' + insideMessage + ', 请重试'});
                        }
                    }else{
                        $.errorAlert({content:'' + outMessage + ''});
                    } 
                }) 
            }else{
                //loading
                $('.u-wait-pop').show();
                $('.m-mask').show();

                var myDate=new Date();  

                myDate = myDate.Format("yyyy-MM-dd hh:mm:ss");
                ZS_queryDATA.tradeHead.tradeTime = myDate;
                ZS_queryDATA.tradeBody.entityInfo.verification = $('#J-zs-verify-code').val();
                ZS_queryDATA.tradeBody.entityInfo.queryId = ZS_queryID; 
                ZS_queryDATA.tradeBody.entityInfo.loanOrder =  ZS_loanOrder;

                $.ajax({
                    url: 'http://'+loanUrl+':8080/open-service/api/dealsLoan/cmbQuery',
                    type: 'get',
                    dataType: 'jsonp',
                    data: {
                        data: JSON.stringify(ZS_queryDATA)
                    },
                })
                .done(function(data) {
                    //移除loading
                    $('.u-wait-pop').hide();
                    $('.m-mask').hide();

                    var dataInfo = JSON.parse(data.tradeBody.entityInfo);
                    if(dataInfo){
                        var outReturnCode = dataInfo.ReturnCode ||''; // 外层状态
                        var outMessage = dataInfo.Message||'';    //外层提示

                        var insideReturnCode = dataInfo.Data.ReturnCode||''; //内层报错状态  E007
                        var insideReturnEorrer = dataInfo.Data.Message||''; //内层报错提示

                        var insideReturnCode = dataInfo.Data.ReturnCode||''; //内层状态
                        var insideMessage = dataInfo.Data.message||'';  //内层提示;
                        var insideAmt = dataInfo.Data.maxAmt2||'';  //额度;

                        //内层报错，通常是验证码
                        if(insideReturnCode == "E007"){
                            $.errorAlert({content:'' + insideReturnEorrer + ''});
                            return false;
                        }

                        setTimeout(function(){
                            if(outReturnCode == '0000' && dataInfo.Data.statusCode == '2'){
                                resultVm.priceBool=false;
                                resultVm.sucessBool=true;
                            }else{
                                resultVm.priceBool=false;
                                resultVm.sucessBool=false;
                            }
                        },100)
                    }else{
                        setTimeout(function(){
                            resultVm.priceBool=false;
                            resultVm.sucessBool=false;
                        },100)
                    }

                    loanNav();
                    $('#J-query-message').text(insideMessage)   //提示
                    $('#J-result-order').text(ZS_loanOrder);  //订单号
                    resultInfo()
                    $('#J-step-zs-3').hide();
                    $('#J-result-wrap').show();

                })   
            }
        }                           
    }); 

    //联动
    function formLink(select,obj){
        $(select).on('click',function(){
            var _bool = $(this).attr('data-bool');
            if(_bool == 'true'){
                $(obj).show().find('input').attr('disabled',false);
            }else{
                $(obj).hide().find('input').attr('disabled',true);
            }
        })
    }
    formLink('.J-house','.J-house-link');
    formLink('.J-carInf','.J-carInf-link');

    //获取车型,城市,经销商
    $('.J-series-list').on('click',function(){
        var _brandId = $(this).attr('data-brand'); 
        var _seriesID = $(this).attr('data-id');

        typeOps.param.car_series_id = _seriesID;                   //车型
        proinceListOps.param.car_series_id = _seriesID;            //省
        proinceOps.param.car_series_id = _seriesID;                //获取市
        cityOps.param.car_series_id = _seriesID;                   //获取区
        dealerOps.param.series_id = _seriesID;                 //获取经销商
        downpayOps.param.series_id = _seriesID;                    //所有首付
        periodyOps.param.series_id = _seriesID;                    //期数
        financialOps.param.car_series_id = _seriesID;                  //金融方案
        seriesOps.param.car_series_id = _seriesID;

        $('#J-brand').val(_brandId)

        //获取省
        $.ajax({
            url: proinceListOps.url,
            dataType: 'json',
            data: proinceListOps.param,
        }) 
        .done(function(data) {
            var data = data.result.province_list;
            proinceListVm.array = data || []; 
        })

        //获取区
        $.ajax({
            url: cityOps.url,
            dataType: 'json',
            data: cityOps.param,
        })
        .done(function(data) {
            var data = data['result']['county_list'];
            countyVm.array = data || []; 
        })

        //获取车系url
        $.ajax({
            url: seriesOps.url,
            dataType: 'json',
            data: seriesOps.param
        })
        .done(function(data) {
            var _city = $('#J-jump').attr('data-city');
            var _url = data.result.url; 
            _url = _city + _url;
            $('#J-jump').attr('href',_url);
        })        

        //获取车型
        $.ajax({
            url: typeOps.url,
            dataType: 'json',
            data:typeOps.param
        })
        .done(function(data) {


            var data = data['result'];
            var _provinceFlag = false;
            var _dealerFlag = false;
            var typeVmData = [];
            
            // for(var i=0; i<data['result'].length; i++ ){
            //     typeVmData.push(data['result'][i])
            // }


            // console.log(typeVmData)

            typeVm.array = data; 
            $('#J-type-id').attr('value','');

            ajaxDeaer(dealerOps); 

            $('#J-form-type').removeClass('valid').show();
            $('#J-form-city').show();

            //结果页车型图片 
            $('#J-result-pic').prop('src',data[0]['car_type_list'][0].imgs[0].CDNPATH)
        })

        ajaxDeaer(dealerOps);
    })   

    //服务条款
    $('.J-agree-dialog').on('click',function(){
        $.Alert({
            title:"任性贷服务条款与隐私政策",
            height:'518',
            cssName:'agree-dialog',
            content:'<div class="agree-body"><p style="margin-top: 15px;margin-bottom: 15px;text-indent: 32px;line-height: 22px"><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">任性贷由东风日产数据服务有限公司（以下简称<span style="font-family:Arial">“</span><span style="font-family:宋体">我们</span><span style="font-family:Arial">”</span><span style="font-family:宋体">）运营，我们依照以下服务条款向您提供本服务条款涉及&nbsp;的相关服务。请您使用任性贷服务前</span><span style="font-family:Arial">,</span><span style="font-family:宋体">仔细阅本服务条款。&nbsp;您只有完全同意所有服务条款，才能成为东风日产汽车商城的用户（</span><span style="font-family:Arial">&quot;</span><span style="font-family:宋体">用户</span><span style="font-family:Arial">&quot;</span><span style="font-family:宋体">）并使用相应服务。您在申请任性贷服务过程中点击</span><span style="font-family:Arial">&quot;</span><span style="font-family:宋体">同意任性贷服务条款</span><span style="font-family:Arial">&quot;</span><span style="font-family:宋体">按钮即表示您&nbsp;已明确同意遵&nbsp;守本服务条款以及经参引而并入其中的所有条款、政策以及指南，并受该等规则的约束（合称</span><span style="font-family:Arial">&quot;</span><span style="font-family:宋体">本服务条款</span><span style="font-family:Arial">&quot;</span><span style="font-family:宋体">）。我们可能根据法律法规的要求或业务运营&nbsp;的需要，&nbsp;对本服务条款不时进行修改。除非另有规定，否则任何变更或修改将在修订内容于任性贷发布之时立即生效，您对任性贷的使用、继续使用将表明您接受此等变&nbsp;更或修&nbsp;改。如果您不同意本服务条款（包括我们可能不定时对其或其中引述的其他规则所进行的任何修改）的全部规定，则请勿使用任性贷，或您可以主动取消任性贷提&nbsp;供的服务。</span></span></p><p style="margin-top: 15px;margin-bottom: 15px;text-indent: 32px;line-height: 22px"><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">为了便于您了解适用于您使用任性贷的条款和条件，我们将在任性贷上发布我们对本服务条款的修改，您应不时地审阅本服务条款以及经参引而并入其中的其他规则。</span></p><p><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(51,51,51);font-size:14px">一、服</span><span style=";font-family:宋体;color:rgb(51,51,51);font-size:14px">务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(51,51,51);font-size:14px">内容</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">1.&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">的具体服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">内容由我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">根据</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">实际</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">情况提供，包括但不限于信息、</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">图</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">片、文章、</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">评论</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">、</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">积</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">分抽</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">奖</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">活</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">动</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">等，我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">将定期或不定期根据用</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">户</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">的意愿，以</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">电</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">子</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">邮</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">件、短信、</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">&nbsp;</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">电话的方式为用户提供信息，并向用户提供学习、交流平台（以上统称</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">“</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">”</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">）。我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们对</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">提供的服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">在法律范</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">围</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">内</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">拥</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">有最</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">终</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">解</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">释权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">。</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">2.&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务仅</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">供个人用</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">户</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">使用。除我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们书</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">面同意，您或其他用</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">户</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">均不得将任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">上的任何信息用于商</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">业</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">及其他一切</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">经济</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">目的。</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">3.&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">您使用任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务时</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">所需的相关的</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">设备</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">以及网</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">络资</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">源等（如个人</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">电脑</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">及其他与接入互</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">联</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">网或移</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">动</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">网有关的装置）及所需的</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">费</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">用（如</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">为</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">接入互</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">联</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">网而支付的</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">电话费</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">及上网</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">费</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">）均由您自行</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">负</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">担。</span></p><p><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(51,51,51);font-size:14px">二、信息提供和</span><span style=";font-family:宋体;color:rgb(51,51,51);font-size:14px">隐</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(51,51,51);font-size:14px">私保</span><span style=";font-family:宋体;color:rgb(51,51,51);font-size:14px">护</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">1.&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">您在</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">访问</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">、使用任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">或申</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">请</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">使用任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务时</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">，必</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">须</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">提供本人真</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">实</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">的个人信息，且您</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">应该</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">根据</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">实际变动</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">情况及</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">时</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">更新个人信息。保</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">护</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">用</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">户隐</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">私是我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">的重点原</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">&nbsp;</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">则，我们通过各种技术手段和强化内部管理等办法提供隐私保护服务功能，充分保护您的个人信息安全</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">。</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">2.&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">不</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">负责审</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">核您提供的个人信息的真</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">实</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">性、准确性或完整性，因信息不真</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">实</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">、不准确或不完整而引起的任何</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">问题</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">及其后果，由您自行承担，且您</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">应</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">保</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">证</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">免受由</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">此而</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">产</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">生的任何</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">损</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">害或</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">责</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任。若我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们发现</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">您提供的个人信息是虚假、不准确或不完整的，我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">有</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">自行决定</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">终</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">止向您提供服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">。</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">3.&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">您理解，</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">为</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">申</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">请获得任性贷服务，您应向我们提供您的个人信息，为向您提供服务之目的，我们须向第三方透露您的个人信息。您特此向我们授权，为提供</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">之目的，我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">有</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">使用您的个人信息、您申</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">请</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务时</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">提供相关信息和您在使用服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务时储</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">存在任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">的非公开内容（以下</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">简</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">称</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">“</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">个人</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">资</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">料</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">”</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">）。我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">保</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">证</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">在除</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">为</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">提供</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">之目的外，不</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">对</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">外公开或向第三方提供您的个人</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">资</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">料，但下列情况除外：</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:Arial;color:rgb(102,102,102);font-size:14px">1.&nbsp;</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">(1)</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">事先</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">获</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">得您的明确授</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">；</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:Arial;color:rgb(102,102,102);font-size:14px">2.&nbsp;</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">(2)</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">按照相关司法机构或政府主管部</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">门</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">的要求；</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:Arial;color:rgb(102,102,102);font-size:14px">3.&nbsp;</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">(3)</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">以</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">维护</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">合法</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">益之目的；</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:Arial;color:rgb(102,102,102);font-size:14px">4.&nbsp;</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">(4)</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">维护社会公众利益</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">；</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:Arial;color:rgb(102,102,102);font-size:14px">5.&nbsp;</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">(5)</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">为了配合政府或法律的合法</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">要求、</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">传</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">票或指令，</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">为</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">了保</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">护</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">的系</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">统</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">和用</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">户</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">，或者</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">为</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">了确保任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷业务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">和系</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">统</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">的完整与操作，我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">可</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">获</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">取和披露其</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">认为</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">必要或恰</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">当的任何信息，包括但不限于用</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">户</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">的个人信息、</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">IP</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">地址和流量信息、使用</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">历</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">史以及</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">发</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">布内容。</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:Arial;color:rgb(102,102,102);font-size:14px">6.&nbsp;</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">(6)</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">符合其他合法要求。</span></p><p><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(51,51,51);font-size:14px">三、使用准</span><span style=";font-family:宋体;color:rgb(51,51,51);font-size:14px">则</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">1.&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">您在使用任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务过</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">程中，必</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">须</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">遵循国家的相关法律法</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">规</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">，不通</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">过</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷发</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">布、复制、上</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">传</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">、散播、分</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">发</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">、存</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">储</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">、</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">创</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">建或以其它方式公开含有以下内容的信息：</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:Arial;color:rgb(102,102,102);font-size:14px">1.&nbsp;</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">(1)</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">反</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">对宪</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">法所确定的基本原</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">则</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">的；</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:Arial;color:rgb(102,102,102);font-size:14px">2.&nbsp;</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">(2)</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">危害国家安全，泄露国家秘密，</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">颠</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">覆国家政</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">，破坏国家</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">统</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">一的；</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:Arial;color:rgb(102,102,102);font-size:14px">3.&nbsp;</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">(3)</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">损害国家荣誉和利益的</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">；</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:Arial;color:rgb(102,102,102);font-size:14px">4.&nbsp;</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">(4)</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">煽</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">动</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">民族仇恨、民族歧</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">视</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">，破坏民族</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">团结</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">的；</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:Arial;color:rgb(102,102,102);font-size:14px">5.&nbsp;</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">(5)</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">破坏国家宗教政策，宣</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">扬</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">邪教和封建迷信的；</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:Arial;color:rgb(102,102,102);font-size:14px">6.&nbsp;</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">(6)</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">散布</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">谣</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">言，</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">扰</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">乱社会秩序，破坏社会</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">稳</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">定的；</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:Arial;color:rgb(102,102,102);font-size:14px">7.&nbsp;</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">(7)</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">散布淫</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">秽</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">、色情、</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">赌</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">博、暴力、凶</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">杀</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">、恐怖或者教唆犯罪的、欺</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">诈</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">性的或以其它令人反感的</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">讯</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">息、数据、信息、文本、音</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">乐</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">、声音、照片、</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">图</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">形、代</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">码</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">或其它材料；</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:Arial;color:rgb(102,102,102);font-size:14px">8.&nbsp;</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">(8)</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">侮辱或者</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">诽谤</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">他人，侵害他人合法</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">益的；</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:Arial;color:rgb(102,102,102);font-size:14px">9.&nbsp;</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">(9)</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">其他</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">违</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">反</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">宪</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">法和法律、行政法</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">规</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">或</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">规</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">章制度的；</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:Arial;color:rgb(102,102,102);font-size:14px">10.&nbsp;</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">(10)</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">可能侵犯他人的</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">专</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">利、商</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">标</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">、商</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">业</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">秘密、版</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">或其它知</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">识产权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">或</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">专</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">有</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">利的内容；</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:Arial;color:rgb(102,102,102);font-size:14px">11.&nbsp;</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">(11)</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">假冒任何人或</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">实</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">体或以其它方式歪曲您与任何人或</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">实</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">体之关</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">联</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">性的内容；</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:Arial;color:rgb(102,102,102);font-size:14px">12.&nbsp;</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">(12)</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">未</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">经请</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">求而擅自提供的促</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">销</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">信息、政治活</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">动</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">、广告或意</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">见</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">征集；</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:Arial;color:rgb(102,102,102);font-size:14px">13.&nbsp;</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">(13)</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任何第三方的私人信息，包括但不限于地址、</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">电话</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">号</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">码</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">、</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">电</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">子</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">邮</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">件地址、身份</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">证</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">号以及信用卡卡号；</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:Arial;color:rgb(102,102,102);font-size:14px">14.&nbsp;</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">(14)</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">病毒、不可靠数据或其它有害的、破坏性的或危害性的文件；</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:Arial;color:rgb(102,102,102);font-size:14px">15.&nbsp;</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">(15)</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">与内容所在的互</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">动</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">区域的</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">话题</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">不相关的内容；</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:Arial;color:rgb(102,102,102);font-size:14px">16.&nbsp;</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">(16)</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">依我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">的自行判断，足以令人反感的内容，或者限制或妨碍他人使用或享受互</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">动</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">区域或任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">的内容，或者可能使我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">或我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">关</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">联</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">方或其他用</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">户</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">遭致任何</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">类</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">型</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">损</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">害或</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">责</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任的内容；</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:Arial;color:rgb(102,102,102);font-size:14px">17.&nbsp;</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">(17)</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">包含法律或行政法</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">规</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">禁止内容的其他内容。</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">2.&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">用</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">户</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">不得利用任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">的服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">从事下列危害</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">计</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">算机信息网</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">络</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">安全的活</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">动</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">：</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:Arial;color:rgb(102,102,102);font-size:14px">1.&nbsp;</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">(1)</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">未</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">经</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">允</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">许</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">，</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">进</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">入</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">计</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">算机信息网</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">络</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">或者使用</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">计</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">算机信息网</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">络资</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">源；</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:Arial;color:rgb(102,102,102);font-size:14px">2.&nbsp;</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">(2)</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">未</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">经</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">允</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">许</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">，</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">对计</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">算机信息网</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">络</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">功能</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">进</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">行</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">删</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">除、修改或者增加；</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:Arial;color:rgb(102,102,102);font-size:14px">3.&nbsp;</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">(3)</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">未</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">经</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">允</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">许</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">，</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">对进</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">入</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">计</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">算机信息网</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">络</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">中存</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">储</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">、</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">处</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">理或者</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">传输</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">的数据和</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">应</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">用程序</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">进</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">行</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">删</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">除、修改或者增加；</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:Arial;color:rgb(102,102,102);font-size:14px">4.&nbsp;</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">(4)</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">故意制作、</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">传</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">播</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">计</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">算机病毒等破坏性程序；</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:Arial;color:rgb(102,102,102);font-size:14px">5.&nbsp;</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">(5)</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">其他危害</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">计</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">算机信息网</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">络</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">安全的行</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">为</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">。</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">3.&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">保留在任何</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">时</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">候</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">为</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任何理由而不</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">经</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">通知地</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">过滤</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">、移除、</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">筛查</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">或</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">编辑</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">本网站上</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">发</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">布或存</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">储</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">的任何内容的</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">利，您</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">须</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">自行</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">负责备</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">份和替</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">换</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">在本网站</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">发</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">布或存</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">储</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">的任何内容，成本和</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">费</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">用自理。</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">4.&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">您</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">须对</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">自己在使用任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务过</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">程中的行</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">为</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">承担法律</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">责</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任。若您</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">为</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">限制行</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">为</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">能力或无行</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">为</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">能力者，</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">则</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">您的法定</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">监护</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">人</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">应</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">承担相</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">应</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">的法律</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">责</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任。</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">5.&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">如您的操作影响系</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">统总</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">体</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">稳</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">定性或完整性，我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">将</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">暂</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">停或</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">终</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">止您的操作，直到相关</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">问题</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">得到解决。</span></p><p><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(51,51,51);font-size:14px">四、免</span><span style=";font-family:宋体;color:rgb(51,51,51);font-size:14px">责</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(51,51,51);font-size:14px">声明</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">1.&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">是一个开放平台，用</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">户</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">将文章或照片等个人</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">资</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">料上</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">传</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">到互</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">联</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">网上，有可能会被其他</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">组织</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">或个人复制、</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">转载</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">、擅改或做其它非法用途，用</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">户</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">必</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">须</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">充分意</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">识</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">此</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">类风险</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">的存在。作</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">为</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">网</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">络</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">的提供者，我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们对</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">用</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">户</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">在任何</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">论坛</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">、个人主</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">页</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">或其它互</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">动</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">区域提供的</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任何</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">陈</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">述、声明或内容均不承担</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">责</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任。您明确同意使用任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">所存在的</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">风险</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">或</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">产</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">生的一切后果将完全由您自身承担，我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们对</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">上述</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">风险</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">或后果不承担任何</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">责</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任。</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">2.&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">您</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">违</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">反本服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">条款、</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">违</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">反道德或法律的，侵犯他人</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">利（包括但不限于知</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">识产权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">）的，我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">不承担任何</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">责</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任。同</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">时</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">，我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们对</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任何第三方通</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">过</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷发</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">送服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">或包含在服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">中的任何内容不承担</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">责</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任。</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:宋体;color:rgb(102,102,102);font-size:14px">3.&nbsp;</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">对您、其他用户或任何第三方发布、存储或上传的任何内容或由该等内容导致的任何损失或损害，我们不承担责任</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">。</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:宋体;color:rgb(102,102,102);font-size:14px">4.&nbsp;</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">对任何第三方通过任性贷可能对您造成的任何错误、中伤、诽谤、诬蔑、不作为、谬误、淫秽、色情或亵渎，我们不承担责任</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">。</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:宋体;color:rgb(102,102,102);font-size:14px">5.&nbsp;</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">对黑客行为、计算机病毒、或因您保管疏忽致使帐号、密码被他人非法使用、盗用、篡改的或丢失，或由于与本网站链接的其它网站所造成您个人资料的泄</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">露，我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">不承担</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">责</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任。如您</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">发现</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任何非法使用用</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">户帐</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">号或安全漏洞的情况，</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">请</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">立即与我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们联</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">系。</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">6.&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">因任何非任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">原因造成的网</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">络</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">中断或其他缺陷，我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">不承担任何</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">责</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任。</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">7.&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">不保</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">证</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">一定能</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">满</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">足您的要求；不保</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">证</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">不会中断，也不保</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">证</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">的及</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">时</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">性、安全性、准确性。</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">8.&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任何情况下，因使用任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">而引起或与使用任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">有关的而</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">产</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">生的由我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们负</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">担的</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">责</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">总额</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">，无</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">论</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">是基于合同、保</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">证</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">、侵</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">、</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">产</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">品</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">责</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任、</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">严</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">格</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">责</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任或其它理</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">论</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">，均不得超</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">过</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">您因</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">访问</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">或使用本网站而向任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">支付的任何</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">报</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">酬（如果有的</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">话</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">）。</span></p><p><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(51,51,51);font-size:14px">五、服</span><span style=";font-family:宋体;color:rgb(51,51,51);font-size:14px">务变</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(51,51,51);font-size:14px">更、中断或</span><span style=";font-family:宋体;color:rgb(51,51,51);font-size:14px">终</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(51,51,51);font-size:14px">止</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">1.&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">如因升</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">级</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">的需要而需</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">暂</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">停网</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">络</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">、或</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">调</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">整服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">内容，我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">将尽可能在网站上</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">进</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">行通告。由于用</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">户</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">未能及</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">时浏览</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">通告而造成的</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">损</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">失，我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">不承担任何</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">责</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任。</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">2.&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">您明确同意，我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">保留根据</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">实际</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">情况随</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">时调</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">整任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">提供的服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">内容、种</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">类</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">和形式，或自行决定授</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">第三方向您提供原本我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">提供的服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">。因</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">业务调</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">整</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">给</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">您或其</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">他用</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">户</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">造成的</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">损</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">失，我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">不承担任何</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">责</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任。同</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">时</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">，我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">保留随</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">时变</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">更、中断或</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">终</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">止任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">全部或部分服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">的</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">利。</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:宋体;color:rgb(102,102,102);font-size:14px">3.&nbsp;</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">发生下列任何一种情形，我们有权单方面中断或终止向您提供服务而无需通知您，且无需对您或第三方承担任何责任</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">：</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:Arial;color:rgb(102,102,102);font-size:14px">1.&nbsp;</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">(1)</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">您提供的个人</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">资</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">料不真</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">实</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">；</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:Arial;color:rgb(102,102,102);font-size:14px">2.&nbsp;</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">(2)</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">您</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">违</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">反本服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">条款及其他网站内</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">规</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">定；</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:Arial;color:rgb(102,102,102);font-size:14px">3.&nbsp;</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">(3)</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">未</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">经</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们书</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">面同意，将任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">平台用于商</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">业</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">及任何</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">经济</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">目的。</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">4.&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">您可随</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">时</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">通知我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们终</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">止向您提供服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">或直接取消任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">。自您</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">终</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">止或取消服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">之日起，我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">不再向您承担任何形式的</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">责</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任。</span></p><p><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(51,51,51);font-size:14px">六、知</span><span style=";font-family:宋体;color:rgb(51,51,51);font-size:14px">识产权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(51,51,51);font-size:14px">及其它</span><span style=";font-family:宋体;color:rgb(51,51,51);font-size:14px">权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(51,51,51);font-size:14px">利</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">1.&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">用</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">户</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">可以充分利用任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">平台共享信息。您可以在任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷发</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">布从任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">个人主</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">页</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">或其他网站复制的</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">图</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">片和信息等内容，但</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">这</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">些内容必</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">须</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">属于公共</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">领</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">域或者您</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">拥</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">有以上</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">述使用方式使用</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">该</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">等内容的</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">利，且您有</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">权对该</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">等内容作出本条款下之授</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">、同意、</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">认</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">可或承</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">诺</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">。</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:宋体;color:rgb(102,102,102);font-size:14px">2.&nbsp;</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">对您在任性贷发布或以其它方式传播的内容，您作如下声明和保证</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">：</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:宋体;color:rgb(102,102,102);font-size:14px">1.&nbsp;</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">对于该等内容，您具有所有权或使用权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">；</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:宋体;color:rgb(102,102,102);font-size:14px">2.&nbsp;</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">该等内容是合法的、真实的、准确的、非误导性的</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">；</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">3.&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">使用和</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">发</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">布此等内容或以其它方式</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">传</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">播此等内容不</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">违</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">反本服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">条款，也不侵犯任何人或</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">实</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">体的任何</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">利或造成</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">对</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任何人或</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">实</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">体的</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">伤</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">害。</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">3.&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">未</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">经</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">相关内容</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">利人的事先</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">书</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">面同意，您不得擅自复制、</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">传</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">播在任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">的</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">该</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">等内容，或将其用于任何商</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">业</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">目的，所有</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">这</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">些</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">资</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">料或</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">资</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">料的任何部分</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">仅</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">可作</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">为</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">个人或</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">非商</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">业</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">用途而保存在某台</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">计</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">算机内。否</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">则</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">，我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">及</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">/</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">或</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">利人将追究您的法律</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">责</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任。</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">4.&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">您在任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷发</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">布或</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">传</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">播的自有内容或具有使用</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">的内容，您特此同意如下：</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:Arial;color:rgb(102,102,102);font-size:14px">1.&nbsp;</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">(1)</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">授予我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">使用、复制、修改、改</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">编</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">、翻</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">译</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">、</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">传</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">播、</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">发</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">表此等内容，从此等内容</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">创</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">建派生作品，以及在全世界范</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">围</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">内通</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">过</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任何媒介（</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">现</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">在已知的或今后</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">发</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">明的）公开展示和表演此等内容的</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">利；</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:Arial;color:rgb(102,102,102);font-size:14px">2.&nbsp;</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">(2)</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">授予任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">及其关</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">联</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">方和再</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">许</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">可人一</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">项权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">利，可依他</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">的</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">选择</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">而使用用</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">户</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">有关此等内容而提交的名称；</span></p><p style="margin: 10px 5px 10px 61px;line-height: 25px"><span style="font-family:Arial;color:rgb(102,102,102);font-size:14px">3.&nbsp;</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">(3)</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">授予我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">在第三方侵犯您在任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">的</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">益、或您</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">发</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">布在任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">的内容情况下，依法追究其</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">责</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任的</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">利（但</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">这</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">并非我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">的</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">义务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">）；</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">5.&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">您在任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">公开</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">发</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">布或</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">传</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">播的内容、</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">图</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">片等</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">为</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">非保密信息，我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">没有</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">义务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">将此等信息作</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">为</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">您的保密信息</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">对</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">待。在不限制前述</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">规</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">定的前提下，我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">保留以适当</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">的方式使用内容的</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">利，包括但不限于</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">删</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">除、</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">编辑</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">、更改、不予采</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">纳</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">或拒</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">绝发</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">布。我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">无</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">义务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">就您提交的内容而向您付款。一旦内容已在任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷发</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">布，我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">也不保</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">证</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">向</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">您提供</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">对</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">在任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷发</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">布内容</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">进</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">行</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">编辑</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">、</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">删</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">除或作其它修改的机会。</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">6.&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">如有</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">利人</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">发现</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">您在任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷发</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">表的内容侵犯其</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">利，并依相关法律、行政法</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">规</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">的</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">规</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">定向我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们发</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">出</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">书</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">面通知的，任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">有</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">在不事先通知您的情况下自行移除相关内</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">容，并依法保留相关数据。您同意不因</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">该</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">种移除行</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">为</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">向我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">主</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">张</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任何</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">赔偿</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">，如我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">因此遭受任何</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">损</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">失，您</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">应</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">向</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">赔偿</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">的</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">损</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">失（包括但不限于</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">赔偿</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">各种</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">费</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">用及律</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">师</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">&nbsp;</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">费）</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">。</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">7.&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">若您</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">认为</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">您</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">发</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">布第</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">6.6</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">条指向内容并未侵犯其他方的</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">利，您可以向我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">以</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">书</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">面方式</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">说</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">明被移除内容不侵犯其他方</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">利的</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">书</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">面通知，</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">该书</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">面通知</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">应</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">包含如下内容：</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">8.&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">您</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">详细</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">的身份</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">证</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">明、住址、</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">联</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">系方式、您</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">认为</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">被移除内容不侵犯其他方</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">利的</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">证</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">明、被移除内容在任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">上的位置以及</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">书</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">面通知内容的真</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">实</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">性声明。我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">收</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">到</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">该书</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">面通知后，有</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">决定是否恢复被移除内容。</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">9.&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">您特此同意，如果</span><span style=";font-family:Arial;color:rgb(102,102,102);font-size:14px">6.7</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">条中的</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">书</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">面通知的</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">陈</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">述失</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">实</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">，您将承担由此造成的全部法律</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">责</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任，如我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">因此遭受任何</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">损</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">失，您</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">应</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">向</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">赔偿</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">的</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">损</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">失（包括但不限于</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">赔偿</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">各种</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">费</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">用及律</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">师费</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">）。</span></p><p><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(51,51,51);font-size:14px">七、特</span><span style=";font-family:宋体;color:rgb(51,51,51);font-size:14px">别约</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(51,51,51);font-size:14px">定</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">1.&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">您使用本服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">的行</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">为</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">若有任何</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">违</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">反国家法律法</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">规</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">或侵犯任何第三方的合法</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">益的情形</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">时</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">，我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">有</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">直接</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">删</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">除</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">该</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">等</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">违</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">反</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">规</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">定之信息，并可以</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">暂</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">停或</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">终</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">止向您提供服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">。</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">2.&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">若您利用任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">从事任何</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">违</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">法或侵</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">权</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">行</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">为</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">，由您自行承担全部</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">责</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">任，因此</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">给</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">或任何第三方造成任何</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">损</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">失，您</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">应负责</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">全</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">额赔偿</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">，并使我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">免受由此</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">产</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">生的任何</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">损</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">害。</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">3.&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">您同意我</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">们</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">通</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">过</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">重要</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">页</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">面的公告、通告、</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">电</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">子</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">邮</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">件以及常</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">规</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">信件的形式向您</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">传</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">送与任性</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">贷</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">有关的任何通知和通告。</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">4.&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">本服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">条款之效力、解</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">释</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">、</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">执</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">行均适用中</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">华</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">人民共和国法律。</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">5.&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">如就本</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">协议</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">内容或其</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">执</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">行</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">发</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">生任何争</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">议</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">，</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">应</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">尽量友好</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">协</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">商解决；</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">协</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">商不成</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">时</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">，任何一方均可向</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">东风</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">日</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">产</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">数据服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">有限公司所在地的人民法院提起</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">诉讼</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">。</span></p><p style="margin: 10px 5px 10px 33px;line-height: 25px"><span style="font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">6.&nbsp;</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">本服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">条款中的</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">标题仅为</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">方便而</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">设</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">，不影响</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">对</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">于条款本身的解</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">释</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">。在法律允</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">许</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">的范</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">围</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">内，本服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">条款最</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">终</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">解</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">释权归东风</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">日</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">产</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">数据服</span><span style=";font-family:宋体;color:rgb(102,102,102);font-size:14px">务</span><span style=";font-family:&#39;MS Mincho&#39;;color:rgb(102,102,102);font-size:14px">有限公司所有。</span></p><p><span style=";font-family:Calibri;font-size:16px">&nbsp;</span></p><p><br/></p></div>',
            ft:'<div class="agree-btn"><a class="u-btn-deepred J-close" href="javascript:;">关闭</a></div>'
        }) 
    })  

    //招行服务条款
    $('.J-ZS-agree-dialog').on('click',function(){
        $.Alert({
            title:"招商银行信用卡消费信贷业务",
            height:'518',
            cssName:'agree-dialog',
            content:'<p style="text-align: center; line-height: 1.5em;"><span style="font-family: STHeiti; font-size: 12px; line-height: 1.5em; text-indent: 32px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;本协议是由招商银行股份有限公司信用卡中心（以下简称“卡中心”）与使用招商银行信用卡消费信贷业务在线服务的用户(以下简称“您”)就招商银行信用卡消费信贷业务在线服务（以下简称“本服务”）的使用等相关事项所订立的有效合约。您通过互联网（Internet）点击确认或以其他方式选择接受本协议，即表示您同意接受本协议的全部约定内容，确认承担由此产生的一切责任。</span><br/></p><p style="text-indent: 32px; line-height: 1.5em;"><span style="font-size: 12px;font-family: STHeiti">在接受本协议之前，请您仔细阅读本协议的全部内容（特别是以<strong><span style="text-decoration:underline;">粗体下划线标注</span></strong>的内容）。如果您不同意本协议的任何内容，或者无法准确理解相关条款的解释，请不要进行后续操作。<br/><br/>“招商银行信用卡消费信贷业务在线服务”是卡中心在招商银行信用卡网站上为您提供的招商银行信用卡消费信贷业务在线预约办理、预审的服务。</span></p><p style="text-indent: 32px; line-height: 1.5em;"><strong><span style="text-decoration:underline;"><span style="font-size: 12px;font-family: STHeiti">您确认：卡中心对本协议中有关免除或限制卡中心责任、卡中心单方面拥有某些权利、增加您责任或限制您权利的条款，均已向您本人进行了提示和说明。在申请本服务以接受本服务之前，您已充分阅读、理解并接受本协议的全部内容，一旦使用本服务，即表示您同意遵循本协议之所有约定。</span></span></strong></p><p style="text-indent: 32px; line-height: 1.5em;"><strong><span style="text-decoration:underline;"><span style="font-size: 12px;font-family: STHeiti">您同意：基于运行和交易安全等的需要，卡中心有权变更、暂停本服务，有权暂时停止提供或者限制本服务部分功能或提供新的功能，有权修改、终止本协议，并于执行前通过卡中心网站、招商银行营业网点、对账单、电子邮件、短信、报刊、语音电话等方式进行公告。相关公告经网站、营业网点、对账单、电子邮件、短信、报刊、语音电话等方式发布视为您已收到并对您有约束力。您在公告执行后继续办理使用本服务的，视同您接受有关本协议、本服务修改、变更的内容并将遵循修改、变更后的内容使用本服务；若您不同意接受有关本协议、本服务修改、变更的内容，您应停止使用本服务。本协议终止后，卡中心在协议终止前已接收的申请仍有效，您应承担其后果。</span></span></strong></p><p style="text-indent: 32px; line-height: 1.5em;"><strong><span style="text-decoration:underline;"><span style="font-size: 12px;font-family: STHeiti">您声明：本协议内容不受您所属国家或地区法律的排斥，否则，您应立即停止使用本服务。</span></span></strong></p><p style="text-indent: 32px; line-height: 1.5em;"><strong><span style="text-decoration:underline;"><span style="font-size: 12px;font-family: STHeiti">卡中心将根据您所填写的个人信息进行消费信贷业务的预审等。您充分了解并自愿填写申请信息并保证填写的信息真实有效。您同意：</span></span></strong><span style="font-size: 12px;font-family: STHeiti">&nbsp;<br/><strong><span style="text-decoration:underline;">1</span></strong></span><strong><span style="text-decoration:underline;"><span style="font-size: 12px;font-family: STHeiti">）根据本服务的提示，准确提供相关消费信贷业务申请资料。若卡中心有合理理由怀疑您提供的资料错误、不实、过时或不完整等，卡中心有权暂停或终止向您提供部分或全部的招商银行信用卡消费信贷业务在线服务。卡中心对此不承担任何责任。</span></span></strong><span style="font-size: 12px;font-family: STHeiti">&nbsp;<br/><strong><span style="text-decoration:underline;">2</span></strong></span><strong><span style="text-decoration:underline;"><span style="font-size: 12px;font-family: STHeiti">）预审结果将根据您提交的材料分析得出，预审结果仅供参考，您是否具备办理消费信贷业务的资格及分期金额以卡中心最终审核结果为准。因预审结果与卡中心最终审核结果不一致而产生的任何后果均由您自行承担，卡中心不承担任何责任。&nbsp;</span></span></strong><span style="font-size: 12px;font-family: STHeiti"><br/><strong><span style="text-decoration:underline;">3</span></strong></span><strong><span style="text-decoration:underline;"><span style="font-size: 12px;font-family: STHeiti">）使用本服务在线登记、申请、查询等均视为您本人所为。您对使用本服务在线进行的申请、查询等一切操作负完全责任，</span></span></strong><span style="font-size: 12px;font-family: STHeiti">&nbsp;<br/><strong><span style="text-decoration:underline;">4</span></strong></span><strong><span style="text-decoration:underline;"><span style="font-size: 12px;font-family: STHeiti">）您应妥善保管好自己的信息，对于您保管不善被他人使用、申请、查核预审结果等或造成其他损失的，由您自行承担。</span></span></strong></p><p style="text-indent: 32px; line-height: 1.5em;"><strong><span style="text-decoration:underline;"><span style="font-size: 12px;font-family: STHeiti">一旦您同意签订本协议，完成本服务的全部流程，视同您同意并授权卡中心对您进行消费信贷业务的预审，包括但不限于向任何有关方面了解和查询您的资产、资信、个人信用信息、人行记录等情况。</span></span></strong></p><p style="line-height: 1.5em;"><span style="font-size: 12px;font-family: STHeiti;background: white">本服务通过互联网网络实现，卡中心非网络服务商，您理解并同意本服务提供过程中的合理时间。使用本服务时，可能由于网络连线问题、信用卡账户额度不足或其他不可抗拒因素，造成本服务无法提供，卡中心不承担任何责任。在使用过程中如有任何疑问，请及时联系招商银行信用卡消费信贷客户服务中心电话：4008-855-855。</span><span style="font-size: 12px;font-family: STHeiti"><br/><br/></span><span style="font-size: 12px;font-family: STHeiti;background: white">您不得利用本服务进行非法活动、欺诈或违反诚信原则的行为，且有义务配合卡中心进行相关调查，一旦您拒绝配合进行相关调查或卡中心认为您存在或涉嫌任何非法活动、欺诈或违反诚信原则的行为、或违反本协议约定的，卡中心有权采取以下一种、多种或全部措施：（1）暂停或终止提供本服务；（2）终止本协议；（3）取消您的信用卡使用资格。</span></p><p style="line-height: 1.5em;"><span style="font-size: 12px;font-family: STHeiti;background: white">卡中心与您在履行本协议中发生的争议，由双方协商解决，协商不成提起诉讼的，由上海市浦东新区人民法院管辖。</span><span style="font-size: 12px;font-family: STHeiti"><br/><br/><br/></span></p><p style="text-indent: 32px; line-height: 1.5em;"><strong><span style="text-decoration:underline;"><span style="font-size: 12px;font-family: STHeiti">本协议适用中华人民共和国大陆地区有关法律和中国人民银行、中国银行业监督管理委员会的有关规定，未尽事宜依据招商银行信用卡领用合约、《招商银行信用卡章程》、业务规定及金融惯例、国家外汇管理有关规定办理。</span></span></strong></p><p style="line-height: 1.5em;">&nbsp;</p><p><br/></p>',
            ft:'<div class="agree-btn"><a class="u-btn-deepred J-close" href="javascript:;">关闭</a></div>'
        }) 
    })
})