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
      target: $('.city_select'),
      selected: function(result) {
        console.log(JSON.stringify(data));
      },
      fail: function(err) {
        console.log('网络不稳定，暂时获取不到城市信息', err);
      },
      template: '<div class="g-slider-fix-city">\
      <div class="m-change-city">\
        <div class="u-title-center-main">\
          选择城市\
          <i class="u-icon u-icon-close j-back"></i>\
        </div>\
        <div class="city-wrap">\
          <dl class="current">\
            <dt>当前城市</dt>\
            <dd><span>广东省</span><span>广州市</span><span>花都区</span></dd>\
          </dl>\
          <dl class="hot">\
            <dt>热门城市</dt>\
            <dd></dd>\
          </dl>\
          <dl class="city"></dl>\
        </div>\
        <div class="nav"></div>\
      </div>\
    </div>'
    };
    this.options = $.extend({}, this.defaults, options);
  }

  CitySelect.prototype = {
    init: function() {
      var _this = this;
      if ($('.m-change-city').length) {
        $('.m-change-city').show();
        return;
      }
      _this.options.target.append(_this.options.template);
      _this.load(_this);
    },
    load: function(_this) {
      $.get(_this.options.api_hotCitys).done(function(hot) {
        var content = [''];
        $.each(hot, function(key, city) {
          content.push(' < span data - id = "' + city.city_id + '"data - alias = "' + city.city_alias + '" > ' + city.city_name + ' < /span>')
        });
        $('.m-change-city .hot dd').html(content.join(''));
      }).fail(function(err) {
        _this.options.fail(err);
      });
      $.get(_this.options.api_allCitys).done(function(all) {
        var content = [],
          nav = [];
        $.each(all, function(key, letter) {
          nav.push('<a href="#nav_' + key + '">' + key + '</a > ');
          content.push('<dt id="nav_' + key + '">' + key + ' </dt>');
          $.each(letter, function(key, province) {
            content.push('<dd>' + province.data.province_name + '<div class="m-cityItems">');
            $.each(province.citys, function(key, city) {
              content.push(' < span data - id = "' + city.city_id + '"data - alias = "' + city.city_alias + '" > ' + city.city_name + ' < /span>');
            });
            content.push('</div></dd>');
          })
        });
        $('.m-change-city .nav').html(nav.join(''));
        $('.m-change-city .content').html(content.join(''));
        $('.m-change-city [data-id]').click(function() {
          _this.options.selected({
            city_id: $(this).data('id'),
            city_name: $(this).text(),
            city_alias: $(this).data('alias')
          });
        });
        var $city_items = $('.m-change-city .content [data-id]');
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