
String.prototype.dfFormat = function(info)
{
    var args = info;
    return this.replace(/\{(\d+)\}/g,
        function(m,i){
            return args[i];
        });
};

var init_page = function() {
    $(".api_result").hide();
    $(".api_title").click(function(){
        $(this).siblings(".api_result").toggle();
    });

    $("#show_detail_btn").click(function(){
        $(".section").show();
    });

    $("#hide_detail_btn").click(function(){
        $(".section").hide();
    });

    $("#toggle_detail_btn").click(function(){
        $(".section").toggle();
    });

    $(".highlight").children("p").click(function(){
        $(this).siblings(".section").toggle();
    });

    var api_result_list = $(".json_result");
    for(var i = 0; i < api_result_list.length; i++) {
        var tmp_api_result = api_result_list.eq(i);
        var tmp_json = json_dict[tmp_api_result.attr("json_key")];
        tmp_api_result.JSONView(tmp_json, { collapsed: true });
    }

    $('.collapse-btn').on('click', function() {
        $(this).siblings('.json_result').JSONView('collapse');
    });

    $('.expand-btn').on('click', function() {
        $(this).siblings('.json_result').JSONView('expand');
    });

    $('.toggle-btn').on('click', function() {
        $(this).siblings('.json_result').JSONView('toggle');
    });

    $('.toggle-1-btn').on('click', function() {
        $(this).siblings('.json_result').JSONView('toggle', 1);
    });

    $('.toggle-2-btn').on('click', function() {
        $(this).siblings('.json_result').JSONView('toggle', 2);
    });

    $('.toggle-3-btn').on('click', function() {
        $(this).siblings('.json_result').JSONView('toggle', 3);
    });

    $('.toggle-4-btn').on('click', function() {
        $(this).siblings('.json_result').JSONView('toggle', 4);
    });
};


