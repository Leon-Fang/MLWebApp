$(document).ready(function(){
    var count=$("a.lastPage").text();
    if(count>1){
        var aEle = "<a></a>";
        var liEle = "<li></li>";

    }
  });


$("div.list-group").find("a").click(function(){
    var newsTitle = $(this).find("h4").text();
    var newsCotent =  $(this).find("div#newsContents").text();
    console.log(newsTitle+"  ss  "+newsCotent);
    $("h5.modal-title").text(newsTitle);
    $("div.modal-body").text(newsCotent);
});