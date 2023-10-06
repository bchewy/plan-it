



var targetlatlng={lat:1.4296517,lng:103.8564199};
var targetaddress=getAddress(targetlatlng);
console.log(targetaddress);


function checklocation(position){
var latitude=position.coords.latitude;
var longitude=position.coords.longitude;
var currentlatlng={lat:latitude,lng:longitude};

var currentaddress=getAddress(currentlatlng);
console.log(currentaddress)

if(targetaddress==currentaddress){
  console.log("Reached target");
  navigator.geolocation.clearWatch(id);
}
}

function errorHandler(err) {
  if(err.code == 1) {
     alert("Error: Access is denied!");
  } else if( err.code == 2) {
     alert("Error: Position is unavailable!");
  }
}
function getLocationUpdate(){
            
  if(navigator.geolocation){
     
     // timeout at 60000 milliseconds (60 seconds)
     var options = {timeout:60000,enableHighAccuracy: true};
     geoLoc = navigator.geolocation;
     id = geoLoc.watchPosition(checklocation, errorHandler, options);
  } else {
     alert("Sorry, browser does not support geolocation!");
  }
}


function getAddress(latlng){
  
tlat=latlng.lat;
tlng=latlng.lng;
const getLocationName = async (lat,lng) => {
  try {
    const response = await axios.get(`https://maps.googleapis.com/maps/api/geocode/json?latlng=${lat},${lng}&key=AIzaSyAhsqiabZ9UAv8Lb6p6X0TcefSuakTcmg4`)
   ;
    
    if (response.data.results && response.data.results.length > 0) {
      // Return the formatted address of the first result
      return response.data.results[0].formatted_address;
    }
  } catch (error) {
    console.error('Failed to fetch location name:', error);
  }
  return '';  // Return an empty string if the location name could not be fetched
};


address=getLocationName(tlat,tlng);
return address

}














  