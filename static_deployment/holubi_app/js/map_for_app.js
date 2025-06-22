// zobrazení mapy Leaflet
var map = L.map('map').setView([50.0755, 14.4378], 11);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

// načtení dat z JSON
let data = JSON.parse(document.getElementById('data_json').textContent);

// vytvoření markerů
data.forEach(one => {
    L.marker([one.latitude, one.longitude]).addTo(map)
        .bindPopup("<b><a href='" + one.detail_url + "'>" + one.adresa + "</a></b>");
        
}
    
)