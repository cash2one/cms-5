/**
 * Created by zhoumusheng on 2016/1/18.
 */
(function ($) {
    $.fn.extend({
        //插件名称 - seriesPlug
        seriesPlug: function (options) {

            //参数和默认值
            var defaults = {
                el_wrap: "",//容器表单 jq对象
                hoverColor: "#F9F9F9",
                width:203,
                maxheight:250,
                background_color:"#fff",
                url:"",
                callback:"",
                nameLable:"" //文字表单 jq对象
            };

            var options = $.extend(defaults, options);
            var $EL=options.el_wrap;

            function getSeries(url,callback){

                return $.ajax({
                    url:url,
                    data:"",
                    success:function(data){
                        if(data.status==="success"){
                            callback(data.result);
                            return false;
                        }
                    }
                });
            }

            return this.each(function () {
                var o = options;
                var $th = $(this);
                getSeries(o.url,function(obj){initUl(o.el_wrap,obj)})
                function initUl(el,obj){
                    var $ul=$("<ul class='u-plug-series'></ul>"),sLi="";
                    $.each(obj,function(i,item){
                        if(!item.series_list.length){
                            return;
                        }
                        var seriesList=item.series_list;
                        sLi+='<li class="series_brand">'+item.brand.name+'</li>'
                        $.each(seriesList,function(i,item){
                            sLi+='<li class="series_name" data-seriesid="'+item.id+'">'+item.name+'</li>'
                        })
                    })
                    $ul.append($(sLi));
                    $ul.find("li").click(function(){
                        if($(this).hasClass("series_brand")){
                            return false;
                        }
                        var seriesName=$(this).text(),seriesid=$(this).attr("data-seriesid");
                        select(seriesName,seriesid);
                        o.callback? o.callback(seriesName,seriesid):"";
                        close();
                        return false;
                    });
                    $EL.append($ul);
                }
                function select(seriesName,seriesid){
                    if(o.nameLable.attr("type")){
                        o.nameLable.val(seriesName).attr("data-seriesid",seriesid);
                    }else{
                        o.nameLable.text(seriesName).attr("data-seriesid",seriesid);
                    }
                }
                function close(){
                    $EL.removeClass("cur").find("ul").hide();
                    return false;
                }

            });
        }
    });
})(jQuery);
