var CBB = {
  //图片懒加载
  lazyLoad : function (object) {
     var arr = object,
         len = arr.length;
     if (len <= 0) {
          return false;
     }
     for(var i in arr){
         $(arr[i].id).find("img").each(function () {
             var ost_top = $(this).offset().top,
                 _top = arr[i].top || 10,
                 defHeight = $(window).height() + $(window).scrollTop() + _top,
                 dataLazy = $(this).attr("data-lazy");
             if ( defHeight >= ost_top ) {
                 if (dataLazy) {
                     $(this).attr("src", dataLazy).removeAttr("data-lazy").show(300).on('error',function () {
                         $(this).attr('src','');
                     });
                 }
             }   
         });
     }
  },
  //页面滚动到什么高度
  animateTo : function(p){
      $('body,html').animate({ 'scrollTop': p + 'px' }, 500);
  },
  //加载效果
  loading:function(obj,container){
      $(container).empty().append('<div id="'+obj+'" class="u-loading"></div>');
  },
  //获取url参数   radian
  getUrlParam:function(name){
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", ["i"]); //构造一个含有目标参数的正则表达式对象
    var r = window.location.search.substr(1).match(reg); //匹配目标参数
    if (r != null) return unescape(r[2]);
    return null; //返回参数值
  },
  //角度
  toDegrees:function(angle) {
    return angle * (180 / Math.PI);
  },
  //弧度
  toRadians:function(angle) {
    return angle * (Math.PI / 180);
  },
  //获取距离
  getDistance:function(lat1, lng1, lat2, lng2){
    var r = 6378.137;
    var lat1 = this.toRadians(lat1);
    var lng1 = this.toRadians(lng1);
    var lat2 = this.toRadians(lat2);
    var lng2 = this.toRadians(lng2);
    var d1 = Math.abs(lat1 - lat2);
    var d2 = Math.abs(lng1 - lng2);
    var p = (Math.pow(Math.sin(d1 / 2), 2) + Math.cos(lat1) * Math.cos(lat2) * Math.pow(Math.sin(d2 / 2), 2));
    var dis = r * 2 * Math.asin(Math.sqrt(p));
    return dis;    
  }


};

CBB.Cookie = {
  set: function(c_name, value, expireMin) {
    var exdate = new Date()
      //exdate.setDate(exdate.getDate() + expiredays);
    exdate.setTime(exdate.getTime() + expireMin * 1000 * 60); //过期时间 分钟
    document.cookie = c_name + "=" + escape(value) +";expires=" + exdate.toGMTString();

  },
  get: function(c_name) {
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
  del: function(c_name) {
    CBB.Cookie.set(c_name, '', -1);
  }
}

$(function(){

  // 判断是否pc设备，若是pc，需要更改touch事件为鼠标事件，否则默认触摸事件
  var touchEvents = {
      touchstart: "touchstart",
      touchmove: "touchmove",
      touchend: "touchend",

      initTouchEvents: function () {
          if (!this.isMobileUserAgent()) {
              this.touchstart = "mousedown";
              this.touchmove = "mousemove";
              this.touchend = "mouseup";
          }
      },
      isMobileUserAgent:function(){
          return (/iphone|ipod|android.*mobile|windows.*phone|blackberry.*mobile/i.test(window.navigator.userAgent.toLowerCase()));
      }
  };  
  touchEvents.initTouchEvents();           
  window.touchEvents = touchEvents;

  //每次加载页面的时候滚动条滚动1px触发lazyLoad懒加载图片事件
  CBB.animateTo($(window).scrollTop() + 1);

  //click 300秒延迟修复
  FastClick.attach(document.body);

});