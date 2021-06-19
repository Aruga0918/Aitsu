//スマホで閲覧されているとき自動調節
function initMap() {
    var useragent = navigator.userAgent;
    var mapdiv = document.getElementById("map");
  
    if (useragent.indexOf('iPhone') != -1 || useragent.indexOf('Android') != -1){
      mapdiv.style.width = '100%';
      mapdiv.style.height = '100%';
    }
  
    var opts = {
      zoom: 15,
      center: new google.maps.LatLng(38.260247,140.879723)
    };
    var map = new google.maps.Map(mapdiv, opts);
  }