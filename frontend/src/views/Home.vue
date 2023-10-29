<template>
  <header>
    <!-- nav -->
    <NavBar />
  </header>

  <!--username content-->
  <section class="text-center col-12 m-0 p-0 beige-colour" style=" margin: 0; padding: 0;">
      <h2 v-if="isAuthenticated" class="text-muted" style = "padding:1%">Ready to go <span class = "text-success">green </span>, {{ user.name }}?</h2>
  </section>


  <!--flexbox thingy!-->
  <!--section class="text-muted text-center d-flex align-items-center justify-content-center"-->
  <section class="text-muted text-center vh-100 d-flex align-items-center justify-content-center bg-supergreen" style="background-image: url('@/assets/homepage/background.png'); background-size: cover;">
    <div class="container">
      <div class="d-sm-flex align-items-center justify-content-center"> <!-- Center vertically and horizontally -->
        <div class="text-center">
          <h1><span class="text-success">Carbon-First </span> Routing.</h1>
          <p class="lead">
            Account for your own carbon footprint for your traffic taken, value-add and commit to reducing your carbon footprint and reduce your personal impact.
          </p>
        </div>
        <!--div class="text-center"--> <!-- Center the image horizontally -->
        <!--img class="img-fluid" src="@/assets/homepage/co2.jpg" alt=""-->
      </div>
    </div>
    <!--/div-->
  </section>

  <!-- boxes-->
  <section class="p-5 bg-supergreen">
    <div class="container">
      <div class="row text-center">
        <div class="col-md" v-for="(card, index) in cards" :key="index">
          <div class="card text-muted h-100 beige-colour">
            <div class="card-body d-flex flex-column justify-content-between">
              <div class="text-center">
                <div class="h1 mb-3">
                  <font-awesome-icon :icon="card.icon"></font-awesome-icon>
                </div>
                <h3 class="card-title mb-3">{{ card.title }}</h3>
                <p class="card-text">{{ card.description }}</p>
                <!-- "Learn More" button for each card -->
                <button class="btn btn-success" @click="openModal(index)">Learn More</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>


  <LearnMore :visible="currentCardIndex !== -1" :card="currentCardIndex !== -1 ? cards[currentCardIndex] : {}" @close="closeModal" />

  <div class="bg-supergreen" style="height: 50px;"></div> <!-- Adjust the height as needed -->

  <!-- Question Accordion -->
  <section id="questions" class="p-5 bg-supergreen ">
    <div class="container">
      <h2 class="text-center text-muted mb-4">Frequently Asked Questions</h2>
      <div class="accordion accordion-flush " id="questions">
        <!--Item 1-->
        <div class="accordion-item ">
          <h2 class="accordion-header ">
            <button class="accordion-button collapsed beige-colour text-muted" type="button" data-bs-toggle="collapse" data-bs-target="#question-one">
             <b>1: How does your eco-friendly navigation system work?</b>
            </button>
          </h2>
          <div id="question-one" class="accordion-collapse collapse text-muted" data-bs-parent="#questions">
            <div class="accordion-body">Our eco-friendly navigation system combines advanced routing algorithms with real-time environmental data. It considers factors like traffic conditions, emissions, and more to suggest the most eco-friendly route. This reduces your carbon footprint and helps you make sustainable travel choices effortlessly.</div>
          </div>
        </div>
        <!--Item 2-->
        <div class="accordion-item">
          <h2 class="accordion-header">
            <button class="accordion-button collapsed beige-colour text-muted" type="button" data-bs-toggle="collapse" data-bs-target="#question-two">
				<b>2: What types of rewards can I earn through the Incentivising Public Transport feature?</b>
            </button>
          </h2>
          <div id="question-two" class="accordion-collapse collapse text-muted " data-bs-parent="#questions">
            <div class="accordion-body">With our Incentivising Public Transport feature, you can earn various rewards such as discounts on future journeys, eco-friendly badges, and even contributions to environmental causes. The more you choose public transport, the greater your rewards become.</div>
          </div>
        </div>
        <!--Item 3-->
        <div class="accordion-item">
          <h2 class="accordion-header">
            <button class="accordion-button collapsed beige-colour text-muted" type="button" data-bs-toggle="collapse" data-bs-target="#question-three">
			<b> 3: Can I use your platform internationally, or is it limited to specific regions?</b>
            </button>
          </h2>
          <div id="question-three" class="accordion-collapse collapse " data-bs-parent="#questions">
            <div class="accordion-body">Our eco-friendly navigation platform is currently tailored to Singapore. While we're focused on providing the best eco-friendly navigation experience in Singapore, we have plans to expand to other regions in the future. Stay tuned for updates on our international availability!</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <div class="bg-supergreen" style="height: 80px;"></div> <!-- Adjust the height as needed -->

  <!-- refer friend now-->
  <section class="text-muted bg-supergreen ">
    <div class="container">
      <div class="d-md-flex justify-content-between align-items-center mb-3 mb-md-0">
        <h4 class="news-input">Refer a friend now!</h4> <!-- Apply the "news-input" class -->
        <div class="input-group news-input">
          <input type="text" class="form-control news-input" placeholder="Friend's Email Address" aria-label="Friend's Email Address" aria-describedby="button-addon2">
          <button class="btn btn-lg beige-colour" id="button-addon2">Send</button>
        </div>
      </div>
    </div>
  </section>

  <!-- Add space between "Refer a friend" section and footer -->
  <div class="bg-supergreen" style="height: 71px;"></div> <!-- Adjust the height as needed -->

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
import LearnMore from '../components/LearnMore.vue';
import { ref } from 'vue';

export default {
  name: 'Home',
  components: {
    NavBar,
    LearnMore
  },
  setup() {
    const { loginWithRedirect, user, isAuthenticated } = useAuth0();
    const cards = [
      {
        icon: "fa-solid fa-leaf",
        title: "Eco-friendly Navigation",
        description: "Navigate with a conscience! Discover a greener way to plan your journeys.",
        details: "Experience eco-friendly navigation that goes beyond the usual routes. Our app empowers you to make sustainable choices, reduce your carbon footprint, and explore eco-conscious alternatives. Discover routes that prioritize public transport, carpooling, biking, and walking while offering insights into your environmental impact. With us, every journey is a step towards a cleaner, greener future.",
        variant: "success",
      },
      {
        icon: "fa-solid fa-shoe-prints",
        title: "Traffic Optimization",
        description: "Efficient routes, cleaner air. Optimize traffic for a greener planet.",
        details: "Traffic Optimization is about more than just getting from A to B. It's about creating a sustainable future. Our app intelligently manages traffic to minimize congestion and emissions. By prioritizing eco-friendly modes of transport and offering real-time traffic insights, we help you reduce your carbon footprint and contribute to cleaner, healthier communities. Discover the details behind our innovative traffic solutions and take a step towards a more sustainable world.",
        variant: "success",
      },
      {
        icon: "fa-solid fa-bus",
        title: "Incentivising Public Transport",
        description: "Unlock rewards while saving the environment. Embrace public transport with badges.",
        details: "Our 'Incentivising Public Transport' feature revolutionizes the way you commute. We believe that public transport should not only be convenient but also rewarding. Our badge system encourages you to choose eco-friendly options like buses, subways, and trams. Each journey you make brings you closer to earning valuable rewards, while collectively we make our cities cleaner and greener. Learn more about how we're making public transport an attractive choice for you and a better choice for the planet.",
        variant: "success",
      },
    ];

    const currentCardIndex = ref(-1); // Track the currently selected card

    const openModal = (index) => {
      currentCardIndex.value = index;
    };

    const closeModal = () => {
      currentCardIndex.value = -1;
    };

    return {
      login: async () => {
        try {
          await loginWithRedirect();
        } catch (e) {
          alert('Failed to login');
          console.error('Failed to login:', e);
        }
      },
      cards,
      currentCardIndex,
      openModal,
      closeModal,
      isAuthenticated,
      user,
    }
  },
};
</script>


<style scoped>
/* Other component-specific styles */

.news-input {
  width: 50%;
  /* Set the width to 50% */
}

.bg-supergreen {
  background-color: #739072;
}

.beige-colour {
  /* background-color: ; */
  background-color: #ECE3CE;
}

.light-green {
  background-color: rgb(209, 244, 209)
}




/* Additional styles if needed */
</style>
