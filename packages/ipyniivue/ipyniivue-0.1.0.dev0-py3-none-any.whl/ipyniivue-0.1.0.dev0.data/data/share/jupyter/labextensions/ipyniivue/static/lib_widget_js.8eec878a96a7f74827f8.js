(self["webpackChunkipyniivue"] = self["webpackChunkipyniivue"] || []).push([["lib_widget_js"],{

/***/ "./lib/utils.js":
/*!**********************!*\
  !*** ./lib/utils.js ***!
  \**********************/
/***/ ((__unused_webpack_module, exports) => {

"use strict";

Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.arrayBufferToBase64 = void 0;
//https://stackoverflow.com/a/9458996
function arrayBufferToBase64(buffer) {
    var binary = '';
    var bytes = new Uint8Array(buffer);
    var len = bytes.byteLength;
    for (var i = 0; i < len; i++) {
        binary += String.fromCharCode(bytes[i]);
    }
    return btoa(binary);
}
exports.arrayBufferToBase64 = arrayBufferToBase64;
//# sourceMappingURL=utils.js.map

/***/ }),

/***/ "./lib/version.js":
/*!************************!*\
  !*** ./lib/version.js ***!
  \************************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {

"use strict";

// Copyright (c) NiiVue
// Distributed under the terms of the Modified BSD License.
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.MODULE_NAME = exports.MODULE_VERSION = void 0;
// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-ignore
// eslint-disable-next-line @typescript-eslint/no-var-requires
const data = __webpack_require__(/*! ../package.json */ "./package.json");
/**
 * The _model_module_version/_view_module_version this package implements.
 *
 * The html widget manager assumes that this is the same as the npm package
 * version number.
 */
exports.MODULE_VERSION = data.version;
/*
 * The current package name.
 */
exports.MODULE_NAME = data.name;
//# sourceMappingURL=version.js.map

/***/ }),

/***/ "./lib/widget.js":
/*!***********************!*\
  !*** ./lib/widget.js ***!
  \***********************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";

// Copyright (c) NiiVue
// Distributed under the terms of the Modified BSD License.
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    Object.defineProperty(o, k2, { enumerable: true, get: function() { return m[k]; } });
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.NiivueView = exports.NiivueModel = void 0;
//Much of the structure and many of the functions/classes in this file
//are from https://github.com/martinRenou/ipycanvas. NiivueModel is based off of  CanvasModel and NiivueView is based off of CanvasView.
const niivue = __importStar(__webpack_require__(/*! @niivue/niivue */ "webpack/sharing/consume/default/@niivue/niivue/@niivue/niivue"));
const utils_1 = __webpack_require__(/*! ./utils */ "./lib/utils.js");
const base_1 = __webpack_require__(/*! @jupyter-widgets/base */ "webpack/sharing/consume/default/@jupyter-widgets/base");
const version_1 = __webpack_require__(/*! ./version */ "./lib/version.js");
__webpack_require__(/*! ../css/styles.css */ "./css/styles.css");
const COMMANDS = [
    'saveScene',
    'addVolumeFromUrl',
    'removeVolumeByUrl',
    'setCornerOrientationText',
    'setRadiologicalConvention',
    'setMeshThicknessOn2D',
    'setSliceMosaicString',
    'setSliceMM',
    'setHighResolutionCapable',
    'addVolume',
    'addMesh',
    'drawUndo',
    'loadDrawingFromUrl',
    'drawOtsu',
    'removeHaze',
    'saveImage',
    'setMeshProperty',
    'reverseFaces',
    'setMeshLayerProperty',
    'setPan2Dxyzmm',
    'setRenderAzimuthElevation',
    'setVolume',
    'removeVolume',
    'removeVolumeByIndex',
    'removeMesh',
    'removeMeshByUrl',
    'moveVolumeToBottom',
    'moveVolumeUp',
    'moveVolumeDown',
    'moveVolumeToTop',
    'setClipPlane',
    'setCrosshairColor',
    'setCrosshairWidth',
    'setDrawingEnabled',
    'setPenValue',
    'setDrawOpacity',
    'setSelectionBoxColor',
    'setSliceType',
    'setOpacity',
    'setScale',
    'setClipPlaneColor',
    'loadDocumentFromUrl',
    'loadVolumes',
    'addMeshFromUrl',
    'loadMeshes',
    'loadConnectome',
    'createEmptyDrawing',
    'drawGrowCut',
    'setMeshShader',
    'setCustomMeshShader',
    'updateGLVolume',
    'setColorMap',
    'setColorMapNegative',
    'setModulationImage',
    'setFrame4D',
    'setInterpolation',
    'moveCrosshairInVox',
    'drawMosaic',
    'addVolumeFromBase64'
];
function serializeImageData(array) {
    return new DataView(array.buffer.slice(0));
}
function deserializeImageData(dataview) {
    if (dataview === null) {
        return null;
    }
    return new Uint8ClampedArray(dataview.buffer);
}
class NiivueModel extends base_1.DOMWidgetModel {
    constructor() {
        super(...arguments);
        this.currentProcessing = Promise.resolve();
    }
    //for drawing things
    defaults() {
        return Object.assign(Object.assign({}, super.defaults()), { _model_name: NiivueModel.model_name, _model_module: NiivueModel.model_module, _model_module_version: NiivueModel.model_module_version, _view_name: NiivueModel.view_name, _view_module: NiivueModel.view_module, _view_module_version: NiivueModel.view_module_version, height: 480, width: 640 });
    }
    initialize(attributes, options) {
        super.initialize(attributes, options);
        this.on('msg:custom', (command, buffers) => {
            this.currentProcessing = this.currentProcessing.then(() => __awaiter(this, void 0, void 0, function* () {
                yield this.onCommand(command, buffers);
            }));
        });
        this.createNV();
    }
    onCommand(command, buffers) {
        return __awaiter(this, void 0, void 0, function* () {
            const name = COMMANDS[command[0]];
            const args = command[1];
            switch (name) {
                case 'saveScene':
                    this.nv.saveScene(args[0]);
                    break;
                case 'addVolumeFromUrl':
                    this.nv.addVolumeFromUrl({ url: args[0] });
                    break;
                case 'removeVolumeByUrl':
                    this.nv.removeVolumeByUrl(args[0]);
                    break;
                case 'setCornerOrientationText':
                    this.nv.setCornerOrientationText(args[0]);
                    break;
                case 'setRadiologicalConvention':
                    this.nv.setRadiologicalConvention(args[0]);
                    break;
                case 'setMeshThicknessOn2D':
                    this.nv.setMeshThicknessOn2D(args[0]);
                    break;
                case 'setSliceMosaicString':
                    this.nv.setSliceMosaicString(args[0]);
                    break;
                case 'setSliceMM':
                    this.nv.setSliceMM(args[0]);
                    break;
                case 'setHighResolutionCapable':
                    this.nv.setHighResolutionCapable(args[0]);
                    break;
                case 'addVolume':
                    this.nv.addVolume(args[0]);
                    break;
                case 'addMesh':
                    this.nv.addMesh(args[0]);
                    break;
                case 'drawUndo':
                    this.nv.drawUndo();
                    break;
                case 'loadDrawingFromUrl':
                    this.nv.loadDrawingFromUrl(args[0]);
                    break;
                case 'drawOtsu':
                    this.nv.drawOtsu(args[0]);
                    break;
                case 'removeHaze':
                    this.nv.removeHaze(args[0], args[1]);
                    break;
                case 'saveImage':
                    this.nv.saveImage(args[0], args[1]);
                    break;
                case 'setMeshProperty':
                    this.nv.setMeshProperty(args[0], args[1], args[2]);
                    break;
                case 'reverseFaces':
                    this.nv.reverseFaces(args[0]);
                    break;
                case 'setMeshLayerProperty':
                    this.nv.setMeshLayerProperty(args[0], args[1], args[2], args[3]);
                    break;
                case 'setPan2Dxyzmm':
                    this.nv.setPan2Dxyzmm(args[0]);
                    break;
                case 'setRenderAzimuthElevation':
                    this.nv.setRenderAzimuthElevation(args[0], args[1]);
                    break;
                case 'setVolume':
                    this.nv.setVolume(args[0], args[1]);
                    break;
                case 'removeVolume':
                    this.nv.removeVolume(args[0]);
                    break;
                case 'removeVolumeByIndex':
                    this.nv.removeVolumeByIndex(args[0]);
                    break;
                case 'removeMesh':
                    this.nv.removeMesh(args[0]);
                    break;
                case 'removeMeshByUrl':
                    this.nv.removeMeshByUrl(args[0]);
                    break;
                case 'moveVolumeToBottom':
                    this.nv.moveVolumeToBottom(args[0]);
                    break;
                case 'moveVolumeUp':
                    this.nv.moveVolumeUp(args[0]);
                    break;
                case 'moveVolumeDown':
                    this.nv.moveVolumeDown(args[0]);
                    break;
                case 'moveVolumeToTop':
                    this.nv.moveVolumeToTop(args[0]);
                    break;
                case 'setClipPlane':
                    this.nv.setClipPlane(args[0]);
                    break;
                case 'setCrosshairColor':
                    this.nv.setCrosshairColor(args[0]);
                    break;
                case 'setCrosshairWidth':
                    this.nv.setCrosshairWidth(args[0]);
                    break;
                case 'setDrawingEnabled':
                    this.nv.setDrawingEnabled(args[0]);
                    break;
                case 'setPenValue':
                    this.nv.setPenValue(args[0], args[1]);
                    break;
                case 'setDrawOpacity':
                    this.nv.setDrawOpacity(args[0]);
                    break;
                case 'setSelectionBoxColor':
                    this.nv.setSelectionBoxColor(args[0]);
                    break;
                case 'setSliceType':
                    this.nv.setSliceType(args[0]);
                    break;
                case 'setOpacity':
                    this.nv.setOpacity(args[0], args[1]);
                    break;
                case 'setScale':
                    this.nv.setScale(args[0]);
                    break;
                case 'setClipPlaneColor':
                    this.nv.setClipPlaneColor(args[0]);
                    break;
                case 'loadDocumentFromUrl':
                    this.nv.loadDocumentFromUrl(args[0]);
                    break;
                case 'loadVolumes':
                    this.nv.loadVolumes(args[0]);
                    break;
                case 'addMeshFromUrl':
                    this.nv.addMeshFromUrl(args[0]);
                    break;
                case 'loadMeshes':
                    this.nv.loadMeshes(args[0]);
                    break;
                case 'loadConnectome':
                    this.nv.loadConnectome(args[0]);
                    break;
                case 'createEmptyDrawing':
                    this.nv.createEmptyDrawing();
                    break;
                case 'drawGrowCut':
                    this.nv.drawGrowCut();
                    break;
                case 'setMeshShader':
                    this.nv.setMeshShader(args[0], args[1]);
                    break;
                case 'setCustomMeshShader':
                    this.nv.setCustomMeshShader(args[0], args[1]);
                    break;
                case 'updateGLVolume':
                    this.nv.updateGLVolume();
                    break;
                case 'setColorMap':
                    this.nv.setColorMap(args[0], args[1]);
                    break;
                case 'setColorMapNegative':
                    this.nv.setColorMapNegative(args[0], args[1]);
                    break;
                case 'setModulationImage':
                    this.nv.setModulationImage(args[0], args[1], args[2]);
                    break;
                case 'setFrame4D':
                    this.nv.setFrame4D(args[0], args[1]);
                    break;
                case 'setInterpolation':
                    this.nv.setInterpolation(args[0]);
                    break;
                case 'moveCrosshairInVox':
                    this.nv.moveCrosshairInVox(args[0], args[1], args[2]);
                    break;
                case 'drawMosaic':
                    this.nv.drawMosaic(args[0]);
                    break;
                case 'addVolumeFromBase64':
                    this.nv.addVolume(niivue.NVImage.loadFromBase64({ name: args[0], base64: utils_1.arrayBufferToBase64(buffers[0].buffer) }));
                    break;
            }
        });
    }
    createNV() {
        return __awaiter(this, void 0, void 0, function* () {
            this.nv = new niivue.Niivue({
                isResizeCanvas: false,
                logging: true,
                textHeight: this.get('text_height'),
                colorbarHeight: this.get('colorbar_height'),
                colorbarMargin: this.get('colorbar_margin'),
                crosshairWidth: this.get('crosshair_width'),
                rulerWidth: this.get('ruler_width'),
                backColor: this.get('back_color'),
                crosshairColor: this.get('crosshair_color'),
                fontColor: this.get('font_color'),
                selectionBoxColor: this.get('selection_box_color'),
                clipPlaneColor: this.get('clip_plane_color'),
                rulerColor: this.get('ruler_color'),
                show3Dcrosshair: this.get('show_3D_crosshair'),
                trustCalMinMax: this.get('trust_cal_min_max'),
                clipPlaneHotKey: this.get('clip_plane_hot_key'),
                viewModeHotKey: this.get('view_mode_hot_key'),
                keyDebounceTime: this.get('key_debounce_time'),
                doubleTouchTimeout: this.get('double_touch_timeout'),
                longTouchTimeout: this.get('long_touch_timeout'),
                isRadiologicalConvention: this.get('is_radiological_convention'),
                loadingText: this.get('loading_text'),
                dragAndDropEnabled: this.get('drag_and_drop_enabled'),
                isNearestInterpolation: this.get('is_nearest_interpolation'),
                isAtlasOutline: this.get('is_atlas_outline'),
                isRuler: this.get('is_ruler'),
                isColorbar: this.get('is_colorbar'),
                isOrientCube: this.get('is_orient_cube'),
                multiplanarPadPixels: this.get('multiplanar_pad_pixels'),
                multiplanarForceRender: this.get('multiplanar_force_render'),
                meshThicknessOn2D: this.get('mesh_thickness_on_2D') == 1.7976931348623157e+308 ? undefined : this.get('mesh_thickness_on_2D'),
                dragMode: this.get('drag_mode'),
                isDepthPickMesh: this.get('is_depth_pick_mesh'),
                isCornerOrientationText: this.get('is_corner_orientation_text'),
                sagittalNoseLeft: this.get('sagittal_nose_left'),
                isSliceMM: this.get('is_slice_MM'),
                isHighResolutionCapable: this.get('is_high_resolution_capable'),
                drawingEnabled: this.get('drawing_enabled'),
                penValue: this.get('pen_value') == 1.7976931348623157e+308 ? undefined : this.get('pen_value'),
                isFilledPen: this.get('is_filled_pen'),
                maxDrawUndoBitmaps: this.get('max_draw_undo_bitmaps'),
                thumbnail: this.get('thumbnail')
            });
        });
    }
}
exports.NiivueModel = NiivueModel;
NiivueModel.serializers = Object.assign(Object.assign({}, base_1.DOMWidgetModel.serializers), { _canvas_manager: { deserialize: base_1.unpack_models }, image_data: {
        serialize: serializeImageData,
        deserialize: deserializeImageData
    } });
NiivueModel.model_name = 'NiivueModel';
NiivueModel.model_module = version_1.MODULE_NAME;
NiivueModel.model_module_version = version_1.MODULE_VERSION;
NiivueModel.view_name = 'NiivueView'; // Set to null if no view
NiivueModel.view_module = version_1.MODULE_NAME; // Set to null if no view
NiivueModel.view_module_version = version_1.MODULE_VERSION;
class NiivueView extends base_1.DOMWidgetView {
    //for changing things / listening to callbacks
    render() {
        //reason for canvas creation being in here is 2-fold
        //1) NiivueVIEW
        //2) https://ipywidgets.readthedocs.io/en/7.7.0/examples/Widget%20Low%20Level.html#Models-and-Views
        //   "Multiple WidgetViews can be linked to a single WidgetModel. This is how you can redisplay the same Widget multiple times and it still works."    
        this.canvas = document.createElement('canvas');
        this.canvas.classList.add('niivue-widget');
        this.resize();
        this.updateCanvas();
        //this.value_changed();
        this.model.on_some_change(['width', 'height'], this.resize, this);
        //this.model.on('change:value', this.value_changed, this);
    }
    resize() {
        //resize div
        this.el.setAttribute('width', this.model.get('width'));
        this.el.setAttribute('height', this.model.get('height'));
        this.el.setAttribute('style', `width: ${this.model.get('width')}px; height: ${this.model.get('height')}px;`);
        //resize canvas
        this.canvas.setAttribute('width', this.model.get('width'));
        this.canvas.setAttribute('height', this.model.get('height'));
        this.canvas.setAttribute('style', `width: ${this.model.get('width')}px; height: ${this.model.get('height')};`);
        //redraw
        this.model.nv.drawScene();
    }
    updateCanvas() {
        this.el.appendChild(this.canvas);
        this.model.nv.attachToCanvas(this.canvas);
        this.el.style.backgroundColor = 'transparent';
    }
    //proof of concept - can have updates from variable changes
    value_changed() {
        this.model.nv.loadVolumes([{ url: this.model.get("value") }]);
    }
    //this makes this.el become a custom tag (div in this case). Technically this is not necessary.
    preinitialize() {
        this.tagName = 'div';
    }
}
exports.NiivueView = NiivueView;
//# sourceMappingURL=widget.js.map

/***/ }),

/***/ "./node_modules/css-loader/dist/cjs.js!./css/styles.css":
/*!**************************************************************!*\
  !*** ./node_modules/css-loader/dist/cjs.js!./css/styles.css ***!
  \**************************************************************/
/***/ ((module, exports, __webpack_require__) => {

// Imports
var ___CSS_LOADER_API_IMPORT___ = __webpack_require__(/*! ../node_modules/css-loader/dist/runtime/api.js */ "./node_modules/css-loader/dist/runtime/api.js");
exports = ___CSS_LOADER_API_IMPORT___(false);
// Module
exports.push([module.id, "canvas.niivue-widget {\n  cursor: crosshair;\n}", ""]);
// Exports
module.exports = exports;


/***/ }),

/***/ "./node_modules/css-loader/dist/runtime/api.js":
/*!*****************************************************!*\
  !*** ./node_modules/css-loader/dist/runtime/api.js ***!
  \*****************************************************/
/***/ ((module) => {

"use strict";


/*
  MIT License http://www.opensource.org/licenses/mit-license.php
  Author Tobias Koppers @sokra
*/
// css base code, injected by the css-loader
// eslint-disable-next-line func-names
module.exports = function (useSourceMap) {
  var list = []; // return the list of modules as css string

  list.toString = function toString() {
    return this.map(function (item) {
      var content = cssWithMappingToString(item, useSourceMap);

      if (item[2]) {
        return "@media ".concat(item[2], " {").concat(content, "}");
      }

      return content;
    }).join('');
  }; // import a list of modules into the list
  // eslint-disable-next-line func-names


  list.i = function (modules, mediaQuery, dedupe) {
    if (typeof modules === 'string') {
      // eslint-disable-next-line no-param-reassign
      modules = [[null, modules, '']];
    }

    var alreadyImportedModules = {};

    if (dedupe) {
      for (var i = 0; i < this.length; i++) {
        // eslint-disable-next-line prefer-destructuring
        var id = this[i][0];

        if (id != null) {
          alreadyImportedModules[id] = true;
        }
      }
    }

    for (var _i = 0; _i < modules.length; _i++) {
      var item = [].concat(modules[_i]);

      if (dedupe && alreadyImportedModules[item[0]]) {
        // eslint-disable-next-line no-continue
        continue;
      }

      if (mediaQuery) {
        if (!item[2]) {
          item[2] = mediaQuery;
        } else {
          item[2] = "".concat(mediaQuery, " and ").concat(item[2]);
        }
      }

      list.push(item);
    }
  };

  return list;
};

function cssWithMappingToString(item, useSourceMap) {
  var content = item[1] || ''; // eslint-disable-next-line prefer-destructuring

  var cssMapping = item[3];

  if (!cssMapping) {
    return content;
  }

  if (useSourceMap && typeof btoa === 'function') {
    var sourceMapping = toComment(cssMapping);
    var sourceURLs = cssMapping.sources.map(function (source) {
      return "/*# sourceURL=".concat(cssMapping.sourceRoot || '').concat(source, " */");
    });
    return [content].concat(sourceURLs).concat([sourceMapping]).join('\n');
  }

  return [content].join('\n');
} // Adapted from convert-source-map (MIT)


function toComment(sourceMap) {
  // eslint-disable-next-line no-undef
  var base64 = btoa(unescape(encodeURIComponent(JSON.stringify(sourceMap))));
  var data = "sourceMappingURL=data:application/json;charset=utf-8;base64,".concat(base64);
  return "/*# ".concat(data, " */");
}

/***/ }),

/***/ "./css/styles.css":
/*!************************!*\
  !*** ./css/styles.css ***!
  \************************/
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var api = __webpack_require__(/*! !../node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js */ "./node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js");
            var content = __webpack_require__(/*! !!../node_modules/css-loader/dist/cjs.js!./styles.css */ "./node_modules/css-loader/dist/cjs.js!./css/styles.css");

            content = content.__esModule ? content.default : content;

            if (typeof content === 'string') {
              content = [[module.id, content, '']];
            }

var options = {};

options.insert = "head";
options.singleton = false;

var update = api(content, options);



module.exports = content.locals || {};

/***/ }),

/***/ "./node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js":
/*!****************************************************************************!*\
  !*** ./node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js ***!
  \****************************************************************************/
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var isOldIE = function isOldIE() {
  var memo;
  return function memorize() {
    if (typeof memo === 'undefined') {
      // Test for IE <= 9 as proposed by Browserhacks
      // @see http://browserhacks.com/#hack-e71d8692f65334173fee715c222cb805
      // Tests for existence of standard globals is to allow style-loader
      // to operate correctly into non-standard environments
      // @see https://github.com/webpack-contrib/style-loader/issues/177
      memo = Boolean(window && document && document.all && !window.atob);
    }

    return memo;
  };
}();

var getTarget = function getTarget() {
  var memo = {};
  return function memorize(target) {
    if (typeof memo[target] === 'undefined') {
      var styleTarget = document.querySelector(target); // Special case to return head of iframe instead of iframe itself

      if (window.HTMLIFrameElement && styleTarget instanceof window.HTMLIFrameElement) {
        try {
          // This will throw an exception if access to iframe is blocked
          // due to cross-origin restrictions
          styleTarget = styleTarget.contentDocument.head;
        } catch (e) {
          // istanbul ignore next
          styleTarget = null;
        }
      }

      memo[target] = styleTarget;
    }

    return memo[target];
  };
}();

var stylesInDom = [];

function getIndexByIdentifier(identifier) {
  var result = -1;

  for (var i = 0; i < stylesInDom.length; i++) {
    if (stylesInDom[i].identifier === identifier) {
      result = i;
      break;
    }
  }

  return result;
}

function modulesToDom(list, options) {
  var idCountMap = {};
  var identifiers = [];

  for (var i = 0; i < list.length; i++) {
    var item = list[i];
    var id = options.base ? item[0] + options.base : item[0];
    var count = idCountMap[id] || 0;
    var identifier = "".concat(id, " ").concat(count);
    idCountMap[id] = count + 1;
    var index = getIndexByIdentifier(identifier);
    var obj = {
      css: item[1],
      media: item[2],
      sourceMap: item[3]
    };

    if (index !== -1) {
      stylesInDom[index].references++;
      stylesInDom[index].updater(obj);
    } else {
      stylesInDom.push({
        identifier: identifier,
        updater: addStyle(obj, options),
        references: 1
      });
    }

    identifiers.push(identifier);
  }

  return identifiers;
}

function insertStyleElement(options) {
  var style = document.createElement('style');
  var attributes = options.attributes || {};

  if (typeof attributes.nonce === 'undefined') {
    var nonce =  true ? __webpack_require__.nc : 0;

    if (nonce) {
      attributes.nonce = nonce;
    }
  }

  Object.keys(attributes).forEach(function (key) {
    style.setAttribute(key, attributes[key]);
  });

  if (typeof options.insert === 'function') {
    options.insert(style);
  } else {
    var target = getTarget(options.insert || 'head');

    if (!target) {
      throw new Error("Couldn't find a style target. This probably means that the value for the 'insert' parameter is invalid.");
    }

    target.appendChild(style);
  }

  return style;
}

function removeStyleElement(style) {
  // istanbul ignore if
  if (style.parentNode === null) {
    return false;
  }

  style.parentNode.removeChild(style);
}
/* istanbul ignore next  */


var replaceText = function replaceText() {
  var textStore = [];
  return function replace(index, replacement) {
    textStore[index] = replacement;
    return textStore.filter(Boolean).join('\n');
  };
}();

function applyToSingletonTag(style, index, remove, obj) {
  var css = remove ? '' : obj.media ? "@media ".concat(obj.media, " {").concat(obj.css, "}") : obj.css; // For old IE

  /* istanbul ignore if  */

  if (style.styleSheet) {
    style.styleSheet.cssText = replaceText(index, css);
  } else {
    var cssNode = document.createTextNode(css);
    var childNodes = style.childNodes;

    if (childNodes[index]) {
      style.removeChild(childNodes[index]);
    }

    if (childNodes.length) {
      style.insertBefore(cssNode, childNodes[index]);
    } else {
      style.appendChild(cssNode);
    }
  }
}

function applyToTag(style, options, obj) {
  var css = obj.css;
  var media = obj.media;
  var sourceMap = obj.sourceMap;

  if (media) {
    style.setAttribute('media', media);
  } else {
    style.removeAttribute('media');
  }

  if (sourceMap && typeof btoa !== 'undefined') {
    css += "\n/*# sourceMappingURL=data:application/json;base64,".concat(btoa(unescape(encodeURIComponent(JSON.stringify(sourceMap)))), " */");
  } // For old IE

  /* istanbul ignore if  */


  if (style.styleSheet) {
    style.styleSheet.cssText = css;
  } else {
    while (style.firstChild) {
      style.removeChild(style.firstChild);
    }

    style.appendChild(document.createTextNode(css));
  }
}

var singleton = null;
var singletonCounter = 0;

function addStyle(obj, options) {
  var style;
  var update;
  var remove;

  if (options.singleton) {
    var styleIndex = singletonCounter++;
    style = singleton || (singleton = insertStyleElement(options));
    update = applyToSingletonTag.bind(null, style, styleIndex, false);
    remove = applyToSingletonTag.bind(null, style, styleIndex, true);
  } else {
    style = insertStyleElement(options);
    update = applyToTag.bind(null, style, options);

    remove = function remove() {
      removeStyleElement(style);
    };
  }

  update(obj);
  return function updateStyle(newObj) {
    if (newObj) {
      if (newObj.css === obj.css && newObj.media === obj.media && newObj.sourceMap === obj.sourceMap) {
        return;
      }

      update(obj = newObj);
    } else {
      remove();
    }
  };
}

module.exports = function (list, options) {
  options = options || {}; // Force single-tag solution on IE6-9, which has a hard limit on the # of <style>
  // tags it will allow on a page

  if (!options.singleton && typeof options.singleton !== 'boolean') {
    options.singleton = isOldIE();
  }

  list = list || [];
  var lastIdentifiers = modulesToDom(list, options);
  return function update(newList) {
    newList = newList || [];

    if (Object.prototype.toString.call(newList) !== '[object Array]') {
      return;
    }

    for (var i = 0; i < lastIdentifiers.length; i++) {
      var identifier = lastIdentifiers[i];
      var index = getIndexByIdentifier(identifier);
      stylesInDom[index].references--;
    }

    var newLastIdentifiers = modulesToDom(newList, options);

    for (var _i = 0; _i < lastIdentifiers.length; _i++) {
      var _identifier = lastIdentifiers[_i];

      var _index = getIndexByIdentifier(_identifier);

      if (stylesInDom[_index].references === 0) {
        stylesInDom[_index].updater();

        stylesInDom.splice(_index, 1);
      }
    }

    lastIdentifiers = newLastIdentifiers;
  };
};

/***/ }),

/***/ "./package.json":
/*!**********************!*\
  !*** ./package.json ***!
  \**********************/
/***/ ((module) => {

"use strict";
module.exports = JSON.parse('{"name":"ipyniivue","version":"0.1.0","description":"NiiVue Jupyter Library","keywords":["jupyter","jupyterlab","jupyterlab-extension","widgets"],"files":["lib/**/*.js","dist/*.js","css/*.css"],"homepage":"https://github.com/niivue/ipyniivue","bugs":{"url":"https://github.com/niivue/ipyniivue/issues"},"license":"BSD-3-Clause","author":{"name":"NiiVue"},"main":"lib/index.js","types":"./lib/index.d.ts","repository":{"type":"git","url":"https://github.com/niivue/ipyniivue"},"scripts":{"install":"npm install --prefix ./niivue && npm run --prefix ./niivue build && npm install ./niivue","build":"yarn run build:lib && yarn run build:nbextension && yarn run build:labextension:dev","build:prod":"yarn run build:lib && yarn run build:nbextension && yarn run build:labextension","build:labextension":"jupyter labextension build .","build:labextension:dev":"jupyter labextension build --development True .","build:lib":"tsc","build:nbextension":"webpack","clean":"yarn run clean:lib && yarn run clean:nbextension && yarn run clean:labextension","clean:lib":"rimraf lib","clean:labextension":"rimraf ipyniivue/labextension","clean:nbextension":"rimraf ipyniivue/nbextension/static/index.js","lint":"eslint . --ext .ts,.tsx --fix","lint:check":"eslint . --ext .ts,.tsx","prepack":"yarn run build:lib","test":"jest","watch":"npm-run-all -p watch:*","watch:lib":"tsc -w","watch:nbextension":"webpack --watch --mode=development","watch:labextension":"jupyter labextension watch ."},"dependencies":{"@jupyter-widgets/base":"^1.1.10 || ^2 || ^3 || ^4 || ^5 || ^6","@niivue/niivue":"file:niivue","buffer":"^6.0.3"},"devDependencies":{"@babel/core":"^7.5.0","@babel/preset-env":"^7.5.0","@jupyter-widgets/base-manager":"^1.0.2","@jupyterlab/builder":"^3.0.0","@lumino/application":"^1.6.0","@lumino/widgets":"^1.6.0","@types/jest":"^26.0.0","@types/webpack-env":"^1.13.6","@typescript-eslint/eslint-plugin":"^3.6.0","@typescript-eslint/parser":"^3.6.0","acorn":"^7.2.0","css-loader":"^3.2.0","eslint":"^7.4.0","eslint-config-prettier":"^6.11.0","eslint-plugin-prettier":"^3.1.4","fs-extra":"^7.0.0","identity-obj-proxy":"^3.0.0","jest":"^26.0.0","mkdirp":"^0.5.1","npm-run-all":"^4.1.3","prettier":"^2.0.5","rimraf":"^2.6.2","source-map-loader":"^1.1.3","style-loader":"^1.0.0","ts-jest":"^26.0.0","ts-loader":"^8.0.0","typescript":"~4.1.3","webpack":"^5.61.0","webpack-cli":"^4.0.0"},"jupyterlab":{"extension":"lib/plugin","outputDir":"ipyniivue/labextension/","sharedPackages":{"@jupyter-widgets/base":{"bundled":false,"singleton":true}}}}');

/***/ })

}]);
//# sourceMappingURL=lib_widget_js.8eec878a96a7f74827f8.js.map