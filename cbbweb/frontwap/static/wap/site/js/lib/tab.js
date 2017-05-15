var  tab = {
  init:function(nav,itm,ops,lis){
    this.ops = $.extend({},ops);      //初始化参数
    this.$nav = nav;                  //导航条                  
    this.$itm = itm; //子对象     
    this.bindEvent(lis);
  },
  bindEvent:function(lis){
    var self = this;
    this.$nav.on('click',lis,function(){
      self.changeTo(self.$itm.index($(this)));
    });
  },
  changeTo:function(index){           //获取单击nav.itm index
    this.$itm.removeClass('active').eq(index).addClass('active');
    this.ops.cnt.changeTo(index);
  }
}

//滚动对象
var scroll = {
  init:function(sign,index,ops,cnt,page){
    this.ops= $.extend({},ops);
    this.index = index;
    if(page){
      this.page = page;
      this.ops.param[page] =2;
    }else{ 
      this.ops.param.page =2;
    };
    this.cnt = cnt;
    this._bindEvent();
    this.flag = true;
    this.continue= true;
    if(sign  ){
      this.flag = false;
      this.ajaxData(this.ops)
    };
    return this;
  },
  cntInit:function(sign,index,ops,cnt,page){
    this.ops= $.extend({},ops);
    this.index = index;
    if(page){
      this.page = page;
      this.ops.param[page] =1;
    }else{ 
      this.ops.param.page =1;
    };
    this.cnt = cnt;
    this._bindEvent();
    this.flag = true;
    this.continue= true;
    if(sign && this.flag ){
     this.flag = false;
     this.ajaxData(this.ops)
    };
    return this;
  },
  _bindEvent:function(){
    var self =this
    $(window).scroll(function(event) {
      self.scrollbtm();
    });
  },
  loading:function(index){},
  scrollbtm:function(){
    var objHeight = this.cnt.height()+this.cnt.offset().top;
    var winHeight = window.innerHeight?  window.innerHeight:$(window).height();
    var scrollHeight = $(window).scrollTop() + winHeight;
    if(scrollHeight>objHeight-10 && this.flag && this.continue){
      this.flag = false;
      this.ajaxData();
    }
  },
  ajaxData:function(){
    var self = this;
    var ops = this.ops;
    this.loading(this.index);
    $.ajax({url: ops.url,cache:true,type: 'GET',dataType: 'json',data: ops.param,})
    .done(function(data) {
        self.continue = self.respondData(data,self.index);
        if(self.page){
          self.ops.param[self.page] =self.ops.param[self.page]+1;
        }else{ 
          self.ops.param.page =self.ops.param['page']+1;
        };
        //每次加载页面的时候滚动条滚动1px触发lazyLoad懒加载图片事件
        CBB.animateTo($(window).scrollTop() + 1); 
     })
    .fail(function(){ 
        console.log('error');
    })
    .always(function() {
      self.flag=true;
      console.log('complete');
    });
  },
  respondData:function(respond,index){}
}

//内容页对象
var cnt = {
  cntInit:function(cnt,itm,sign,ops,flag){
    this.ops =$.extend({url:'',param:{}},ops);       
    this.$cnt = cnt;
    this.$cntItm = itm;
    this.sign = sign;
    this.flag = flag;
    return this;
  },
  changeTo:function(index){
    if(this.changeReset(this,index)){
      this.changeMeth(index);
    }
  },
  changeReset:function(obj,index){},

  changeMeth:function(index){
    this.$cnt.addClass('f-dn').eq(index).removeClass('f-dn');
    //$('body').scrollTop(0);
    this.$cnt.eq(index).html('')
    scroll.cntInit(true,index,this.ops,this.$cnt.eq(index),this.flag);
  }
}

var main = {
  ops:{
    nav:'',
    navItm:'',
    cnt:'',
    cntItm:'',
    sign:'',
    index:0,
    lis:''
  },
  init:function(ops){
    this.ops=$.extend({},ops);
    this.scroll=scroll.init(false,0,ops.param,ops.cnt.eq(0),ops.page);
    this.cnt = cnt.cntInit(ops.cnt,ops.cntItm,ops.sign,ops.param,ops.page);
    this.tab = tab.init(ops.nav,ops.navItm,{cnt:this.cnt},ops.lis);
  }
}

