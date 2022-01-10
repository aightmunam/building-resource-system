const startDate = $('input[name="date-start"]');
const endDate = $('input[name="date-end"]');

var meterChartData = function (chartData) {
    return {
            datasets: [{
                label: `${chartData.label.resource} Consumption (${chartData.label.unit})`,
                data: chartData.readings,
                borderWidth: 3,
                radius: 2,
                borderColor: "#c45850",
                backgroundColor: "#c45850"
            }]
    };
};

readingChart(
    'meter-chart-canvas',
    'line',
    startDate,
    endDate,
    $('#meter-chart').data('url'),
    meterChartData
);
