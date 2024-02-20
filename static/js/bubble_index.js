/**
 * Main entry point -- this file has been added to index.html in a <script> tag. Add whatever code you want below.
 */

fetch("static/data.json")
  .then((response) => response.json())
  .then((data) => {
    console.log(data);

    Highcharts.chart("container", {
      title: {
        text: "",
      },
      chart: {
        type: "packedbubble",
      },
      plotOptions: {
        packedbubble: {
          minSize: "30%",
          maxSize: "600%",
          zMin: 0,
          zMax: 1000,
          marker: {
            symbol: "circle",
            fillColor: "transparent",
            lineColor: "transparent",
          },
        },
      },
      tooltip: {
        useHTML: true,
        formatter: function () {
          const roundedValue = this.point.value.toFixed(0);
          return `<b>${this.point.name}</b><br>usage: ${roundedValue}%`;
        },
      },
      series: [
        {
          name: "",
          data: data,
        },
      ],
    });
  })
  .catch((error) => console.error("Error loading the JSON data:", error));
