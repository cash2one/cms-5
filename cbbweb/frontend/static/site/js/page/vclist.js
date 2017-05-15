function ajaxFinancial(financialOps) {
  financialVm.loading = true;
  $.ajax({
    url: financialOps.url,
    type: 'GET',
    dataType: 'json',
    data: financialOps.param
  }).done(function(data) {
    var _data = data.result;
    //判断是否显示没有数据
    if(_data.length){
      financialVm.noData = false;
    }else{
      financialVm.noData = true;
    }
    financialVm.loading = false;
    financialVm.arrList = _data || [];
  })
}

function ajaxTypePrice(purchaseTaxOps) {
  $.ajax({
    url: purchaseTaxOps.url,
    type: 'GET',
    dataType: 'json',
    data: purchaseTaxOps.param
  })
  .done(function(data) {
    var _data = data.result;
    purchaseTaxVm.obj = _data || '';
  })
}

function ajaxDealer(dealerOps, index) {
  $.ajax({
    url: dealerOps.url,
    type: 'GET',
    dataType: 'json',
    data: dealerOps.param
  })
  .done(function(data) {
    var hasId = false;
    var _data = data.result;
    var dealerOfferPrice;

    dealerVm.arrSs = _data || [];
    //指导价
    dealerOfferPrice = dealerVm.arrSs[index].offer_price.public_offer_price;

    dealerVm.currenDlCode = dealerVm.arrSs[index].dealer.dlr_code;

    purchaseTaxOps.param.price = dealerOfferPrice;
    purchaseTaxVm.originalPrice = dealerOfferPrice;
    dealerVm.dealerPrice = dealerOfferPrice;

    ajaxFinancial(financialOps);
    ajaxTypePrice(purchaseTaxOps);
  })
}

var financialVm = avalon.define({
    $id: "c-financial",
    arrList:[],
    orderBy:'',
    loading:false,       //loading
    priceToggle:true,    //价格
    hotToggle:true,      //热门
    noData:false,         //没有数据
    //价格排行
    rankPrice:function(){
      financialVm.priceToggle = !financialVm.priceToggle;
      financialOps.param.order_by = financialVm.priceToggle? 'monthly_payment':'-monthly_payment';
      ajaxFinancial(financialOps);
    },
    //热门排行
    rankHot:function(){
      financialVm.hotToggle = !financialVm.hotToggle;
      financialOps.param.order_by = financialVm.hotToggle? 'hot':'-hot';
      ajaxFinancial(financialOps);
    },
    //切换状态
    status:function(){
      $(this).addClass('z-active').siblings().removeClass('z-active');
    },
    //首付比例
    selectFirstPay:function(){
      var _val = $(this).text();
      var num;

      _val = _val.substring(0,_val.length-1);
      purchaseTaxVm.percent = _val;
      financialOps.param.first_pay_percent = _val;

      ajaxFinancial(financialOps);
    },
    //期数
    selectSkuItem:function(){
      var _val = $(this).text();

      _val = _val.substring(0,_val.length-1);
      financialOps.param.sku_item=_val;
      ajaxFinancial(financialOps);
    }
})
var purchaseTaxVm = avalon.define({
    $id: "c-purchaseTax",  
    percent:30,                                  //百分数
    originalPrice:purchaseTaxOps.param.price,    //价格       
    typeid:purchaseTaxOps.param.car_type_id,     //车型ID
    obj:pythonData.purchaseTaxJson,         
})  
var typeVm = avalon.define({
    $id: "c-type",
    typeName:pythonData.carSeriesJson[0].name,
    typeId:pythonData.carSeriesJson[0].id, 
    typePrice:pythonData.carSeriesJson[0].guide_price,
    arrCars:pythonData.carSeriesJson,
    selectType:function(){
      dealerOps.param.car_type_id=$(this).attr('data-id');
      ajaxDealer(dealerOps,0);  

      typeVm.typeName = $(this).text();
      typeVm.typeId = $(this).attr('data-id'); 
      typeVm.typePrice = $(this).attr('data-price');
    }
})  
var dealerVm = avalon.define({
    $id: "c-dealer",
    dealerPrice:pythonData.dealerJson[0].offer_price.public_offer_price,
    arrSs:pythonData.dealerJson,
    currenDlCode:pythonData.dealerJson[0].dealer.dlr_code,
    selectDealer:function(){

      var _index = $(this).attr('data-index');
      var _dealerId = $(this).attr('data-id');

      financialOps.param.dealer_id = _dealerId

      ajaxDealer(dealerOps,_index);        
    } 
})  

$(function(){ 
  //下拉框
  $.cbbSelect();
  
  //金融方案
  ajaxFinancial(financialOps);
})
