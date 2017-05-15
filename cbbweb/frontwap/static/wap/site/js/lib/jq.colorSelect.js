(function($,document,window,undefined){
  var ColorSel = function(ele,opt){
    this.$element = ele;
    this.defaults = {
      ajaxData:{
        url:'',
        type:'GET',
        data:{
          car_type_id:''
        }
      },
      flag:'',
      target:''
    };
    this.options = $.extend({},this.defaults,opt);
  };

  ColorSel.prototype = {
    constructor:ColorSel,
    init:function(){
      if ($('.cars').length) {
        $('.cars').remove();
      };
      $('html').addClass('f-lock');
      $('.g-slider-fix').addClass('g-slider-fix-active');
      this.load();
      this.bind();
    },
    load:function(){
      var that = this;
      $.ajax(this.options.ajaxData).done(function(data){
        $('#template').append('<ul class="cars"></ul>');
        that.output(data);
      })
      .fail(function(err){
        console.log(err);
      });
    },
    output:function(data){
      switch (this.options.flag){
        case 'outer':
          if(data.result){
            var colData = data.result.color_code,
              contents = [];
            $.each(colData,function(idx,itm){
              contents.push('<li>\
                <i style="background-color:'+itm.rgb_value+'" class="u-icon-color f-fl"></i>\
                <a class="j-choseOuterCol" href="javascript:;">'+itm.color_name+'</a>\
                </li>');
            });
            $('.cars').html(contents.join(''));
          }else{
            $('.cars').html('暂无数据');
          };
          break;
        case 'inner':
          if(data.result){
            var colData = data.result.incolor_code;
              contents = [];
            $.each(colData,function(idx,itm){
              contents.push('<li>\
                <i style="background-color:'+itm.rgb_value+'" class="u-icon-color f-fl"></i>\
                <a class="j-choseInnerCol " href="javascript:;">'+itm.color_name+'</a>\
                </li>');
            });
            $('.cars').html(contents.join(''));
          }else{
            $('.cars').html('暂无数据');
          };
          break;
        default:
          console.log('no template');
          break;
      }
    },
    bind:function(){
      $('body').on('click','.j-choseOuterCol',function(){
        $('html').reomveClass('f-lock');
        $('#outer').text($(this).text());
        $('.g-slider-fix').removeClass('g-slider-fix-active');
      });
      $('body').on('click','.j-choseInnerCol',function(){
        $('html').reomveClass('f-lock');
        $('#inner').text($(this).text());
        $('.g-slider-fix').removeClass('g-slider-fix-active');
      });
      $('body').on('click','.j-back',function(){
        $('html').reomveClass('f-lock');
        $('.g-slider-fix').removeClass('g-slider-fix-active');
      });
    }
  }

  $.fn.colorSel = function(options){
    var color = new ColorSel(this,options);
    color.init();
    return this;
  }
}(jQuery,document,window));