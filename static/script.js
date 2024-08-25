let loadButton = document.getElementById("load");
timetable_data = null;
timetable_request = null;
session_request = undefined;
session = undefined;

async function getSession() {
  const session_json = {
    username: username,
    password: password,
  };

  session_request = await fetch("/session", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(session_json),
  });

  session = await session_request.text();
  console.log("got session " + session);
  getSchema();
}

async function getSchema() {
  if (session === undefined) {
    getSession();
    return;
  }
  loadButton.disabled = true;
  var schemaWidth = window.innerWidth - 5 > 1280 ? 1280 : window.innerWidth - 5;
  currentSchemaWidth = schemaWidth;

  const timetable_json = {
    session: session,
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
  b.clearTimetable(document.getElementById("timetableElement"));
  localStorage.setItem(
    "cached",
    encodeURIComponent(JSON.stringify(timetable_data))
  );
  loadTimetable(timetable_data);
  loadButton.disabled = false;
}

function loadTimetable(di) {
  b.renderTimetable(
    di["data"]["boxList"],
    di["data"]["lineList"],
    di["data"]["textList"],
    document.getElementById("timetableElement")
  );
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
  d = d.replace("\\u0026#229;", "å");
  d = d.replace("\\u0026#246;", "ö");
  d = d.replace("\\u0026#228;", "ä");
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
      document.getElementById("lunchtext").innerText = lunch;
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
var cached = localStorage.getItem("cached");
console.log("Laddar användare: " + username);
if (username != null) {
  if (cached != null) {
    loadTimetable(JSON.parse(decodeURIComponent(cached)));
  }
  document.getElementById("username").value = username;
  document.getElementById("password").value = password;
  //getSchema(username);
}
