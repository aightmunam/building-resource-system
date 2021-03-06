var readingChart = function (canvasId, chartType, startDate, endDate, url, configChartData) {
    var CSRFToken = $('[name="csrfmiddlewaretoken"]').val();

    const ctx = document.getElementById(canvasId).getContext('2d');

    const startDatepicker = flatpickr(startDate, {});
    const endDatepicker = flatpickr(endDate, {});


    function sendGraphDataRequest() {
        var requestUrl = `${url}?start=${encodeURIComponent(startDatepicker.input.value) || ''}&end=${encodeURIComponent(endDatepicker.input.value) || ''}`;

        $.ajax({
            url: requestUrl,
            headers: {'X-CSRFToken': CSRFToken},
            type: 'GET',

            success: function (response) {
                renderGraph(JSON.parse(response));
            }
        });
    }

    function renderGraph(chartData) {
        let chartStatus = Chart.getChart(canvasId);
        if (chartStatus != undefined) {
            chartStatus.destroy();
        }
        const readingChart = new Chart(ctx, {
            type: chartType,
            data: configChartData(chartData),
            options: {
                responsive: true,
                scales: {
                    y: {
                        title: {
                            display: true,
                            text: 'Value'
                        },
                        beginAtZero: true,
                    },
                    x: {
                        title: {
                            display: true,
                            text: 'Reading Timestamp'
                        },
                    }
                }
            }
        });
    }

    $(startDate).on('change', function () {
        sendGraphDataRequest();
    });


    $(endDate).on('change', function () {
        sendGraphDataRequest();
    });

};


