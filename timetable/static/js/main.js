$(document).ready( function(){

    $('.mark').click( function(event){
        $mark_value = $('.mark-value');
        $mark_value.hide();

        $button = $(this);
        $subject_id = $button.attr('data-subject_id');

        $.get('/get_mark/', {subject_id: $subject_id}, function(data){

            $mark_value.fadeIn(1000);
            $mark_value.html(data);
            $('.mark').show();
            $button.hide();
        });


    });

});