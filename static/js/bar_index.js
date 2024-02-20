Highcharts.chart("container", {
  chart: {
    type: "bar",
  },
  title: {
    text: "Top Three Emojis Used",
  },
  xAxis: {
    categories: ["😊", "❤️", "👍"],
  },
  yAxis: {
    title: {
      text: "Number of Times Used",
    },
  },
  plotOptions: {
    series: {
      dataLabels: {
        enabled: true,
        format: "{point.y}",
      },
    },
  },
  series: [
    {
      name: "Emojis",
      data: [10, 8, 6],
      color: {
        linearGradient: { x1: 0, x2: 0, y1: 0, y2: 1 },
        stops: [
          [0, "#4e5eff"],
          [1, "#00bfff"],
        ],
      },
    },
  ],
});
