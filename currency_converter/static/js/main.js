// API website : https://www.exchangerate-api.com/docs/overview

// Variable declaration
const c1 = document.getElementById("from_currency");
const c2 = document.getElementById("target_currency");
const amount1 = document.getElementById("from_price");
const amount2 = document.getElementById("target_price");
const swap = document.getElementById("swap");
const theRate = document.getElementById("rate");
// Fetch exchange rate from the API
function calculate() {
  console.log("called calculate()");
  const curr1 = c1.value;
  const curr2 = c2.value;
  fetch(
    `https://v6.exchangerate-api.com/v6/07c7436812f210f455d48d84/latest/${curr1}`
  )
    .then((res) => res.json())
    .then((data) => {
      // console.log(data);
      // Updating the data
      const rate = data.conversion_rates[curr2];
      theRate.innerText = `1 ${curr1} = ${rate} ${curr2}`;
      amount2.value = (amount1.value * rate).toFixed(2);
    });
    console.log(amount1.value + " " + amount2.value)
}

// Event  Listeners
c1.addEventListener("change", calculate);
amount1.addEventListener("input", calculate);
c2.addEventListener("change", calculate);
amount2.addEventListener("input", calculate);