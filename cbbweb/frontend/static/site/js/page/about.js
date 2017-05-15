$(function(){
    $('.m-sidebar dd a').on('click',function(){
        $('.m-sidebar dd a').removeClass('active');
        $(this).addClass('active');
    });

    jQuery.CBBtab =function(tabBar,tabCon,class_name,tabEvent,i){
    var $tab_menu=$(tabBar);
      // 初始化操作
      $tab_menu.removeClass(class_name);
      $(tabBar).eq(i).addClass(class_name);
      $(tabCon).hide();
      $(tabCon).eq(i).show();
      
      $tab_menu.bind(tabEvent,function(){
        $tab_menu.removeClass(class_name);
          $(this).addClass(class_name);
          var index=$tab_menu.index(this);
          $(tabCon).hide();
          $(tabCon).eq(index).show();
      });
    }

    $.CBBtab("#J-tab .tabBar span","#J-tab .tabCon","active","click","0");
    $.CBBtab("#J-tab2 .tabBar span","#J-tab .tabCon","active","click","0");
})