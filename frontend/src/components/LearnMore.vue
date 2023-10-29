<template>
    <div v-if="visible" class="modal fade show custom-modal" style="display: block;" tabindex="-1" aria-labelledby="exampleModalLabel" aria-modal="true" role="dialog">
      <div class="modal-dialog modal-lg">
        <div class="modal-content custom-modal-content" style="background-color: #ECE3CE">
          <div class="modal-header">
            <h5 class="modal-title text-muted text-center" id="exampleModalLabel">{{ card.title }}</h5>
            <button type="button" class="btn-close btn-close-green" @click="closeModal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div class="text-center">
              <div class="h1 mb-3">
                <font-awesome-icon :icon="card.icon"></font-awesome-icon>
              </div>
              <p class="text-muted">{{ card.description }}</p>
              <p class="text-muted">{{ card.details }}</p> <!-- Display the details -->
            </div>
            <button type="button" class="btn btn-success" @click="closeModal">Close</button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      visible: Boolean,
      card: Object,
    },
    methods: {
      closeModal() {
        this.$emit('close');
      },
    },
  };
  </script>
  