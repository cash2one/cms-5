/**
 * Created by zhoumusheng on 2016/1/18.
 */
$(function(){
    //$.Alert("<p>点击事件内容</p>");
    //document 点击事件
    $(document).click(function(ev){
        $(".exchange-model-wrap").removeClass("cur");
    })

    //发送到手机
    $("#send-to-phone").click(function(){
        var sendToPhone=new sendObj(this,{})
        sendToPhone.init();
    })

    //在售车系切换
    $(".car-type-tap dd").click(function(){changeCarModels(this)});

    //下拉 切换车型
    $(".series-name").click(function(ev){
        modelPop(this);
        return false;
    })
// 百度地图  经销商地图
    initMap();
})

//车系切换
function changeCarModels(el){
    var _index=$(el).index(),$contentList=$(".car-type-list");
    $(el).siblings().removeClass("cur");
    $(el).addClass("cur");
    $contentList.hide();
    $contentList.eq(_index).show();
}
//车型弹窗
function modelPop(el){
    if($(el).next().find(".u-plug-model").length){
        $(el).parent().addClass("cur");
        $(el).next().show();
        $(el).next().find(".u-plug-model").show();
        return false;
    }
    var $exchange=$(el).parent(),$nameLb=$(el).find("span"),$ulWrap=$exchange.find(".model-wrap");
    var plug_url=$("#sale-model").attr("data-modeurl"),
        dealer_id=$("#sale-model").attr("data-dealer"),
        plug_series_id=$(el).attr("data-seriesid");
    $exchange.addClass("cur");
    var modelPlg = new modelPlug({
        el_wrap: $ulWrap,
        nameLable: $(el).find(".name-sp"),
        dealer_id:dealer_id,
        isClear:true,
        showData: true,
        callback:modelClick
    })
    modelPlg.main(plug_url,plug_series_id);
    //$exchange.find(".u-plug-model").css({position:"inherit"});
}
function modelClick(modelName,modelId,el){
    var dealer_price=$(el).attr("data-dealerprice"),
        model_price=$(el).find("span").text(),
        $exchangeWrap=$(el).parents(".exchange-model-wrap"),
        $btn_a_list=$(el).parents(".series-text").find(".car-btn a"),
        dealer_id=$("#sale-model").attr("data-dealer"),
        series_id=$exchangeWrap.find(".series-name").attr("data-seriesid");
    $exchangeWrap.removeClass("cur");
    $exchangeWrap.next().find("label").text(model_price);
    $exchangeWrap.next().find("b").text(dealer_price);
    $btn_a_list.eq(0).attr("href","/info/apply?series_id="+series_id+"&model_id="+modelId+"&dealer_id="+dealer_id+"&server=7&lead_key=NV-Chebabanew-pc-V2-Ch-Le-PoC-Msg1-02-0000")
    $btn_a_list.eq(1).attr("href","/info/apply?series_id="+series_id+"&model_id="+modelId+"&dealer_id="+dealer_id+"&server=2&lead_key=NV-Chebabanew-pc-V2-Ch-Le-PoC-Msg3-02-0000")
}

//地图
function initMap(){
    var latitude=$("#dshop-map").attr("data-latitude"),longitude=$("#dshop-map").attr("data-longitude");
    var dl_name = $(".dsp-detail h2").attr("data-content"),dl_address = $("#dsp-address").text(),
        phone= $("#dsp-phone").text();
    // 百度地图API功能
    var map = new BMap.Map('dshop-map');
    var poi = new BMap.Point(longitude,latitude);
    map.centerAndZoom(poi, 16);
    map.enableScrollWheelZoom();

    var content = '<div style="margin:0;line-height:20px;padding:2px;">' +
        "<p>"+dl_address +"</p>"+
        "<p>"+phone +"</p>"+
        '</div>';

    //创建检索信息窗口对象
    var searchInfoWindow = null;
    searchInfoWindow = new BMapLib.SearchInfoWindow(map, content, {
        title  : dl_name,      //标题
        width  : 290,             //宽度
        height : 80,              //高度
        panel  : "panel",         //检索结果面板
        enableAutoPan : true,     //自动平移
        searchTypes   :[
            BMAPLIB_TAB_TO_HERE,  //到这里去
            BMAPLIB_TAB_FROM_HERE //从这里出发
        ]
    });
    var marker = new BMap.Marker(poi); //创建marker对象
    marker.enableDragging(); //marker可拖拽
    marker.addEventListener("click", function(e){
        searchInfoWindow.open(marker);
    })
    map.addOverlay(marker); //在地图中添加marker
    map.addControl(new BMap.NavigationControl());
    map.addControl(new BMap.ScaleControl());
    map.addControl(new BMap.OverviewMapControl());
    map.addControl(new BMap.MapTypeControl());
    marker.setAnimation(BMAP_ANIMATION_BOUNCE);
    searchInfoWindow.open(marker);
}

//
