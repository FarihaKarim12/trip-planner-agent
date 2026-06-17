<<<<<<< HEAD
const API_BASE = "";

const LOADING_STEPS = [
  "Initializing travel agent…",
  "Running BFS to explore all itinerary combinations…",
  "Applying CSP constraints to prune invalid paths…",
  "Running Greedy Best-First Search with heuristic…",
  "Selecting optimal itinerary…",
  "Generating AI travel plan…",
];

let loadingInterval = null;
let loadingStepIndex = 0;

document.addEventListener("DOMContentLoaded", () => {
  loadDestinations();
  // Fix: use .chip class (not .interest-chip)
  document.querySelectorAll(".chip").forEach(chip => {
    chip.addEventListener("click", () => {
      chip.classList.toggle("active");
    });
  });
});

async function loadDestinations() {
  try {
    const res = await fetch(`${API_BASE}/destinations`);
    const data = await res.json();
    const select = document.getElementById("destination");
    data.destinations.forEach(dest => {
      const opt = document.createElement("option");
      opt.value = dest;
      opt.textContent = dest;
      select.appendChild(opt);
    });
  } catch (e) {
    const demo = ["Paris", "Tokyo", "New York", "Dubai", "Istanbul"];
    const select = document.getElementById("destination");
    demo.forEach(dest => {
      const opt = document.createElement("option");
      opt.value = dest;
      opt.textContent = dest;
      select.appendChild(opt);
    });
  }
}

function getSelectedInterests() {
  return Array.from(document.querySelectorAll(".chip.active"))
    .map(c => c.dataset.value);
}

async function generatePlan() {
  const destination = document.getElementById("destination").value;
  const num_days    = parseInt(document.getElementById("num_days").value);
  const budget      = parseFloat(document.getElementById("budget").value);
  const interests   = getSelectedInterests();

  const errorEl = document.getElementById("error-msg");
  errorEl.classList.add("hidden");

  if (!destination) { showError("Please select a destination."); return; }
  if (!num_days || num_days < 1 || num_days > 14) { showError("Number of days must be between 1 and 14."); return; }
  if (!budget || budget < 50) { showError("Please enter a budget of at least $50."); return; }

  document.getElementById("results").classList.add("hidden");
  document.getElementById("loading").classList.remove("hidden");
  startLoadingAnimation();

  const btn = document.getElementById("generate-btn");
  btn.disabled = true;

  try {
    const response = await fetch(`${API_BASE}/plan`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ destination, num_days, budget, interests }),
    });
    const data = await response.json();
    stopLoadingAnimation();
    document.getElementById("loading").classList.add("hidden");

    if (data.success) {
      renderResults(data, destination, num_days, budget);
    } else {
      showError(data.error || "Something went wrong.");
    }
  } catch (err) {
    stopLoadingAnimation();
    document.getElementById("loading").classList.add("hidden");
    showError("Could not connect to the backend. Make sure Flask is running on port 5000.");
  } finally {
    btn.disabled = false;
  }
}

function startLoadingAnimation() {
  loadingStepIndex = 0;
  const el = document.getElementById("loading-step");
  el.textContent = LOADING_STEPS[0];
  loadingInterval = setInterval(() => {
    loadingStepIndex = (loadingStepIndex + 1) % LOADING_STEPS.length;
    el.style.opacity = "0";
    setTimeout(() => {
      el.textContent = LOADING_STEPS[loadingStepIndex];
      el.style.transition = "opacity 0.4s";
      el.style.opacity = "1";
    }, 200);
  }, 1600);
}

function stopLoadingAnimation() {
  if (loadingInterval) { clearInterval(loadingInterval); loadingInterval = null; }
}

function renderResults(data, destination, num_days, budget) {
  // Only show destination, duration, total cost — NO algorithm
  document.getElementById("sum-dest").textContent = destination;
  document.getElementById("sum-days").textContent = `${data.summary.days} days`;
  document.getElementById("sum-cost").textContent = `$${data.summary.total_cost} / $${Math.round(budget)}`;

  // Show AI text only
  document.getElementById("ai-output").textContent = data.travel_plan;

  document.getElementById("results").classList.remove("hidden");
  document.getElementById("results").scrollIntoView({ behavior: "smooth", block: "start" });
}

function showError(msg) {
  const el = document.getElementById("error-msg");
  el.textContent = `⚠ ${msg}`;
  el.classList.remove("hidden");
  el.scrollIntoView({ behavior: "smooth", block: "nearest" });
}

function resetForm() {
  document.getElementById("results").classList.add("hidden");
  document.getElementById("error-msg").classList.add("hidden");
  document.querySelectorAll(".chip").forEach(c => c.classList.remove("active"));
  document.getElementById("destination").value = "";
  document.getElementById("num_days").value = 3;
  document.getElementById("budget").value = 500;
  window.scrollTo({ top: 0, behavior: "smooth" });
=======
const API_BASE = "";

const LOADING_STEPS = [
  "Initializing travel agent…",
  "Running BFS to explore all itinerary combinations…",
  "Applying CSP constraints to prune invalid paths…",
  "Running Greedy Best-First Search with heuristic…",
  "Selecting optimal itinerary…",
  "Generating AI travel plan…",
];

let loadingInterval = null;
let loadingStepIndex = 0;

document.addEventListener("DOMContentLoaded", () => {
  loadDestinations();
  // Fix: use .chip class (not .interest-chip)
  document.querySelectorAll(".chip").forEach(chip => {
    chip.addEventListener("click", () => {
      chip.classList.toggle("active");
    });
  });
});

async function loadDestinations() {
  try {
    const res = await fetch(`${API_BASE}/destinations`);
    const data = await res.json();
    const select = document.getElementById("destination");
    data.destinations.forEach(dest => {
      const opt = document.createElement("option");
      opt.value = dest;
      opt.textContent = dest;
      select.appendChild(opt);
    });
  } catch (e) {
    const demo = ["Paris", "Tokyo", "New York", "Dubai", "Istanbul"];
    const select = document.getElementById("destination");
    demo.forEach(dest => {
      const opt = document.createElement("option");
      opt.value = dest;
      opt.textContent = dest;
      select.appendChild(opt);
    });
  }
}

function getSelectedInterests() {
  return Array.from(document.querySelectorAll(".chip.active"))
    .map(c => c.dataset.value);
}

async function generatePlan() {
  const destination = document.getElementById("destination").value;
  const num_days    = parseInt(document.getElementById("num_days").value);
  const budget      = parseFloat(document.getElementById("budget").value);
  const interests   = getSelectedInterests();

  const errorEl = document.getElementById("error-msg");
  errorEl.classList.add("hidden");

  if (!destination) { showError("Please select a destination."); return; }
  if (!num_days || num_days < 1 || num_days > 14) { showError("Number of days must be between 1 and 14."); return; }
  if (!budget || budget < 50) { showError("Please enter a budget of at least $50."); return; }

  document.getElementById("results").classList.add("hidden");
  document.getElementById("loading").classList.remove("hidden");
  startLoadingAnimation();

  const btn = document.getElementById("generate-btn");
  btn.disabled = true;

  try {
    const response = await fetch(`${API_BASE}/plan`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ destination, num_days, budget, interests }),
    });
    const data = await response.json();
    stopLoadingAnimation();
    document.getElementById("loading").classList.add("hidden");

    if (data.success) {
      renderResults(data, destination, num_days, budget);
    } else {
      showError(data.error || "Something went wrong.");
    }
  } catch (err) {
    stopLoadingAnimation();
    document.getElementById("loading").classList.add("hidden");
    showError("Could not connect to the backend. Make sure Flask is running on port 5000.");
  } finally {
    btn.disabled = false;
  }
}

function startLoadingAnimation() {
  loadingStepIndex = 0;
  const el = document.getElementById("loading-step");
  el.textContent = LOADING_STEPS[0];
  loadingInterval = setInterval(() => {
    loadingStepIndex = (loadingStepIndex + 1) % LOADING_STEPS.length;
    el.style.opacity = "0";
    setTimeout(() => {
      el.textContent = LOADING_STEPS[loadingStepIndex];
      el.style.transition = "opacity 0.4s";
      el.style.opacity = "1";
    }, 200);
  }, 1600);
}

function stopLoadingAnimation() {
  if (loadingInterval) { clearInterval(loadingInterval); loadingInterval = null; }
}

function renderResults(data, destination, num_days, budget) {
  // Only show destination, duration, total cost — NO algorithm
  document.getElementById("sum-dest").textContent = destination;
  document.getElementById("sum-days").textContent = `${data.summary.days} days`;
  document.getElementById("sum-cost").textContent = `$${data.summary.total_cost} / $${Math.round(budget)}`;

  // Show AI text only
  document.getElementById("ai-output").textContent = data.travel_plan;

  document.getElementById("results").classList.remove("hidden");
  document.getElementById("results").scrollIntoView({ behavior: "smooth", block: "start" });
}

function showError(msg) {
  const el = document.getElementById("error-msg");
  el.textContent = `⚠ ${msg}`;
  el.classList.remove("hidden");
  el.scrollIntoView({ behavior: "smooth", block: "nearest" });
}

function resetForm() {
  document.getElementById("results").classList.add("hidden");
  document.getElementById("error-msg").classList.add("hidden");
  document.querySelectorAll(".chip").forEach(c => c.classList.remove("active"));
  document.getElementById("destination").value = "";
  document.getElementById("num_days").value = 3;
  document.getElementById("budget").value = 500;
  window.scrollTo({ top: 0, behavior: "smooth" });
>>>>>>> 8589fb43ed2959927bc961d281d88a84f4bd1a8f
}