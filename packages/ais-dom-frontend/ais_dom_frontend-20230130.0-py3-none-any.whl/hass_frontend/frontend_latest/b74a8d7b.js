/*! For license information please see b74a8d7b.js.LICENSE.txt */
"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[14930,95337],{55020:(e,t,r)=>{r.d(t,{j:()=>n});var i={};function n(){return i}},23682:(e,t,r)=>{function i(e,t){if(t.length<e)throw new TypeError(e+" argument"+(e>1?"s":"")+" required, but only "+t.length+" present")}r.d(t,{Z:()=>i})},86102:(e,t,r)=>{r.d(t,{u:()=>n});var i={ceil:Math.ceil,round:Math.round,floor:Math.floor,trunc:function(e){return e<0?Math.ceil(e):Math.floor(e)}};function n(e){return e?i[e]:i.trunc}},90394:(e,t,r)=>{function i(e){if(null===e||!0===e||!1===e)return NaN;var t=Number(e);return isNaN(t)?t:t<0?Math.ceil(t):Math.floor(t)}r.d(t,{Z:()=>i})},4535:(e,t,r)=>{r.d(t,{Z:()=>d});var i=r(34327);function n(e){var t=new Date(Date.UTC(e.getFullYear(),e.getMonth(),e.getDate(),e.getHours(),e.getMinutes(),e.getSeconds(),e.getMilliseconds()));return t.setUTCFullYear(e.getFullYear()),e.getTime()-t.getTime()}var o=r(59429),a=r(23682),s=864e5;function l(e,t){(0,a.Z)(2,arguments);var r=(0,o.Z)(e),i=(0,o.Z)(t),l=r.getTime()-n(r),c=i.getTime()-n(i);return Math.round((l-c)/s)}function c(e,t){var r=e.getFullYear()-t.getFullYear()||e.getMonth()-t.getMonth()||e.getDate()-t.getDate()||e.getHours()-t.getHours()||e.getMinutes()-t.getMinutes()||e.getSeconds()-t.getSeconds()||e.getMilliseconds()-t.getMilliseconds();return r<0?-1:r>0?1:r}function d(e,t){(0,a.Z)(2,arguments);var r=(0,i.Z)(e),n=(0,i.Z)(t),o=c(r,n),s=Math.abs(l(r,n));r.setDate(r.getDate()-o*s);var d=Number(c(r,n)===-o),p=o*(s-d);return 0===p?0:p}},35040:(e,t,r)=>{r.d(t,{Z:()=>a});var i=r(4535),n=r(23682),o=r(86102);function a(e,t,r){(0,n.Z)(2,arguments);var a=(0,i.Z)(e,t)/7;return(0,o.u)(null==r?void 0:r.roundingMethod)(a)}},59429:(e,t,r)=>{r.d(t,{Z:()=>o});var i=r(34327),n=r(23682);function o(e){(0,n.Z)(1,arguments);var t=(0,i.Z)(e);return t.setHours(0,0,0,0),t}},59401:(e,t,r)=>{r.d(t,{Z:()=>s});var i=r(34327),n=r(90394),o=r(23682),a=r(55020);function s(e,t){var r,s,l,c,d,p,u,f;(0,o.Z)(1,arguments);var h=(0,a.j)(),m=(0,n.Z)(null!==(r=null!==(s=null!==(l=null!==(c=null==t?void 0:t.weekStartsOn)&&void 0!==c?c:null==t||null===(d=t.locale)||void 0===d||null===(p=d.options)||void 0===p?void 0:p.weekStartsOn)&&void 0!==l?l:h.weekStartsOn)&&void 0!==s?s:null===(u=h.locale)||void 0===u||null===(f=u.options)||void 0===f?void 0:f.weekStartsOn)&&void 0!==r?r:0);if(!(m>=0&&m<=6))throw new RangeError("weekStartsOn must be between 0 and 6 inclusively");var y=(0,i.Z)(e),v=y.getDay(),g=(v<m?7:0)+v-m;return y.setDate(y.getDate()-g),y.setHours(0,0,0,0),y}},34327:(e,t,r)=>{r.d(t,{Z:()=>o});var i=r(23682);function n(e){return n="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},n(e)}function o(e){(0,i.Z)(1,arguments);var t=Object.prototype.toString.call(e);return e instanceof Date||"object"===n(e)&&"[object Date]"===t?new Date(e.getTime()):"number"==typeof e||"[object Number]"===t?new Date(e):("string"!=typeof e&&"[object String]"!==t||"undefined"==typeof console||(console.warn("Starting with v2.0.0-beta.1 date-fns doesn't accept strings as date arguments. Please use `parseISO` to parse strings. See: https://github.com/date-fns/date-fns/blob/master/docs/upgradeGuide.md#string-arguments"),console.warn((new Error).stack)),new Date(NaN))}},95337:(e,t,r)=>{r.d(t,{L:()=>o});const i={en:"US",zh:"CN",zh_hans:"CN",hans:"CN",wuu:"CN",hsn:"CN",hak:"CN",nan:"CN",gan:"CN",hi:"IN",te:"IN",mr:"IN",ta:"IN",gu:"IN",kn:"IN",or:"IN",ml:"IN",pa_guru:"IN",bho:"IN",awa:"IN",as:"IN",mwr:"IN",mai:"IN",mag:"IN",bgc:"IN",hne:"IN",dcc:"IN",dz:"BT",tn:"BW",am:"ET",om:"ET",quc:"GT",id:"ID",jv:"ID",su:"ID",mad:"ID",ms_arab:"ID",ga:"IE",he:"IL",jam:"JM",ja:"JP",km:"KH",ko:"KR",lo:"LA",mh:"MH",my:"MM",mt:"MT",ne:"NP",fil:"PH",ceb:"PH",ilo:"PH",ur:"PK",pa:"PK",pa_arab:"PK",arab:"PK",lah:"PK",ps:"PK",sd:"PK",sd_arab:"PK",skr:"PK",gn:"PY",th:"TH",tts:"TH",aeb:"TN",zh_hant:"TW",hant:"TW",sm:"WS",zu:"ZA",sn:"ZW",arq:"DZ",ar:"EG",arz:"EG",fa:"IR",az_arab:"IR",ary:"MA",bn:"BD",rkt:"BD",dv:"MV"};const n={AG:0,ATG:0,28:0,AR:0,ARG:0,32:0,AS:0,ASM:0,16:0,AU:0,AUS:0,36:0,BR:0,BRA:0,76:0,BS:0,BHS:0,44:0,BT:0,BTN:0,64:0,BW:0,BWA:0,72:0,BZ:0,BLZ:0,84:0,CA:0,CAN:0,124:0,CN:0,CHN:0,156:0,CO:0,COL:0,170:0,DM:0,DMA:0,212:0,DO:0,DOM:0,214:0,ET:0,ETH:0,231:0,GT:0,GTM:0,320:0,GU:0,GUM:0,316:0,HK:0,HKG:0,344:0,HN:0,HND:0,340:0,ID:0,IDN:0,360:0,IE:0,IRL:0,372:0,IL:0,ISR:0,376:0,IN:0,IND:0,356:0,JM:0,JAM:0,388:0,JP:0,JPN:0,392:0,KE:0,KEN:0,404:0,KH:0,KHM:0,116:0,KR:0,KOR:0,410:0,LA:0,LA0:0,418:0,MH:0,MHL:0,584:0,MM:0,MMR:0,104:0,MO:0,MAC:0,446:0,MT:0,MLT:0,470:0,MX:0,MEX:0,484:0,MZ:0,MOZ:0,508:0,NI:0,NIC:0,558:0,NP:0,NPL:0,524:0,NZ:0,NZL:0,554:0,PA:0,PAN:0,591:0,PE:0,PER:0,604:0,PH:0,PHL:0,608:0,PK:0,PAK:0,586:0,PR:0,PRI:0,630:0,PY:0,PRY:0,600:0,SA:0,SAU:0,682:0,SG:0,SGP:0,702:0,SV:0,SLV:0,222:0,TH:0,THA:0,764:0,TN:0,TUN:0,788:0,TT:0,TTO:0,780:0,TW:0,TWN:0,158:0,UM:0,UMI:0,581:0,US:0,USA:0,840:0,VE:0,VEN:0,862:0,VI:0,VIR:0,850:0,WS:0,WSM:0,882:0,YE:0,YEM:0,887:0,ZA:0,ZAF:0,710:0,ZW:0,ZWE:0,716:0,AE:6,ARE:6,784:6,AF:6,AFG:6,4:6,BH:6,BHR:6,48:6,DJ:6,DJI:6,262:6,DZ:6,DZA:6,12:6,EG:6,EGY:6,818:6,IQ:6,IRQ:6,368:6,IR:6,IRN:6,364:6,JO:6,JOR:6,400:6,KW:6,KWT:6,414:6,LY:6,LBY:6,434:6,MA:6,MAR:6,504:6,OM:6,OMN:6,512:6,QA:6,QAT:6,634:6,SD:6,SDN:6,729:6,SY:6,SYR:6,760:6,BD:5,BGD:5,50:5,MV:5,MDV:5,462:5};function o(e){return function(e,t,r){if(e){var i,n=e.toLowerCase().split(/[-_]/),o=n[0];if(n[1]&&4===n[1].length?(o+="_"+n[1],i=n[2]):i=n[1],i||(i=t[o]),i)return function(e,t){var r=t["string"==typeof e?e.toUpperCase():e];return"number"==typeof r?r:1}(i.match(/^\d+$/)?Number(i):i,r)}return 1}(e,i,n)}},37610:(e,t,r)=>{var i=r(37500),n=r(36924);r(52039);function o(){o=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(r){t.forEach((function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach((function(i){t.forEach((function(t){var n=t.placement;if(t.kind===i&&("static"===n||"prototype"===n)){var o="static"===n?e:r;this.defineClassElement(o,t)}}),this)}),this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var i=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===i?void 0:i.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],i=[],n={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,n)}),this),e.forEach((function(e){if(!l(e))return r.push(e);var t=this.decorateElement(e,n);r.push(t.element),r.push.apply(r,t.extras),i.push.apply(i,t.finishers)}),this),!t)return{elements:r,finishers:i};var o=this.decorateConstructor(r,t);return i.push.apply(i,o.finishers),o.finishers=i,o},addElementPlacement:function(e,t,r){var i=t[e.placement];if(!r&&-1!==i.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");i.push(e.key)},decorateElement:function(e,t){for(var r=[],i=[],n=e.decorators,o=n.length-1;o>=0;o--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,n[o])(s)||s);e=l.element,this.addElementPlacement(e,t),l.finisher&&i.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);r.push.apply(r,c)}}return{element:e,finishers:i,extras:r}},decorateConstructor:function(e,t){for(var r=[],i=t.length-1;i>=0;i--){var n=this.fromClassDescriptor(e),o=this.toClassDescriptor((0,t[i])(n)||n);if(void 0!==o.finisher&&r.push(o.finisher),void 0!==o.elements){e=o.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return u(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?u(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=p(e.key),i=String(e.placement);if("static"!==i&&"prototype"!==i&&"own"!==i)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+i+'"');var n=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var o={kind:t,key:r,placement:i,descriptor:Object.assign({},n)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(n,"get","The property descriptor of a field descriptor"),this.disallowProperty(n,"set","The property descriptor of a field descriptor"),this.disallowProperty(n,"value","The property descriptor of a field descriptor"),o.initializer=e.initializer),o},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:d(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=d(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var i=(0,t[r])(e);if(void 0!==i){if("function"!=typeof i)throw new TypeError("Finishers must return a constructor.");e=i}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}function a(e){var t,r=p(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var i={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(i.decorators=e.decorators),"field"===e.kind&&(i.initializer=e.value),i}function s(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function l(e){return e.decorators&&e.decorators.length}function c(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function d(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function p(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var i=r.call(e,t||"default");if("object"!=typeof i)return i;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function u(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,i=new Array(t);r<t;r++)i[r]=e[r];return i}!function(e,t,r,i){var n=o();if(i)for(var d=0;d<i.length;d++)n=i[d](n);var p=t((function(e){n.initializeInstanceElements(e,u.elements)}),r),u=n.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===o.key&&e.placement===o.placement},i=0;i<e.length;i++){var n,o=e[i];if("method"===o.kind&&(n=t.find(r)))if(c(o.descriptor)||c(n.descriptor)){if(l(o)||l(n))throw new ReferenceError("Duplicated methods ("+o.key+") can't be decorated.");n.descriptor=o.descriptor}else{if(l(o)){if(l(n))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+o.key+").");n.decorators=o.decorators}s(o,n)}else t.push(o)}return t}(p.d.map(a)),e);n.initializeClassElements(p.F,u.elements),n.runClassFinishers(p.F,u.finishers)}([(0,n.Mo)("ha-tip")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"method",key:"render",value:function(){return i.dy`
      <ha-svg-icon .path=${"M12,2A7,7 0 0,1 19,9C19,11.38 17.81,13.47 16,14.74V17A1,1 0 0,1 15,18H9A1,1 0 0,1 8,17V14.74C6.19,13.47 5,11.38 5,9A7,7 0 0,1 12,2M9,21V20H15V21A1,1 0 0,1 14,22H10A1,1 0 0,1 9,21M12,4A5,5 0 0,0 7,9C7,11.05 8.23,12.81 10,13.58V16H14V13.58C15.77,12.81 17,11.05 17,9A5,5 0 0,0 12,4Z"}></ha-svg-icon>
      <span class="prefix">Tip!</span>
      <span class="text"><slot></slot></span>
    `}},{kind:"field",static:!0,key:"styles",value:()=>i.iv`
    :host {
      display: block;
      text-align: center;
    }

    .text {
      margin-left: 2px;
      color: var(--secondary-text-color);
    }

    .prefix {
      font-weight: 500;
    }
  `}]}}),i.oi)},27849:(e,t,r)=>{r(39841);var i=r(50856);r(28426);class n extends(customElements.get("app-header-layout")){static get template(){return i.d`
      <style>
        :host {
          display: block;
          /**
         * Force app-header-layout to have its own stacking context so that its parent can
         * control the stacking of it relative to other elements (e.g. app-drawer-layout).
         * This could be done using \`isolation: isolate\`, but that's not well supported
         * across browsers.
         */
          position: relative;
          z-index: 0;
        }

        #wrapper ::slotted([slot="header"]) {
          @apply --layout-fixed-top;
          z-index: 1;
        }

        #wrapper.initializing ::slotted([slot="header"]) {
          position: relative;
        }

        :host([has-scrolling-region]) {
          height: 100%;
        }

        :host([has-scrolling-region]) #wrapper ::slotted([slot="header"]) {
          position: absolute;
        }

        :host([has-scrolling-region])
          #wrapper.initializing
          ::slotted([slot="header"]) {
          position: relative;
        }

        :host([has-scrolling-region]) #wrapper #contentContainer {
          @apply --layout-fit;
          overflow-y: auto;
          -webkit-overflow-scrolling: touch;
        }

        :host([has-scrolling-region]) #wrapper.initializing #contentContainer {
          position: relative;
        }

        #contentContainer {
          /* Create a stacking context here so that all children appear below the header. */
          position: relative;
          z-index: 0;
          /* Using 'transform' will cause 'position: fixed' elements to behave like
           'position: absolute' relative to this element. */
          transform: translate(0);
          margin-left: env(safe-area-inset-left);
          margin-right: env(safe-area-inset-right);
          padding-top: env(safe-area-inset-top);
          padding-bottom: env(safe-area-inset-bottom);
        }

        @media print {
          :host([has-scrolling-region]) #wrapper #contentContainer {
            overflow-y: visible;
          }
        }
      </style>

      <div id="wrapper" class="initializing">
        <slot id="headerSlot" name="header"></slot>

        <div id="contentContainer"><slot></slot></div>
        <slot id="fab" name="fab"></slot>
      </div>
    `}}customElements.define("ha-app-layout",n)},79578:(e,t,r)=>{r.a(e,(async e=>{r.r(t);r(44577),r(53268),r(12730);var i=r(37500),n=r(36924),o=r(14516),a=r(7323),s=(r(81545),r(22098),r(10983),r(99282),r(48932),r(52039),r(37610),r(45339)),l=r(24833),c=r(52415),d=(r(27849),r(73826)),p=r(11654),u=r(27322),f=(r(88165),r(29311)),h=r(80736),m=(r(74402),r(95306),e([h]));function y(){y=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(r){t.forEach((function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach((function(i){t.forEach((function(t){var n=t.placement;if(t.kind===i&&("static"===n||"prototype"===n)){var o="static"===n?e:r;this.defineClassElement(o,t)}}),this)}),this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var i=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===i?void 0:i.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],i=[],n={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,n)}),this),e.forEach((function(e){if(!b(e))return r.push(e);var t=this.decorateElement(e,n);r.push(t.element),r.push.apply(r,t.extras),i.push.apply(i,t.finishers)}),this),!t)return{elements:r,finishers:i};var o=this.decorateConstructor(r,t);return i.push.apply(i,o.finishers),o.finishers=i,o},addElementPlacement:function(e,t,r){var i=t[e.placement];if(!r&&-1!==i.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");i.push(e.key)},decorateElement:function(e,t){for(var r=[],i=[],n=e.decorators,o=n.length-1;o>=0;o--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,n[o])(s)||s);e=l.element,this.addElementPlacement(e,t),l.finisher&&i.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);r.push.apply(r,c)}}return{element:e,finishers:i,extras:r}},decorateConstructor:function(e,t){for(var r=[],i=t.length-1;i>=0;i--){var n=this.fromClassDescriptor(e),o=this.toClassDescriptor((0,t[i])(n)||n);if(void 0!==o.finisher&&r.push(o.finisher),void 0!==o.elements){e=o.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return A(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?A(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=E(e.key),i=String(e.placement);if("static"!==i&&"prototype"!==i&&"own"!==i)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+i+'"');var n=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var o={kind:t,key:r,placement:i,descriptor:Object.assign({},n)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(n,"get","The property descriptor of a field descriptor"),this.disallowProperty(n,"set","The property descriptor of a field descriptor"),this.disallowProperty(n,"value","The property descriptor of a field descriptor"),o.initializer=e.initializer),o},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:k(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=k(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var i=(0,t[r])(e);if(void 0!==i){if("function"!=typeof i)throw new TypeError("Finishers must return a constructor.");e=i}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}function v(e){var t,r=E(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var i={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(i.decorators=e.decorators),"field"===e.kind&&(i.initializer=e.value),i}function g(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function b(e){return e.decorators&&e.decorators.length}function w(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function k(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function E(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var i=r.call(e,t||"default");if("object"!=typeof i)return i;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function A(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,i=new Array(t);r<t;r++)i[r]=e[r];return i}function C(){return C="undefined"!=typeof Reflect&&Reflect.get?Reflect.get.bind():function(e,t,r){var i=P(e,t);if(i){var n=Object.getOwnPropertyDescriptor(i,t);return n.get?n.get.call(arguments.length<3?e:r):n.value}},C.apply(this,arguments)}function P(e,t){for(;!Object.prototype.hasOwnProperty.call(e,t)&&null!==(e=S(e)););return e}function S(e){return S=Object.setPrototypeOf?Object.getPrototypeOf.bind():function(e){return e.__proto__||Object.getPrototypeOf(e)},S(e)}h=(m.then?await m:m)[0];!function(e,t,r,i){var n=y();if(i)for(var o=0;o<i.length;o++)n=i[o](n);var a=t((function(e){n.initializeInstanceElements(e,s.elements)}),r),s=n.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===o.key&&e.placement===o.placement},i=0;i<e.length;i++){var n,o=e[i];if("method"===o.kind&&(n=t.find(r)))if(w(o.descriptor)||w(n.descriptor)){if(b(o)||b(n))throw new ReferenceError("Duplicated methods ("+o.key+") can't be decorated.");n.descriptor=o.descriptor}else{if(b(o)){if(b(n))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+o.key+").");n.decorators=o.decorators}g(o,n)}else t.push(o)}return t}(a.d.map(v)),e);n.initializeClassElements(a.F,s.elements),n.runClassFinishers(a.F,s.finishers)}([(0,n.Mo)("ha-config-dashboard")],(function(e,t){class r extends t{constructor(...t){super(...t),e(this)}}return{F:r,d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean,reflect:!0})],key:"narrow",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"isWide",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"cloudStatus",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"showAdvanced",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_tip",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_repairsIssues",value:()=>({issues:[],total:0})},{kind:"field",key:"_pages",value(){return(0,o.Z)(((e,t)=>{const r=[];return e&&t&&r.push({component:"cloud",path:"/config/cloud",name:"Home Assistant Cloud",info:this.cloudStatus,iconPath:"M14.2 14.5V14.74C13.5 15.34 13 16.24 13 17.2V20H6.5C5 20 3.69 19.5 2.61 18.43C1.54 17.38 1 16.09 1 14.58C1 13.28 1.39 12.12 2.17 11.1S4 9.43 5.25 9.15C5.67 7.62 6.5 6.38 7.75 5.43S10.42 4 12 4C13.95 4 15.6 4.68 16.96 6.04C18.08 7.16 18.73 8.5 18.93 10C16.36 10.04 14.2 12.08 14.2 14.5M23 17.3V20.8C23 21.4 22.4 22 21.7 22H16.2C15.6 22 15 21.4 15 20.7V17.2C15 16.6 15.6 16 16.2 16V14.5C16.2 13.1 17.6 12 19 12S21.8 13.1 21.8 14.5V16C22.4 16 23 16.6 23 17.3M20.5 14.5C20.5 13.7 19.8 13.2 19 13.2S17.5 13.7 17.5 14.5V16H20.5V14.5Z",iconColor:"#3B808E"}),[...r,...f.configSections.dashboard]}))}},{kind:"method",key:"hassSubscribe",value:function(){return[(0,s.$X)(this.hass.connection,(e=>{const t=e.issues.filter((e=>!e.ignored));this._repairsIssues={issues:t.sort(((e,t)=>s.wC[e.severity]-s.wC[t.severity])).slice(0,3===t.length?t.length:2),total:t.length};const r=new Set;for(const e of this._repairsIssues.issues)r.add(e.domain);this.hass.loadBackendTranslation("issues",[...r])}))]}},{kind:"method",key:"render",value:function(){const{updates:e,total:t}=this._filterUpdateEntitiesWithInstall(this.hass.states),{issues:r,total:n}=this._repairsIssues;return i.dy`
      <ha-app-layout>
        <app-header fixed slot="header">
          <app-toolbar>
            <ha-menu-button
              .hass=${this.hass}
              .narrow=${this.narrow}
            ></ha-menu-button>
            <div main-title>${this.hass.localize("panel.config")}</div>
            <ha-icon-button
              .label=${this.hass.localize("ui.dialogs.quick-bar.title")}
              .path=${"M9.5,3A6.5,6.5 0 0,1 16,9.5C16,11.11 15.41,12.59 14.44,13.73L14.71,14H15.5L20.5,19L19,20.5L14,15.5V14.71L13.73,14.44C12.59,15.41 11.11,16 9.5,16A6.5,6.5 0 0,1 3,9.5A6.5,6.5 0 0,1 9.5,3M9.5,5C7,5 5,7 5,9.5C5,12 7,14 9.5,14C12,14 14,12 14,9.5C14,7 12,5 9.5,5Z"}
              @click=${this._showQuickBar}
            ></ha-icon-button>
            <ha-button-menu
              corner="BOTTOM_START"
              @action=${this._handleMenuAction}
              activatable
            >
              <ha-icon-button
                slot="trigger"
                .label=${this.hass.localize("ui.common.menu")}
                .path=${"M12,16A2,2 0 0,1 14,18A2,2 0 0,1 12,20A2,2 0 0,1 10,18A2,2 0 0,1 12,16M12,10A2,2 0 0,1 14,12A2,2 0 0,1 12,14A2,2 0 0,1 10,12A2,2 0 0,1 12,10M12,4A2,2 0 0,1 14,6A2,2 0 0,1 12,8A2,2 0 0,1 10,6A2,2 0 0,1 12,4Z"}
              ></ha-icon-button>

              <mwc-list-item>
                ${this.hass.localize("ui.panel.config.updates.check_updates")}
              </mwc-list-item>
            </ha-button-menu>
          </app-toolbar>
        </app-header>

        <ha-config-section
          .narrow=${this.narrow}
          .isWide=${this.isWide}
          full-width
        >
          ${r.length||e.length?i.dy`<ha-card outlined>
                ${r.length?i.dy`
                      <ha-config-repairs
                        .hass=${this.hass}
                        .narrow=${this.narrow}
                        .total=${n}
                        .repairsIssues=${r}
                      ></ha-config-repairs>
                      ${n>r.length?i.dy`
                            <a class="button" href="/config/repairs">
                              ${this.hass.localize("ui.panel.config.repairs.more_repairs",{count:n-r.length})}
                            </a>
                          `:""}
                    `:""}
                ${r.length&&e.length?i.dy`<hr />`:""}
                ${e.length?i.dy`
                      <ha-config-updates
                        .hass=${this.hass}
                        .narrow=${this.narrow}
                        .total=${t}
                        .updateEntities=${e}
                      ></ha-config-updates>
                      ${t>e.length?i.dy`
                            <a class="button" href="/config/updates">
                              ${this.hass.localize("ui.panel.config.updates.more_updates",{count:t-e.length})}
                            </a>
                          `:""}
                    `:""}
              </ha-card>`:""}
          <ha-card outlined>
            <ha-config-navigation
              .hass=${this.hass}
              .narrow=${this.narrow}
              .showAdvanced=${this.showAdvanced}
              .pages=${this._pages(this.cloudStatus,(0,a.p)(this.hass,"cloud"))}
            ></ha-config-navigation>
          </ha-card>
          <ha-tip>${this._tip}</ha-tip>
        </ha-config-section>
      </ha-app-layout>
    `}},{kind:"method",key:"updated",value:function(e){C(S(r.prototype),"updated",this).call(this,e),!this._tip&&e.has("hass")&&(this._tip=((e,t)=>{const r=[];let n=[{content:e.localize("ui.panel.config.tips.join","forums",i.dy`<a
          href="https://community.home-assistant.io"
          target="_blank"
          rel="noreferrer"
          >Forums</a
        >`,"twitter",i.dy`<a
          href=${(0,u.R)(e,"/twitter")}
          target="_blank"
          rel="noreferrer"
          >Twitter</a
        >`,"discord",i.dy`<a
          href=${(0,u.R)(e,"/join-chat")}
          target="_blank"
          rel="noreferrer"
          >Chat</a
        >`,"blog",i.dy`<a
          href=${(0,u.R)(e,"/blog")}
          target="_blank"
          rel="noreferrer"
          >Blog</a
        >`,"newsletter",i.dy`<span class="keep-together"
          ><a
            href=${(0,u.R)(e,"/newsletter")}
            target="_blank"
            rel="noreferrer"
            >Newsletter</a
          >
        </span>`),weight:2,narrow:!0},{content:e.localize("ui.tips.key_c_hint"),weight:1,narrow:!1},{content:e.localize("ui.tips.key_m_hint"),weight:1,narrow:!1}];return t&&(n=n.filter((e=>e.narrow))),n.forEach((e=>{for(let t=0;t<e.weight;t++)r.push(e.content)})),r[Math.floor(Math.random()*r.length)]})(this.hass,this.narrow))}},{kind:"field",key:"_filterUpdateEntitiesWithInstall",value:()=>(0,o.Z)((e=>{const t=(0,l.Fj)(e);return{updates:t.slice(0,3===t.length?t.length:2),total:t.length}}))},{kind:"method",key:"_showQuickBar",value:function(){(0,c.H)(this,{commandMode:!0,hint:this.hass.localize("ui.dialogs.quick-bar.key_c_hint")})}},{kind:"method",key:"_handleMenuAction",value:async function(e){if(0===e.detail.index)(0,l.M$)(this,this.hass)}},{kind:"get",static:!0,key:"styles",value:function(){return[p.Qx,i.iv`
        ha-card:last-child {
          margin-bottom: env(safe-area-inset-bottom);
        }
        :host(:not([narrow])) ha-card:last-child {
          margin-bottom: max(24px, env(safe-area-inset-bottom));
        }
        ha-config-section {
          margin: auto;
          margin-top: -32px;
          max-width: 600px;
        }
        ha-card {
          overflow: hidden;
        }
        ha-card a {
          text-decoration: none;
          color: var(--primary-text-color);
        }
        a.button {
          display: inline-block;
          color: var(--primary-text-color);
          padding: 6px 16px;
          margin: 8px 16px 16px 16px;
          border-radius: 32px;
          border: 1px solid var(--divider-color);
        }
        .title {
          font-size: 16px;
          padding: 16px;
          padding-bottom: 0;
        }

        @media all and (max-width: 600px) {
          ha-card {
            border-width: 1px 0;
            border-radius: 0;
            box-shadow: unset;
          }
          ha-config-section {
            margin-top: -42px;
          }
        }

        ha-tip {
          margin-bottom: max(env(safe-area-inset-bottom), 8px);
        }

        .new {
          color: var(--primary-color);
        }

        .keep-together {
          display: inline-block;
        }

        hr {
          height: 1px;
          background-color: var(
            --ha-card-border-color,
            var(--divider-color, #e0e0e0)
          );
          border: none;
          margin-top: 0;
        }
      `]}}]}}),(0,d.f)(i.oi))}))},74402:(e,t,r)=>{r(24103),r(44577);var i=r(37500),n=r(36924),o=r(60228);r(22098),r(99282),r(35197);function a(){a=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(r){t.forEach((function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach((function(i){t.forEach((function(t){var n=t.placement;if(t.kind===i&&("static"===n||"prototype"===n)){var o="static"===n?e:r;this.defineClassElement(o,t)}}),this)}),this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var i=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===i?void 0:i.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],i=[],n={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,n)}),this),e.forEach((function(e){if(!c(e))return r.push(e);var t=this.decorateElement(e,n);r.push(t.element),r.push.apply(r,t.extras),i.push.apply(i,t.finishers)}),this),!t)return{elements:r,finishers:i};var o=this.decorateConstructor(r,t);return i.push.apply(i,o.finishers),o.finishers=i,o},addElementPlacement:function(e,t,r){var i=t[e.placement];if(!r&&-1!==i.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");i.push(e.key)},decorateElement:function(e,t){for(var r=[],i=[],n=e.decorators,o=n.length-1;o>=0;o--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,n[o])(s)||s);e=l.element,this.addElementPlacement(e,t),l.finisher&&i.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);r.push.apply(r,c)}}return{element:e,finishers:i,extras:r}},decorateConstructor:function(e,t){for(var r=[],i=t.length-1;i>=0;i--){var n=this.fromClassDescriptor(e),o=this.toClassDescriptor((0,t[i])(n)||n);if(void 0!==o.finisher&&r.push(o.finisher),void 0!==o.elements){e=o.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return f(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?f(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=u(e.key),i=String(e.placement);if("static"!==i&&"prototype"!==i&&"own"!==i)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+i+'"');var n=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var o={kind:t,key:r,placement:i,descriptor:Object.assign({},n)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(n,"get","The property descriptor of a field descriptor"),this.disallowProperty(n,"set","The property descriptor of a field descriptor"),this.disallowProperty(n,"value","The property descriptor of a field descriptor"),o.initializer=e.initializer),o},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:p(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=p(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var i=(0,t[r])(e);if(void 0!==i){if("function"!=typeof i)throw new TypeError("Finishers must return a constructor.");e=i}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}function s(e){var t,r=u(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var i={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(i.decorators=e.decorators),"field"===e.kind&&(i.initializer=e.value),i}function l(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function c(e){return e.decorators&&e.decorators.length}function d(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function p(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function u(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var i=r.call(e,t||"default");if("object"!=typeof i)return i;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function f(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,i=new Array(t);r<t;r++)i[r]=e[r];return i}!function(e,t,r,i){var n=a();if(i)for(var o=0;o<i.length;o++)n=i[o](n);var p=t((function(e){n.initializeInstanceElements(e,u.elements)}),r),u=n.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===o.key&&e.placement===o.placement},i=0;i<e.length;i++){var n,o=e[i];if("method"===o.kind&&(n=t.find(r)))if(d(o.descriptor)||d(n.descriptor)){if(c(o)||c(n))throw new ReferenceError("Duplicated methods ("+o.key+") can't be decorated.");n.descriptor=o.descriptor}else{if(c(o)){if(c(n))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+o.key+").");n.decorators=o.decorators}l(o,n)}else t.push(o)}return t}(p.d.map(s)),e);n.initializeClassElements(p.F,u.elements),n.runClassFinishers(p.F,u.finishers)}([(0,n.Mo)("ha-config-navigation")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"narrow",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"pages",value:void 0},{kind:"method",key:"render",value:function(){const e=this.pages.filter((e=>{var t;return"#external-app-configuration"===e.path?null===(t=this.hass.auth.external)||void 0===t?void 0:t.config.hasSettingsScreen:(0,o.j)(this.hass,e)})).map((e=>({...e,name:e.name||this.hass.localize(`ui.panel.config.dashboard.${e.translationKey}.main`),description:"cloud"===e.component&&e.info?e.info.logged_in?`\n                  ${this.hass.localize("ui.panel.config.cloud.description_login")}\n                `:`\n                  ${this.hass.localize("ui.panel.config.cloud.description_features")}\n                `:`\n                ${e.description||this.hass.localize(`ui.panel.config.dashboard.${e.translationKey}.secondary`)}\n              `})));return i.dy`
      <ha-navigation-list
        hasSecondary
        .hass=${this.hass}
        .narrow=${this.narrow}
        .pages=${e}
        .label=${this.hass.localize("panel.config")}
      ></ha-navigation-list>
    `}},{kind:"field",static:!0,key:"styles",value:()=>i.iv`
    ha-navigation-list {
      --navigation-list-item-title-font-size: 16px;
    }
  `}]}}),i.oi)},27322:(e,t,r)=>{r.d(t,{R:()=>i});const i=(e,t)=>`https://${e.config.version.includes("b")?"rc":e.config.version.includes("dev")?"next":"www"}.home-assistant.io${t}`}}]);
//# sourceMappingURL=b74a8d7b.js.map