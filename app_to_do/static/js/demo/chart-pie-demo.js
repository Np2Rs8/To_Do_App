// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

//TODO Modificación

//const contextInc = document.getElementById("porcEstInc");
//let ProcInc = contextInc.textContent;

//alert(contextInc);

const valContextInc = document.querySelector("#porcEstInc");
let ValProcInc = parseFloat(valContextInc.textContent);

const valContextPro = document.querySelector("#porcEstPro");
let ValProcPro = parseFloat(valContextPro.textContent);

const valContextCom = document.querySelector("#porcEstCom");
let ValProcCom = parseFloat(valContextCom.textContent);

//alert(`${ValProcInc} ----- ${ValProcPro} ----- ${ValProcCom}`)

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ["Incompleto", "Proceso", "Completado"],
    datasets: [{
      data: [ValProcInc, ValProcPro, ValProcCom],
      backgroundColor: ['#e74a3b', '#f6c23e', '#1cc88a'],
      hoverBackgroundColor: ['#2e59d9', '#17a673', '#2c9faf'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});
