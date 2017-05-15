/**
 * Created by heshichun on 2016/1/27.
 */

//隐藏，显示参数
$("caption").on("click",function(){
    $(this).children("span").toggleClass("ico-arg-t-u");
    $(this).children("span").toggleClass("ico-arg-t-d");
    $(this).nextAll().fadeToggle("fast");
});

//动态给所有TD,select增加标识
var oTr = $(".list tr");
var carDataTable = $(".list");

function getEachTD(callback){

    $.each(oTr,function(i){

        var oTd = $(oTr[i]).children("td");

        $.each(oTd,function(j){
            callback($(oTd[j]),j);
        });

    });
}

getEachTD(function(td,j){
    td.data("index",j);
});

function eachSelect(){
    $(".J_carMod").each(function(i){
        $(this).data("index",i);
    });
}

eachSelect();

//删除车型与参数
$(".btn-arg-close").on("click",function(){

    $(this).parents("td").remove();

    var index = $(this).data("index");

    getEachTD(function(td,j){

        if (td.data("index") == index){

            td.remove();
            eachSelect();
        }
    });

});


//只显示不同点
var difBtn = $("#dis_no");
difBtn.attr("checked",false);
var switchPoint = false;

function compareTxt(a){
    var isSame = true;
    for(var i = 0; i < a.length; i++){
        var j = i + 1;
        var k = (j == a.length) ? (a.length -1) : j;

        if (a[i] !== a[k]){
            return false;
        }
    }
    return isSame;
}


difBtn.on("click",function(){
    switchPoint = !switchPoint;
    if (switchPoint){

        $.each(oTr,function(i){
            var a = [];
            var oTd = $(oTr[i]).children("td");

            $.each(oTd,function(j){

                var txt = $.trim($(oTd[j]).text());

                a.push(txt);

                if (!compareTxt(a)){

                    oTd.addClass("dif");
                }

            });
        });

    }else{

        getEachTD(function(td,j){

            td.removeClass("dif");
        });

    }
});


//更改下拉车型
$(".J_carMod").on("change",function(){

    if($(this).val()){

        //获取车型ID
        var carTypeId = $(this).val();

        var index = $(this).data("index");
        //更改车型信息
        getCarModInfo(carTypeId,$(this));
        //更改车型参数
        getCarModPro(carTypeId,index);
        //更改试驾按钮参数
        getUrl($(this),carTypeId)

    }

});

function getCarModInfo(typeId,select){

    var carProperty = carTypeList.car_type_list[typeId];

    var price = parseFloat(carProperty.guide_price / 10000).toFixed(2);
    var discount = carProperty.offer_price.discount;
    //dom处理
    var nodeDl = select.parents(".mod");
    nodeDl.find("dl dd img").attr("src",carProperty.imgs[0].CDNPATH);
    nodeDl.find("dl dt").text(carProperty.name);
    nodeDl.find("dl dd:eq(1)").text("指导价：" + price + "万");
    nodeDl.find("dl dd span").text(discount + "元");
}

function getCarModPro(typeId,index){
    var data = carTypeList.car_type_list[typeId].property;
    $.each(data,function(i){

        getCarModTitle(data[i],index);

    });
}

function getCarModTitle(o,index){

    $.each(carDataTable,function(i){
        //caption text
        if ($(carDataTable[i]).find("caption").text() == o.group_name){

            var th = $(carDataTable[i]).find("th");

            var list = o.property_list;

            for (var j = 0,k = 0;j < th.length,k < list.length;j++,k++){

                if ($(th[j]).text() == o.property_list[k].name){

                    getCarModVal($(th[j]).siblings("td").eq(index),o.property_list[k].property_value);
                    //$(th[j]).siblings("td").eq(index).css("background","red");
                    //console.log(index)
                }
            }


        }

    });
}

function getUrl(select,index){

    var seriesId = carTypeList.series.id,
        modelId = carTypeList.car_type_list[index].id,
        server = 2,
        leadKey = "NV-Chebabanew-Pc-V1-Ch-Le-PoC-Msg1-07-0000",
        applyUrl = infoApplyUrl + "series_id=" + seriesId + "&model_id=" + modelId + "&server=" + server + "&lead_key=" + leadKey,

        btnTry = select.next("a");

    btnTry.attr("href",applyUrl);


}

function getCarModVal(td,val){
    var tdTxt = (val == null || val == "" || val == "无") ? "-" : val;
    td.text(val);
}







