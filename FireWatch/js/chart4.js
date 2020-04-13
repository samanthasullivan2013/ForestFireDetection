window.onload = function () {
            var labels = [];
            var values = [];
            var ctx = document.getElementById("chartContainer4").getContext("2d");	//The ID
            var intervalID = window.setInterval(runGetRequestAndCreateOrUpdateChart, 5000);
            var chartVariable;

            function loadValuesAndDates(data){
                labels = [];
                values = [];
                $.each(data, function (key, val) {
                    labels.push(new Date(val.date).toLocaleTimeString());
                    values.push(val.units);
                });
            }

            function runGetRequestAndCreateOrUpdateChart() {
            $(document).ready(function () {
                $.getJSON("/tempData.json", function (data) {	//Where the directory link to data file goes
                    success:
                        loadValuesAndDates(data);
                        chartVariable? updateChart(chartVariable):createChart();
                });
            });
            }


            function updateChart(chartVariable ){
                chartVariable.data.labels = labels;
                chartVariable.data.datasets[0].data = values;
                chartVariable.clear();
                chartVariable.update();
            }
            function createChart() {
                chartVariable = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: labels,
                        datasets: [{
                            label: 'Data',
                            data: values,
                            backgroundColor: "rgba(153,255,51,0.6)"
                        }]
                    },
                    options: {
                        responsive: true,
                        legend: {
                            position: 'bottom',
                        },
                        hover: {
                            mode: 'label'
                        },
                        scales: {
                            xAxes: [{
                                display: true,
                                scaleLabel: {
                                    display: true,
                                    labelString: 'Time'
                                }
                            }],
                            yAxes: [{
                                display: true,
                                ticks: {
                                    beginAtZero: true,
                                    steps: 10,
                                    stepValue: 5,
                                    min: 0
                                }
                            }]
                        },
                    }
                });
            }
        }