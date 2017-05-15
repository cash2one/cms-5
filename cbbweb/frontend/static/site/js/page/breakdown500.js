function ajaxData (ops){
        $.ajax({
            url: ops.url,
            type: 'GET',
            dataType: 'json',
            data: ops.param
        })
        .done(function(data) {
        	 //console.log(data.result);
            var _data = data.result;
  			$(_data).each(function(index, el) {
                if(_data[index].service_auth){
  				  _data[index].service_auth = _data[index].service_auth.split(',');
                }
  			});
			
				
			
	        vmcarHot.arrcarHot = _data || [];
//		console.log(_data);
			//vcTong($('.m-list-g'),_data[0].PASS_PERCENT) ;

    	})
    }
ajaxData (carHot);