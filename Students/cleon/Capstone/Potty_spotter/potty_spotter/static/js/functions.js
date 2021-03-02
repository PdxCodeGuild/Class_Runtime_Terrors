function renderMap(latLon) {
    var mymap = L.map('mapid').setView(latLon, 13);
    var marker = L.marker(latLon).addTo(mymap);
    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: '',
        maxZoom: 18,
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1,
        accessToken: //
    }).addTo(mymap);
}

function load_render_location() {
    $('.render-location').on('click', function (e) {
        e.preventDefault()
        var $this = $(this)

        var lat = $this.data('lat')
        var lon = $this.data('lon')

        $('#my_location').html('<div id="mapid" style="height: 300px;"></div>')
        renderMap([lat, lon])
    })
}


function get_checkbox_value($item) {
    if ($item.prop("checked")) {
        return true;
    } else if (!$item.prop("checked")) {
        return false;
    }
}
