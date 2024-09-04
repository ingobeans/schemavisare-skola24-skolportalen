let loadButton = document.getElementById("load");
timetable_data = null;
timetable_request = null;

function invertColors(hex) {
  function hexToRgb(hex) {
    if (hex[0] === "#") hex = hex.slice(1);
    let bigint = parseInt(hex, 16);
    return {
      r: (bigint >> 16) & 255,
      g: (bigint >> 8) & 255,
      b: bigint & 255,
    };
  }

  function rgbToHex(r, g, b) {
    return `#${((1 << 24) + (r << 16) + (g << 8) + b)
      .toString(16)
      .slice(1)
      .toUpperCase()}`;
  }

  function calculateBrightness(r, g, b) {
    return 0.2126 * r + 0.7152 * g + 0.0722 * b;
  }

  const { r, g, b } = hexToRgb(hex);

  const originalBrightness = calculateBrightness(r, g, b);

  const invertedBrightness = 255 - originalBrightness;
  if (originalBrightness != 0) {
    const factor = invertedBrightness / originalBrightness;
    const newR = Math.min(255, Math.round(r * factor));
    const newG = Math.min(255, Math.round(g * factor));
    const newB = Math.min(255, Math.round(b * factor));
    return rgbToHex(newR, newG, newB);
  }
  return "#ffffff";
}

function invertAllColors() {
  const root = document.documentElement;
  const styles = root.style;
  const variables = Array.from(styles).filter((name) =>
    name.startsWith("--color-box-")
  );

  variables.forEach((variable) => {
    const color = styles.getPropertyValue(variable).trim();
    const invertedColor = invertColors(color);
    root.style.setProperty(variable, invertedColor);
  });
}

let themes = {
  light: {
    dark: false,
    "--color-border": "rgb(0, 0, 0)",
    "--color-background": "rgb(255, 255, 255)",
    "--color-tab": "#ccc",
    "--color-text": "#000",
  },
  dark: {
    dark: true,
    "--color-border": "rgb(0, 0, 0)",
    "--color-background": "#1d1f20",
    "--color-tab": "#393d3e",
    "--color-text": "#fff",
  },
};

function switchTheme(themeName) {
  const themeData = themes[themeName];
  if (!themeData) {
    console.log("no such theme as ", themeName);
    return;
  }
  localStorage.setItem("theme", themeName);
  theme = themeName;
  for (const variable in themeData) {
    if (variable == "dark") {
      loadTimetable(cached);
      continue;
    }
    if (themeData.hasOwnProperty(variable)) {
      document.documentElement.style.setProperty(variable, themeData[variable]);
    }
  }
}

function changeTheme() {
  console.log(theme);
  if (theme == "light") {
    switchTheme("dark");
  } else {
    switchTheme("light");
  }
}

async function getSchema() {
  loadButton.disabled = true;
  var schemaWidth = window.innerWidth - 5 > 1280 ? 1280 : window.innerWidth - 5;
  currentSchemaWidth = schemaWidth;

  const timetable_json = {
    username: username,
    password: password,
    width: schemaWidth,
  };

  timetable_request = await fetch("/timetable", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(timetable_json),
  });

  timetable_data = await timetable_request.json();
  localStorage.setItem(
    "cached",
    encodeURIComponent(JSON.stringify(timetable_data))
  );
  loadTimetable(timetable_data);
  loadButton.disabled = false;
}

function loadTimetable(di) {
  b.clearTimetable(document.getElementById("timetableElement"));
  cached = di;
  b.renderTimetable(
    di["data"]["boxList"],
    di["data"]["lineList"],
    di["data"]["textList"],
    document.getElementById("timetableElement")
  );
  if (themes[theme]["dark"] == true) {
    invertAllColors();
  }
}

function submit() {
  var u = document.getElementById("username").value.trim();
  var p = document.getElementById("password").value.trim();
  console.log("Nytt användarnamn: " + u);
  console.log("Nytt lösenord: " + p);
  localStorage.setItem("username", u);
  localStorage.setItem("password", p);
  username = localStorage.getItem("username");
  password = localStorage.getItem("password");
  getSchema(username);
}
function clearData() {
  localStorage.clear();

  var te = document.getElementById("timetableElement");
  te.style.height = "0px";
  b.clearTimetable(te);
  document.getElementById("username").value = "";
  document.getElementById("password").value = "";
}

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) {
    return parts.pop().split(";").shift();
  }
}

function getCurrentDay() {
  const days = [
    "Söndag",
    "Måndag",
    "Tisdag",
    "Onsdag",
    "Torsdag",
    "Fredag",
    "Lördag",
  ];
  const currentDate = new Date();
  const dayOfWeek = currentDate.getDay();

  return days[dayOfWeek];
}

function extractLunchOfDay(day, data) {
  if (day == "Måndag") {
    day = "ndag";
  }
  var d = data.split(day)[1];
  d = d.split("Dagens r\\u0026#228;tt \\u003c/span\\u003e")[1];
  d = d.split("\\u003c/li\\u003e")[0];
  d = d.replace(/\\u0026/g, "&");
  return d;
}

function getLastMondayFormatted() {
  const today = new Date();
  const dayOfWeek = today.getDay();
  const daysUntilLastMonday = (dayOfWeek + 6) % 7;
  today.setDate(today.getDate() - daysUntilLastMonday);

  const year = today.getFullYear();
  const month = String(today.getMonth() + 1).padStart(2, "0");
  const day = String(today.getDate()).padStart(2, "0");
  return `${year}-${month}-${day}`;
}

function getLunch() {
  var day = getCurrentDay();
  if (day == "Lördag" || day == "Söndag") {
    document.getElementById("lunchtext").innerText = "Det är helg";
    return;
  }
  const lastMondayFormatted = getLastMondayFormatted();
  const url =
    "https://corsproxy.io/?" +
    encodeURIComponent(
      "https://maltidsservice.uppsala.se/OpenMealBlock/GetMeals/?startdate=" +
        lastMondayFormatted +
        " 16:00:00&menuType=OpenMealDistributorIdSchool&distributorId=ac50752d-16f3-4ffd-8037-3c3ec42c301f"
    );
  const headers = {
    Cookie:
      "ASP.NET_SessionId=we2k4k04pmmvwnlancy3cqf4; _pk_ref.44.e1d3=%5B%22%22%2C%22%22%2C1694011041%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_id.44.e1d3=976e2c22aab2e167.1694011041.; _pk_ses.44.e1d3=1; AcceptCookies_maltidsservice.uppsala.se=True",
  };
  fetch(url, {
    method: "GET",
    headers: headers,
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.text();
    })
    .then((data) => {
      var lunch = extractLunchOfDay(day, data);
      document.getElementById("lunchtext").innerHTML = lunch;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

var b = new PdfRenderer("Arial", false, "gonk");
var currentSchemaWidth = null;

window.addEventListener("resize", function (event) {
  if (username == null) {
    return;
  }
  if (currentSchemaWidth != null) {
    if (currentSchemaWidth >= 1280 && window.innerWidth >= 1280) {
      return;
    }
  }
  //getSchema(username);
});

getLunch();
var username = localStorage.getItem("username");
var password = localStorage.getItem("password");
var cached = JSON.parse(decodeURIComponent(localStorage.getItem("cached")));
var theme = localStorage.getItem("theme");

console.log("Laddar användare: " + username);
if (username != null) {
  if (cached != null) {
    loadTimetable(cached);
  }
  document.getElementById("username").value = username;
  document.getElementById("password").value = password;
  //getSchema(username);
}

if (theme == null) {
  theme = "light";
}
switchTheme(theme);
