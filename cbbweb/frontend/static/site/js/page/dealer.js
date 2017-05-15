var dealerVm = avalon.define({
    $id: "c-dealer",
    array:pythonData.dealer,
    color:['GT-Rrz','Nyd','esczh','gxfw','rc','lsyz','jkcrz'],
    loading:false
})
$(function(){
	//url拼接
	function urlJoin(type){
		var _url = '?';
		var _arr = [];
		var countyVal;
		var brandVal;
		var seriesVal;
		countyVal = $('.J-filter-county a.active').attr('data-id');	
		brandVal = $('.J-filter-brand a.active').attr('data-id');	
		seriesVal = $('.J-filter-series a.active').attr('data-id');	

		if(countyVal){
			_arr.push('county='+countyVal);
		}
		if(brandVal){
			_arr.push('brand='+brandVal);
		}
		if(seriesVal && type!='brand'){
			_arr.push('series='+seriesVal);
		}

		_url += _arr.join('&');
		window.location.href=_url
	}

    function ajaxData (ops){
        dealerVm.loading = true;
        $.ajax({
            url: ops.url,
            type: 'GET',
            dataType: 'json',
            data: ops.param
        })
        .done(function(data) {
            var _data = data.result.dealer_list;
	        dealerVm.array = _data || []
            dealerVm.loading = false;
    	})
    }

    // ajaxData(ops);

    //当前条件
    $('#J-filter a.active').each(function(i,e){
    	var _val = $(this).text();
    	var _id = $(this).attr('data-id');
    	if(_id){
    		$('#J-condition').append('<a href="javascript:;">'+_val+'<i class="cbb cbb-close"></i></a>')
    	}
    })

    //条件删除
    $('#J-condition i').on('click',function(){
    	var _val = $(this).closest('a').text();
    	var _eachVal;

    	$(this).closest('a').remove();
    	$('#J-filter a').each(function(i, e) {
    		_eachVal = $(this).text();
    		if(_val == _eachVal){
    			$(this).removeClass('active').closest('dd').find('a:first').addClass('active');
    			urlJoin();
    		}
    	});
    })

    //条件筛选
	$('#J-filter a').on('click',function(){
        var _type = $(this).closest('dl').attr('data-type');
		$(this).addClass('active').siblings().removeClass('active');

		urlJoin(_type);
	})

	//获取位置
    var offsetTop = $('.condition').offset().top;

    //分页组件
    $(".m-page").createPage({
        pageCount:pageToal,
        current:1,
        callback:function(p){
            dealerOps.param.page = p;
            ajaxData(dealerOps);
            $("html,body").animate({scrollTop:offsetTop},200);
        }
    });

    //城市切换
    $('.m-btn-group li a').on('click',function(){
        var txt = $(this).text();
        var parentsBtn = $(this).closest('.m-btn-group');
        var obj = parentsBtn.find('.val');
        var cityId = $(this).attr('data-cityId');

        if(cityId){
            window.location.href="/dealer?city_id="+cityId
        }
    
    }) 
})