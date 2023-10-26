<template>
	<header>
		<!-- nav -->
		<NavBar />
	</header>

<!--showcase-->
<section class="text-center col-12 m-0 p-0" style="background-color: rgb(209, 244, 209); margin: 0; padding: 0;">
  <div class="container" style="max-width: 100%; padding: 0;">
    <h1>Plan-It!</h1>
  </div>
</section>


<!--flexbox thingy!-->
<section class="text-muted p-5 text-center">
  <div class="container">
    <div class="d-sm-flex align-items-center justify-content-center"> <!-- Center vertically and horizontally -->
      <div class="text-center">
        <h1><span class="text-success">Carbon-First </span> Routing.</h1>
        <p class="lead">
          Account for your own carbon footprint for your traffic taken, value-add and commit to reducing your carbon footprint and reduce your personal impact.
        </p>
        <h3 v-if="isAuthenticated" class="mt-3">Hi, {{ user.name }}!</h3> <!-- Display the user's name if authenticated -->
      </div>
      <div class="text-center"> <!-- Center the image horizontally -->
        <img class="img-fluid" src="@/assets/homepage/co2.jpg" alt="">
      </div>
    </div>
  </div>
</section>


  <!-- boxes-->
 <section class="p-5">
  <div class="container">
    <div class="row text-center">
      <div class="col-md" v-for="(card, index) in cards" :key="index">
        <div class="card text-muted h-100">
          <div class="card-body d-flex flex-column justify-content-between">
            <div class="text-center">
              <div class="h1 mb-3">
                <font-awesome-icon :icon="card.icon"></font-awesome-icon>
              </div>
              <h3 class="card-title mb-3">{{ card.title }}</h3>
              <p class="card-text">{{ card.description }}</p>
              <p class="card-details" v-show="card.showDetails">{{ card.details }}</p>
            </div>
            <button class="btn btn-success" @click="toggleDetails(index)">
              {{ card.showDetails ? "Show Less" : "Learn More" }}
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

	<!-- refer friend now-->
	<section class="bg-success text-light">
		<div class="container">
			<div class="d-md-flex justify-content-between align-items-center mb-3 mb-md-0">
				<h4 class="news-input">Refer a friend now!</h4> <!-- Apply the "news-input" class -->
				<div class="input-group news-input">
					<input type="text" class="form-control news-input" placeholder="Friend's Email Address" aria-label="Friend's Email Address" aria-describedby="button-addon2">
					<button class="btn btn-lg" id="button-addon2">Send</button>
				</div>
			</div>
		</div>
	</section>

    <!-- Question Accordion -->
	<section id = "questions" class = "p-5">
	<div class = "container">
		<h2 class = "text-center mb-4">Frequently Asked Questions</h2>
		<div class="accordion accordion-flush" id="questions">
	<!--Item 1-->
  <div class="accordion-item">
    <h2 class="accordion-header">
      <button 
	  class="accordion-button collapsed" 
	  type="button" 
	  data-bs-toggle="collapse" 
	  data-bs-target="#question-one">
        Q1
      </button>
    </h2>
    <div id="question-one" class="accordion-collapse collapse" data-bs-parent="#questions">
      <div class="accordion-body">Add answers later</div>
    </div>
  </div>
	<!--Item 2-->
	<div class="accordion-item">
    <h2 class="accordion-header">
      <button 
	  class="accordion-button collapsed" 
	  type="button" 
	  data-bs-toggle="collapse" 
	  data-bs-target="#question-two">
        Q2
      </button>
    </h2>
    <div id="question-two" class="accordion-collapse collapse" data-bs-parent="#questions">
      <div class="accordion-body">Add answers later</div>
    </div>
  </div>
  	<!--Item 3-->
	  <div class="accordion-item">
    <h2 class="accordion-header">
      <button 
	  class="accordion-button collapsed" 
	  type="button" 
	  data-bs-toggle="collapse" 
	  data-bs-target="#question-three">
        Q3
      </button>
    </h2>
    <div id="question-three" class="accordion-collapse collapse" data-bs-parent="#questions">
      <div class="accordion-body">Add answers later</div>
    </div>
  </div>
</div>
</div>
</section>

<footer class="p-5 text-center position-relative" style="background-color: rgb(209, 244, 209);">
  <!-- footer -->
  <div class="container">
    <p class="lead">Copyright &copy; 2023 wad2winners</p>
    <a href="#" class="position-absolute bottom-0 end-0 p-5 text-center">
      <i class="bi bi-arrow-up-circle h1 text-success" style="background-color: transparent;"></i>
    </a>
  </div>
</footer>

</template>
  
<script>
import NavBar from '../components/Navbar.vue';
import { useAuth0 } from '@auth0/auth0-vue';

export default {
  name: 'Home',
  components: {
    NavBar,
  },
  setup() {
    const { loginWithRedirect, user, isAuthenticated } = useAuth0();

    return {
      login: async () => {
        try {
          await loginWithRedirect();
        } catch (e) {
          alert('Failed to login');
          console.error('Failed to login:', e);
        }
      },
      cards: [
        {
          icon: "fa-solid fa-leaf",
          title: "Eco-friendly Navigation",
          description: "this is so great and green! change writeup at the end.",
          details: "Additional details about Eco-friendly Navigation.",
          showDetails: false,
        },
        {
          icon: "fa-solid fa-shoe-prints",
          title: "Traffic Optimization",
          description: "This reduces our carbon footprint.",
          details: "Additional details about Traffic Optimization.",
          showDetails: false,
        },
        {
          icon: "fa-solid fa-bus",
          title: "Incentivising Public Transport",
          description: "Encourages more people to take public transport through badges.",
          details: "Additional details about Incentivising Public Transport.",
          showDetails: false,
        },
      ],
      toggleDetails(index) {
        this.cards[index].showDetails = !this.cards[index].showDetails;
      },
    };
  },
};
</script>

<style scoped>
/* Other component-specific styles */

.news-input {
  width: 50%;
  /* Set the width to 50% */
}

/* Additional styles if needed */
</style>
