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
    "--color-background": "rgb(255, 255, 255)",
    "--color-tab": "#ccc",
    "--color-text": "#000",
    "--color-line": "#000",
  },
  dark: {
    dark: true,
    "--color-background": "#1d1f20",
    "--color-tab": "#333",
    "--color-text": "#fff",
    "--color-line": "#000",
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
      if (cached != null) {
        loadTimetable(cached);
      }
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

  if (di == null) {
    return;
  }
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
  data = data.replace(/\\u0026/g, "&");
  data = data.replace(/&#(\d+);/g, (match, dec) => {
    return String.fromCharCode(dec);
  });
  data = data.split(day)[1].split("</ul>")[0];
  console.log(data);
  let text = "";
  let main = data.split("Dagens rätt </span>")[1];
  main = main.split("</li>")[0];
  text += main;
  if (data.includes("gröna")) {
    let veg = data.split("Dagens gröna </span>")[1];
    veg = veg.split("</li>")[0];
    text += "\n" + veg;
  }
  if (data.includes("extra")) {
    let extra = data.split("Dagens extra </span>")[1];
    extra = extra.split("</li>")[0];
    text += "\n" + extra;
  }
  return text;
}

function getLunch() {
  var day = getCurrentDay();
  if (day == "Lördag" || day == "Söndag") {
    document.getElementById("lunchtext").innerText = "Det är helg";
    return;
  }
  let url =
    "https://corsproxy.io/?" +
    encodeURIComponent(
      "https://maltidsservice.uppsala.se/mat-och-menyer/gymnasieskolans-meny/"
    );
  fetch(url, {
    method: "GET",
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.text();
    })
    .then((data) => {
      var lunch = extractLunchOfDay(day, data);
      document.getElementById("lunchtext").innerText = lunch;
    })
    .catch((error) => {
      document.getElementById("lunchtext").innerText =
        "Kunde inte hämta matsedel\nError: " + error.toString();
    });
}

var b = new PdfRenderer("Arial", false, "gonk");
var currentSchemaWidth = null;

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
}

if (theme == null) {
  theme = "light";
}
switchTheme(theme);
