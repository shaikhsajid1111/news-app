$(document).ready(function(){
    $('#social-media-container').hide();                /*By default, enter task panel is hidden */
    $('#toggle').click(function(){
        $('#social-media-container').slideToggle();             /*toggle the add task panel */
    });

});