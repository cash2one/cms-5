//验证数组
var arrSign = {
    name: false,
    tel: false,
    loction: false,
    ss: false
};
//传参数数组
var arrInfo = {
    name: '',
    sex: 'man',
    tel: '',
    carId: '',
    p: '广东省',
    c: '广州市',
    v: '天河区',
    ssID1: '',
    ssID2: '',
    ssID3: '',
    fwID: '获取优惠',
    jhTime: '一个月内',
    fsID: '全款购车',
};


$(function () {
    //sam
    //获取URL参数：
    var series_id = CBB.getUrlParam("series_id"),
        model_id = CBB.getUrlParam("model_id"),
        city = CBB.getUrlParam("city") || $("#default-data").attr("data-defaultcity"),
        area = CBB.getUrlParam("area"),
        dealer_id = CBB.getUrlParam("dealer_id"),
        server = CBB.getUrlParam("server"),
        lead_key = CBB.getUrlParam("lead_key"),
        brand_id = $("#default-data").attr("data-brand");
    var getModelUrl = $("#model_plug").attr("data-modeUrl"),
        getCityUrl = $("#address").attr("data-url");



    //如果有dealer_id参数,获取dealer 名称等信息显示
    if (dealer_id) {
        var alist = dealer_id.split("|");
        var dealer_n = 0;
        $.each(alist, function (i, item) {
            if (i > 2) {
                return false;
            }
            if (i == 0) {
                $("#selected-dealer").html("");
            }
            $.ajax({
                url: "/beijing/api/dealer_by_id/",
                data: {dealer_id: item},
                success: function (data) {
                    if (data.result) {
                        dealer_n++;
                        $(".j-zyd-n").text(dealer_n);
                        $("#selected-dealer").append('<li class="u-list-zyd" xg-zyd-index="' + data.result.dlr_code + '" data-dealerid="' + data.result.id + '">' +
                            '<span class="s-main zyd">' + data.result.dlr_short_name + '</span><span class="s-main d">' + data.result.county_name + '</span>' +
                            '<div class="f-fr f-va-m x j-zyd-x"><i class="u-icon u-icon-x"></i></div></li>');
                    }
                }
            })
        })

    }

    //初始默认城市数据
    initCity(city, area);


    //选项数组
    var arrArea = [];
    var areaLength = 3;

    //下拉框
    $('.j-select-area').on('click', function () {
        $(this).find('.j-down').css({
            borderBottomColor: '#fff'
        })
        $(this).find('.j-down .u-iconright').removeClass('u-icon-arrowdown').addClass('u-icon-arrowsup');
        $(this).find('.j-areas').show();
    }).on('mouseleave', function () {
        $(this).find('.j-down').css({
            borderBottomColor: '#e2e2e2'
        })
        $(this).find('.j-down').children('.u-iconright').removeClass('u-icon-arrowsup').addClass('u-icon-arrowdown');
        $(this).find('.j-areas').hide();
    });
    $('.j-areas li').on('click', function () {
        $(this).parent().prev().find('span').html($(this).find('a').text());
        if ($(this).find('a').hasClass('z-none')) {
            $(this).parent().prev().find('span').addClass('z-none');
        } else {
            $(this).parent().prev().find('span').removeClass('z-none');
        }

        $(this).parents('.j-select-area').find('.j-down').css({
            borderBottomColor: '#e2e2e2'
        })
        $(this).parents('.j-select-area').find('.j-down').children('.u-iconright').removeClass('u-icon-arrowsup').addClass('u-icon-arrowdown');
        $(this).parents('.j-select-area').find('.j-areas').hide();

        juNone();
        closeList($(this).parents(".j-select-area"));
        if ($(this).parents("#buy-plan-time").length) {
            $("#buy-time-plan").val($(this).find("a").attr("data-value"))
            return false;
        }

    });
    //判断是否为无计划
    function juNone() {
        if ($('.j-down').find('span').hasClass("z-none")) {
            $('.j-jh').hide();
        } else {
            $('.j-jh').show();
        }
    }

    juNone();
    //模式选择按钮
    $('.u-btn-select').on('click', function () {
        var txt = $(this).find("span").text();
        $(this).parent().children('.u-btn-select').removeClass('z-active');
        $(this).addClass('z-active');
        if (txt == "获取优惠") {
            $(".s-lg").text("获取优惠");
        } else if (txt == "预约试驾") {
            $(".s-lg").text("预约试驾");
        }
    });
    //姓名，手机号码验证
    $('.xg-name').on('blur', function () {
        $(this).formCheck(
            {
                checkModel: 'nameCheck',
                ref: /^[\u4e00-\u9fa5A-Za-z0-9_]{1,32}$/,
                msg: '请输入正确的姓名',
                emptyMsg: '姓名不能为空'
            }
        );
        var msg = $(this).attr('data-xg-msg');
        if (this.resultBool) {
            //通过
            $('.xg-msg-name').html('');
            $('.xg-msg-name').prev().removeClass('u-icon-hongtan').addClass('u-icon-lvdui');
            $(this).removeClass('z-input-error');
            arrSign.name = true;
            arrInfo.name = $(this).val();
        } else {
            //没通过
            $('.xg-msg-name').html(msg);
            $('.xg-msg-name').prev().removeClass('u-icon-lvdui').addClass('u-icon-hongtan');
            $(this).addClass('z-input-error');
            arrSign.name = false;
            arrInfo.name = '无名氏';
        }
        $('.xg-msg-name').parent().show();
        enableSubmit();
    });
    $('.xg-tel').on('blur', function () {
        $(this).formCheck(
            {
                checkModel: 'phoneCheck',
                msg: '请输入正确的11位手机号',
                emptyMsg: '手机号码不能为空'
            }
        );
        var msg = $(this).attr('data-xg-msg');
        if (this.resultBool) {
            //通过
            $('.xg-msg-tel').html('');
            $('.xg-msg-tel').prev().removeClass('u-icon-hongtan').addClass('u-icon-lvdui');
            $(this).removeClass('z-input-error');
            arrSign.tel = true;
            arrInfo.tel = $(this).val();
        } else {
            //没通过
            $('.xg-msg-tel').html(msg);
            $('.xg-msg-tel').prev().removeClass('u-icon-lvdui').addClass('u-icon-hongtan');
            $(this).addClass('z-input-error');
            arrSign.tel = false;
            arrInfo.tel = '';
        }
        $('.xg-msg-tel').parent().show();
        enableSubmit()
    });
//选择性别
    $('.sex').children('a').on('click', function () {
        $('.sex').children('a').removeClass('z-active');
        $(this).addClass('z-active');
        arrInfo.sex = $(this).attr('sex');
//    alert(arrInfo.sex);
    });
    //$('.aa').click();
    //选择省市
    $(".select-address").delegate("li", "click", function () {
        var str = $(this).children('a').text(),
            li_type = $(this).attr("data-area");
        var brand_id = $("#default-data").attr("data-brand");
        var isPop = $(this).parent().attr("data-popwin") == "1" ? true : false;
        var $parentDiv = $(this).parents(".j-select-area");

        $(this).parent().prev().children('span').html(str);
        $(this).parent().hide();
        switch (li_type) {
            case "li-area-pv":
                var id = $(this).attr("data-pvid");
                $(this).parent().prev().attr({"data-pvid": id});
                getCityByPv(id, isPop);
                cleanCtAr("li-area-pv", isPop);
                if ($(this).parent().prev().attr("id") == "dealer-address-pv") {
                    $("#dealer-address-ct .s-main").text("选择城市");
                    $("#dealer-address-ar").next().html("");
                    $("#dealer-address-ar .s-main").text("选择区县");
                } else {
                    $("#dealer-address-ct .s-main,#address-ct-div .s-main").text("选择城市");
                    $("#address-ar-div").next().html("");
                    $("#dealer-address-ar").next().html("");
                    $("#dealer-address-ar .s-main,#address-ar-div .s-main").text("选择区县");
                }

                break;
            case "li-area-ct":
                var id = $(this).attr("data-cityid");
                $(this).parent().prev().attr({"data-ctid": id});
                getAreaByCt(id, isPop);
                cleanCtAr("li-area-ct", isPop)
                if (isPop) {
                    arrArea = [];
                    $("#pop-dealer-ul").html('<img src="../../static/site/images/lib/loding.gif">');
                    getDealerByCity(brand_id, id)
                }
                if ($(this).parent().prev().attr("id") == "dealer-address-ct") {
                    $("#dealer-address-ar").next().html("");
                    $("#dealer-address-ar .s-main").text("选择区县");
                } else {
                    $("#address-ar-div").next().html("");
                    $("#dealer-address-ar").next().html("");
                    $("#dealer-address-ar .s-main,#address-ar-div .s-main").text("选择区县");
                }

                break;
            case "li-area-ar":
                var id = $(this).attr("data-areaid");
                $(this).parent().prev().attr({"data-arid": id});
                if (isPop) {
                    $("#pop-dealer-ul li").hide();
                    $(".area-" + id).show();
                }
                break;
            default :
                break;

        }
        closeList($parentDiv);
        return false;
    })
    //点击 更多 弹出框
    $("body").on("click", ".j-zyd-more", function () {
        $("body").css({
            overflow: 'hidden'
        })
        $(".m-cover").show();
        $(".j-zyd").show();
//      $('.m-popup-list-zyd').find('.z-active').each(function(index,el){
//        pushArea($(el).parent().parent().get(0));
//      });
        //初始 经销商弹窗 默认城市数据
        $("#pop-dealer-ul").html('<img src="../../static/site/images/lib/loding.gif">');
        setDealerByAddBrand(brand_id);
    });
    //关闭更多弹窗
    /*$(".m-popup .close").click(function(){
     $(".m-cover").hide();
     $(".j-zyd").hide();
     })*/

    function xgArea(t, addr, loc, id, dl_code, dl_id) {
        this.t = t;
        this.addr = addr;
        this.loc = loc;
        this.id = id;
        this.dl_code = dl_code;
        this.dealer_id = dl_id;
        return this;
    }

    //确认选择
    $("body").on("click", ".j-close", function () {
        var _select = $('.m-popup-list-zyd').find('.z-active');
        if (!_select.length) {
            $(".m-cover").hide();
            $(".j-zyd").hide();
            return false;
        }
        $("body").css({
            overflow: 'auto'
        })
        $(".m-cover").hide();
        $(".j-zyd").hide();
        var str = '';
        $('.m-popup-list-zyd').find('.z-active').each(function (index, el) {
            pushArea($(el).parent().parent().get(0));
        });
        for (var i = 0; i < arrArea.length; i++) {
            str += '<li class="u-list-zyd" xg-zyd-index="';
            str += arrArea[i].dl_code;
            str += '" data-dealerid="' + arrArea[i].dealer_id + '"><span class="s-main zyd">';
            str += arrArea[i].t;
            str += '</span> <span class="s-main d">';
            str += arrArea[i].loc;
            str += '</span><div class="f-fr f-va-m x j-zyd-x"><i class="u-icon u-icon-x"></i></div>';
        }
        $('.j-zyd-n').text(arrArea.length);

        $('.m-list-zyd').html(str);
        getPriceByDlMd(arrArea);
        enableSubmit();
    });
    //删除专营店 自运行
    (function deletezyd() {
        $(".m-list-zyd").delegate(".j-zyd-x", "click", function () {
            if (arrArea.length > 0) {
                deleteArea($(this).parent().attr('xg-zyd-index'));
                $(this).parent().remove();
                /*if (arrArea.length == 1) {
                 $('.j-zyd-x').hide();
                 }*/
            } else {
                var n = parseInt($(".j-zyd-n").text());
                $(this).parent().remove();
                $(".j-zyd-n").text((n - 1) ? n - 1 : 0);
            }
            getPriceByDlMd(arrArea);
            enableSubmit();
        })

    })()

    //选择专营店
    $("#pop-dealer-ul").delegate("li", "click", function () {
        var n;
        if ($(this).find('.st').hasClass('z-active')) {
            $(this).find('.st').removeClass('z-active');
            deleteArea($(this).attr('xg-zyd-index'));
        } else {
            //n = $(this).parent().find('.z-active').length;
            n = arrArea.length;
            if (n >= areaLength) {
                $.errorAlert({content: '不能选择超过' + areaLength + '个经销商。'});
            } else {
                $(this).find('.st').addClass('z-active');
                pushArea(this);
            }
        }
    })
//更新数组元素
//添加数组元素
    function pushArea(el) {
        var temp = true;
        showArealength();
        if (arrArea.length > areaLength) {
            temp = false;
            //$.errorAlert('数组长度超过' + areaLength + '了');
            $.errorAlert({content: '不能选择超过3个经销商。'});
            return;
        }

        //
        for (var i = 0; i < arrArea.length; i++) {
            if (arrArea[i].dl_code == $(el).attr('xg-zyd-index')) {
                temp = temp && false;//temp false
            } else {
                temp = temp && true;
            }
        }
        if (temp) {
            var t = $(el).find('.t').text();
            var addr = $(el).find('.addr').text();
            var loc = $(el).find('.d').text();
            var id = $(el).attr('xg-zyd-index'),
                dl_code = $(el).attr("data-dlcode"),
                dealer_id = $(el).attr("data-dealerid");
            var tempArea = new xgArea(t, addr, loc, id, dl_code, dealer_id);
            arrArea.push(tempArea);
        }
        showArealength()
    }

    //删除数组元素
    function deleteArea(id) {
        for (var i = 0; i < arrArea.length; i++) {
            if (arrArea[i].dl_code == id) {
                arrArea.splice(i, 1);
                showArealength()
                return;
            }
        }
        showArealength()
    }

    //显示数组长度
    function showArealength() {
        var len = arrArea.length || $("#selected-dealer li").length;
        $('.j-zyd-n').html(len);
    }

//提交数据
    $('.j-submit').on('click', function () {
        if ($(this).hasClass("f-disable")) {
            return false;
        }
        $(this).addClass("f-disable");
        $.lodingWin();
        var _th = this,
            post_url = $(this).attr("data-url"),
            name = $(".xg-name").val(),
            phone = $(".xg-tel").val(),
            gender = $(".sex .z-active").attr("data-value"),
            dealers_el = $("#selected-dealer li"),
            series_id = $("#carSeriesId").val(),
            model_id = $("#product_id").attr("data-model"),
            address = $("#address-pv-div .s-main").text() + "省" + $("#address-ct-div .s-main").text() + "市" + $("#address-ar-div .s-main").text() + "区",
            city_id = $("#address-ct-div").attr("data-ctid"),
            countyId = $("#address-ar-div").attr("data-arid"),
            server_type = $("#server-type .z-active").attr("data-value"),
            method = $("#buy-method .z-active").attr("data-value"),
            buy_time = $("#buy-time-plan").val();
        var lead_key = CBB.getUrlParam("lead_key"),
            activity_name = decodeURI(encodeURI(CBB.getUrlParam("activity")));


        var dealers = [];
        $.each(dealers_el, function (i, item) {
            dealers.push($(item).attr("xg-zyd-index"));
        })
        var param = {
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
            name: name,
            sex: gender,
            phone: phone,
            dlrCode: dealers,
            source: 4,
            clueType: server_type,
            carTypeId: model_id,
            carSeriesId: series_id,
            address: address,
            cityId: city_id,
            countyId: countyId,
            buyPlanTimeCode: buy_time,
            activityName: key_name[lead_key],
            buyWayCode: method,
            pageId: lead_key
        }

        var _param = param,
            param_dlrCode_len = param.dlrCode.length,
            isAllFail = [];
        $.each(param.dlrCode, function (i, item) {
            _param.dlrCode = item;
            $.ajax({
                url: post_url,
                data: _param,
                method: "post",
                success: function (data) {
                    var _data = $.parseJSON(data.result);
                    if (parseInt(_data.error) > 0) {
                        isAllFail.push(false);
                    } else {
                        _smq.push(['custom','cbb-lead-done',_data.clueCode,'']);
                        location.href = $(_th).attr("data-success");
                    }
                },
                error: function () {
                    var isPass = false;
                    if (isAllFail.length >= param_dlrCode_len) {
                        $.each(isAllFail, function (i, item) {
                            isPass = (isPass || item)
                        })
                        if (!isPass) {
                            $(_th).removeClass("f-disable");
                            $.lodingWin.fClose();
                        }
                    }
                    /* $(_th).removeClass("f-disable");
                     $.lodingWin.fClose();*/
                }
            }).done(function () {
                var isPass = false;
                if (isAllFail.length >= param_dlrCode_len) {
                    $.each(isAllFail, function (i, item) {
                        isPass = (isPass || item)
                    })
                    if (!isPass) {
                        $(_th).removeClass("f-disable");
                        $.lodingWin.fClose();
                        $.errorAlert({
                            content: "数据提交不成功，请重试！"
                        })
                    }
                }
            })
        })
        return;
    });
//计划


    //sam

    if (server == "2") {
        $(".m-info-title .s-lg").text("预约试驾");
    }


    //初始化车型插件
    initModle(getModelUrl, series_id);

    //
    $("#model_plug").click(function () {
        $(".model-list-wrap").show().find(".u-plug-model").show();
    })
    $("#model_plug").on("mouseleave", function () {
        $(".model-list-wrap").hide();
    })


    //获取传递过来的 城市数据
    function initCity(city, area) {
        $.ajax({
            url: getCityUrl,
            data: {city_id: city, county_id: area},
            success: function (data) {
                setAddress(data.result)
            }
        })
    }

    //设置默认城市 数据
    function setAddress(obj) {
        var $pv = $(".u-div-p"),
            $ct = $(".u-div-c"),
            $ar = $(".u-div-d");
        if (obj && obj.province) {
            $pv.attr({"data-pvid": obj.province.province_id});
            $pv.find("span").text(obj.province.province_name)
        }
        if (obj && obj.city) {
            $ct.attr({"data-ctid": obj.city.city_id});
            $ct.find("span").text(obj.city.city_name)
        }
        if (obj && obj.county) {
            $ar.attr({"data-arid": obj.county.county_id});
            $ar.find("span").text(obj.county.county_name)
        } else {
            $ar.find("span").text("选择区县")
        }
        obj && getCityByPv(obj.province.province_id);
        obj && getAreaByCt(obj.city.city_id);
    }

    //设置经销商弹窗的数据
    function setDealerByAddBrand(brandid) {
        //var _th=this;
        var $pv = $("#address-pv-div"), $ct = $("#address-ct-div"), $ar = $("#address-ar-div");
        var province_id = $pv.attr("data-pvid"),
            province_name = $pv.find(".s-main").text(),
            city_id = $ct.attr("data-ctid"),
            city_name = $ct.find(".s-main").text(),
            area_id = $ar.attr("data-arid"),
            area_name = $ar.find(".s-main").text();
        var url = "", param = {per_page: 500, page: 1, car_brand_id: brandid};
        var $province = $("#dealer-address-pv"),
            $city = $("#dealer-address-ct"),
            $area = $("#dealer-address-ar");

        //设置地址数据
        $province.attr({"data-pvid": province_id}).find("span").text(province_name);
        $city.attr({"data-ctid": city_id}).find("span").text(city_name);
        $area.attr({"data-arid": area_id}).find("span").text(area_name);

        //如有 区 则根据区显示否则根据 城市 显示  这里会有切换区后没数据的问题 改成只根据城市显示数据
        url = "/beijing/api/finance_city_brand_dealer/";
        param.city_id = city_id;

        $.ajax({
            url: url,
            data: param,
            success: function (data) {
                //渲染经销商弹窗数据
                randerDealer(data.result);
                if (area_id) {
                    $("#dealer-address-ar").next().find("li[data-areaid=" + area_id + "]").trigger("click");
                }
                //保证弹窗中选项的选中状态与外面页面一致
                $('.m-popup-list-zyd').find('.m-popup-zyd').each(function (index, el) {
                    $(el).find('.j-st').removeClass('z-active');
                    for (var i = 0; i < arrArea.length; i++) {
                        if ($(el).attr('xg-zyd-index') == arrArea[i].dl_code) {
                            $(el).find('.j-st').addClass('z-active');
                        }
                    }
                });
            }
        })
    }

    //弹窗 ：根据城市获取经销商 弹窗更改 城市时使用 城市参数与页面上不一样，故单独起一FUNCTION
    function getDealerByCity(brandid, cityId) {
        var param = {per_page: 500, page: 1, car_brand_id: brandid, city_id: cityId};
        $.ajax({
            url: "/beijing/api/finance_city_brand_dealer/",
            data: param,
            success: function (data) {
                //渲染经销商弹窗数据
                randerDealer(data.result);

                //保证弹窗中选项的选中状态与外面页面一致
                $('.m-popup-list-zyd').find('.m-popup-zyd').each(function (index, el) {
                    $(el).find('.j-st').removeClass('z-active');
                    for (var i = 0; i < arrArea.length; i++) {
                        if ($(el).attr('xg-zyd-index') == arrArea[i].dl_code) {
                            $(el).find('.j-st').addClass('z-active');
                        }
                    }
                });
            }
        })
    }

    //根据所选 第一家经销商 及 车型ID 获取 报价
    function getPriceByDlMd(aDealers) {
        var model_id = $("#product_id").attr("data-model");
        var price_wrap = $(".price-price-r .s-nm");
        price_wrap.html("");//清空原有报价，待后面更新
        var a_tmp = [];
        if (!aDealers || !aDealers.length) {
            aDealers = $(".m-list-zyd li");
            $.each(aDealers, function (i, item) {
                a_tmp.push({dealer_id: $(item).attr("data-dealerid")})
            })
            aDealers = a_tmp;
        }
        if (aDealers.length && model_id) {
            $.ajax({
                url: "/beijing/api/finance_dealer_car_types_price/",
                data: {'dealer_id': aDealers[0].dealer_id, 'car_type_id': model_id},
                success: function (data) {
                    refsDlPrice(data.result)
                }
            })
        }

    }

    //更新右边小块 经销商报价
    function refsDlPrice(obj) {
        var price_wrap = $(".price-price-r li");
        if (obj) {
            price_wrap.eq(0).find(".s-nm").text((obj.guide_price / 10000).toFixed(2) + "万")
            price_wrap.eq(1).find(".s-nm").text((obj.price / 10000).toFixed(2) + "万")
            price_wrap.eq(2).find(".s-nm").text(obj.discount >= 10000 ? (obj.discount / 10000).toFixed(2) + "万" : obj.discount + "元");
        } else {
            price_wrap.eq(0).find(".s-nm").text("暂无报价")
            price_wrap.eq(1).find(".s-nm").text("暂无报价")
            price_wrap.eq(2).find(".s-nm").text("暂无优惠");
        }

    }

    //初始化车型插件
    function initModle(plug_url, series_id) {
        var modelPlg = new modelPlug({
            el_wrap: $(".model-list-wrap"),
            nameLable: $("#product_id"),
            isClear: true,
            showData: true,
            callback: function (modelName, modelId, el) {
                getPriceByDlMd(arrArea, modelId);
                $("#price-block-name .s-sm").text(modelName);
            },
            fucAfter: function (el) {
                if (model_id) {
                    $("#model_plug li[data-modelid='" + model_id + "']").trigger("click")
                } else {
                    el.find(".model_name").eq(0).trigger("click");
                }
                if (server) {
                    $("#server-type .u-btn-select[data-value='" + server + "']").trigger("click")
                }
            }
        })
        modelPlg.main(plug_url, series_id);
    }

    //判断是否选择经销商
    function checkDealersNum() {
        var n = parseInt($(".j-zyd-n").text());
        if (n) {
            return true;
        } else {
            return false;
        }
    }

    function enableSubmit() {
        var isPass = checkDealersNum() && $('.xg-name').get(0).resultBool && $('.xg-tel').get(0).resultBool;
        if (isPass) {
            $(".j-submit").removeClass("f-disable");
        } else {
            $(".j-submit").addClass("f-disable");
        }
    }

})
//  $(document).ready() end;


//通过省获取市 数据
function getCityByPv(pvid, isPopWin) {
    $.ajax({
        url: "/beijing/api/finance_all_city/",
        data: {province_id: pvid},
        success: function (data) {
            randerCity(data.result, isPopWin)
        }
    })
}
//通过市获取区 数据
function getAreaByCt(ctid, isPopWin) {
    $.ajax({
        url: "/beijing/api/finance_all_county/",
        data: {city_id: ctid},
        success: function (data) {
            randerArea(data.result, isPopWin)
        }
    })
}
//渲染城市、 区 数据
function randerCity(obj, isPopWin) {
    var len = obj.length,
        li_html = "";
    for (var i = 0; i < len; i++) {
        li_html += '<li class="u-box-areas-cc" data-area="li-area-ct" data-cityid="' + obj[i].city_id + '"><a href="javascript:void(0);" class="s-sm">' + obj[i].city_name + '</a></li>';
    }
    if (isPopWin) {
        $("#dealer-address-ct").next().html(li_html)
    } else {
        $(".u-box-areas-c").html(li_html);
    }
}
function randerArea(obj, isPopWin) {
    var len = obj.length,
        li_html = "";
    for (var i = 0; i < len; i++) {
        li_html += '<li class="u-box-areas-cc" data-area="li-area-ar" data-areaid="' + obj[i].county_id + '"><a href="javascript:void(0);" class="s-sm">' + obj[i].county_name + '</a></li>';
    }
    if (isPopWin) {
        $("#dealer-address-ar").next().html(li_html)
    } else {
        $(".u-box-areas-d").html(li_html);
    }
}
//清除城市、地区数据
function cleanCtAr(ctorar, isPopWin) {
    if (ctorar === "li-area-pv") {
        if (isPopWin) {
            $("#dealer-address-ct").attr({"data-ctid": ""}).find("span").text("");
            $("#dealer-address-ar").attr({"data-arid": ""}).find("span").text("");
        } else {
            $("#address-ct-div").attr({"data-ctid": ""}).find("span").text("");
            $("#address-ar-div").attr({"data-arid": ""}).find("span").text("");
        }
    } else if (ctorar === "li-area-ct") {
        if (isPopWin) {
            $("#dealer-address-ar").attr({"data-arid": ""}).find("span").text("");
        } else {
            $("#address-ar-div").attr({"data-arid": ""}).find("span").text("");
        }
    }

}


//渲染经销商弹窗数据
function randerDealer(oDealer) {
    var li_html = "", len = oDealer.length;
    for (var i = 0; i < len; i++) {
        li_html += '<li class="m-popup-zyd area-' + oDealer[i].county_id + '" xg-zyd-index="' + oDealer[i].dlr_code + '" data-dlcode="' + oDealer[i].dlr_code + '" data-dealerid="' + oDealer[i].id + '">' +
            '<dl><dt class="f-ib st j-st z-active"><i class="u-icon u-icon-xz"></i></dt>' +
            '<dd class="f-ib f-cb ">' +
            '<dl class="f-fl zyd">' +
            '<dt class="s-main t">' + oDealer[i].dlr_short_name + '</dt>' +
            '<dd class="s-sm addr">地址:' + oDealer[i].cont_address + '</dd>' +
            '</dl>' +
            '<div class="f-fr loc">' +
            '<span  class="s-sm d">' + oDealer[i].county_name + '</span>' +
            '</div></dd></dl></li>'
    }
    $("#pop-dealer-ul").html(li_html);
}


//关闭下拉列表
function closeList($el) {
    $el.find('.j-down').css({
        "border-bottom-color": '#e2e2e2'
    })
    $el.find('.j-down').children('.u-iconright').removeClass('u-icon-arrowsup').addClass('u-icon-arrowdown');
    $el.find('.j-areas').hide();
    $el.find('.j-down').text()
    return false;
}