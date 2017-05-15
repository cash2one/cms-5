/**
 * Created by zhoumusheng on 2016/2/19.
 */

    (function(){
        //菜单JS
        $(".carmod-c-1").on("mouseleave",function(){$(this).css("background-color","")})
        $(".sub").on("mouseleave",function(){
            $(".carmod-c-1").css("background-color","#fff")
        })
        //分享
        var p = {
            url:location.href,
            showcount:'0',/*是否显示分享总数,显示：'1'，不显示：'0' */
            desc:'',/*默认分享理由(可选)*/
            summary:'',/*分享摘要(可选)*/
            title:'车巴巴商城-'+document.title,/*分享标题(可选)*/
            site:'',/*分享来源 如：腾讯网(可选)*/
            pics:'', /*分享图片的路径(可选)*/
            style:'201',
            width:39,
            height:39
        };
        var s = [];
        for(var i in p){
            s.push(i + '=' + encodeURIComponent(p[i]||''));
        }
        $("#qq-zone").html(['<a version="1.0" class="qzOpenerDiv" style="background:none;" href="http://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?',s.join('&'),'" target="_blank">分享</a>'].join(''));

        //返回顶部
        $("#back-top").click(function(){
            $("body").animate({"scrollTop":"0"},500);
        })

    })();
