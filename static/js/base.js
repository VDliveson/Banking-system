var form
const checkbox = document.getElementById("checkbox")
checkbox.addEventListener("change", () => {
  document.body.classList.toggle("dark")
  form=document.getElementsByClassName('reset-form')[0]
  form.classList.toggle("dark")
  card_footer=document.getElementsByClassName('card-footer')[0]
  card_footer.classList.toggle("dark")
})