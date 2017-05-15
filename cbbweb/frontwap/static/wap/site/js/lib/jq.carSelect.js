/*
  车型车系选择插件：
  target:加载插件输出模板的父元素;
  type:车系或者车型 两种类型选择
  outer_template:外层具有共性的模板
  api_car_type:车型ajax参数
  api_car_series:车系ajax参数
*/
;(function($,window,document,undefined){
  var CarSelect = function(ele,opt){
    this.$element = ele;
    this.defaults = {
      target:'body',
      type:'type',
      outer_template:'<div class="g-slider-fix g-slider-fix-active">\
                          <div class="m-changeCar">\
                            <div id="template"></div>\
                            <div class="back j-back">\
                              点击此处返回\
                              <span class="icon">\
                                <i class="u-icon u-icon-left-white"></i>\
                              </span>\
                            </div>\
                          </div>\
                        </div>',
      api_car_type:{},
      api_car_series:{},
      car_series_name:'',
      reset_url:'',
    },
    this.options = $.extend({},this.defaults,opt);
  }
  
  CarSelect.prototype = {
    constructor:CarSelect,
    init:function(){
      if($('.g-slider-fix').length){
        $('.g-slider-fix').remove();
      };
      $('html').addClass('f-lock');
      $(this.options.target).append(this.options.outer_template);
      this.toChoose();
      this.bind();
    },
    toChoose:function(){
      switch(this.options.type){
        case 'type':
          var contents = [],
              that = this;
          $('#template').html('');
          $('#template').html('<div class="u-title-ver title">\
                                <div class="tit">选择'+$('#series').text()+'的具体车型</div>\
                              </div><ul class="cars"></ul>');
          if (api_car_type) {
            var data = api_car_type.result;
          }else{
            var data = this.options.api_car_type;
          };
          $.each(data,function(idx,itm){
            var car_type_name = itm.name.replace($('#series').text(),'');
            var price = (itm.guide_price/10000).toFixed(2)
            contents.push('<li class="j-choseType" data-type='+itm.id+'>\
              <a href="javascript:;">'+car_type_name+'</a>\
              <div class="p">'+price+'万元</div>\
            </li>');
          });
          $('.cars').html(contents.join(''));
          break;
        case 'series':
          var contents = [];
          $('#template').html('');
          $('#template').html('<div class="u-title-ver title">\
                                <div class="tit">选择车系</div>\
                               </div>\
                               <ul class="cars" id="df"><li class="sub-tit">东风日产</li></ul>\
                               <ul class="cars" id="qc"><li class="blue-tit">启辰</li></ul>\
                               <ul class="cars" id="jk"><li class="sub-tit">进口日产</li></ul>');
          $.each(this.options.api_car_series,function(idx,itm){
            switch(itm.car_brand_id){
              case 1:
                $('#df').append('<li class="j-choseSeries" series-id='+itm.id+'>\
                 <a href="javascript:;">'+itm.car_series_cn+'</a>\
                 </li>'); 
                break;
              case 2:
                $('#qc').append('<li class="j-choseSeries" series-id='+itm.id+'>\
                 <a href="javascript:;">'+itm.car_series_cn+'</a>\
                 </li>');
                break;
              case 6:
                $('#jk').append('<li class="j-choseSeries" series-id='+itm.id+'>\
                 <a href="javascript:;">'+itm.car_series_cn+'</a>\
                 </li>');
                break;
              default:
                console.log('no template');
                break;
            }

          });
          break;
        default:
          console.log('no template');
          break;
      }
    },
    bind:function(){
      var that = this;
      $('body').on('click','.j-choseType',function(){
        $('#type').text($(this).find('a').text());
        $('#type').attr('data-type',$(this).data('type'));
        $('html').removeClass('f-lock');
        $('.g-slider-fix').removeClass('g-slider-fix-active');
      });
      $('body').on('click','.j-choseSeries',function(){
        $('#series').text($(this).find('a').text());
        $('html').removeClass('f-lock');
        $('.g-slider-fix').removeClass('g-slider-fix-active');
        $.ajax({
          url:that.options.reset_url,
          type:'GET',
          data:{car_series_id:$(this).attr('series-id')}
        })
        .done(function(data){
          api_car_type = data;
          if(data.result.length >0){
            $('#type').text(data.result[0].name.replace($('#series').text(),''));
            $('#type').attr('data-type',data.result[0].id);
          }
        });
      });
      $('body').on('click','.j-back',function(){
        $('html').removeClass('f-lock');
        $('.g-slider-fix').removeClass('g-slider-fix-active');
      });
    }
  }

  $.fn.selectCar = function(options){
    var choice = new CarSelect(this,options);
    choice.init();
    return this;
  }
})(jQuery,window,document);