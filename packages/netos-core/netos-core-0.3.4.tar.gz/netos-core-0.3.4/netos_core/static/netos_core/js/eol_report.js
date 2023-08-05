(function () {
    const report = document.getElementById("report-chart");
    const deviceTypeId = report.dataset.devicetypeid;
    const devApiUrl = report.dataset.devapiurl;

    if (deviceTypeId && devApiUrl) {
        fetch(`${devApiUrl}?device_type_id=${deviceTypeId}`)
            .then(r => r.json())
            .then(r => r.results)
            .then(r => { renderChart(r[0]) })
            .catch(err => {
                renderNoData()
                console.error(err)
            })
    } else {
        console.error("Missing deviceTypeId!")
        el = document.createElement("div")
        el.textContent = "Missing device id!"
        report.appendChild(el)
    }

    const renderNoData = () => {
        el = document.createElement("div")
        el.textContent = "No Eol report available"
        report.appendChild(el)
    }

    const renderChart = (res) => {
        options = {
            series: [{
                name: "EoL report",
                data: [res.eol_maintanance_days, res.eol_vulnerability_days, res.eol_anncouncement_days, res.eol_support_days]
            },
            ],
            chart: {
                type: 'bar',
                height: 350
            },
            plotOptions: {
                bar: {
                    horizontal: false,
                    columnWidth: '55%',
                    endingShape: 'rounded'
                },
            },
            dataLabels: {
                enabled: false
            },
            stroke: {
                show: true,
                width: 2,
                colors: ['transparent']
            },
            xaxis: {
                categories: ["EoL Maintanance", "EoL Vulnerability", "EoL Anncouncement", "EoL Support"]
            },
            yaxis: {
                title: {
                    text: 'Days'
                }
            },
            fill: {
                opacity: 1,
            },
            tooltip: {
                y: {
                    formatter: function (val) {
                        return val + " days"
                    }
                }
            },
            noData: {
                text: "No Data Found",
                align: 'center',
                verticalAlign: 'middle',
                offsetX: 0,
                offsetY: 0,
                style: {
                    color: undefined,
                    fontSize: '14px',
                    fontFamily: undefined
                }
            }
        }

        const chart = new ApexCharts(report, options);
        chart.render();
    }

})()
