"use strict";function _interopRequireDefault(e){return e&&e.__esModule?e:{"default":e}}Object.defineProperty(exports,"__esModule",{value:!0});var _getIterator2=require("babel-runtime/core-js/get-iterator"),_getIterator3=_interopRequireDefault(_getIterator2),_regenerator=require("babel-runtime/regenerator"),_regenerator2=_interopRequireDefault(_regenerator),_asyncToGenerator2=require("babel-runtime/helpers/asyncToGenerator"),_asyncToGenerator3=_interopRequireDefault(_asyncToGenerator2),invokeScripts=function(){var e=(0,_asyncToGenerator3["default"])(_regenerator2["default"].mark(function r(e){var t,n;return _regenerator2["default"].wrap(function(r){for(;;)switch(r.prev=r.next){case 0:if(t=require(_path2["default"].join(e,"package.json")),n=_fs2["default"].readdirSync(e),t.scripts||(t.scripts={}),n.indexOf("binding.gyp")>-1&&!t.scripts.install&&(t.scripts.install="node-gyp rebuild"),!(t.scripts.preinstall||t.scripts.install||t.scripts.postinstall)){r.next=15;break}return r.prev=5,r.next=8,(0,_expose.exposeScripts)(_path2["default"].join(e,"node_modules"));case 8:return r.next=10,(0,_run2["default"])(e,t,"install");case 10:r.next=15;break;case 12:r.prev=12,r.t0=r["catch"](5),console.log(r.t0);case 15:case"end":return r.stop()}},r,this,[[5,12]])}));return function(r){return e.apply(this,arguments)}}(),_fs=require("fs"),_fs2=_interopRequireDefault(_fs),_path=require("path"),_path2=_interopRequireDefault(_path),_expose=require("./expose"),_run=require("./run"),_run2=_interopRequireDefault(_run);exports["default"]=function(){function e(e){return r.apply(this,arguments)}var r=(0,_asyncToGenerator3["default"])(_regenerator2["default"].mark(function t(r){var n,a,s,i,u,o,c,p,f,l,_,d;return _regenerator2["default"].wrap(function(t){for(;;)switch(t.prev=t.next){case 0:n=!0,a=!1,s=void 0,t.prev=3,i=(0,_getIterator3["default"])(r);case 5:if(n=(u=i.next()).done){t.next=13;break}if(o=u.value,!o.finalDest){t.next=10;break}return t.next=10,invokeScripts(o.finalDest);case 10:n=!0,t.next=5;break;case 13:t.next=19;break;case 15:t.prev=15,t.t0=t["catch"](3),a=!0,s=t.t0;case 19:t.prev=19,t.prev=20,!n&&i["return"]&&i["return"]();case 22:if(t.prev=22,!a){t.next=25;break}throw s;case 25:return t.finish(22);case 26:return t.finish(19);case 27:c=!0,p=!1,f=void 0,t.prev=30,l=(0,_getIterator3["default"])(r);case 32:if(c=(_=l.next()).done){t.next=40;break}if(d=_.value,!d.dependencies){t.next=37;break}return t.next=37,e(d.dependencies);case 37:c=!0,t.next=32;break;case 40:t.next=46;break;case 42:t.prev=42,t.t1=t["catch"](30),p=!0,f=t.t1;case 46:t.prev=46,t.prev=47,!c&&l["return"]&&l["return"]();case 49:if(t.prev=49,!p){t.next=52;break}throw f;case 52:return t.finish(49);case 53:return t.finish(46);case 54:case"end":return t.stop()}},t,this,[[3,15,19,27],[20,,22,26],[30,42,46,54],[47,,49,53]])}));return e}();