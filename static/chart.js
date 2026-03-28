new Chart(ctx, {
 type: 'pie',
 data: {
  labels: ['High Risk','Medium Risk','Low Risk'],
  datasets: [{
   data: [5,3,10]
  }]
 }
});