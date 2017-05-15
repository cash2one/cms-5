(function($,document,window,undefined){
  var Finance_Car_Dealer = function(ele,opt){
    this.$element = ele;
    this.defaults = {
      type:'',
      target:'body',
      city_id:'',
      series_id:'',
      finance_id:'',
      data_car_type:{},
      data_dealer:{},
      reset_finance_url:'',
    };
    this.options = $.extend({},this.defaults,opt);
  };

  Finance_Car_Dealer.prototype = {
    constructor:Finance_Car_Dealer,
    init:function(){
      if($('.cars').length){
        $('.cars').remove();
      };
      $('html').addClass('f-lock');
      $('.g-slider-fix').addClass('g-slider-fix-active');
      this.load();
      this.bind();
    },

    load:function(){
      switch (this.options.type){
        case 'type':
          var contents = [],
              that = this;
          $('#template').html('<div class="u-title-ver title">\
                                <div class="tit">选择'+$('#series').text()+'的具体车型</div>\
                              </div><ul class="cars"></ul>');
          
          $.each(that.options.data_car_type,function(idx,itm){
            if (itm) {
              var car_type_name = itm.name.replace($('#series').text(),''),
                price = (itm.guide_price/10000).toFixed(2);
              contents.push('<li class="j-choseType" data-type='+itm.id+'>\
                <a href="javascript:;">'+car_type_name+'</a>\
                <div class="p">'+price+'万元</div>\
              </li>');
            }
          });
          $('.cars').html(contents.join(''));
          break;
        case 'dealer':
          var contents = [];
          $('#template').html('<div class="u-title-ver title">\
                                <div class="tit">选择 1 家经销商为您服务</div>\
                              </div><ul class="cars dealer"></ul>');
          
          $.each(this.options.data_dealer,function(idx,itm){
            contents.push('<li class="j-choseDealer" data-id='+itm.id+'\
             data-dealer = '+itm.dlr_code+'>\
              <div class="al">\
                <h3>'+itm.dlr_full_name+'</h3>\
                <p>'+itm.cont_address+'</p>\
              </div>\
              <div class="fr">\
                <p class="map"><i class="u-icon u-icon-map"></i></p>\
                <p>'+itm.distance.toFixed(2)+'km</p>\
              </div>\
              </li>');
          });
          $('.cars').html(contents.join(''));
          break;
        default:
          console.log('no template');
          break;
      }
    },
    
    bind:function(){
      var that = this;
      $('body').on('click','.j-back',function(){
        $('html').removeClass('f-lock');
        $('.g-slider-fix').removeClass('g-slider-fix-active');
      });

      //车型选择
      $('body').on('click','.j-choseType',function(){
        $('#type').text($(this).find('a').text());
        $('#type').attr('data-type',$(this).data('type'));

        resetFinance(that);
      });

      //经销商选择
      $('body').on('click','.j-choseDealer',function(){
        $('#dealer').text($(this).children('.al').children('h3').text());
        $('#dealer').attr('data-dealer',$(this).data('dealer'));

        resetFinance(that);
      });
    }
  };
  
  //重置金融
  function resetFinance(that){
    $.ajax({
      url:that.options.reset_finance_url,
      type:'GET',
      data:{
        city_id:that.options.city_id,
        car_type_id:$('#type').data('type'),
        dealer_id:$('#dealer').data('id'),
        car_series_id:that.options.series_id,
        finacial_product_id:that.options.finance_id
      }
    })
    .done(function(data){
      console.log(data);
      //贷款期限
      $('#loan_line').text(data.result.sku_item);
      //首付金额
      $('#first_num').text((data.result.first_pay_amount/10000).toFixed(2));
      //首付比例
      $('#first_scale').text(data.result.first_pay_percent);
      //月供金额
      $('#month_num').text(data.result.monthly_pay_amount);
      //贷款成本
      $('#loan_num').text(data.result.loan_cost);

      $('html').removeClass('f-lock');
      $('.g-slider-fix').removeClass('g-slider-fix-active');
    });
  }

  $.fn.finance_Car_Dealer = function(options){
    var choice = new Finance_Car_Dealer(this,options);
    choice.init();
    return this;
  }

}(jQuery,document,window))