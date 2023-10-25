<template>
  <header>
    <!-- nav -->
    <NavBar />
  </header>
  <!-- <AddFriends :user="user" /> -->
  <svg id="mySvg" width="800" height="600"></svg>


  <footer>
    <!-- footer -->
  </footer>
</template>
<script>
import NavBar from "../components/Navbar.vue";
import AddFriends from "../components/AddFriends.vue";
import { useAuth0 } from "@auth0/auth0-vue";
import * as d3 from "d3";


export default {
  name: "Home",
  components: {
    NavBar,
    AddFriends,
  },
  setup() {
    const { loginWithRedirect, user, isAuthenticated } = useAuth0();

    console.log("Setup method is called");
    console.log("user is here", user);




    return {
      login: async () => {
        console.log("Login button clicked");
        try {
          await loginWithRedirect();
          // console.log('User:', user);
          // console.log('Authenticated:', isAuthenticated);
        } catch (e) {
          alert("Failed to login");
          console.error("Failed to login:", e);
        }
      },
      user,
      isAuthenticated,
    };
  },
  mounted() {
    const routesData = [{
      "_id": {
        "$oid": "653913688f5ad5e4f064762f"
      },
      "route_id": "route_1698239336195",
      "start_point_lat_lng": "Point(1.3544924, 103.9886015)",
      "end_point_lat_lng": "Point(1.3397443, 103.7067297)",
      "start_point_name": "Singapore Changi Airport (SIN), Singapore",
      "end_point_name": "11 Jurong West Central 2, Singapore",
      "transport_mode": "DRIVE",
      "carbon_emission": 4.66176,
      "timestamp": {
        "$date": "2023-10-25T21:08:56.498Z"
      },
      "user_id": "brian@bchewy.com"
    }]


    const svg = d3.select("#mySvg");
    const projection = d3.geoMercator()
      .center([103.8, 1.35])
      .scale(100000);

    routesData.forEach(route => {
      const startCoordinates = extractCoordinates(route.start_point_lat_lng);
      const endCoordinates = extractCoordinates(route.end_point_lat_lng);

      const start = projection([startCoordinates.lng, startCoordinates.lat]);
      const end = projection([endCoordinates.lng, endCoordinates.lat]);

      svg.append("circle")
        .attr("cx", start[0])
        .attr("cy", start[1])
        .attr("r", 5)
        .attr("fill", "blue");

      svg.append("circle")
        .attr("cx", end[0])
        .attr("cy", end[1])
        .attr("r", 5)
        .attr("fill", "red");

      svg.append("line")
        .attr("x1", start[0])
        .attr("y1", start[1])
        .attr("x2", end[0])
        .attr("y2", end[1])
        .attr("stroke", "black");
    });

    function extractCoordinates(pointString) {
      const match = pointString.match(/Point\(([^,]+), ([^\)]+)\)/);
      if (match) {
        console.log(parseFloat(match[1]))
        console.log(parseFloat(match[2]))
        return {
          lat: parseFloat(match[1]),
          lng: parseFloat(match[2])
        };
      }
      return null;
    }
  },
};
</script>
