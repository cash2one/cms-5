/**
 * Created by zhoumusheng on 2016/1/18.
 */
$(function(){
    //同城/经销商活动
    $("#activity-nav span").click(function(){
        var contentList=$(".tab-find-c ul"),_index=$(this).index();
        $(this).addClass("active").siblings().removeClass("active");
        $(contentList[_index]).show().siblings().hide();
    })
    //活动过期  暂时不使用 : zzb
    /*if($("#is-passed-activity").length){
        isActivityPass();
    }*/
})

//活动过期提醒内容
function activityPassCon(){
    var _htm=""
    _htm+='<p class="activity-passed-p"><span></span>本活动已过期啦！为您推荐轩逸最新活动</p>';
    _htm+='<dl class="activity-passed-c clearfix">' +
        '<a href="#"><dd><img src=""><h2>广州东风南方广大</h2><p>买新车，省半税，送保养</p></dd></a>' +
        '<a href="#"><dd><img src=""><h2>广州东风南方广大</h2><p>买新车，省半税，送保养</p></dd></a>' +
        '</dl>';
    _htm+='<div><a class="activity-more-btn" href="javascript:;">更多活动 >></a> </div>'
    return _htm;
}
//活动过期弹窗
function isActivityPass(){
    var cont=activityPassCon();
    $.Alert({
        title:"活动过期提醒",
        content:cont
    })
}
