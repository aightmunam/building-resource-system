const startDate = $('input[name="date-start"]');
const endDate = $('input[name="date-end"]');

var meterChartData = function (chartData) {
    return {
            datasets: [{
                label: `${chartData.label.resource} Consumption (${chartData.label.unit})`,
                data: chartData.readings,
                radius: 1.5,
                borderWidth: 1.5,
                borderColor: "#c45850",
            }]
    };
};

readingChart(
    'meter-chart-canvas',
    'bar',
    startDate,
    endDate,
    $('#meter-chart').data('url'),
    meterChartData
);
