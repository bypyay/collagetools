/**
 * Daily1Step Collage Studio PRO — Master Controller & High-Definition Canvas Engine
 * Built for ultra-clean, modern, glitch-free collage editing with 4K export.
 */

(function() {
  'use strict';

  // ══════════════════════════════════════════════════════════════════
  // 1. LAYOUT DEFINITIONS (Normalized 0.0 to 1.0)
  // ══════════════════════════════════════════════════════════════════
  const LAYOUTS = {
    // 1 Photo
    '1-full': [{ x: 0, y: 0, w: 1, h: 1 }],

    // 2 Photos
    '2-side': [
      { x: 0, y: 0, w: 0.5, h: 1 },
      { x: 0.5, y: 0, w: 0.5, h: 1 }
    ],
    '2-stack': [
      { x: 0, y: 0, w: 1, h: 0.5 },
      { x: 0, y: 0.5, w: 1, h: 0.5 }
    ],
    '2-big-left': [
      { x: 0, y: 0, w: 0.65, h: 1 },
      { x: 0.65, y: 0, w: 0.35, h: 1 }
    ],

    // 3 Photos
    '3-left-big': [
      { x: 0, y: 0, w: 0.5, h: 1 },
      { x: 0.5, y: 0, w: 0.5, h: 0.5 },
      { x: 0.5, y: 0.5, w: 0.5, h: 0.5 }
    ],
    '3-top-big': [
      { x: 0, y: 0, w: 1, h: 0.5 },
      { x: 0, y: 0.5, w: 0.5, h: 0.5 },
      { x: 0.5, y: 0.5, w: 0.5, h: 0.5 }
    ],
    '3-columns': [
      { x: 0, y: 0, w: 1/3, h: 1 },
      { x: 1/3, y: 0, w: 1/3, h: 1 },
      { x: 2/3, y: 0, w: 1/3, h: 1 }
    ],
    '3-rows': [
      { x: 0, y: 0, w: 1, h: 1/3 },
      { x: 0, y: 1/3, w: 1, h: 1/3 },
      { x: 0, y: 2/3, w: 1, h: 1/3 }
    ],

    // 4 Photos
    '4-grid': [
      { x: 0, y: 0, w: 0.5, h: 0.5 },
      { x: 0.5, y: 0, w: 0.5, h: 0.5 },
      { x: 0, y: 0.5, w: 0.5, h: 0.5 },
      { x: 0.5, y: 0.5, w: 0.5, h: 0.5 }
    ],
    '4-hero-left': [
      { x: 0, y: 0, w: 0.6, h: 1 },
      { x: 0.6, y: 0, w: 0.4, h: 1/3 },
      { x: 0.6, y: 1/3, w: 0.4, h: 1/3 },
      { x: 0.6, y: 2/3, w: 0.4, h: 1/3 }
    ],
    '4-hero-top': [
      { x: 0, y: 0, w: 1, h: 0.6 },
      { x: 0, y: 0.6, w: 1/3, h: 0.4 },
      { x: 1/3, y: 0.6, w: 1/3, h: 0.4 },
      { x: 2/3, y: 0.6, w: 1/3, h: 0.4 }
    ],

    // 5 Photos (Magazine Default)
    '5-mag': [
      { x: 0, y: 0, w: 0.5, h: 0.5 },
      { x: 0.5, y: 0, w: 0.5, h: 0.5 },
      { x: 0, y: 0.5, w: 1/3, h: 0.5 },
      { x: 1/3, y: 0.5, w: 1/3, h: 0.5 },
      { x: 2/3, y: 0.5, w: 1/3, h: 0.5 }
    ],
    '5-hero-center': [
      { x: 0, y: 0, w: 0.3, h: 0.5 },
      { x: 0.7, y: 0, w: 0.3, h: 0.5 },
      { x: 0.3, y: 0, w: 0.4, h: 1 },
      { x: 0, y: 0.5, w: 0.3, h: 0.5 },
      { x: 0.7, y: 0.5, w: 0.3, h: 0.5 }
    ],

    // 6 Photos
    '6-grid': [
      { x: 0, y: 0, w: 1/3, h: 0.5 },
      { x: 1/3, y: 0, w: 1/3, h: 0.5 },
      { x: 2/3, y: 0, w: 1/3, h: 0.5 },
      { x: 0, y: 0.5, w: 1/3, h: 0.5 },
      { x: 1/3, y: 0.5, w: 1/3, h: 0.5 },
      { x: 2/3, y: 0.5, w: 1/3, h: 0.5 }
    ],
    '6-hero-left': [
      { x: 0, y: 0, w: 0.5, h: 1 },
      { x: 0.5, y: 0, w: 0.25, h: 0.5 },
      { x: 0.75, y: 0, w: 0.25, h: 0.5 },
      { x: 0.5, y: 0.5, w: 0.25, h: 0.5 },
      { x: 0.75, y: 0.5, w: 0.25, h: 0.5 },
      { x: 0.5, y: 0.75, w: 0.5, h: 0.25 }
    ],

    // 8 Photos
    '8-grid': [
      { x: 0, y: 0, w: 0.25, h: 0.5 },
      { x: 0.25, y: 0, w: 0.25, h: 0.5 },
      { x: 0.5, y: 0, w: 0.25, h: 0.5 },
      { x: 0.75, y: 0, w: 0.25, h: 0.5 },
      { x: 0, y: 0.5, w: 0.25, h: 0.5 },
      { x: 0.25, y: 0.5, w: 0.25, h: 0.5 },
      { x: 0.5, y: 0.5, w: 0.25, h: 0.5 },
      { x: 0.75, y: 0.5, w: 0.25, h: 0.5 }
    ],

    // 9 Photos (Best Nine)
    '9-grid': [
      { x: 0, y: 0, w: 1/3, h: 1/3 },
      { x: 1/3, y: 0, w: 1/3, h: 1/3 },
      { x: 2/3, y: 0, w: 1/3, h: 1/3 },
      { x: 0, y: 1/3, w: 1/3, h: 1/3 },
      { x: 1/3, y: 1/3, w: 1/3, h: 1/3 },
      { x: 2/3, y: 1/3, w: 1/3, h: 1/3 },
      { x: 0, y: 2/3, w: 1/3, h: 1/3 },
      { x: 1/3, y: 2/3, w: 1/3, h: 1/3 },
      { x: 2/3, y: 2/3, w: 1/3, h: 1/3 }
    ],

    // 12 Photos
    '12-grid': [
      { x: 0, y: 0, w: 0.25, h: 1/3 },
      { x: 0.25, y: 0, w: 0.25, h: 1/3 },
      { x: 0.5, y: 0, w: 0.25, h: 1/3 },
      { x: 0.75, y: 0, w: 0.25, h: 1/3 },
      { x: 0, y: 1/3, w: 0.25, h: 1/3 },
      { x: 0.25, y: 1/3, w: 0.25, h: 1/3 },
      { x: 0.5, y: 1/3, w: 0.25, h: 1/3 },
      { x: 0.75, y: 1/3, w: 0.25, h: 1/3 },
      { x: 0, y: 2/3, w: 0.25, h: 1/3 },
      { x: 0.25, y: 2/3, w: 0.25, h: 1/3 },
      { x: 0.5, y: 2/3, w: 0.25, h: 1/3 },
      { x: 0.75, y: 2/3, w: 0.25, h: 1/3 }
    ]
  };

  function createCustomGrid(cols, rows) {
    var list = [];
    var cw = 1 / cols;
    var ch = 1 / rows;
    for (var r = 0; r < rows; r++) {
      for (var c = 0; c < cols; c++) {
        list.push({ x: c * cw, y: r * ch, w: cw, h: ch });
      }
    }
    return list;
  }

  // ══════════════════════════════════════════════════════════════════
  // 2. STUDIO STATE
  // ══════════════════════════════════════════════════════════════════
  var state = {
    canvasW: 800,
    canvasH: 800,
    zoom: 1.0,
    activeLayout: '5-mag',
    cells: LAYOUTS['5-mag'],
    images: [],
    slotImages: {}, // slotIndex -> HTMLImageElement
    activeCellIndex: null,
    
    // Spacing & Border
    gap: 8,
    radius: 6,
    margin: 8,
    borderColor: '#ffffff',
    borderWidth: 0,
    
    // Background
    bgType: 'color', // 'color', 'gradient'
    bgColor: '#ffffff',
    gradFrom: '#6366f1',
    gradTo: '#ec4899',
    gradAngle: '135deg',
    
    // Filters & Adjustments
    filter: 'none',
    brightness: 100,
    contrast: 100,
    saturation: 100,
    
    // Layers
    textLayers: [],
    stickers: []
  };

  var canvas = document.getElementById('proCanvas');
  if (!canvas) return;
  var ctx = canvas.getContext('2d');

  // ══════════════════════════════════════════════════════════════════
  // 3. TAB SWITCHING & DRAWER CONTROLLER
  // ══════════════════════════════════════════════════════════════════
  window.switchDrawerTab = function(tabKey, btn) {
    document.querySelectorAll('.nav-rail-btn').forEach(function(b) { b.classList.remove('active'); });
    document.querySelectorAll('.drawer-content').forEach(function(d) { d.classList.remove('active'); });
    if (btn) btn.classList.add('active');
    var target = document.getElementById('drawer-' + tabKey);
    if (target) target.classList.add('active');
  };

  // ══════════════════════════════════════════════════════════════════
  // 4. ASPECT RATIO PRESETS
  // ══════════════════════════════════════════════════════════════════
  window.setAspectRatio = function(w, h, btn) {
    state.canvasW = w;
    state.canvasH = h;
    canvas.width = w;
    canvas.height = h;
    document.querySelectorAll('.aspect-pill').forEach(function(p) { p.classList.remove('active'); });
    if (btn) btn.classList.add('active');
    var badge = document.getElementById('canvasSizeBadge');
    if (badge) badge.textContent = w + ' × ' + h;
    renderCanvas();
    autoFitZoom();
  };

  // ══════════════════════════════════════════════════════════════════
  // 5. LAYOUT SELECTION & CUSTOM BUILDER
  // ══════════════════════════════════════════════════════════════════
  window.selectLayoutPro = function(layoutKey, btn) {
    state.activeLayout = layoutKey;
    state.cells = LAYOUTS[layoutKey] || LAYOUTS['4-grid'];
    document.querySelectorAll('.layout-card-pro').forEach(function(c) { c.classList.remove('active'); });
    if (btn) btn.classList.add('active');
    updateFilledBadge();
    renderCanvas();
  };

  window.applyNxMGrid = function() {
    var cols = parseInt(document.getElementById('customGridCols').value || 3);
    var rows = parseInt(document.getElementById('customGridRows').value || 3);
    state.cells = createCustomGrid(cols, rows);
    state.activeLayout = 'custom-' + cols + 'x' + rows;
    updateFilledBadge();
    renderCanvas();
  };

  // ══════════════════════════════════════════════════════════════════
  // 6. PHOTO MANAGEMENT & UPLOAD
  // ══════════════════════════════════════════════════════════════════
  var fileInput = document.getElementById('proFileInput');
  var singleCellInput = document.getElementById('singleCellInput');

  if (fileInput) {
    fileInput.addEventListener('change', function(e) {
      if (e.target.files && e.target.files.length > 0) {
        handleBulkFiles(Array.from(e.target.files));
      }
    });
  }

  if (singleCellInput) {
    singleCellInput.addEventListener('change', function(e) {
      if (e.target.files && e.target.files[0] && state.activeCellIndex !== null) {
        var reader = new FileReader();
        var targetIndex = state.activeCellIndex;
        reader.onload = function(ev) {
          var img = new Image();
          img.onload = function() {
            state.slotImages[targetIndex] = img;
            updateFilledBadge();
            renderCanvas();
          };
          img.src = ev.target.result;
        };
        reader.readAsDataURL(e.target.files[0]);
      }
    });
  }

  function handleBulkFiles(files) {
    var loaded = 0;
    files.forEach(function(file) {
      var reader = new FileReader();
      reader.onload = function(ev) {
        var img = new Image();
        img.onload = function() {
          state.images.push(img);
          addPhotoToTray(ev.target.result);
          // Auto fill next available empty slot
          for (var i = 0; i < state.cells.length; i++) {
            if (!state.slotImages[i]) {
              state.slotImages[i] = img;
              break;
            }
          }
          loaded++;
          if (loaded === files.length) {
            updateFilledBadge();
            renderCanvas();
          }
        };
        img.src = ev.target.result;
      };
      reader.readAsDataURL(file);
    });
  }

  function addPhotoToTray(dataUrl) {
    var tray = document.getElementById('trayPhotosGrid');
    if (!tray) return;
    var img = document.createElement('img');
    img.src = dataUrl;
    img.className = 'tray-photo-thumb';
    tray.appendChild(img);
    var count = document.getElementById('photoCountBadge');
    if (count) count.textContent = state.images.length;
  }

  function updateFilledBadge() {
    var badge = document.getElementById('fillCountBadge');
    if (!badge) return;
    var filled = 0;
    for (var i = 0; i < state.cells.length; i++) {
      if (state.slotImages[i]) filled++;
    }
    badge.textContent = filled + ' / ' + state.cells.length + ' filled';
  }

  window.shuffleAllPhotos = function() {
    if (state.images.length === 0) return;
    var pool = state.images.slice();
    for (var i = pool.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var temp = pool[i];
      pool[i] = pool[j];
      pool[j] = temp;
    }
    state.cells.forEach(function(c, idx) {
      state.slotImages[idx] = pool[idx % pool.length];
    });
    updateFilledBadge();
    renderCanvas();
  };

  window.autoFillSlots = function() {
    if (state.images.length === 0) return;
    state.cells.forEach(function(c, idx) {
      state.slotImages[idx] = state.images[idx % state.images.length];
    });
    updateFilledBadge();
    renderCanvas();
  };

  window.clearAllCanvas = function() {
    if (confirm('Are you sure you want to clear the canvas and remove all photos?')) {
      state.images = [];
      state.slotImages = {};
      state.textLayers = [];
      state.stickers = [];
      var tray = document.getElementById('trayPhotosGrid');
      if (tray) tray.innerHTML = '';
      var count = document.getElementById('photoCountBadge');
      if (count) count.textContent = '0';
      updateFilledBadge();
      renderCanvas();
    }
  };

  // ══════════════════════════════════════════════════════════════════
  // 7. CELL CLICK & DRAG/DROP
  // ══════════════════════════════════════════════════════════════════
  canvas.addEventListener('click', function(e) {
    var rect = canvas.getBoundingClientRect();
    var scaleX = canvas.width / rect.width;
    var scaleY = canvas.height / rect.height;
    var clickX = (e.clientX - rect.left) * scaleX;
    var clickY = (e.clientY - rect.top) * scaleY;

    // Check which cell was clicked
    var W = canvas.width;
    var H = canvas.height;
    for (var i = 0; i < state.cells.length; i++) {
      var cell = state.cells[i];
      var cellX = cell.x * W;
      var cellY = cell.y * H;
      var cellW = cell.w * W;
      var cellH = cell.h * H;
      if (clickX >= cellX && clickX <= cellX + cellW && clickY >= cellY && clickY <= cellY + cellH) {
        state.activeCellIndex = i;
        if (singleCellInput) singleCellInput.click();
        break;
      }
    }
  });

  // ══════════════════════════════════════════════════════════════════
  // 8. STYLING, GAP, RADIUS, FILTERS
  // ══════════════════════════════════════════════════════════════════
  window.updateGapPro = function(val) {
    state.gap = parseInt(val);
    var el = document.getElementById('valGap');
    if (el) el.textContent = val + 'px';
    renderCanvas();
  };

  window.updateRadiusPro = function(val) {
    state.radius = parseInt(val);
    var el = document.getElementById('valRadius');
    if (el) el.textContent = val + 'px';
    renderCanvas();
  };

  window.updateMarginPro = function(val) {
    state.margin = parseInt(val);
    var el = document.getElementById('valMargin');
    if (el) el.textContent = val + 'px';
    renderCanvas();
  };

  window.setBgColorPro = function(hex, btn) {
    state.bgType = 'color';
    state.bgColor = hex;
    document.querySelectorAll('.color-swatch-item').forEach(function(s) { s.classList.remove('active'); });
    if (btn) btn.classList.add('active');
    renderCanvas();
  };

  window.applyGradientPro = function() {
    state.bgType = 'gradient';
    state.gradFrom = document.getElementById('gradFromColor').value;
    state.gradTo = document.getElementById('gradToColor').value;
    state.gradAngle = document.getElementById('gradAngleSelect').value;
    renderCanvas();
  };

  window.setFilterPro = function(filterKey, btn) {
    state.filter = filterKey;
    document.querySelectorAll('.filter-card-item').forEach(function(f) { f.classList.remove('active'); });
    if (btn) btn.classList.add('active');
    renderCanvas();
  };

  window.updateBrightnessPro = function(val) {
    state.brightness = parseInt(val);
    var el = document.getElementById('valBrightness');
    if (el) el.textContent = val + '%';
    renderCanvas();
  };

  window.updateContrastPro = function(val) {
    state.contrast = parseInt(val);
    var el = document.getElementById('valContrast');
    if (el) el.textContent = val + '%';
    renderCanvas();
  };

  window.updateSaturationPro = function(val) {
    state.saturation = parseInt(val);
    var el = document.getElementById('valSaturation');
    if (el) el.textContent = val + '%';
    renderCanvas();
  };

  // ══════════════════════════════════════════════════════════════════
  // 9. TEXT & STICKERS
  // ══════════════════════════════════════════════════════════════════
  window.addTextLayerPro = function() {
    var txtInput = document.getElementById('inputCaptionText');
    var fontSelect = document.getElementById('selectTextFont');
    var colorInput = document.getElementById('inputTextColor');
    if (!txtInput || !txtInput.value.trim()) return;

    state.textLayers.push({
      text: txtInput.value.trim(),
      font: fontSelect ? fontSelect.value : "'Plus Jakarta Sans', sans-serif",
      color: colorInput ? colorInput.value : "#ffffff",
      size: 42,
      x: state.canvasW / 2,
      y: state.canvasH - 40
    });
    txtInput.value = '';
    renderCanvas();
  };

  window.addStickerPro = function(emoji) {
    state.stickers.push({
      emoji: emoji,
      x: state.canvasW / 2,
      y: state.canvasH / 2,
      size: 54
    });
    renderCanvas();
  };

  // ══════════════════════════════════════════════════════════════════
  // 10. MASTER RENDER ENGINE (Retina Canvas 2D)
  // ══════════════════════════════════════════════════════════════════
  function renderCanvas() {
    var W = canvas.width;
    var H = canvas.height;

    // 1. Draw Background
    if (state.bgType === 'gradient') {
      var grad = ctx.createLinearGradient(0, 0, W, H);
      grad.addColorStop(0, state.gradFrom);
      grad.addColorStop(1, state.gradTo);
      ctx.fillStyle = grad;
    } else {
      ctx.fillStyle = state.bgColor;
    }
    ctx.fillRect(0, 0, W, H);

    // 2. Compute inner area considering outer margin
    var innerW = W - state.margin * 2;
    var innerH = H - state.margin * 2;
    var startX = state.margin;
    var startY = state.margin;

    // 3. Draw Each Cell
    state.cells.forEach(function(cell, idx) {
      var cellX = startX + cell.x * innerW + state.gap / 2;
      var cellY = startY + cell.y * innerH + state.gap / 2;
      var cellW = cell.w * innerW - state.gap;
      var cellH = cell.h * innerH - state.gap;

      if (cellW <= 0 || cellH <= 0) return;

      ctx.save();
      ctx.beginPath();
      if (ctx.roundRect) {
        ctx.roundRect(cellX, cellY, cellW, cellH, state.radius);
      } else {
        ctx.rect(cellX, cellY, cellW, cellH);
      }
      ctx.clip();

      var img = state.slotImages[idx];
      if (img && img.complete && img.naturalWidth > 0) {
        // Draw image aspect fill
        var imgAspect = img.naturalWidth / img.naturalHeight;
        var cellAspect = cellW / cellH;
        var drawW, drawH, drawX, drawY;

        if (imgAspect > cellAspect) {
          drawH = cellH;
          drawW = cellH * imgAspect;
          drawX = cellX + (cellW - drawW) / 2;
          drawY = cellY;
        } else {
          drawW = cellW;
          drawH = cellW / imgAspect;
          drawX = cellX;
          drawY = cellY + (cellH - drawH) / 2;
        }

        // Apply Shaders & Filters
        var filterStr = '';
        if (state.filter === 'vivid') filterStr += 'saturate(180%) contrast(110%) ';
        else if (state.filter === 'warm') filterStr += 'sepia(30%) saturate(140%) hue-rotate(-10deg) ';
        else if (state.filter === 'cool') filterStr += 'hue-rotate(180deg) saturate(110%) ';
        else if (state.filter === 'vintage') filterStr += 'sepia(60%) contrast(115%) brightness(95%) ';
        else if (state.filter === 'bw') filterStr += 'grayscale(100%) contrast(120%) ';
        else if (state.filter === 'noir') filterStr += 'grayscale(100%) contrast(160%) brightness(90%) ';
        else if (state.filter === 'cinematic') filterStr += 'contrast(125%) saturate(120%) ';

        filterStr += 'brightness(' + state.brightness + '%) contrast(' + state.contrast + '%) saturate(' + state.saturation + '%)';
        ctx.filter = filterStr;

        ctx.drawImage(img, drawX, drawY, drawW, drawH);
      } else {
        // Modern Empty Cell Placeholder
        ctx.fillStyle = "#eef2ff";
        ctx.fillRect(cellX, cellY, cellW, cellH);

        // Dashed circle
        var centerX = cellX + cellW / 2;
        var centerY = cellY + cellH / 2;
        var circleR = Math.min(26, Math.min(cellW, cellH) / 6);

        ctx.beginPath();
        ctx.arc(centerX, centerY - 8, circleR, 0, Math.PI * 2);
        ctx.fillStyle = "#ffffff";
        ctx.fill();
        ctx.strokeStyle = "#818cf8";
        ctx.lineWidth = 1.5;
        ctx.setLineDash([4, 4]);
        ctx.stroke();
        ctx.setLineDash([]);

        // Plus Icon
        ctx.fillStyle = "#6366f1";
        ctx.font = "bold 20px 'Plus Jakarta Sans', sans-serif";
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        ctx.fillText("+", centerX, centerY - 7);

        // Text label
        ctx.fillStyle = "#6366f1";
        ctx.font = "600 13px 'Plus Jakarta Sans', sans-serif";
        ctx.fillText("Tap to add photo", centerX, centerY + circleR + 10);
      }
      ctx.restore();
    });

    // 4. Draw Text Layers
    state.textLayers.forEach(function(layer) {
      ctx.save();
      ctx.font = "800 " + layer.size + "px " + layer.font;
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";

      // Shadow
      ctx.shadowColor = "rgba(0,0,0,0.6)";
      ctx.shadowBlur = 8;
      ctx.shadowOffsetX = 2;
      ctx.shadowOffsetY = 2;

      ctx.fillStyle = layer.color;
      ctx.fillText(layer.text, layer.x, layer.y);
      ctx.restore();
    });

    // 5. Draw Stickers
    state.stickers.forEach(function(stk) {
      ctx.save();
      ctx.font = stk.size + "px 'Plus Jakarta Sans', sans-serif";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText(stk.emoji, stk.x, stk.y);
      ctx.restore();
    });
  }

  // ══════════════════════════════════════════════════════════════════
  // 11. ZOOM CONTROLS
  // ══════════════════════════════════════════════════════════════════
  window.changeZoomPro = function(delta) {
    state.zoom = Math.max(0.3, Math.min(2.5, state.zoom + delta));
    applyZoom();
  };

  window.resetZoomPro = function() {
    state.zoom = 1.0;
    applyZoom();
  };

  function autoFitZoom() {
    var wrap = document.querySelector('.workspace-viewport');
    if (!wrap) return;
    var availW = wrap.clientWidth - 70;
    var availH = wrap.clientHeight - 70;
    var fitW = availW / state.canvasW;
    var fitH = availH / state.canvasH;
    state.zoom = Math.min(1.0, Math.min(fitW, fitH));
    applyZoom();
  }

  function applyZoom() {
    var el = document.getElementById('canvasShadowContainer');
    if (el) {
      el.style.transform = 'scale(' + state.zoom + ')';
    }
    var pctEl = document.getElementById('zoomPctBadge');
    if (pctEl) {
      pctEl.textContent = Math.round(state.zoom * 100) + '%';
    }
  }

  // ══════════════════════════════════════════════════════════════════
  // 12. EXPORT MODAL & 4K DOWNLOAD
  // ══════════════════════════════════════════════════════════════════
  var selectedExportFmt = 'png';

  window.openExportModalPro = function() {
    var modal = document.getElementById('proExportModal');
    if (modal) modal.style.display = 'flex';
  };

  window.closeExportModalPro = function() {
    var modal = document.getElementById('proExportModal');
    if (modal) modal.style.display = 'none';
  };

  window.setExportFmtPro = function(fmt, card) {
    selectedExportFmt = fmt;
    document.querySelectorAll('.export-card-opt').forEach(function(c) { c.classList.remove('active'); });
    if (card) card.classList.add('active');
    var qualityRow = document.getElementById('jpegQualityRow');
    if (qualityRow) {
      qualityRow.style.display = (fmt === 'jpg' || fmt === 'jpeg') ? 'block' : 'none';
    }
  };

  window.downloadCollagePro = function() {
    var scale = parseInt(document.getElementById('exportScaleSelect').value || 2);
    var filename = (document.getElementById('exportFilenameInput').value || 'photo-collage').trim();
    var quality = parseFloat(document.getElementById('jpegQualitySlider') ? document.getElementById('jpegQualitySlider').value : 95) / 100;

    // Render onto high-res export canvas
    var expCanvas = document.createElement('canvas');
    expCanvas.width = canvas.width * scale;
    expCanvas.height = canvas.height * scale;
    var expCtx = expCanvas.getContext('2d');
    expCtx.scale(scale, scale);

    // Render
    var oldCanvas = canvas;
    var oldCtx = ctx;
    canvas = expCanvas;
    ctx = expCtx;
    renderCanvas();
    canvas = oldCanvas;
    ctx = oldCtx;

    // Format handling
    var mime = 'image/png';
    if (selectedExportFmt === 'jpg' || selectedExportFmt === 'jpeg') mime = 'image/jpeg';
    else if (selectedExportFmt === 'webp') mime = 'image/webp';

    var dataUrl = expCanvas.toDataURL(mime, quality);

    if (selectedExportFmt === 'pdf' && window.jspdf) {
      var { jsPDF } = window.jspdf;
      var pdf = new jsPDF({
        orientation: expCanvas.width > expCanvas.height ? 'landscape' : 'portrait',
        unit: 'px',
        format: [canvas.width, canvas.height]
      });
      pdf.addImage(dataUrl, 'PNG', 0, 0, canvas.width, canvas.height);
      pdf.save(filename + '.pdf');
    } else {
      var a = document.createElement('a');
      a.download = filename + '.' + (selectedExportFmt === 'jpg' ? 'jpeg' : selectedExportFmt);
      a.href = dataUrl;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
    }

    closeExportModalPro();
  };

  // Initial Boot
  window.addEventListener('resize', autoFitZoom);
  setTimeout(function() {
    renderCanvas();
    autoFitZoom();
  }, 100);

})();
