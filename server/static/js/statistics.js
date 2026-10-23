(function($) {
    $(document).ready(function() {
        $.get($('#myChart').data('chart-url'), function(data) {
            var ctx = $("#myChart").get(0).getContext("2d");
            new Chart(ctx, {
                type: 'line', 
                data: data
            });
        });
    });
})(django.jQuery);
