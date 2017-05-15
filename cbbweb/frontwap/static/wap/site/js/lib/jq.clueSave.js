(function($,window,document,undefined){
  var ClueSave = function(ele,opt){
    this.$element = ele;
    this.defaults = {
      ajaxData:{
        url:'',
        type:'POST',
        data:{
          name:'',
          phone:'',
          storeId:'',
          carTypeId:'',
          carSeriesId:''
        }
      },
      locationData:{
        url:''
      }
    };
    this.options = $.extend({},this.defaults,opt);
  };

  ClueSave.prototype = {
    constructor:ClueSave,
    init:function(){
      if (this.clueJudge()) {
        this.clueSubmit();
      }else{
        $('#clueFlock').remove();
        $('#clueLoading').remove();
        if(!$('#userName').val()){
          $('#userName').siblings('.error-tip').show();
          errorGone();
          return;
        }else{
          $('#userTel').siblings('.error-tip').show();
          errorGone();
          return;
        };
      };
    },
    clueJudge:function(){
      if(this.options.ajaxData.url 
        && this.options.ajaxData.data.name 
        && this.options.ajaxData.data.phone
        && this.options.ajaxData.data.dlrCode
        && (this.options.ajaxData.data.carTypeId 
        || this.options.ajaxData.data.carSeriesId)){
        
        var myreg = /^(((13[0-9]{1})|(15[0-9]{1})|(18[0-9]{1}))+\d{8})$/;
        if(!myreg.test(this.options.ajaxData.data.phone)){
          return false;
        }
        return true;
      }else{
        return false;
      }
    },
    clueSubmit:function(){
      var that = this;
      $.ajax( this.options.ajaxData )
      .done(function(data){
        var status = JSON.parse(data.result); 
        var locationOps = that.options.locationData;

        $('#clueFlock').remove();
        $('#clueLoading').remove();  
        
        locationOps.callback ? locationOps.callback(status) : '';            
        if(status.error == 0){
          window.location.href = locationOps.url
                                   +'?key='+locationOps.flag;
        }
      })
      .fail(function(err){
        failSubmit(err);
      })
    },
  }

  function failSubmit(err){
    console.log(err);  
  };

  $.fn.clueSave = function(options){
    var clue = new ClueSave(this,options);
    clue.init();
    return this;
  }

}(jQuery,window,document));