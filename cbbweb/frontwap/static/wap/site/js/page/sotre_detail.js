$(function(){ 
	function ajaxSaleCar(onSaleCarOps){
		$.ajax({
			url: onSaleCarOps.url,
			type: 'GET',
			dataType: 'json',
			data: onSaleCarOps.param,
			beforeSend:function(){
				scroll_Flag = false;
			}
		}) 
		.done(function(data) {
			if(data.result.length){
				$(data.result).each(function(i,e){
					onSaleCarVm.items.push(data.result[i]);
				})
				scroll_Flag = true;
			}else{
				scroll_Flag = false;
			}
			onSaleCarOps.callback?onSaleCarOps.callback():'';
		})      
		.always(function() {
			onSaleCarOps.param.page++;
		});	
	}

	var onSaleCarVm = new Vue({
	  el: '#c-onSaleCar',
	  data: {
	    items: pythonData.onsaleJson
	  }
	})

    var dataArray = [],
        ajaxData = [];

	var $items = $('.j-tab');
	var tabTop = $items.offset().top-100;
	//防止滚动时重复发送请求
	var scroll_Flag = true; 

	//跳转
	$('body').on('click','.j-three',function(){
		var key = $(this).data('key'),
		    series = $(this).data('series'),
		    type = $(this).data('type');
		window.location.href = pythonData.cityAlias+"/info/apply?key="+key+"&car_series="+series+"&car_type="+type+"&dealer_id="+pythonData.dealerId;
	});

	//获取车型
	$('.m-tabContent').on('click','.j-change',function (){
		dataArray = [];
		$($(this).find('.select-icon')[0]).addClass('arrow-active');
		$('.cars').html(''); 
		var series_name =$(this).data('name'),
		    series_id = $(this).data('series');

		$.ajax({
		  url:pythonData.getTypeUrl,
		  type:'GET',
		  data:{
		    car_series_id:series_id
		  }
		}) 
		.done(function(data){
		  $.each(data.result,function(idx,itm){
		    dataArray.push(itm);
		    var html_node ='<li>\
		              <div href="javascript:;" class="j-changeItm" data-to="'+series_name+'" data-type="'+itm.id+'" data-idx="'+idx+'">\
		               <div class="p">'+itm.name+'</div>\
		              </div>\
		            </li>';
		    $('.cars').append(html_node);
		  }); 
		});
		$('html').addClass('f-lock');
		$('.g-slider-fix').addClass('g-slider-fix-active');
	});

	//返回
	$('.j-back').click(function(){
		$('html').removeClass('f-lock');
		$('.g-slider-fix').removeClass('g-slider-fix-active');
		$($('li').find('.select-icon')).removeClass('arrow-active');
	});

	//改变车型
	$('body').on('click','.j-changeItm',function(){  
		var _this = $(this);
		var changeItm = dataArray[Number($(this).data('idx'))];
		var guide_price = (changeItm.guide_price/10000).toFixed(2) + '万';
		var typeId = $(this).data('type')
		var price;

		$.ajax({   
		  url: pythonData.getTypePrice,
		  type: 'get',
		  dataType: 'json',   
		  data: {dealer_id: pythonData.dealerId,car_type_id:typeId},
		})
		.done(function(data) {
		  var price = (data.result.price/10000).toFixed(2) + '万';
		  $("li[data-flag="+_this.data('to')+"]").find('.j-change').find('span').text('');
		  $("li[data-flag="+_this.data('to')+"]").find('.j-change').find('span').text(changeItm.name.replace(_this.data('to'),''));
		  $("li[data-flag="+_this.data('to')+"]").find('.j-price').text(price);
		  $("li[data-flag="+_this.data('to')+"]").find('.j-guide').text(guide_price);

		  $('html').removeClass('f-lock');
		  $('.g-slider-fix').removeClass('g-slider-fix-active');
		  $($("li[data-flag="+_this.data('to')+"]").find('.select-icon')).removeClass('arrow-active');
		  $("li[data-flag="+_this.data('to')+"]").find('.j-three').attr('data-type',_this.data('type'));
		})
	});

	$('.j-tab li').on('click',function(){
		var _typeId = $(this).data('type');

		$(this).addClass('active').siblings().removeClass('active');
  		onSaleCarOps.param.page = 1;
  		onSaleCarVm.items = [];
  		onSaleCarOps.param.car_type = _typeId;

  		ajaxSaleCar(onSaleCarOps);
  		CBB.animateTo(0)

	})


	//滚动事件
	$(window).on('scroll', function(){

		//懒加载
		CBB.lazyLoad([{
		  id:'.J-tab-ul',top:50
		}]);

		/*固定顶部*/
		var scrollHeight = $(window).scrollTop();
		if(scrollHeight >= tabTop){
		  $items.addClass('z-title-fixed');
		}else{
		  $items.removeClass('z-title-fixed');
		}

	    var _top = $(this).scrollTop(),
	        _winH = $(this).height(),
	        _get_more_top = $('.J-get-more').offset().top + $('.J-get-more').outerHeight();

        if (_top + _winH >= _get_more_top && scroll_Flag) {
            ajaxSaleCar(onSaleCarOps)
        }
	});

    var pos = [];
    var geolocation = new BMap.Geolocation();

    geolocation.getCurrentPosition(function(r){
      if(this.getStatus() == BMAP_STATUS_SUCCESS){
      	var _distance;
      	var _url;

        pos.push(Number(r.point.lat));
        pos.push(Number(r.point.lng));

        _distance = (CBB.getDistance(pos[0],pos[1],pythonData.dealerLa,pythonData.dealerLo)).toFixed(2)+'km';

  		_url = 'http://api.map.baidu.com/direction?origin=latlng:'+pos[0]+','+pos[1]+'|name:我的位置&destination=latlng:'+pythonData.dealerLa+','+pythonData.dealerLo+'|name:'+pythonData.dealerName+'&mode=driving&region='+pythonData.dealerCity+'&output=html&src=yourCompanyName|yourAppName';

  		$('#J-distance').text(_distance);
  		$('#J-go').attr('href',_url);

      }
      else {
        console.log('fail');
      }        
    },{enableHighAccuracy: true});
})
