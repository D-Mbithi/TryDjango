$(document).ready(function(){
    $(".content-markdown").each(function(){
        let content = $(this).text();
        let markedContent = marked(content);
        $(this).html(markedContent);
    })
    $(".content-markdown img").each(function(){
        $(this).addClass("img-fluid")
    })
    // $(".content-markdown pre").each(function(){
    //     $(this).addClass("hidden")
    // })
    $(".article-body img").each(function(){
        $(this).addClass('img-fluid')

    })

    //preview title & content variable
    let titleItem = $('#id_title');
    let contentItem = $('#id_post');

    //preview content function
    function setContent(value){
        let markedContent = marked(value);
        $('.preview-content').html(markedContent);
        $('.preview-content img').addClass('img-fluid');
    }

    setContent(contentItem.val());

    contentItem.keyup(function(){
        let newContent = $(this).val()
        setContent(contentItem.val());
    })

    //Preview title function

    function setTitle(value){
        let markedTitle = marked(value);
        $('.preview-title').html(markedTitle);
    }

    setTitle(titleItem.val());

    titleItem.keyup(function(){
        let newTitle = $(this).val()
        setTitle(titleItem.val())
    })

    $('.div_id_published div').addClass('form-inline');
})
