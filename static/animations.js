// Restart invalid animations on reload
document.querySelectorAll(".invalid").forEach(input => {
  input.style.animation = "none";
  input.offsetHeight;
  input.style.animation = null;
});
function closeModal() {
  const errorState = document.getElementById("errorState");
  if (errorState) {
    errorState.remove();
  }
}
