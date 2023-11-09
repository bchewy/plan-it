<template>
  <header>
    <!-- nav -->
    <NavBar />
  </header>
  <div class="container-fluid p-0">


    <section class=" section-background text-light text-center vh-100 d-flex align-items-center justify-content-center" >
      <div class="container">
        <div class="d-sm-flex align-items-center justify-content-center"> <!-- Center vertically and horizontally -->
          <div class="text-center">
            <h1><span class="text-supergreen element"></span></h1>
            <p class="lead">
              Account for your own carbon footprint for your traffic taken, <br>value-add and commit to reducing your carbon footprint <br>and reduce your personal impact.
            </p>
          </div>
        </div>
      </div>
      <!--/div-->
    </section>
    <!-- </Parallaxy> -->

    <!-- boxes-->
    <section class="h-25 bg-brown pt-5" >
      <div class="container">
        <div class="row text-center">
          <div class="col-md" v-for="(card, index) in cards" :key="index">
            <div class="card h-100 beige-colour">
              <div class="card-body d-flex flex-column justify-content-between">
                <div class="text-center">
                  <div class="h1 mb-3">
                    <font-awesome-icon :icon="card.icon"></font-awesome-icon>
                  </div>
                  <h3 class="card-title mb-3 ">{{ card.title }}</h3>
                  <p class="card-text text-muted">{{ card.description }}</p>
                  <!-- "Learn More" button for each card -->
                  <button class="btn btn-success" @click="openModal(index)">Learn More</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    

    <!-- "Learn More" modal -->
    <LearnMore :visible="currentCardIndex !== -1" :card="currentCardIndex !== -1 ? cards[currentCardIndex] : {}" @close="closeModal" />

    <!-- <div class="bg-supergreen" style="height: 50px;"></div> Adjust the height as needed -->

    
    


    <!-- Question Accordion -->
    
      <div class="container" style="margin-top: 100px;">
       
        <div class="accordion accordion-flush " id="questions">
          <div class="accordion-item ">
            <h3 class="accordion-header text-center beige-colour py-2">
              
                <b>Frequently Asked Questions</b>
            
            </h3>
            
          </div>
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


    <!-- refer friend now-->
    <!-- <section class="text-muted bg-supergreen">
      <div class="container">
        <div class="d-md-flex justify-content-between align-items-center mb-3 mb-md-0">
          <h4 class="news-input">Refer a friend now!</h4>
          <div class="input-group news-input">
            <input type="text" class="form-control news-input" placeholder="Friend's Email Address" aria-label="Friend's Email Address" aria-describedby="button-addon2">
            <button class="btn btn-lg beige-colour" id="button-addon2">Send</button>
          </div>
        </div>
      </div>
    </section> -->

    <!-- Add space between "Refer a friend" section and footer -->

    <!-- Footer -->
    <!-- <Footer /> -->
  </div>
</template>

<script>
import NavBar from '../components/Navbar.vue';
import { useAuth0 } from '@auth0/auth0-vue';
import LearnMore from '../components/LearnMore.vue';
import { ref } from 'vue';
import Typed from 'typed.js';
import Footer from '../components/Footer.vue'
// import Parallaxy from '@lucien144/vue3-parallaxy';


export default {
  name: 'Home',
  data() {
    return {
      isTypedInitialized: false

    };
  },
  components: {
    NavBar,
    LearnMore,
    Footer,
  },
  mounted() {
    const element = document.querySelector('.element');
    const cursors = document.querySelectorAll('.typed-cursor');
    cursors.forEach(cursor => cursor.remove());  // Remove existing cursors

    if (!this.isTypedInitialized) {
      new Typed(element, {
        strings: ["Carbon-First Routing.", "Take the green route.", "Your footprint matters.", "Drive less, save more."],
        typeSpeed: 50,
        backSpeed: 50,
        loop: true
      });
      this.isTypedInitialized = true;
    }
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

.text-supergreen {
  color: #a7c957;
}

.light-green {
  background-color: #d1f4d1
}

.h-25.bg-brown.pt-5 {
  position: relative;
}
.h-25.bg-brown.pt-5::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  min-height: 50em;
  background-image: url('https://bchewy-images.s3.ap-southeast-1.amazonaws.com/plan-it/Brown+pathway.jpg');
  background-size: cover;
  opacity: 0.7; /* Adjust this to your liking */
  z-index: -1;

}
.section-background {
  position: relative;
}

.section-background::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url('https://bchewy-images.s3.ap-southeast-1.amazonaws.com/planit.png');
  background-size: cover;
  opacity: 0.9; /* Adjust this to your liking */
  z-index: -1;
}


/* Additional styles if needed */
</style>
