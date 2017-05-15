/**
 * Created by zhoumusheng on 2016/1/30.
 */

var modelPlug=function(options){
    this.defaults = {
        el_wrap: "",//容器表单 带类符 . 或 ID符 #
        hoverColor: "#F9F9F9",
        width:203,
        maxheight:250,
        dealer_id:"",
        background_color:"#fff",
        callback:"",
        isClear:false,//添加数据前是否清空容器内容，默认：否
        nameLable:"", //文字表单 带类符 . 或 ID符 #
        showData:false,//是否默认显示
        showPrice:false, //是否显示指导价
        fucAfter:function(){}
    };
    this.options = $.extend({},this.defaults,options);
    this.$EL=$(this.options.el_wrap);
}

modelPlug.prototype = {
    //入口方法
    main:function(url,series_id){
        this.getModel(url,series_id);
    },
    initUl: function (obj) {
        var _th=this;
        if (this.$EL.find(".u-plug-model").length) {
            this.reflesh(obj);
            return false;
        }
        var $ul = $("<ul class='u-plug-model'></ul>");

        if(_th.options.isClear){
            this.$EL.empty();
        }

        $ul.delegate("li","click",function () {
            if ($(this).hasClass("model_pl")) {
                return false;
            }
            var modelName = $(this).find("label").text(),modelId=$(this).attr("data-modelid");
            _th.select(modelName, modelId);
            if(typeof (_th.options.callback) == "function"){
                _th.options.callback(modelName, modelId,this);
            }
            _th.close();
            return false;
        });

        this.$EL.append($ul);

        this.reflesh(obj);


        if (this.options.showData) {
            this.show();
        }
    },
    //渲染li
    reflesh: function (obj) {
        var sLi = ""
        $.each(obj, function (i, item) {
            var modelList = item.car_type_list;
            sLi += '<li class="model_pl"><b>' + item.value + '</b><span>指导价</span></li>';
            $.each(modelList, function (i, item) {
                //是否有经销商报价
                if(item.offer_price && item.offer_price.price){
                    sLi += '<li class="model_name" data-dealerprice="'+(item.offer_price.price / 10000).toFixed(2)+'" data-modelid="' + item.id + '"><label>' + item.name + '</label><span>' + (item.guide_price / 10000).toFixed(2) + '</span></li>'
                }else{
                    sLi += '<li class="model_name" data-modelid="' + item.id + '"><label>' + item.name + '</label><span>' + (item.guide_price / 10000).toFixed(2) + '</span></li>'
                }
            })
        })
        this.$EL.find(".u-plug-model").html(sLi);
        this.options.fucAfter(this.$EL);
    },
    //获取URL
    getModel: function (url,series_id) {
        var _this=this;
        var param={
            car_series_id: series_id,
            property_key: 'pailiang'
        }
        if(_this.options.dealer_id){
            param.dealer_id= _this.options.dealer_id
        }
        return $.ajax({
            url: url,
            data: param,
            success: function (data) {
                if (data.status === "success") {
                    _this.initUl(data.result);
                }
            }
        });
    },
    //默认点击事件
    select: function (modelName,modelId) {
        if ($(this.options.nameLable).attr("type")) {
            $(this.options.nameLable).val(modelName).attr("data-model", modelId);
        } else {
            $(this.options.nameLable).text(modelName).attr("data-model", modelId);
        }
    },
    close: function () {
        this.$EL.removeClass("cur").find("ul").hide();
        return false;
    },
    show: function () {
        this.$EL.find(".u-plug-model").show();
        return false;
    }
}
