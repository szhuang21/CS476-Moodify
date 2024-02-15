/**
 * Main entry point -- this file has been added to index.html in a <script> tag. Add whatever code you want below.
 */
import data from "../data.json" assert { type: "json" };
("use strict");

window.addEventListener("load", () => {
  console.log(data);

  Highcharts.chart("container", {
    chart: {
      type: "packedbubble",
    },
    plotOptions: {
      packedbubble: {
        minSize: "30%",
        maxSize: "120%",
        zMin: 0,
        zMax: 100,
      },
    },
    /*  tooltip: { // TODO: add information to tooltips
    useHTML: true,
    pointFormat: '<b>{data.name} title emoji'
  },  */
    series: [
      {
        marker: {
          symbol: "url(https://www.highcharts.com/samples/graphics/earth.svg)",
        },
        data: data,
      },
    ],
  });
});
