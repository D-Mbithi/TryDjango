$(document).ready(function(){
    $(".content-markdown").ForEach(function(){
        var content = $(this).text();
        var markedContent = marked(content);
        $(this).html(markedContent);
    })
})
