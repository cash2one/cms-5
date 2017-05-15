/**
 * Created by zhoumusheng on 2016/1/25.
 */
    var sendObj = function(ele,options){
        this.element = ele;
        this.$wrap=$('<div class="send-phone-wrap"></div>');
        this._html = '<div class="f-field clearfix"><span>姓名</span><div class="send-phone-drop">' +
            '<input type="text" name="name" value="" placeholder="请输入姓名">' +
            '<a href="javascript:;" class="active" data-sex=""><i id="man"></i><span>先生</span></a>' +
            '<a href="javascript:;" class="active" data-sex=""><i id="woman"></i><span>女士</span></a>' +
            '</div></div>';
        this._html+='<div class="f-field clearfix"><span>手机号码</span><div class="send-phone-drop">' +
            '<input type="text" name="phone" value="" placeholder="请输11位手机号码">' +
            '</div></div>';
        this.submitBtn=$('<div class="f-field clearfix"><span></span><a class="send-phone-btn" href="javascript:;">提交申请</a></div>')
        this.$wrap.append(this._html).append(this.submitBtn);

        //参数和默认值
        this.defaults = {
            width:600,
            height:150,
            padding:10,
            cssName:"",
            strCon:"",
            title:"发送信息到手机",
            content:"ddddddsssssss",
            btn:"",//类名
            f_btn_click:function(){}
        };
        this.options = $.extend({},this.defaults,options);
    }
    sendObj.prototype={
        init:function(){
            var _th=this;
            $.Alert({
                title:_th.options.title,
                content:_th.$wrap
            })
        }
    }
