var FontFamily = /** @class */ function () {
  function FontFamily(name, fonts) {
    this.fonts = fonts;
    this.name = name;
  }
  Object.defineProperty(FontFamily.prototype, "familyName", {
    get: function () {
      return this.name;
    },
    enumerable: true,
    configurable: true,
  });
  FontFamily.prototype.getFont = function (style) {
    var font = this.fonts.filter(function (f) {
      return f.style === style;
    });
    if (font.length > 1)
      throw new Error(
        "More than one font with the same style in the font family."
      );
    if (font.length < 1)
      throw new Error("Font with the style does not exist in the font family.");
    return font[0];
  };
  return FontFamily;
};
var PdfRenderer = /** @class */ (function () {
  function PdfRenderer(fontFamily, vertical, fileName) {
    this.fileName = "";
    this.vertical = false;
    // Margin is approximately 1 cm (595 points / 21 cm which is width of A4 in points and cm).
    this.marginPoints = 595 / 21;
    this.vertical = vertical;
    this.fileName = fileName;
    this.fontFamily = fontFamily;
    this.fontFamilyName = fontFamily;
  }
  Object.defineProperty(PdfRenderer.prototype, "dimensions", {
    get: function () {
      var document = this.createDocument();
      return {
        width: document.internal.pageSize.getWidth() - this.marginPoints * 2,
        height: document.internal.pageSize.getHeight() - this.marginPoints * 2,
      };
    },
    enumerable: true,
    configurable: true,
  });
  Object.defineProperty(PdfRenderer, "fontStyles", {
    get: function () {
      return ["normal", "bold", "italic", "bolditalic"];
    },
    enumerable: true,
    configurable: true,
  });

  PdfRenderer.prototype.renderTimetable = function (
    boxes,
    lines,
    texts,
    timetableElement
  ) {
    this.boxList = boxes;
    this.textList = texts;
    this.lineList = lines.filter(function (l) {
      return l.type !== "Frame";
    });
    //this.clearTimetable(timetableElement);
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
    this.renderBoxData(timetableElement, svgElement);
    this.renderTextData(svgElement);
    this.renderLineData(svgElement);
    svgElement.setAttribute(
      "viewBox",
      "0 0 " +
        svgElement.width.baseVal.value +
        " " +
        svgElement.height.baseVal.value
    );
  };
  PdfRenderer.prototype.clearTimetable = function (timetableElement) {
    var svg = timetableElement.querySelector("svg");
    if (svg) timetableElement.removeChild(svg);
  };
  PdfRenderer.prototype.renderBoxData = function (timetableElement, svg) {
    var _this = this;
    if (!this.boxList) return;
    timetableElement.id = "timetableElement";
    var lowest = 0;
    var first = true;
    var colorCache = {};
    var _loop_1 = function (box, i) {
      if (first == true) {
        first = false;
        return;
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
      rect.style.stroke = "var(--color-border)";
      rect.style.strokeWidth = "1";
      if (box.type === "Lesson" && this_1.isLessonClickable) {
        rect.setAttribute("focusable", "true");
        rect.setAttribute("tabindex", "0");
        rect.style.cursor = "pointer";
        rect.addEventListener("mouseup" || "pointerup", function () {
          _this.onLessonClick(box.lessonGuids || []);
        });
        rect.addEventListener("keydown", function (e) {
          //enter
          if (e.keyCode === 13) _this.onLessonClick(box.lessonGuids || []);
        });
      }
      rect.setAttributeNS("box-information", "box-type", box.type || "");
      rect.setAttributeNS(
        "box-information",
        "box-id",
        (box.id || "").toString()
      );
      if (box.fColor === box.bColor) rect.style.strokeWidth = "0";
      if (box.y + box.height > lowest) lowest = box.y + box.height;
      svg.appendChild(rect);
    };
    var this_1 = this;
    for (var _i = 0, _a = this.boxList; _i < _a.length; _i++) {
      var box = _a[_i];
      _loop_1(box, _i);
    }
    timetableElement.style.height = lowest + "px";
    svg.setAttribute("height", lowest.toString());
  };
  PdfRenderer.prototype.renderLineData = function (svg) {
    if (!this.lineList) return;
    for (var _i = 0, _a = this.lineList; _i < _a.length; _i++) {
      var line = _a[_i];
      var l = document.createElementNS("http://www.w3.org/2000/svg", "line");
      l.setAttribute("x1", (line.p1x + 1).toString());
      l.setAttribute("y1", (line.p1y + 1).toString());
      l.setAttribute("x2", (line.p2x + 1).toString());
      l.setAttribute("y2", (line.p2y + 1).toString());
      l.setAttribute("stroke", line.color);
      svg.appendChild(l);
    }
  };
  PdfRenderer.prototype.renderTextData = function (svg) {
    if (!this.textList) return;
    for (var _i = 0, _a = this.textList; _i < _a.length; _i++) {
      var text = _a[_i];
      var label = document.createElementNS(
        "http://www.w3.org/2000/svg",
        "text"
      );
      label.textContent = text.text;
      label.style.fontSize = text.fontsize + "px";
      label.style.fontFamily = "var(--font)";
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
  };

  PdfRenderer.prototype.setProperties = function (document) {
    document.setProperties({
      title: "Schema",
      author: "Skola24",
    });
  };
  PdfRenderer.prototype.render = function (document, boxes, lines, texts) {
    this.renderBoxes(document, boxes);
    this.renderLines(document, lines);
    this.renderTexts(document, texts);
  };
  PdfRenderer.prototype.renderBoxes = function (document, boxes) {
    for (var i in boxes) {
      var box = boxes[i];
      document
        .setLineWidth(1)
        .setDrawColor(box.fColor)
        .setFillColor(box.bColor)
        .rect(
          this.getActualCoordinate(box.x),
          this.getActualCoordinate(box.y),
          box.width,
          box.height,
          "DF"
        );
    }
  };
  PdfRenderer.prototype.renderLines = function (document, lines) {
    for (var _i = 0, lines_1 = lines; _i < lines_1.length; _i++) {
      var l = lines_1[_i];
      document
        .setLineWidth(1)
        .setDrawColor(l.color)
        .line(
          this.getActualCoordinate(l.p1x),
          this.getActualCoordinate(l.p1y),
          this.getActualCoordinate(l.p2x),
          this.getActualCoordinate(l.p2y)
        );
    }
  };
  PdfRenderer.prototype.renderTexts = function (document, texts) {
    for (var i in texts) {
      var text = texts[i];
      var actualY = this.getActualCoordinate(text.y) + text.fontsize * 0.25;
      document
        .setFont(this.fontFamilyName, this.getFontStyle(text).style)
        .setFontSize(text.fontsize)
        .setTextColor(text.fColor)
        .text(text.text, this.getActualCoordinate(text.x), actualY, {
          baseline: "top",
          flags: { noBOM: true, autoencode: true },
        });
    }
  };
  PdfRenderer.prototype.getFontStyle = function (text) {
    var font;
    if (text.bold && text.italic) font = this.boldItalicFont;
    else if (text.bold) font = this.boldFont;
    else if (text.italic) font = this.italicFont;
    else font = this.normalFont;
    return font;
  };
  PdfRenderer.prototype.getActualCoordinate = function (coordinate) {
    return coordinate + this.marginPoints;
  };
  PdfRenderer.prototype.loadFonts = function (document) {
    try {
      this.normalFont = "Arial";
      this.boldFont = "Arial";
      this.italicFont = "Arial";
      this.boldItalicFont = "Arial";
    } catch (_a) {
      throw new Error("Could not find all font styles in font family.");
    }
    /*this.addFontToVFS(document, this.normalFont);
    this.addFontToVFS(document, this.boldFont);
    this.addFontToVFS(document, this.italicFont);
    this.addFontToVFS(document, this.boldItalicFont);*/
  };
  PdfRenderer.prototype.addFontToVFS = function (document, font) {
    document.addFileToVFS(font.fileName, font.data);
    document.addFont(
      font.fileName,
      this.fontFamilyName,
      font.style,
      "Identity-H"
    );
  };
  return PdfRenderer;
})();
