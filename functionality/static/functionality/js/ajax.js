$(document).ready(function() {
    $('form').on('submit', function(e) {
        e.preventDefault();

        var params = $(this).serialize();
        var url = '/calc/';

        $.ajax({
            type: 'POST',
            url: url,
            data: params,

            success: function(data) {
                $('div#results').html(data);
            },

            failure: function() {
                alert('Error');
            }
        });
    });
});