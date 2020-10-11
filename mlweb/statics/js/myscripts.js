
$("div.list-group").find("a").click(function(){
    var newsTitle = $(this).find("h4").text();
    var newsCotent =  $(this).find("div#newsContents").text();
    $("h5.modal-title").text(newsTitle);
    $("div.modal-body").text(newsCotent);
});

$("ul#paginationId").find("li").click(function(){
    var currentPageIndex = parseInt($(this).siblings("li.active").text());
    var fisrtNum = $(this).prevAll().length;
    var lastNum = $(this).nextAll().length;

    if(currentPageIndex > 1){
        $("ul#paginationId").find("li:first").removeClass("disabled");
    }else{
        $("ul#paginationId").find("li:first").addClass("disabled");
    };

    if(fisrtNum === 0){
        if($(this).hasClass("disabled")){

        }else{
            $(this).siblings("li.active").prev().addClass("active").siblings("li").removeClass("active");
        }
    }

    if(lastNum === 0){
        $(this).siblings("li.active").next().addClass("active").siblings("li").removeClass("active");
        $(this).removeClass("active");
    }

});

$("div.page-item").find("a").click(function(){
    $(this).parents("li").addClass("active").siblings("li").removeClass("active");

});
