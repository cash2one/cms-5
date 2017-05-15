//经销商
function dealerAjax(options){
	dealerVm.loading = true;
	$.ajax({
		url: options.url,
		dataType: 'json',
		data: delearOps.param
	})
	.done(function(data) {
		dealerVm.array = data.result || [];
		dealerVm.loading = false;
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
		
		productVm.array = _newArr || [];
		if(_data[0]){
			productVm.bigPic = _data[0]['CDNPATH'] || '';
		}

		//轮播 
		setTimeout(function(){
			$('#J-photo-y').flexslider({
				animation: "slide",
				direction:"vertical",
				slideshow:false, 
				animationLoop:false,	
			});
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

//经销商绑定
var dealerVm = avalon.define({
    $id: "c-dealer",
    array:pythonData.dealerJson,
    loading:false
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

//产品图片绑定
var productVm = avalon.define({
    $id: "c-product",
    bigPic:'',             //大图
    click:function(src){
        productVm.bigPic = src
    },
    array:[]         
})
$(function(){
	//下拉框
	$.cbbSelect(); 

	productAjax(productOps);
	//产品图片类型
	$('#J-photo-type a').on('click',function(){
		var key = $(this).attr('data-key');

		productOps.param.position = key
		productAjax(productOps)
	})

	//贷款轮播
	$('#J-slide-x').flexslider({
		animation: "slide",
		slideshow:false	
	});
		
	//本地经销商
	$('#J-dealer').delegate('.J-compare-btn','click',function(){ 
		var parentLi = $(this).closest('li');
		var isActive = parentLi.hasClass('active');
		var activeNum = $('.J-compare-btn .cbb-minus').length;
		
		if(isActive){
			parentLi.removeClass('active');
			parentLi.find('.J-compare-btn i').removeClass('cbb-minus').addClass('cbb-plus');
		}else{
			if(activeNum <= 2){
			parentLi.addClass('active');
			parentLi.find('.J-compare-btn i').removeClass('cbb-plus').addClass('cbb-minus');
			}else{
				$.errorAlert({content:'最多选3间'});
			}
		}

		activeNum = $('.J-compare-btn .cbb-minus').length;
		$('#J-compare-result .num').text(activeNum)

		activeNum? $('#J-compare-result').fadeIn(): $('#J-compare-result').fadeOut();

		//拼接经销商ID
		var idArr = [];
		var dealer_id;
		$('.cbb-minus').each(function(){
			var _id = $(this).closest('.J-compare-btn').attr('data-dealerid');
			idArr.push(_id);
		}); 
		dealer_id = idArr.join('|')
		$('.J-compare-submit').attr('href','/info/apply?dealer_id='+dealer_id+'&series_id='+pythonData.seriesId);
	})

	//选择城市隐藏比价
	$('.m-city').on('click',function(){
		$('#J-compare-result').hide();
	})

	//排序
	$('.J-rank').on('click',function(){
		var obj = $(this).find('i');
		var isUp = obj.hasClass('cbb-long-arrow-up');
		var areaId = $('#J-area a').attr('data-areaId');
		var cityId = $('#J-city .val').attr('data-cityid');
		var orderBy = obj.attr('data-orderBy'); 
		var descen = obj.attr('data-descend');

		$(this).addClass('active').siblings().removeClass('active'); 

		if(isUp){
			obj.removeClass('cbb-long-arrow-up').addClass('cbb-long-arrow-down').attr('data-descend','true');
		}else{
			obj.removeClass('cbb-long-arrow-down').addClass('cbb-long-arrow-up').attr('data-descend','false');
		}

		orderPrice = $('.J-rank-price').find('i').attr('data-descend');
		orderDiscount = $('.J-rank-discount').find('i').attr('data-descend');

		delearOps.param.city_id = cityId;
		delearOps.param.county_id = areaId;
		delearOps.param.orderby = orderBy;
		delearOps.param.descending = descen;
		dealerAjax(delearOps)
	})

	//城市切换
	$('.J-select-link').delegate('.m-btn-group li a','click',function(){
		var	txt = $(this).text();
		var parentsBtn = $(this).closest('.m-btn-group');
		var obj = parentsBtn.find('.val');
		var provinceId = $(this).attr('data-provinceId');
		var cityId = $(this).attr('data-cityId');
		var areaId = $(this).attr('data-areaId');

		if(provinceId){
			obj.text(txt).attr('data-provinceId',provinceId);
			$.ajax({
				url: provinceUrl,
				dataType: 'json',
				data: {province_id: provinceId},
			})
			.done(function(data) {
				dealerVm.array = [];
				var _html = '';
				$(data.result).each(function(i,e){
					_html +='<li><a href="javascript:;" data-cityId="'+e.city_id+'">'+e.city_name+'</a></li>';
				})
				$('#J-city .val').text('请选择城市').attr('data-cityId','');
				$('#J-city ul').empty().append(_html);
				$('#J-area').hide();

			})
		}

		if(cityId){ 
			obj.text(txt).attr('data-cityId',cityId);
			$.ajax({
				url: cityUrl,
				dataType: 'json',
				data: {city_id:cityId},
			})
			.done(function(data) {
				if(data){
					var _html = '<a class="active" href="javascript:;" data-areaId="">不限</a>';
					$(data.result).each(function(i,e){
						_html +='<a href="javascript:;" data-areaId="'+e.county_id+'">'+e.county_name+'（'+e.dealer_count+'）</a>';
					})
					$('#J-area').empty().append(_html).show();

					delearOps.param.city_id = cityId;
					dealerAjax(delearOps);
				}
			})
		}
		
		parentsBtn.removeClass('open').next().show();
	})

	//区切换
	$('#J-area').delegate('a','click',function(){
		var areaId = $(this).attr('data-areaId');
		var cityId = $('#J-city .val').attr('data-cityid');

		$(this).addClass('active').siblings().removeClass('active');

		delearOps.param.city_id = cityId;
		delearOps.param.county_id = areaId;
		dealerAjax(delearOps)
	})
})