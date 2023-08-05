(function () {

    const FieldType = Object.freeze({
        SITE: 'site',
        REGION: 'region',
        MANUFACTURER: 'manufacturer_display',
        DEVICE_TYPE: 'device_type',
        DEVICE_ROLE: 'device_role',
        DEVICE_MODEL: 'device_model'
    })

    const getFieldId = (fieldType) => {
        if (fieldType === FieldType.MANUFACTURER) {
            return `${fieldType.split("_")[0]}_id`;
        } else if (fieldType === FieldType.DEVICE_MODEL) {
            return fieldType
        } else {
            return `${fieldType}_id`;
        }
    }

    const charPrototype = {
        getFieldValue() {
            return this.fieldValue;
        },
        getTitle() {
            return `EoL Status By ${this.title}`;
        }
    };

    function Chart(fieldValue, title) {
        this.fieldValue = fieldValue;
        this.title = title;
    }

    Object.assign(Chart.prototype, charPrototype);

    const site = new Chart(FieldType.SITE, "Site");
    const region = new Chart(FieldType.REGION, "Region");
    const manufacturer = new Chart(FieldType.MANUFACTURER, "Manufacturer");
    const deviceType = new Chart(FieldType.DEVICE_TYPE, "Device Type");
    const device_role = new Chart(FieldType.DEVICE_ROLE, "Device Role");
    const device_model = new Chart(FieldType.DEVICE_MODEL, "Device Model");

    const charts = [
        site,
        region,
        manufacturer,
        deviceType,
        device_role,
        device_model
    ]

    const fetchHardware = async () => {
        const objList = document.querySelector("#charts-list");
        const devApiUrl = objList.dataset.devapiurl;
        const moduleApiUrl = objList.dataset.moduleapiurl;
        const inventoryApiUrl = objList.dataset.inventoryapiurl;
        const objs = await Promise.all([
            fetch(devApiUrl).then(r => r.json()),
            fetch(moduleApiUrl).then(r => r.json()),
            fetch(inventoryApiUrl).then(r => r.json())
        ]
        ).then(res => {
            return res[0].concat(res[1].concat(res[2]))
        }).catch(err => console.error(err))

        return objs
    }

    const groupResults = (chartObj, results) => {
        let groupBy = {}
        results.forEach(e => {
            const fieldName = chartObj.getFieldValue();
            let fieldValue = e[fieldName];
            if (fieldValue in groupBy) {
                groupBy[fieldValue] = {
                    eol_maintanance_days: groupBy[fieldValue]["eol_maintanance_days"] + e.eol_maintanance_days,
                    eol_vulnerability_days: groupBy[fieldValue]["eol_vulnerability_days"] + e.eol_vulnerability_days,
                    eol_anncouncement_days: groupBy[fieldValue]["eol_anncouncement_days"] + e.eol_anncouncement_days,
                    eol_support_days: groupBy[fieldValue]["eol_support_days"] + e.eol_support_days,
                    count: groupBy[fieldValue]["count"] + 1,
                    fieldId: e[getFieldId(fieldName)]
                }
            } else {
                groupBy[fieldValue] = {
                    eol_maintanance_days: e.eol_maintanance_days,
                    eol_vulnerability_days: e.eol_vulnerability_days,
                    eol_anncouncement_days: e.eol_anncouncement_days,
                    eol_support_days: e.eol_support_days,
                    count: 1,
                    fieldId: e[getFieldId(fieldName)]
                }
            }
        });
        return groupBy;
    }
    const chartEl = document.getElementById("charts-list");
    const loading = document.createElement("div");
    loading.innerText = "Loading...";
    chartEl.appendChild(loading);

    fetchHardware().then(res => {
        const groups = charts.map(e => ({ type: e.getFieldValue(), results: groupResults(e, res), title: e.getTitle() }))
        const chartEl = document.getElementById("charts-list");

        groups.forEach(e => JSON.stringify(e))


        groups.forEach(chartObj => {

            const newChart = document.createElement("div");
            const newInnerChart = document.createElement("div");

            newChart.classList.add("col", "col-12", "col-md-6", "col-xl-4")
            newInnerChart.classList.add("card")
            newChart.appendChild(newInnerChart);
            newChart.id = `${chartObj.type}-chart`
            chartEl.appendChild(newChart)

            categories = []
            idMap = {}
            eol_maintanance_days = []
            eol_vulnerability_days = []
            eol_anncouncement_days = []
            eol_support_days = []
            const dataSource = chartObj.results;

            for (let key in dataSource) {
                categories.push(key);
                idMap[key] = dataSource[key].fieldId
                const count = dataSource[key].count
                const avgFunc = (value) => (Math.round(value / count * 100) / 100)

                eol_maintanance_days.push(avgFunc(dataSource[key]["eol_maintanance_days"]));
                eol_vulnerability_days.push(avgFunc(dataSource[key]["eol_vulnerability_days"]));
                eol_anncouncement_days.push(avgFunc(dataSource[key]["eol_anncouncement_days"]));
                eol_support_days.push(avgFunc(dataSource[key]["eol_support_days"]));
            }
            const title = chartObj.title;

            options = {
                series: [{
                    name: 'Avg. EoL Maintanance',
                    data: eol_maintanance_days
                },
                {
                    name: 'Avg. EoL Vulnerability',
                    data: eol_vulnerability_days
                },
                {
                    name: 'Avg. EoL Anncouncement',
                    data: eol_anncouncement_days
                },
                {
                    name: 'Avg. EoL Support',
                    data: eol_support_days
                },

                ],
                chart: {
                    type: 'bar',
                    height: 350,
                    events: {
                        click: function (event, chartContext, config) {
                            const categories = config.config.xaxis.categories;
                            const category = categories[config.dataPointIndex];
                            const categoryId = config.config.metadata.mapping[category]
                            const type = config.config.metadata.type
                            if(type && categoryId) {
                                const tmp = window.location.href.split('?')[0]

                                window.location.href = tmp + `?${type}=${categoryId}`;
                            }
                        }
                    }
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
                    categories: categories
                },
                yaxis: {
                    title: {
                        text: 'Days'
                    }
                },
                fill: {
                    opacity: 1
                },
                tooltip: {
                    y: {
                        formatter: function (val) {
                            return val + " days"
                        }
                    }
                },
                title: {
                    text: title,
                    align: 'center',
                    margin: 10,
                    offsetX: 0,
                    offsetY: 10,
                    floating: false,
                    style: {
                        fontSize: '14px',
                        fontWeight: 'bold',
                        fontFamily: undefined,
                        color: '#263238'
                    },
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
                },
                metadata: {
                    mapping: idMap,
                    type: getFieldId(chartObj.type)
                }
            }

            var chart = new ApexCharts(newInnerChart, options);
            chart.render();
        })

    }).catch(err => {
        const childEl = document.createElement('p');
        childEl.textContent = "Failed during loading the charts";
        console.error(err);
    }).finally(() => {
        chartEl.removeChild(loading);

    })

})()