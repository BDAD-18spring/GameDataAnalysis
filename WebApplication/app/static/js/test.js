$(function () {
	var myChart = Highcharts.chart('chart2', {
	    chart: {
	    	zoomType: 'x',
	    },
	    title: {
	        text: 'Average % Gain from selling X days out'
	    },
	    xAxis: {
					type: 'datetime'
	    },
	    yAxis: {
	        title: {
	            text: '% Gain'
	        }
	    },
	    legend: {
	        enabled: false
	    },
	    series: [{
	        name: 'Days Out',
	        colorByPoint: true,
	        type: 'column',
	        data: [{
	            name: 'Day1',
	            y: {{day1}},
	            drilldown: 'Day1'
	        },
	        {
	            name: 'Day2',
	            y: {{day2}},
	            drilldown: 'Day2'
	        },
	        {
	            name: 'Day3',
	            y: {{day3}},
	            drilldown: 'Day3'
	        },
	        {
	            name: 'Day4',
	            y: {{day4}},
	            drilldown: 'Day4'
	        },
	        {
	            name: 'Day5',
	            y: {{day5}},
	            drilldown: 'Day5'
	        },
	        {
	            name: 'Day6',
	            y: {{day6}},
	            drilldown: 'Day6'
	        },
	        {
	            name: 'Day7',
	            y: {{day7}},
	            drilldown: 'Day7'
	        },
	        {
	            name: 'Day8',
	            y: {{day8}},
	            drilldown: 'Day8'
	        },
	        {
	            name: 'Day9',
	            y: {{day9}},
	            drilldown: 'Day9'
	        },
	        {
	            name: 'Day10',
	            y: {{day10}},
	            drilldown: 'Day10'
	        },
	        {
	            name: 'Day11',
	            y: {{day11}},
	            drilldown: 'Day11'
	        },
	        {
	            name: 'Day12',
	            y: {{day12}},
	            drilldown: 'Day12'
	        },
	        {
	            name: 'Day13',
	            y: {{day13}},
	            drilldown: 'Day13'
	        },
	        {
	            name: 'Day14',
	            y: {{day14}},
	            drilldown: 'Day14'
	        },
	        {
	            name: 'Day15',
	            y: {{day15}},
	            drilldown: 'Day15'
	        }
	        ]
	    }],
	    drilldown: {
	        series: [{
	            name: 'Day1',
	            id: 'Day1',
	            type: 'line',
	            lineWidth: 0,
	            marker: {
	                enabled: true,
	                radius: 2
	            },
	            states: {
	                hover: {
	                    lineWidthPlus: 0
	                    }
	             },
	            data: {{pts1}}
               }, {
	            name: 'Day2',
	            id: 'Day2',
	            type: 'line',
	            lineWidth: 0,
	            marker: {
	                enabled: true,
	                radius: 2
	            },
	            states: {
	                hover: {
	                    lineWidthPlus: 0
	                    }
	             },
	            data: {{pts2}}
               }, {
	            name: 'Day3',
	            id: 'Day3',
	            type: 'line',
	            lineWidth: 0,
	            marker: {
	                enabled: true,
	                radius: 2
	            },
	            states: {
	                hover: {
	                    lineWidthPlus: 0
	                    }
	             },
	            data: {{pts3}}
               }, {
	            name: 'Day4',
	            id: 'Day4',
	            type: 'line',
	            lineWidth: 0,
	            marker: {
	                enabled: true,
	                radius: 2
	            },
	            states: {
	                hover: {
	                    lineWidthPlus: 0
	                    }
	             },
	            data: {{pts4}}
               }, {
	            name: 'Day5',
	            id: 'Day5',
	            type: 'line',
	            lineWidth: 0,
	            marker: {
	                enabled: true,
	                radius: 2
	            },
	            states: {
	                hover: {
	                    lineWidthPlus: 0
	                    }
	             },
	            data: {{pts5}}
               }, {
	            name: 'Day6',
	            id: 'Day6',
	            type: 'line',
	            lineWidth: 0,
	            marker: {
	                enabled: true,
	                radius: 2
	            },
	            states: {
	                hover: {
	                    lineWidthPlus: 0
	                    }
	             },
	            data: {{pts6}}
               }, {
	            name: 'Day7',
	            id: 'Day7',
	            type: 'line',
	            lineWidth: 0,
	            marker: {
	                enabled: true,
	                radius: 2
	            },
	            states: {
	                hover: {
	                    lineWidthPlus: 0
	                    }
	             },
	            data: {{pts7}}
               }, {
	            name: 'Day8',
	            id: 'Day8',
	            type: 'line',
	            lineWidth: 0,
	            marker: {
	                enabled: true,
	                radius: 2
	            },
	            states: {
	                hover: {
	                    lineWidthPlus: 0
	                    }
	             },
	            data: {{pts8}}
               }, {
	            name: 'Day9',
	            id: 'Day9',
	            type: 'line',
	            lineWidth: 0,
	            marker: {
	                enabled: true,
	                radius: 2
	            },
	            states: {
	                hover: {
	                    lineWidthPlus: 0
	                    }
	             },
	            data: {{pts9}}
               }, {
	            name: 'Day10',
	            id: 'Day10',
	            type: 'line',
	            lineWidth: 0,
	            marker: {
	                enabled: true,
	                radius: 2
	            },
	            states: {
	                hover: {
	                    lineWidthPlus: 0
	                    }
	             },
	            data: {{pts10}}
               }, {
	            name: 'Day11',
	            id: 'Day11',
	            type: 'line',
	            lineWidth: 0,
	            marker: {
	                enabled: true,
	                radius: 2
	            },
	            states: {
	                hover: {
	                    lineWidthPlus: 0
	                    }
	             },
	            data: {{pts11}}
               }, {
	            name: 'Day12',
	            id: 'Day12',
	            type: 'line',
	            lineWidth: 0,
	            marker: {
	                enabled: true,
	                radius: 2
	            },
	            states: {
	                hover: {
	                    lineWidthPlus: 0
	                    }
	             },
	            data: {{pts12}}
               }, {
	            name: 'Day13',
	            id: 'Day13',
	            type: 'line',
	            lineWidth: 0,
	            marker: {
	                enabled: true,
	                radius: 2
	            },
	            states: {
	                hover: {
	                    lineWidthPlus: 0
	                    }
	             },
	            data: {{pts13}}
               }, {
	            name: 'Day14',
	            id: 'Day14',
	            type: 'line',
	            lineWidth: 0,
	            marker: {
	                enabled: true,
	                radius: 2
	            },
	            states: {
	                hover: {
	                    lineWidthPlus: 0
	                    }
	             },
	            data: {{pts14}}
               }, {
	            name: 'Day15',
	            id: 'Day15',
	            type: 'line',
	            lineWidth: 0,
	            marker: {
	                enabled: true,
	                radius: 2
	            },
	            states: {
	                hover: {
	                    lineWidthPlus: 0
	                    }
	             },
	            data: {{pts15}}
	        }],
        }
       });
	});









