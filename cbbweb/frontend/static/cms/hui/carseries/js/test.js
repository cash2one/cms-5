
String.prototype.dfFormat = function(info)
{
    var args = info;
    return this.replace(/\{(\d+)\}/g,
        function(m,i){
            return args[i];
        });
};

CAR_SERIES_HTML = '\
<tr>\
    <td>{0}</td>\
    <td>{1}</td>\
</tr>\
';

INFO_HTML = '\
<tr>\
    <td>{0}</td>\
    <td>{1}</td>\
</tr>\
';

var init_page = function() {

    // get page info asyn
    $(".rest_get").on('click', function(){
        var li_index = parseInt($(this).text());
        $("#asynul").children("li").removeClass("active");
        $("#asynul").children("li").eq(li_index-1).addClass("active");

        jQuery.get($(this).attr('rest_url'), 
            function(data, status) {
                if(status == 'success') {
                    //var ret = eval('(' + data + ')');
                    var ret = data;
                    var resStatus = ret['status'];
                    if(resStatus == 'success') {
                        val = ret['result'];
                        var car_table = $("#car_series_tbody");
                        car_table.empty();
                        for(var i = 0; i < val.length; i++) {
                            var car_series = val[i];
                            car_table.append(
                                CAR_SERIES_HTML.dfFormat([
                                    car_series['car_series_cn'],
                                    car_series['car_series_en']
                                ])
                            )
                        }
                    }
                    else {
                        
                    }
                }
        })
        .error(function(){
            
        });
    });

    // get car series list
    $("#getseriesbtn").on('click', function(){
        jQuery.get($(this).attr('rest_url'), 
            function(data, status) {
                if(status == 'success') {
                    //var ret = eval('(' + data + ')');
                    var ret = data;
                    var resStatus = ret['status'];
                    if(resStatus == 'success') {
                        val = ret['result'];
                        var car_table = $("#asyntbody");
                        car_table.empty();
                        for(var i = 0; i < val.length; i++) {
                            var car_series = val[i];
                            car_table.append(
                                INFO_HTML.dfFormat([
                                    car_series['car_series_cn'],
                                    car_series['car_series_en']
                                ])
                            )
                        }
                    }
                    else {
                        
                    }
                }
        })
        .error(function(){
            
        });
    });

    $("#clearseriesbtn").on('click', function(){
        var car_table = $("#asyntbody");
        car_table.empty();
    });

    // get car brand info
    /*
    $("#getinfobtn").on('click', function(){
        jQuery.get($(this).attr('rest_url'), 
            function(data, status) {
                if(status == 'success') {
                    //var ret = eval('(' + data + ')');
                    var ret = data;
                    var resStatus = ret['status'];
                    if(resStatus == 'success') {
                        val = ret['result'];
                        var info_tabel = $("#asyndatatbody");
                        info_tabel.empty();
                        for(var i = 0; i < val.length; i++) {
                            var info = val[i];
                            info_tabel.append(
                                CAR_SERIES_HTML.dfFormat([
                                    info['brand_name'],
                                    info['series_name']
                                ])
                            )
                        }
                    }
                    else {
                        
                    }
                }
        })
        .error(function(){
            
        });
    });
    */
    $("#getinfobtn").on('click', function(){
        jQuery.post($(this).attr('rest_url'), 
            {
                csrfmiddlewaretoken: jQuery("[name='csrfmiddlewaretoken']")[0].attributes["value"].value, 
                id: 1
            },
            function(data, status) {
                if(status == 'success') {
                    //var ret = eval('(' + data + ')');
                    var ret = data;
                    var resStatus = ret['status'];
                    if(resStatus == 'success') {
                        val = ret['result'];
                        var info_tabel = $("#asyndatatbody");
                        info_tabel.empty();
                        for(var i = 0; i < val.length; i++) {
                            var info = val[i];
                            info_tabel.append(
                                CAR_SERIES_HTML.dfFormat([
                                    info['brand_name'],
                                    info['series_name']
                                ])
                            )
                        }
                    }
                    else {
                        
                    }
                }
        })
        .error(function(){
            
        });
    });

    $("#clearinfobtn").on('click', function(){
        var car_table = $("#asyndatatbody");
        car_table.empty();
    });
};



