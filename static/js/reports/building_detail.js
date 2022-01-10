const startDate = $('input[name="date-start"]');
const endDate = $('input[name="date-end"]');

var buildingReadingChartData = function (chartData) {
    return {
            datasets: [{
                label: 'Electricity Consumption (kWh)',
                data: chartData.electricity,
                radius: 3,
                borderWidth: 3,
                fill: 'origin',
                borderColor: "#FF5959",
                backgroundColor: "rgba(255,89,89,0.2)"
            }, {
                label: 'Water Consumption (m3)',
                data: chartData.water,
                radius: 3,
                borderWidth: 3,
                fill: 'origin',
                borderColor: "#1C6DD0",
                backgroundColor: "rgba(28,109,208,0.2)"
            }, {
                label: 'Natural Gas Consumption (kWh)',
                data: chartData.natural_gas,
                radius: 3,
                borderWidth: 3,
                fill: 'origin',
                borderColor: "#A3E4DB",
                backgroundColor: "rgba(163,228,219,0.2)"
            }]
    };
};

readingChart(
    'building-chart-canvas',
    'line',
    startDate,
    endDate,
    $('#building-chart').data('url'),
    buildingReadingChartData
);
