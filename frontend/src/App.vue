<script setup>
import { ref, computed } from 'vue'
import Loader from './components/Loader.vue';
const document = ref('')
const summary = ref('')
const isActive = ref(false)
async function summarize() {
  isActive.value = true
  const data = {
    document: document.value
  }
  let result = await fetch("http://localhost:5000/sum", {
    method: "POST",
    body: JSON.stringify(data),
    headers: {
      "Content-type": "application/json; charset=UTF-8"
    }
  },
  );
  if (!result.ok) {
    console.log(`Error code: ${result.status}`);
    let sum = await result.json();
    console.log(sum['error']);
    isActive.value = false
    return
  }
  let sum = await result.json();
  console.log(sum['summary']);
  summary.value = sum['summary']
  isActive.value = false
  // summary.value = JSON.parse(result)['summary']
}

function clearData() {
  document.value = ''
  summary.value = ''
}

const wordCount = computed(() => {
  let str = document.value.replace(/\s+/g, " ");
  str = str.trim()
  if (str === "") {
    return 0
  }
  let wordCount = str.split(" ").length;
  return wordCount
})

function formatData() {
  document.value = document.value.replace(/\n/g, " ").replace(/\s+/g, " ");
}
</script>

<template>
  <Loader :is-active="isActive"></Loader>
  <h1>Text summarization with BART</h1>
  <div class="container">
    <div class="row">
      <div class="col-md-6">
        <div class="table-header">
          <label for="document">Document</label>
        </div>
        <textarea v-model="document" class="form-control" name="document" id="document" rows="20" cols="1000"></textarea>
        <div>{{ wordCount }}/500</div>
        <div class="d-flex justify-content-between m-1">
          <button type="button" class="btn btn-danger" @click="clearData">
            Clear
          </button>
          <button type="button" class="btn btn-success" @click="summarize">
            Summarize
          </button>
        </div>
      </div>
      <div class="col-md-6">
        <div class="table-header">
          <label for="summary">Summary</label>
        </div>
        <textarea v-model="summary" class="form-control" name="summary" id="summary" rows="20" cols="1000"></textarea>
      </div>
    </div>
  </div>
</template>

<style scoped>
h1 {
  text-align: center;
  margin-bottom: 10px;
}

.table-header {
  text-align: center;
  font-size: large;
  font-weight: bold;
}

textarea {
  max-width: 100%;
  padding: 10px;
}
</style>
