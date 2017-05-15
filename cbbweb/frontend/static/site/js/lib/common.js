
var CBB_CONS = {};
CBB_CONS.COOKIE = {
    SESSION: "cbb_sid",
    CITY: {
        ID: "mycityid",
        NAME: "mycityname"
    }
};
CBB_CONS.BACKEND = {
    URL: 'http://172.26.153.45/cbbweb',
    LANYOU: 'http://172.26.153.45/lanyou',
    PIC: "http://121.41.173.5/taeservice"
};


var CBB = {};
CBB.Cookie = {
    set: function (c_name, value, expireMin) {
        var exdate = new Date()
        //exdate.setDate(exdate.getDate() + expiredays);
        exdate.setTime(exdate.getTime() + expireMin*1000*60);//过期时间 分钟
        document.cookie = c_name + "=" + escape(value) +
            ((expireMin == null) ? "" : ";expires=" + exdate.toGMTString())

    },
    get: function (c_name) {
        if (document.cookie.length > 0) {
            var c_start = document.cookie.indexOf(c_name + "=")
            if (c_start != -1) {
                c_start = c_start + c_name.length + 1
                var c_end = document.cookie.indexOf(";", c_start)
                if (c_end == -1)
                    c_end = document.cookie.length
                return unescape(document.cookie.substring(c_start, c_end))
            }
        }
        return ""
    },
    del: function (c_name) {
        CBB.Cookie.set(c_name, '', -1);
    }
}

CBB.$ = {
    getCityId: function () {
        return CBB.Cookie.get(CBB_CONS.COOKIE.CITY.ID);
    },
    getCityName: function () {
        return CBB.Cookie.get(CBB_CONS.COOKIE.CITY.NAME);
    },
    superstar: function (word, start, end) {
        var repeat = function (str, cnt) {
            var rtnStr = "";
            while (cnt > 0) {
                rtnStr += str;
                cnt--;
            }
            return rtnStr;
        }
        if (word) {
            var wlen = word.length;
            if (start > end) return repeat("*", wlen);
            if (wlen < start) return repeat("*", wlen);
            if (wlen < end) return repeat("*", wlen);

            return word.substring(0, start) + repeat("*", end - start) + word.substring(end);
        } else {
            return "*";
        }
    }
}

CBB.getUrlParam = function (name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", ["i"]); //构造一个含有目标参数的正则表达式对象
    var r = window.location.search.substr(1).match(reg);  //匹配目标参数
    if (r != null) return unescape(r[2]);
    return null; //返回参数值
};

CBB.getStartTimeYear = function (num) {
    return (new Date(parseInt(num) * 1000)).getFullYear();
};
CBB.getStartTimeMon = function (num) {
    return (new Date(parseInt(num) * 1000)).getMonth() + 1;
};
CBB.getStartTimeDay = function (num) {
    return (new Date(parseInt(num) * 1000)).getDate();
};
CBB.getEndTimeYear = function (num) {
    return (new Date(parseInt(num) * 1000)).getFullYear();
};
CBB.getEndTimeMon = function (num) {
    return (new Date(parseInt(num) * 1000)).getMonth() + 1;
};
CBB.getEndTimeDay = function (num) {
    return (new Date(parseInt(num) * 1000)).getDate();
};
CBB.getApiTime = function (num) {
    var result = [];
    result['Y'] = (new Date(parseInt(num) * 1000)).getFullYear();
    result['M'] = (new Date(parseInt(num) * 1000)).getMonth() + 1;
    result['D'] = (new Date(parseInt(num) * 1000)).getDate();
    return result;
};
CBB.loadJsCss = function (filename, filetype) {
    if (filetype == "js") {
        var fileref = document.createElement('script')//创建标签
        fileref.setAttribute("type", "text/javascript")//定义属性type的值为text/javascript
        fileref.setAttribute("src", filename)//文件的地址
    }
    else if (filetype == "css") {
        var fileref = document.createElement("link")
        fileref.setAttribute("rel", "stylesheet")
        fileref.setAttribute("type", "text/css")
        fileref.setAttribute("href", filename)
    }
    if (typeof fileref != "undefined") {
        document.getElementsByTagName("head")[0].appendChild(fileref)
    }
}

//日期时间原型增加格式化方法
Date.prototype.Format = function (formatStr) {
    var str = formatStr;
    var Week = ['日', '一', '二', '三', '四', '五', '六'];

    str = str.replace(/yyyy|YYYY/, this.getFullYear());
    str = str.replace(/yy|YY/, (this.getYear() % 100) > 9 ? (this.getYear() % 100).toString() : '0' + (this.getYear() % 100));
    var month = this.getMonth() + 1;
    str = str.replace(/MM/, month > 9 ? month.toString() : '0' + month);
    str = str.replace(/M/g, month);

    str = str.replace(/w|W/g, Week[this.getDay()]);

    str = str.replace(/dd|DD/, this.getDate() > 9 ? this.getDate().toString() : '0' + this.getDate());
    str = str.replace(/d|D/g, this.getDate());

    str = str.replace(/hh|HH/, this.getHours() > 9 ? this.getHours().toString() : '0' + this.getHours());
    str = str.replace(/h|H/g, this.getHours());
    str = str.replace(/mm/, this.getMinutes() > 9 ? this.getMinutes().toString() : '0' + this.getMinutes());
    str = str.replace(/m/g, this.getMinutes());

    str = str.replace(/ss|SS/, this.getSeconds() > 9 ? this.getSeconds().toString() : '0' + this.getSeconds());
    str = str.replace(/s|S/g, this.getSeconds());
    return str;
}
//CBB.Time.left('2015-11-17 15:10:00' )
CBB.Time = {
    left: function (endTime) {
        var now = new Date().Format("yyyy-MM-dd  hh:mm:ss");
        now = new Date(now.replace(/-/g, '/')).getTime();
        endTime = new Date(endTime.replace(/-/g, '/')).getTime();

        var leftTime = endTime - now;
        if (leftTime <= 0) {
            //时间到了
            return false;
        }
        var leftsecond = parseInt(leftTime / 1000);

        if ($.isNumeric(leftsecond)) {
            var result = [];
            result['day'] = Math.floor(leftsecond / (60 * 60 * 24));

            result['hour'] = Math.floor((leftsecond - result['day'] * 24 * 60 * 60) / 3600);
            result['minute'] = Math.floor((leftsecond - result['day'] * 24 * 60 * 60 - result['hour'] * 3600) / 60);
            result['second'] = Math.floor(leftsecond - result['day'] * 24 * 60 * 60 - result['hour'] * 3600 - result['minute'] * 60);
            //console.log('123');console.log(result);
            return result;
        }

    }
};

CBB.phoneFormat = function(num){
    var reg = /^(\d{3})(\d{4})(\d{4})$/;
    var matches = reg.exec(num);
    var newNum;
    return newNum = matches[1] + '-' + matches[2] + '-' + matches[3];
}

//活动颜色
CBB.activityColor = function () {
    var _colorArr = [];
    for (var i = 0; i < 6; i++) {
        _colorArr.push('blue')
    }
    for (var i = 0; i < 13; i++) {
        _colorArr.push('deepred')
    }
    for (var i = 0; i < 4; i++) {
        _colorArr.push('green')
    }
    for (var i = 0; i < 6; i++) {
        _colorArr.push('orange')
    }
    for (var i = 0; i < 9; i++) {
        _colorArr.push('deepred')
    }
    _colorArr.push('greyBlue')
    return _colorArr;
};
$(function () {
    //header
    var selectTrg = $(".city_pinyin a");
    var selectPlace = $(".citi_li li span");
    var selectCity = {

        getHeight: function (container) {
            return Math.floor(container.offset().top);
        },
        init: function (container, trg) {

        },
        scrollAni: function (container, trg) {
            container.animate({
                scrollTop: selectCity.getHeight(trg)
            }, 500);
        }

    };

    //alert($("#B").offset().top)

    selectTrg.each(function (i) {
        selectTrg.eq(i).on("click", function () {
            var oHeight = $("#B").offset().top
            $(".citi_li").animate({
                scrollTop: oHeight
            }, 500);
            //selectCity.scrollAni($(".citi_li"),selectPlace.eq(i));

        });
    });

    selectPlace.each(function (i) {
        selectPlace.eq(i).on("click", function () {
            alert($(this).attr('id'))
        });
    });

    $(".city_form a,#remenchengshi a").on("click", function () {
        console.log($(this).text());
        console.log($(this).data("cityid"));
    })

    //五星评分
    if ($(".u-star").length) {
        $.each($(".u-star"), function (i, item) {
            var score = $(item).attr("data-star"), percent = (score * 100 / 500).toFixed(2);
            var width = (82 * percent).toFixed(2);
            $(item).append('<span><i style="width:' + width + 'px"></i></span><label>' + score + '</label>')
        })
    }


    //右侧悬浮菜单
    $('.j-l1').on('mouseover', function () {
        //其他改变字，并把显示的二级三级内容隐藏
        $(this).find('.j-i1').hide();
        $(this).find('.j-u1').show();
        $(this).find('.j-l2').show();
        $(this).find('.u-bri').show();
    }).on('mouseout', function () {
        $(this).find('.j-i1').show();
        $(this).find('.j-u1').hide();
        $(this).find('.j-l2').hide();
        $(this).find('.u-bri').hide();
    });
    $('.j-ls2').on('mouseover', function () {
        //其他改变字，并把显示的二级三级内容隐藏
        $(this).find('.j-l3').show();
        $(this).find('.u-bri').show();
    }).on('mouseout', function () {
        $(this).find('.j-l3').hide();
        $(this).find('.u-bri').hide();
    });

    //setting smartCode
    var sc = CBB.getUrlParam("SMARTCODE");
    if (sc && sc.length > 0) {
        CBB.Cookie.set("SMARTCODE", sc, 30);
    }

    // ajax预处理
    $.ajaxPrefilter(function (options) {
        var _ftuc = CBB.getUrlParam('__ftuc');
        var mark = '';

        if (_ftuc) {
            options.url.indexOf('?') >= 0 ? mark = '&' : mark = '?';
            options.url += mark + '__ftuc=1';
        }

        //add smartCode
        if(options.url.indexOf("/api/clue_save_api/") > -1){

            if( options.type.toUpperCase() == 'get'.toUpperCase() ){
                var _url = options.url;
                if( _url.indexOf("?") > -1){
                    options.url += "&smartCode="+CBB.Cookie.get("SMARTCODE");
                }else{
                    options.url += "?smartCode="+CBB.Cookie.get("SMARTCODE");
                }
            }else if( options.type.toUpperCase() == 'post'.toUpperCase() ){
                if(options.data){
                    options.data += "&smartCode="+CBB.Cookie.get("SMARTCODE");
                }else{
                    options.data = "smartCode="+CBB.Cookie.get("SMARTCODE");
                }
            }


        }

    });

    //页头城市选择
    $.citySelect({
        target: $('#citiesTemplate'),
        api_allCitys: '/api/city_data/',
        api_hotCitys: '/api/hot_city/',
        selected: function (data) {
            var tmp = window.location.pathname.split("/");
            tmp[1] = data.city_alias;
            var url = window.location.host + tmp.join("/");
            location.href = "http://" + url;
        }
    });

});

//下拉框插件 
(function ($) {
    //默认参数
    var defaluts = {
        type: 'form',                   //表单验证特殊处理
        openClass: 'open'               //显示隐藏class
    };

    $.extend({
        "cbbSelect": function (options) {
            var opts = $.extend({}, defaluts, options);

            $('.J-select-link').delegate('.m-btn-group', 'mouseover', function () {
                var isOpen = $(this).hasClass(opts.openClass);
                isOpen ? '' : $(this).addClass(opts.openClass);
            }).delegate('.m-btn-group', 'mouseout', function () {
                var isOpen = $(this).hasClass(opts.openClass);
                isOpen ? $(this).removeClass(opts.openClass) : '';
            }).delegate('.m-btn-group li a', 'click', function () {
                var txt = $(this).text();
                var parentsBtn = $(this).closest('.m-btn-group');
                var dataId = $(this).attr('data-id');
                var hasInput = parentsBtn.find('input[type="text"]').prop('type');
                var obj; 

                if(hasInput){
                    obj = parentsBtn.find('input[type="text"]');
                    obj.attr('value', txt);
                }else{
                    obj = parentsBtn.find('.J-select');
                    obj.text(txt);
                } 

                obj.attr('data-id', dataId);

                //隐藏下拉
                parentsBtn.removeClass(opts.openClass);

                if (opts.type == 'form') {
                    //针对表单验证-城市联动
                    if (!parentsBtn.attr('data-from-select')) {
                        $(this).closest('.form-list').removeClass('error').addClass('valid').find('.txt').text('');
                    }
                }
            });

        }
    });
})(window.jQuery);




