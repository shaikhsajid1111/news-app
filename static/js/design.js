$(document).ready(function(){
    $('#social-media-container').hide();                /*By default, enter task panel is hidden */
    $('#toggle').click(function(){
        $('#social-media-container').slideToggle("slow");             /*toggle the add task panel */
    });

    $("#search_word").on("keypress", function(event) {
        var englishAlphabetAndWhiteSpace = /[A-Za-z0-9 @]+/ig;
        var key = String.fromCharCode(event.which);
        if (englishAlphabetAndWhiteSpace.exec(key)) {
            return true;
        }
        else{
        alert ("this character is not aceepted!");
        $("#search_word").val('');
    }
    });

    
    



});