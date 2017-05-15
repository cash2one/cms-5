(function($){
    $.fn.slideSelect = function(option){
      
      //var self = $(this);
      var Default = {
        data:data,
        sign:'',
        callback:function(obj,itm){
        } 
      };
      var ops = $.extend({},Default,option);

      //初始化
      function Init(self){
        var timestamp =(new Date()).valueOf();
        var index= self.data(ops.sign);

        self.attr('data-id',timestamp);
        $('body').append('<div class="g-slider-fix  " id ="'+timestamp+'">\
                            <div class="m-changeCar">\
                              <div class="title1">'+self.data('title')+'</div>\
                              <ul class="cars m-slideSelect">\
                              </ul>\
                              <div class="back j-back"> 点击此处返回 <span class="icon"><i class="u-icon u-icon-left-white"></i></span></div>\
                            </div>\
                          </div>');

        var obj = $('#'+timestamp);
        $.each(ops.data[index],function(index, el) {
          obj.find('.cars').append('<li><p data-value="'+el.value+'" class="c">'+el.name+'</p></li>')
        });
        $('html').addClass('f-lock');
        obj.addClass('g-slider-fix-active');
      }
      $(this).click(function(event) {
        /* Act on the event */
        var id = $(this).data('id');
        if($('#'+id).length>0){
          $('html').addClass('f-lock');
          $('#'+id).addClass('g-slider-fix-active');
        }else{
          Init($(this));
        }
      });
     

      // 侧滑返回
      var intervalId;
      $('body').on('click','.j-back',function(){        
        hideSlide($(this));
      })
      function hideSlide(el){
        $('html').removeClass('f-lock');
        el.closest('.g-slider-fix').removeClass('g-slider-fix-active');
      }

      //子项绑定事件
      $('body').on('click','.m-slideSelect li',function(){
        var id = $(this).closest('.g-slider-fix').attr('id');
        hideSlide($(this));
        //$('[data-id='+id+']').text($(this).find('.c').text());
        ops.callback($('[data-id='+id+']'),{name:$(this).find('.c').text(),value:$(this).find('.c').data('value')})
      });

    }
  }(jQuery));