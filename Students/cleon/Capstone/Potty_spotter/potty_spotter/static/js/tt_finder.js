$(document).ready(function () {
    particlesJS.load('particles-js', '/static/js/assets/particles.json', function () {
        console.log('callback - particles.js config loaded');
    });

    $('#input_location_search').on("change", function (e) {
        var value = $(this).val()
        $.get(`https://api.mapbox.com/geocoding/v5/mapbox.places/${value}.json?access_token=pk.eyJ1Ijoib2hpZDR1IiwiYSI6ImNrbGI4cTdwejBuOHkydnM2eDNsencwbjkifQ.vD9ayLr7sAwDqBcOoLke9w`)
            .then(resp => {
                $("#location_search_results").html('')
                for (const feature of resp.features) {
                    console.log(feature)
                    $("#location_search_results").append(
                        `<a href="#" class="render-location" 
                            data-lat="${feature.geometry.coordinates[1]}" 
                            data-lon="${feature.geometry.coordinates[0]}">${feature.place_name}</a><br>`
                    )
                }
                load_render_location()
            });
    })

    function loadMap() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(showPosition);
        } else {
            alert("Geolocation is not supported by this browser.");
        }
    }

    function showPosition(position) {
        var latitude = position.coords.latitude;
        var longitude = position.coords.longitude;

        renderMap([latitude, longitude])
    }

    // load map
    loadMap()

    $('.select-restroom-status').on('change', function (e) {
        var $this = $(this);
        var url = $('#ajax_restroom_status_update').val();
        var csrfmiddlewaretoken = $('#csrf_token').val();
        var pk = $this.data('pk');
        var status = $this.val();

        bootbox.confirm({
            message: "<h4>Confirm update status?</h4>",
            buttons: {
                confirm: {
                    label: 'Yes',
                    className: 'btn-success'
                },
                cancel: {
                    label: 'No',
                    className: 'btn-danger'
                }
            },
            callback: function (result) {
                if (result) {
                    $.post(url, {
                        csrfmiddlewaretoken,
                        pk,
                        status
                    }, function (result) {
                        if (result['success'] == true) {
                            window.location.reload()
                        }
                        if (result['success'] == false) {
                            bootbox.alert('Something went wrong!');
                        }
                    });
                } else {
                    location.reload();
                }
            }
        });
    });
});