const startDate = $('input[name="date-start"]');
const endDate = $('input[name="date-end"]');

var buildingReadingChartData = function (chartData) {
    return {
            datasets: [{
                label: 'Electricity Consumption (kWh)',
                data: chartData.electricity,
                radius: 1.5,
                borderWidth: 1.5,
                borderColor: "#FF5959",
            }, {
                label: 'Water Consumption (m3)',
                data: chartData.water,
                radius: 1.5,
                borderWidth: 1.5,
                borderColor: "#1C6DD0",
            }, {
                label: 'Natural Gas Consumption (kWh)',
                data: chartData.natural_gas,
                radius: 1.5,
                borderWidth: 1.5,
                borderColor: "#A3E4DB",
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
