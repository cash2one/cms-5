//在售车型
function ajaxSaleData (ops){
    setTimeout(function(){
        saleCar.loading = true;
        $.ajax({
            url: ops.url,
            type: 'GET',
            dataType: 'json',
            data: ops.param
        })
        .done(function(data) {
            var _data = data.result.car_type_list; 
            saleCar.array = _data || [];
            saleCar.loading = false;
        })
    })
}

//产品图片
function productAjax(productOps){
    $.ajax({
        url: productOps.url,
        dataType: 'json',
        data: productOps.param
    })
    .done(function(data) {
        var _data = data.result;
        var _newArr = []

        _newArr.push(_data.slice(0,18));

        productVm.bigPic = _data[0]['CDNPATH'] || '';
        
        productVm.array = _newArr || [];

        //轮播
        setTimeout(function(){
            $('#J-photo-y').flexslider({
                animation: "slide",
                direction:"vertical",
                slideshow:false, 
                animationLoop:false,    
            },1000);
        })
    })
}
//热销车推荐  
function hotCarAjax(options){
    $.ajax({
        url: options.url,
        dataType: 'json',
        data: options.param
    })
    .done(function(data) {
        hotVm.array = data.result || [];
    })
}
//在售车型定
var saleCar = avalon.define({
    $id: "c-car-type",
    array:pythonData.typeJson,
    color:CBB.activityColor(),
    loading:false
})

//产品图片绑定
var productVm = avalon.define({
    $id: "c-product",
    bigPic:'',     //大图
    picNum:'',              //图片数量
    array:[],   
    click:function(src){
        productVm.bigPic = src
    }
})

//热销车绑定
var hotVm = avalon.define({
    $id: "c-hot",
    array:pythonData.hotCarJson,
    loading:false,
    change:function(){
        hotCarAjax(hotOps)
    }
})

$(function(){

    productAjax(productOps)

    //产品图片类型
    $('#J-photo-type a').on('click',function(){
        var key = $(this).attr('data-key');

        productOps.param.position = key
        productAjax(productOps)
    })

    //大图切换
    $('.carser-focus-nav').on('click',function(){
        var picSrc = $(this).find('img').prop('src');
        $('.J-preview-img').prop('src',picSrc);
        $(this).addClass('active').siblings().removeClass('active');
    })

    //大图切换
    $('.J-small-photo').on('click',function(){
        var picSrc = $(this).children('img').prop('src');
        $('.J-big-photo').prop('src',picSrc);
        $(this).addClass('active').siblings('a').removeClass('active');
    })

    //轮播
    setTimeout(function(){
        $('#J-photo-y').flexslider({
            animation: "slide",
            direction:"vertical",
            slideshow:false, 
            animationLoop:false,    
        });
    })

    //大图切换
    $('.J-small-photo').on('click',function(){
        var picSrc = $(this).children('img').prop('src');
        $('.J-big-photo').prop('src',picSrc);
        $(this).addClass('active').siblings('a').removeClass('active');
    })

    //排序
    $('.J-rank').on('click',function(){
        var obj = $(this).find('i');
        var isUp = obj.hasClass('cbb-long-arrow-up');

        var orderBy = obj.attr('data-orderBy'); 
        var descen = obj.attr('data-descend');

        $(this).addClass('active').siblings().removeClass('active'); 

        if(isUp){
            obj.removeClass('cbb-long-arrow-up').addClass('cbb-long-arrow-down').attr('data-descend','True');
        }else{
            obj.removeClass('cbb-long-arrow-down').addClass('cbb-long-arrow-up').attr('data-descend','False');
        }

        orderPrice = $('.J-rank-price').find('i').attr('data-descend');
        orderDiscount = $('.J-rank-discount').find('i').attr('data-descend');

        typeOps.param.orderby = orderBy;
        typeOps.param.descending = descen;
        ajaxSaleData(typeOps)
    })  

    $('#J-carser-test dl:nth-child(3)').css('border-right','none');
    $('#J-carser-test dl:last').css('border-right','none');

    //测评
    setTimeout(function(){
        $('#J-carser-test').waterfall({
            itemCls: 'item',
            colWidth: 318,
            fitWidthBooleantrue:true,  
            loadingMsg:'<a href="" class="car-test-more">加载更多</a>',
            // loadingMsg:'',
            gutterWidth: 15,
            gutterHeight: 15,
            checkImagesLoaded: false,
            dataType: 'json',
            params:{series_id:testOps.param.series_id,count:testOps.param.count},
            path: function(page) {
                return testOps.url+'?page='+testOps.param.page++;
            }, 
            callbacks:{ 
                renderData:function(data,dataType){
                    if(data.result.length){ 
                    // articleArr = articleArr.push(data.result[0]);  
                    var html  = '<dl class="item" ms-repeat="array">'+
                                '    <dd><a href="'+data.result[0].url+'"><img src="'+data.result[0].front_img_path+'"></a></dd>'+
                                '    <dt>'+data.result[0].title+'</dt>   '+
                                '    <dd class="title">来源：'+data.result[0].source+'<span>'+data.result[0].created_date+'</span></dd>'+
                                '    <dd>'+data.result[0].description+'</dd>'+
                                '</dl>';
                    $('#J-carser-test').append(html) 
                    $('#J-carser-test dl:last').css('border-right','none');
                    }else{
                        $('#J-carser-test').waterfall('pause')  
                    }
                }
            }

        });
    },100);
})