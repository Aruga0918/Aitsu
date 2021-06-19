
        function initMap() {
          var opts = {
            zoom: 15,
            center: new google.maps.LatLng(38.260247,140.879723)
          };
          var map = new google.maps.Map(document.getElementById("map"), opts);
          var mposition = {lat: 38.2619978, lng: 140.8804764};
          var marker = new google.maps.Marker({
            position: mposition,
            map: map,
            
            animation: google.maps.Animation.DROP,
            icon: {
              url: "arugaicon.png",
              scaledSize: new google.maps.Size(30, 50)
            }
          });
        }
      