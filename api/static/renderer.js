function renderTimetable(boxes, lines, texts, timetableElement) {
  let boxList = boxes;
  let textList = texts;
  let lineList = lines.filter(function (l) {
    return l.type !== "Frame";
  });
  var svgElement = document.createElementNS(
    "http://www.w3.org/2000/svg",
    "svg"
  );
  svgElement.style.overflow = "visible";
  svgElement.style.position = "absolute";
  svgElement.setAttribute("width", timetableElement.clientWidth.toString());
  svgElement.setAttribute("height", timetableElement.clientHeight.toString());
  svgElement.setAttribute("shape-rendering", "crispEdges");
  timetableElement.insertAdjacentElement("afterbegin", svgElement);
  renderBoxData(timetableElement, svgElement, boxList);
  renderTextData(svgElement, textList);
  renderLineData(svgElement, lineList);
  svgElement.setAttribute(
    "viewBox",
    "0 0 " +
      svgElement.width.baseVal.value +
      " " +
      svgElement.height.baseVal.value
  );
}
function clearTimetable(timetableElement) {
  var svg = timetableElement.querySelector("svg");
  if (svg) timetableElement.removeChild(svg);
}
function renderBoxData(timetableElement, svg, boxList) {
  timetableElement.id = "timetableElement";
  var lowest = 0;
  var first = true;
  var colorCache = {};
  for (var i = 0; i < boxList.length; i++) {
    var box = boxList[i];
    if (first == true) {
      first = false;
      continue;
    }
    var rect = document.createElementNS("http://www.w3.org/2000/svg", "rect");
    rect.setAttribute("x", (box.x + 1).toString());
    rect.setAttribute("y", (box.y + 1).toString());
    rect.setAttribute("width", box.width.toString());
    rect.setAttribute("height", box.height.toString());
    rect.setAttribute("shape-rendering", "crispEdges");
    let cssVarName = Object.keys(colorCache).find(
      (name) => colorCache[name] === box.bColor
    );

    if (!cssVarName) {
      cssVarName = `--color-box-${i.toString()}`;
      document.documentElement.style.setProperty(cssVarName, box.bColor);
      colorCache[cssVarName] = box.bColor;
    }

    rect.style.fill = `var(${cssVarName})`;
    rect.style.stroke = "var(--color-line)";
    rect.style.strokeWidth = "1";
    rect.setAttributeNS("box-information", "box-type", box.type || "");
    rect.setAttributeNS("box-information", "box-id", (box.id || "").toString());
    if (box.fColor === box.bColor) rect.style.strokeWidth = "0";
    if (box.y + box.height > lowest) lowest = box.y + box.height;
    svg.appendChild(rect);
  }
  timetableElement.style.height = lowest + "px";
  svg.setAttribute("height", lowest.toString());
}
function renderLineData(svg, lineList) {
  for (var i = 0; i < lineList.length; i++) {
    var line = lineList[i];
    var l = document.createElementNS("http://www.w3.org/2000/svg", "line");
    l.setAttribute("x1", (line.p1x + 1).toString());
    l.setAttribute("y1", (line.p1y + 1).toString());
    l.setAttribute("x2", (line.p2x + 1).toString());
    l.setAttribute("y2", (line.p2y + 1).toString());
    l.setAttribute("stroke", "var(--color-line)");
    svg.appendChild(l);
  }
}
function renderTextData(svg, textList) {
  for (var i = 0; i < textList.length; i++) {
    var text = textList[i];
    var label = document.createElementNS("http://www.w3.org/2000/svg", "text");
    label.textContent = text.text;
    label.style.fontSize = text.fontsize + "px";
    label.style.fill = "var(--color-text)";
    label.setAttribute("x", (text.x + 1).toString());
    label.setAttribute("y", (text.y + 1 + text.fontsize).toString());
    label.setAttributeNS("text-information", "text-id", text.id.toString());
    if (text.bold) {
      label.style.fontWeight = "bold";
    }
    if (text.italic) {
      label.style.fontStyle = "italic";
    }
    label.style.pointerEvents = "none";
    svg.appendChild(label);
  }
}
function render(document, boxes, lines, texts) {
  renderBoxes(document, boxes);
  renderLines(document, lines);
  renderTexts(document, texts);
}
function renderBoxes(document, boxes) {
  for (var i in boxes) {
    var box = boxes[i];
    document
      .setLineWidth(1)
      .setDrawColor(box.fColor)
      .setFillColor(box.bColor)
      .rect(
        getActualCoordinate(box.x),
        getActualCoordinate(box.y),
        box.width,
        box.height,
        "DF"
      );
  }
}
function renderLines(document, lines) {
  for (var i = 0; i < lines.length; i++) {
    var l = lines[i];
    document
      .setLineWidth(1)
      .setDrawColor(l.color)
      .line(
        getActualCoordinate(l.p1x),
        getActualCoordinate(l.p1y),
        getActualCoordinate(l.p2x),
        getActualCoordinate(l.p2y)
      );
  }
}
function renderTexts(document, texts) {
  for (var i in texts) {
    var text = texts[i];
    var actualY = getActualCoordinate(text.y) + text.fontsize * 0.25;
    document
      .setFontSize(text.fontsize)
      .setTextColor(text.fColor)
      .text(text.text, getActualCoordinate(text.x), actualY, {
        baseline: "top",
        flags: { noBOM: true, autoencode: true },
      });
  }
}
function getActualCoordinate(coordinate) {
  return coordinate;
}
