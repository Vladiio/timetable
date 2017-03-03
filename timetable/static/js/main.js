$(document).ready( function(){

    $('.mark').click( function(event){

        $me = $(this);
        $subject_id = $(this).attr('data-subject_id');

        $.get('/get_mark/', {subject_id: $subject_id}, function(data){

            $me.hide();
            $('.mark-info').html(data);
        });
    });

});