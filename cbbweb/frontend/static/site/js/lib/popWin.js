/**
 * Created by zhoumusheng on 2016/1/25.
 */
(function ($) {
    var popObj = function(ele,options){
        this.element = ele;
        this.$mask = $('<div class="m-mask"></div>');
        this.$popWin = $('<div class="u-popWin"><span class="close"><i class="cbb cbb-close"></i></span></div>');
        this.$titWrap = $('<div class="tit"><i></i><span></span></div>');
        this.$conWrap=$('<div class="content"></div>');
        //参数和默认值
        this.defaults = {
            width:600,
            height:150,
            padding:10,
            cssName:"",
            strCon:"",
            title:"dddd",
            content:"ddddddsssssss",
            ft:'', //底部
            btn:"",//类名
            isBlank:false,
            f_btn_click:function(){}
        };  
        this.options = $.extend({},this.defaults,options);
    }
    popObj.prototype = {
        rander:function(){
            var _th=this;
            this.$popWin.css({
                width:this.options.width+"px",
                "min-height":this.options.height+"px",
                "margin-top":"-"+this.options.height/2+"px",
                "margin-left":"-"+this.options.width/2+"px"
            })
            if(this.options.cssName){
                this.$popWin.addClass(this.options.cssName);
            }
            this.$titWrap.find("span").text(this.options.title);
            _th.setContent();
            if(!this.options.isBlank){
                this.$popWin.append(this.$titWrap);
            }else{
                this.$popWin.find(".close").remove();
            }
            this.$popWin.append(this.$conWrap);

            if(this.options.ft){
                this.$popWin.append(this.options.ft);
            }

            $("body").append(this.$mask);
            $("body").append(this.$popWin);

            this.$popWin.find(".close,.J-close").click(function(){
                _th.close();
            })
            this.$conWrap.find("."+this.btn).click(function(){
                this.options.f_btn_click();
            })
            if(this.$sureBtn){
                this.$sureBtn.click(function(){
                    _th.$popWin.find(".close").trigger("click");
                })
            }
            return this;
        },
        close: function () {
            console.log(this.element);
            this.$conWrap.remove();
            this.$mask.remove();
            this.$popWin.remove();
        },
        setContent:function(){
            this.$conWrap.html("").html(this.options.content);
        }
    }
    //错误毕弹窗  继承Alert
    var errorWin=function(ele,options){
        this.defaults = {
            width:500,
            height:180,
            padding:10,
            cssName:"u-pop-error",
            strCon:"",
            title:"www.chebaba.com上的网页信息：",
            content:"dsafdsafdsfasd",
            btn:"",//类名
            f_btn_click:function(){}
        };
        this.$conWrap=$('<div class="content"><p></p></div>');
        this.$sureBtn=$('<a class="u-btn-deepred" href="javascript:;">确定</a>')
        this.options = $.extend({},this.defaults,options);
    }
    errorWin.prototype=new popObj();
    errorWin.prototype.setContent=function(){
        this.$conWrap.find("p").html(this.options.content);
        this.$conWrap.append(this.$sureBtn);
    }
    //留资等待窗
    var lodingWin=function(ele,options){
        this.defaults={
            width:120,
            height:120,
            padding:20,
            cssName:"u-wait-pop",
            isBlank:true
        }

        this.$conWrap=$('<div class="content"><img src="/static/site/images/lib/wait.gif"></div>');
        this.options = $.extend({},this.defaults,options);
    }
    lodingWin.prototype=new popObj();
    lodingWin.prototype.setContent=function(){
        this.$titWrap.remove();
        this.$conWrap.find("p").html(this.options.content);
        this.$conWrap.append(this.$sureBtn);
    }

//实例化插件
    $.Alert = function(options){
        var popWin = new popObj(this,options);
        popWin.rander();
        return this;
    };
    $.errorAlert=function(options){
        if(!errWin){
            var errWin=new errorWin(this,options);
        }
        errWin.rander();
        return false;
    }
    $.lodingWin=function(options){
        if(!lodWin){
            var lodWin=new lodingWin(this,options);
        }
        lodWin.rander();
        $.lodingWin.fClose=function(){
            $(".m-mask").remove();
            $(".u-wait-pop").remove();
        };
        return false;
    }
})(jQuery);
