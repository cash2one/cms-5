/*
  城市选择插件
  参数：
    api_allCitys  所有城市接口地址
    api_hotCitys  热门城市接口地址
    target        调用插件后填充的目标元素
    selected      选择城市后的回调函数
    fail          调用接口失败的回调函数
    template      用于调整模板
*/
(function($, window, document, undefined) {
  var CitySelect = function(options) {
    this.defaults = {
      api_allCitys: 'data.json',
      api_hotCitys: 'data_hot.json',
      target: $('.city_select'),
      selected: function(result) {
        console.log(JSON.stringify(data));
      },
      fail: function(err) {
        console.log('网络不稳定，暂时获取不到城市信息', err);
      },
      template: '<div class="m-citySelect"><div class="search"><i class="cbb cbb-search fa-4x"></i><input type="text" /><div class="result"></div></div><div class="hot"></div><div class="nav"></div><div class="content"><span class="loading">正在加载中.....</span></div></div>'
    };
    this.options = $.extend({}, this.defaults, options);
  }

  CitySelect.prototype = {
    init: function() {
      var _this = this;
      if ($('.m-citySelect').length) {
        $('.m-citySelect').show();
        return;
      }
      _this.options.target.append(_this.options.template);
      _this.load(_this);
    },
    load: function(_this) {
      $.get(_this.options.api_hotCitys).done(function(hot) {
        var content = ['<i class="cbb cbb-map-marker"></i>','热门城市：'];
        $.each(hot.result, function(key, city) {
          content.push('<span data-id="' + city.city_id + '" data-alias="' + city.city_alias + '">' + city.city_name + '</span>')
        });
        $('.m-citySelect .hot').html(content.join(''));
      }).fail(function(err) {
        _this.options.fail(err);
      });
      $.get(_this.options.api_allCitys).done(function(all) {
        var content = ['<ul>'],
          nav = [],
            ind=0;
        $.each(all.result, function(key, letter) {
          if(ind==0){
            nav.push('<a href="###" class="act">' + key + '</a>');
          }else{
            nav.push('<a href="###">' + key + '</a>');
          }
          ind++;
          content.push('<li><h3>' + key + '</h3>');
          $.each(letter, function(key, province) {
            content.push('<dl><dt>' + province.data.province_name + ':</dt><dd>');
            $.each(province.citys, function(key, city) {
              content.push('<span data-id="' + city.city_id + '" data-alias="' + city.city_alias + '">' + city.city_name + '</span>');
            });
            content.push('</dd></dl>');
          })
          content.push('</li>');
        });
        content.push('</ul>');
        $('.m-citySelect .nav').html(nav.join(''));
        $('.m-citySelect .content').html(content.join(''));
        $('.m-citySelect .nav a').click(function() {
          var $item = $('.m-citySelect .content h3:contains(' + $(this).text() + ')').parent();
          var topVal = $item[0].offsetTop;
          $(this).addClass("act").siblings().removeClass("act");
          $('.m-citySelect .content ul').animate({
            scrollTop: topVal
          }, 300, 'swing');
        });
        $('.m-citySelect [data-id]').click(function() {
          _this.options.selected({
            city_id: $(this).data('id'),
            city_name: $(this).text(),
            city_alias: $(this).data('alias')
          });
        });
        var $city_items = $('.m-citySelect .content [data-id]');
        $('.m-citySelect .search input').keyup(function() {
          var val = $.trim((' ' + $(this).val()).split('').join('.*'));
          var $result_wrap = $('.m-citySelect .search .result');
          $result_wrap.html('');
          $city_items.each(function() {
            var reg = eval("/" + val + "/");
            reg && reg.test($(this).data('alias')) && $result_wrap.append($(this).clone(true));
          });
        });
      }).fail(function(err) {
        _this.options.fail(err);
      });
    }
  }
  $.extend({
    citySelect: function(options) {
      var citySelect = new CitySelect(options);
      return citySelect.init();
    }
  })
})($, window, document);