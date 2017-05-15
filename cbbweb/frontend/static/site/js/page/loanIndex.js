/**
 * Created by zhoumusheng on 2016/1/18.
 */
$(function(){
    //$.Alert({content:'<div><span>车系接口URL</span></div>'});

    var seriesPlgUrl=getApiUrl("#series-wrap","data-url"),//获取 车系接口URL
        modelPlgUrl=getApiUrl("#model-wrap");//获取 车型接口URL

    //车型车系下拉事件
    $(document).click(function(ev){
        hidePlugUl();
    })
    $("#series-wrap").click(function(){
        $(".u-plug-model").hide();
        return false;
    })
    $("#model-wrap").click(function(){
        $(".u-plug-series").hide();
        return false;
    })
    //
    $("#loan-plan-submit").click(function(){
        var seriesVal=$("#loan-form-series").val();
        if(seriesVal==""){

            console.log(seriesVal);
            $("#series-wrap").addClass("cur").find("ul").show();
            $("#series-wrap").find(".cbb").removeClass("cbb-angle-down").addClass("cbb-angle-up");
            return false;
        }
        $("#loan-form-series").val("");
        $("#loan-form-model").val("");
    })
    //金融车型 右移事件 hover
    $(".u-loan-plan").hover(function(){
        $(this).find(".u-loan-plan-wr").animate({"margin-left":"20px"},130);
    })
    $(".u-loan-plan").on("mouseleave",function(){
        $(this).find(".u-loan-plan-wr").animate({"margin-left":"15px"},130);
    })

    //金融产品车型点击事件
    $(".u-series-wrap a").click(function(){
        var series_id=$(this).attr("data-sriesid"),
            subBtn=$(this).parent().next(),
            plan_id=subBtn.attr("data-planid"),
            base_path=subBtn.attr("data-url"),
            sku=subBtn.attr("data-sku"),
            key=subBtn.attr("data-key"),
            percent=subBtn.attr("data-percent");
        $(this).addClass("cur").siblings().removeClass("cur");
        subBtn.attr({"href":base_path+"?series_id="+series_id+"&loan_plan="+plan_id+"&sku="+sku+"&percent="+percent+"&lead_key="+key});
    })

    //贷款方案 车系 车型 控件
    $("#series-wrap").seriesPlug({
        el_wrap:$("#series-wrap"),
        nameLable:$("#loan-form-series"),
        url:seriesPlgUrl,
        callback:setModelPlg
    });

    //$("#series-wrap").modelPlug({el_wrap:$("#model-wrap"),nameLable:$("#loan-form-model")});
    $("#series-wrap").click(function(){
        $(this).addClass("cur").find("ul").show();
        $(this).find(".cbb").removeClass("cbb-angle-down").addClass("cbb-angle-up");
    })
    $("#model-wrap").click(function(){
        if(!$(this).find("ul li").length){
            return false;
        }
        $(this).addClass("cur").find("ul").show();
        $(this).find(".cbb").removeClass("cbb-angle-down").addClass("cbb-angle-up");
    })

    //隐藏控件下拉
    function hidePlugUl(){
        $("#series-wrap").removeClass("cur").find("ul").hide();
        $("#model-wrap").removeClass("cur").find("ul").hide();
        $("#series-wrap").find(".cbb").addClass("cbb-angle-down").removeClass("cbb-angle-up");
        $("#model-wrap").find(".cbb").addClass("cbb-angle-down").removeClass("cbb-angle-up");
    }

    //获取 车系 车型 接口URL
    function getApiUrl(el,prototy){
        var pro=prototy||"data-url";
        return $(el).attr(pro);
    }

    //初始化车型控件
    function setModelPlg(seriesName,seriesId){
        //表单右边小箭头
        $("#series-wrap i").removeClass("cbb-angle-up").addClass("cbb-angle-down");
        $("#loan-plan-submit").attr("href","/finance_detail/"+seriesId)
        resetModel();
        $("#model-wrap").attr("data-seriesid",seriesId);
        //var tmp=$("#model-wrap").attr("data-seriesid");
        //车型控件
        var modelPlg=new modelPlug({
                el_wrap:"#model-wrap",
                nameLable:"#loan-form-model",
                callback:function(modelName, modelId){
                    //表单右边小箭头
                    $("#model-wrap i").removeClass("cbb-angle-up").addClass("cbb-angle-down");
                    var series_id=$("#loan-form-series").attr("data-seriesid")
                    $("#loan-plan-submit").attr("href","/finance_detail/"+series_id+"/"+modelId)
                }
            }),
            param_url = modelPlgUrl,
            param_series_id= seriesId;
        modelPlg.main(param_url,param_series_id);
    }
    //重置车型选择
    function resetModel(){
        $("#loan-form-model").val("").attr({"data-model":"","placeholder":"选择车型（可不选）"})
        $('#model-wrap').removeClass('f-ol-n');
    }
})
