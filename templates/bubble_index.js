/**
 * Main entry point -- this file has been added to index.html in a <script> tag. Add whatever code you want below.
 */
// import data from "../data.json" assert { type: "json" };
// ("use strict");
const data = [
  {
    name: "so funny",
    value: 7.6923076923076925,
    marker: {
      symbol:
        "url(https://cdn.shopify.com/s/files/1/1061/1924/products/Tears_Emoji_Icon_2_70x70.png?v=1485573515)",
    },
  },
  {
    name: "crazy",
    value: 7.6923076923076925,
    marker: {
      symbol:
        "url(https://cdn.shopify.com/s/files/1/1061/1924/files/Tongue_Out_Emoji_1_70x70.png?13752525173949329807)",
    },
  },
  {
    name: "poop",
    value: 3.8461538461538463,
    marker: {
      symbol:
        "url(https://cdn.shopify.com/s/files/1/1061/1924/products/Poop_Emoji_2.png?v=1485573482)",
    },
  },
  {
    name: "okay",
    value: 7.6923076923076925,
    marker: {
      symbol:
        "url(https://cdn.shopify.com/s/files/1/1061/1924/products/OK_Hand_Sign_Emoji_Icon_ios10_70x70.png?v=1511943170)",
    },
  },
  {
    name: "cool",
    value: 15.384615384615385,
    marker: {
      symbol:
        "url(https://cdn.shopify.com/s/files/1/1061/1924/products/Emoji_Icon_-_Sunglasses_cool_emoji.png?v=1485573433)",
    },
  },
  {
    name: "love",
    value: 7.6923076923076925,
    marker: {
      symbol:
        "url(https://cdn.smallseotools.com/emojis/Apple/Red-Heart-on-Apple-iOS-13.3/Red-Heart-on-Apple-iOS-13.3.png)",
    },
  },
  {
    name: "happy",
    value: 11.538461538461538,
    marker: {
      symbol:
        "url(https://cdn.shopify.com/s/files/1/1061/1924/files/Smliing_Emoji_Icon.png?13752525173949329807)",
    },
  },
  {
    name: "delicious",
    value: 3.8461538461538463,
    marker: {
      symbol:
        "url(https://cdn.shopify.com/s/files/1/1061/1924/products/Hungry_Emoji_Icon_c20f1808-f3e2-4051-8941-3d157764e8cb.png?v=1485573460)",
    },
  },
  {
    name: "book",
    value: 7.6923076923076925,
    marker: {
      symbol:
        "url(https://em-content.zobj.net/source/apple/354/open-book_1f4d6.png)",
    },
  },
  {
    name: "stressed",
    value: 7.6923076923076925,
    marker: {
      symbol:
        "url(https://cdn.shopify.com/s/files/1/1061/1924/products/Weary_Face_Emoji_Icon_ios10.png?v=1511762076)",
    },
  },
  {
    name: "sad",
    value: 3.8461538461538463,
    marker: {
      symbol:
        "url(https://cdn.shopify.com/s/files/1/1061/1924/products/Emoji_Icon_-_Sad_Emoji_70x70.png?v=1485573425)",
    },
  },
  {
    name: "shrug",
    value: 3.8461538461538463,
    marker: {
      symbol:
        "url(https://em-content.zobj.net/source/apple/354/woman-shrugging_1f937-200d-2640-fe0f.png)",
    },
  },
  {
    name: "home",
    value: 3.8461538461538463,
    marker: {
      symbol:
        "url(https://em-content.zobj.net/source/apple/354/house_1f3e0.png)",
    },
  },
  {
    name: "sleepy",
    value: 3.8461538461538463,
    marker: {
      symbol:
        "url(https://cdn.shopify.com/s/files/1/1061/1924/products/Sleeping_Emoji_2.png?v=1485573494)",
    },
  },
  {
    name: "bye",
    value: 3.8461538461538463,
    marker: {
      symbol:
        "url(https://cdn.shopify.com/s/files/1/1061/1924/products/Waving_Hand_Sign_Emoji_Icon_ios10_70x70.png?v=1511943171)",
    },
  },
];

window.addEventListener("load", () => {
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
});
