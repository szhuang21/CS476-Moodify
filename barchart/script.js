fetch('data.json')
  .then(response => response.json())
  .then(data => {
    const sortedData = data.sort((a, b) => b.value - a.value);

    const topThree = sortedData.slice(0, 3);

    const categories = topThree.map(item => item.marker.symbol.replace('url(', '').replace(')', ''));
    const chartData = topThree.map(item => ({
        y: item.value,
        name: item.name,
        marker: {
            symbol: item.marker.symbol
        }
    }));

    Highcharts.chart('container', {
      chart: {
          type: 'bar'
      },
      title: {
          text: 'Top Three Emojis Used in Conversation'
      },
      xAxis: {
          categories: categories.map(symbol => `<img src="${symbol}" style="width: 30px; height: 30px;">`),
          labels: {
              useHTML: true
          }, title: {
            text: 'Emojis'
        }
      },
      yAxis: {
          title: {
              text: 'Percent of Times Used in Conversation'
          }
      },
      plotOptions: {
          series: {
              dataLabels: {
                  enabled: true,
                  format: '{point.y:.2f}'
              }
          }
      },
      tooltip: {
          formatter: function() {
              return this.point.name + ': <b>' + this.y + '</b>';
          }
      },
      series: [{
          name: 'Emojis',
          data: chartData,
          color: {
              linearGradient: { x1: 0, x2: 0, y1: 0, y2: 1 },
              stops: [
                  [0, '#4e5eff'],
                  [1, '#00bfff']
              ]
          }
      }]
    });
  })
  .catch(error => console.error('Error loading the JSON data:', error));
