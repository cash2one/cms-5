(function($){
    $.fn.citySelect = function(option){
      
      var html = '<div class="m-citypro">\
                    <div class="hd">\
                      <em></em>\
                      <i></i>\
                    </div>\
                  <div class="cnt">\
                  <ul class="list_l"></ul>\
                  <ul class="list_r"></ul>\
                  </div>';
      var Default = {
        url:'',
        param:{},
        data:{},
        html:html,
        parent:'',
        css:{},
        top:'',
        left:'',
        right:'',
        distance:'10%',
        direction:'left',
        zindex:10,
        pro_id:'',
        city_id:'',
        beforeInit:function(){
       },
       docInit:function(){        
       },
        callback:function(obj){
        } 
      };
      var ops = $.extend({},Default,option);
      function init(){
        if(!$.isEmptyObject(ops.parent)){
          $(ops.parent).css({'position':'relative'}).append(ops.html);
          if(!$.isEmptyObject(ops.css)){
            $(ops.parent).find(".m-citypro").css(ops.css);
          }
          $(ops.parent).find(".m-citypro").css({
            top:ops.top+'px',
            left:ops.left+'px',
            right:ops.right+'px',
            "z-index":ops.zindex
          });
          if(ops.direction == 'right'){
            $(ops.parent).find(".m-citypro .hd em,.m-citypro .hd i").css({
              right:ops.distance
            });
          }else{
            $(ops.parent).find(".m-citypro .hd em,.m-citypro .hd i").css({
              left:ops.distance
            });
          }
          if(!$.isEmptyObject(ops.data)){
            hasData(ops.parent,data,ops.pro_id,ops.city_id);
          }
          if(ops.url){
            ajaxData(ops.url,ops.param,ops.parent,ops.pro_id,ops.city_id);
          }
        }
        _bindEvent();
      };
      function hasData(obj,data,pro_id,city_id){
        if(!$.isEmptyObject(data)){
          $.each(data,function(ind1,itm1){
            $.each(itm1,function(ind2,itm2){
              var proIdDefault = itm2.data.province_id == pro_id? "width":"";
              $(obj).find('.list_l').append('<li class="itm '+proIdDefault+'" data-pro="'+itm2.data.province_id+'">'+itm2.data.province_name+'</li>');
              if(proIdDefault){
                $.each(itm2.citys,function(ind3,itm3){
                  var cityIdDefault = itm3.city_id == city_id? "red":"";
                  $(obj).find('.list_r').append('<li class="itm '+cityIdDefault+'" data-cityen="'+itm3.city_alias+'"  data-city="'+itm3.city_id+'">'+itm3.city_name+'</li>');
                });  
              }/*end if pro*/ 
            });/*end each itm2*/
          });/*end each itm1*/
        }/*end if */
      }/*end hasdata*/

      function _bindEvent(){
        if(!$.isEmptyObject(ops.parent)){
          $(ops.parent).on('click','.list_l .itm',function(event){
            event.stopPropagation();
            $(ops.parent).find('.list_r').html('');
            $(ops.parent).find('.list_l').html('');
            hasData(ops.parent,ops.data,$(this).data('pro'));
          });

          $(ops.parent).on('click','.list_r .itm',function(event){
            event.stopPropagation();
            var data = {
                pro_id:$(ops.parent).find('.list_l .width').data('pro'),
                pro_name:$(ops.parent).find('.list_l .width').text(),
                city_id:$(this).data('city'),
                city_en:$(this).data('cityen'),
                city_name:$(this).text()
            }
            $(this).siblings('li').removeClass('red').end().addClass('red');
            $(ops.parent).find('.m-citypro').hide();
            if(typeof(ops.callback) == 'function'){
              ops.callback(data);
            }
          });
        }
      }

      function ajaxData(url,param,obj,pro_id,city_id){
        $.ajax({
          url: url,
          type: 'GET',
          dataType: 'json',
          data: param,
        })
        .done(function(data) {
          ops.data = data.result;
          hasData(obj,ops.data,pro_id,city_id)
        })
        .fail(function() {
          console.log("error");
        })      
      }
      $(document).click(function(event) {
        /* Act on the event */
        $(ops.parent).find('.m-citypro').hide();
         ops.docInit();
         event.stopPropagation();
      });

      $(this).click(function(event) {
        /* Act on the event */
        if($(ops.parent).find('.m-citypro').length<=0){
         init();
        }else{
          $(ops.parent).find('.m-citypro').toggle();
        }
        ops.beforeInit();
        event.stopPropagation();
      }); 
    }
  }(jQuery));