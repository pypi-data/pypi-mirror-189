/*! For license information please see 42580d3a.js.LICENSE.txt */
"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[73058,49995],{33760:(e,t,n)=>{n.d(t,{U:()=>r});n(10994);var o=n(51644),i=n(26110);const r=[o.P,i.a,{hostAttributes:{role:"option",tabindex:"0"}}]},89194:(e,t,n)=>{n(10994),n(65660),n(70019);var o=n(9672),i=n(50856);(0,o.k)({_template:i.d`
    <style>
      :host {
        overflow: hidden; /* needed for text-overflow: ellipsis to work on ff */
        @apply --layout-vertical;
        @apply --layout-center-justified;
        @apply --layout-flex;
      }

      :host([two-line]) {
        min-height: var(--paper-item-body-two-line-min-height, 72px);
      }

      :host([three-line]) {
        min-height: var(--paper-item-body-three-line-min-height, 88px);
      }

      :host > ::slotted(*) {
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
      }

      :host > ::slotted([secondary]) {
        @apply --paper-font-body1;

        color: var(--paper-item-body-secondary-color, var(--secondary-text-color));

        @apply --paper-item-body-secondary;
      }
    </style>

    <slot></slot>
`,is:"paper-item-body"})},97968:(e,t,n)=>{n(65660),n(70019);const o=document.createElement("template");o.setAttribute("style","display: none;"),o.innerHTML="<dom-module id=\"paper-item-shared-styles\">\n  <template>\n    <style>\n      :host, .paper-item {\n        display: block;\n        position: relative;\n        min-height: var(--paper-item-min-height, 48px);\n        padding: 0px 16px;\n      }\n\n      .paper-item {\n        @apply --paper-font-subhead;\n        border:none;\n        outline: none;\n        background: white;\n        width: 100%;\n        text-align: left;\n      }\n\n      :host([hidden]), .paper-item[hidden] {\n        display: none !important;\n      }\n\n      :host(.iron-selected), .paper-item.iron-selected {\n        font-weight: var(--paper-item-selected-weight, bold);\n\n        @apply --paper-item-selected;\n      }\n\n      :host([disabled]), .paper-item[disabled] {\n        color: var(--paper-item-disabled-color, var(--disabled-text-color));\n\n        @apply --paper-item-disabled;\n      }\n\n      :host(:focus), .paper-item:focus {\n        position: relative;\n        outline: 0;\n\n        @apply --paper-item-focused;\n      }\n\n      :host(:focus):before, .paper-item:focus:before {\n        @apply --layout-fit;\n\n        background: currentColor;\n        content: '';\n        opacity: var(--dark-divider-opacity);\n        pointer-events: none;\n\n        @apply --paper-item-focused-before;\n      }\n    </style>\n  </template>\n</dom-module>",document.head.appendChild(o.content)},53973:(e,t,n)=>{n(10994),n(65660),n(97968);var o=n(9672),i=n(50856),r=n(33760);(0,o.k)({_template:i.d`
    <style include="paper-item-shared-styles">
      :host {
        @apply --layout-horizontal;
        @apply --layout-center;
        @apply --paper-font-subhead;

        @apply --paper-item;
      }
    </style>
    <slot></slot>
`,is:"paper-item",behaviors:[r.U]})},73728:(e,t,n)=>{n.d(t,{pV:()=>a,P3:()=>s,Ky:()=>c,D4:()=>d,XO:()=>p,zO:()=>h,oi:()=>f,d4:()=>u,D7:()=>m,ZJ:()=>w,V3:()=>v,WW:()=>g});var o=n(97330),i=n(38346),r=n(5986);const a=["bluetooth","dhcp","discovery","hardware","hassio","homekit","integration_discovery","mqtt","ssdp","unignore","usb","zeroconf"],s=["reauth"],l={"HA-Frontend-Base":`${location.protocol}//${location.host}`},c=(e,t)=>{var n;return e.callApi("POST","config/config_entries/flow",{handler:t,show_advanced_options:Boolean(null===(n=e.userData)||void 0===n?void 0:n.showAdvanced)},l)},d=(e,t)=>e.callApi("GET",`config/config_entries/flow/${t}`,void 0,l),p=(e,t,n)=>e.callApi("POST",`config/config_entries/flow/${t}`,n,l),h=(e,t,n)=>e.callWS({type:"config_entries/ignore_flow",flow_id:t,title:n}),f=(e,t)=>e.callApi("DELETE",`config/config_entries/flow/${t}`),u=(e,t)=>e.callApi("GET","config/config_entries/flow_handlers"+(t?`?type=${t}`:"")),m=e=>e.sendMessagePromise({type:"config_entries/flow/progress"}),y=(e,t)=>e.subscribeEvents((0,i.D)((()=>m(e).then((e=>t.setState(e,!0)))),500,!0),"config_entry_discovered"),w=e=>(0,o._)(e,"_configFlowProgress",m,y),v=(e,t)=>w(e.connection).subscribe(t),g=(e,t)=>t.context.title_placeholders&&0!==Object.keys(t.context.title_placeholders).length?e(`component.${t.handler}.config.flow_title`,t.context.title_placeholders)||("name"in t.context.title_placeholders?t.context.title_placeholders.name:(0,r.Lh)(e,t.handler)):(0,r.Lh)(e,t.handler)},2852:(e,t,n)=>{n.d(t,{t:()=>s});var o=n(37500),i=n(73728),r=n(5986),a=n(52871);const s=(e,t)=>(0,a.w)(e,t,{loadDevicesAndAreas:!0,createFlow:async(e,t)=>{const[n]=await Promise.all([(0,i.Ky)(e,t),e.loadBackendTranslation("config",t),e.loadBackendTranslation("selector",t),e.loadBackendTranslation("title",t)]);return n},fetchFlow:async(e,t)=>{const n=await(0,i.D4)(e,t);return await e.loadBackendTranslation("config",n.handler),await e.loadBackendTranslation("selector",n.handler),n},handleFlowStep:i.XO,deleteFlow:i.oi,renderAbortDescription(e,t){const n=e.localize(`component.${t.handler}.config.abort.${t.reason}`,t.description_placeholders);return n?o.dy`
            <ha-markdown allowsvg breaks .content=${n}></ha-markdown>
          `:""},renderShowFormStepHeader:(e,t)=>e.localize(`component.${t.handler}.config.step.${t.step_id}.title`)||e.localize(`component.${t.handler}.title`),renderShowFormStepDescription(e,t){const n=e.localize(`component.${t.handler}.config.step.${t.step_id}.description`,t.description_placeholders);return n?o.dy`
            <ha-markdown allowsvg breaks .content=${n}></ha-markdown>
          `:""},renderShowFormStepFieldLabel:(e,t,n)=>e.localize(`component.${t.handler}.config.step.${t.step_id}.data.${n.name}`),renderShowFormStepFieldHelper(e,t,n){const i=e.localize(`component.${t.handler}.config.step.${t.step_id}.data_description.${n.name}`,t.description_placeholders);return i?o.dy`<ha-markdown breaks .content=${i}></ha-markdown>`:""},renderShowFormStepFieldError:(e,t,n)=>e.localize(`component.${t.handler}.config.error.${n}`,t.description_placeholders)||n,renderShowFormStepFieldLocalizeValue:(e,t,n)=>e.localize(`component.${t.handler}.selector.${n}`),renderExternalStepHeader:(e,t)=>e.localize(`component.${t.handler}.config.step.${t.step_id}.title`)||e.localize("ui.panel.config.integrations.config_flow.external_step.open_site"),renderExternalStepDescription(e,t){const n=e.localize(`component.${t.handler}.config.${t.step_id}.description`,t.description_placeholders);return o.dy`
        <p>
          ${e.localize("ui.panel.config.integrations.config_flow.external_step.description")}
        </p>
        ${n?o.dy`
              <ha-markdown
                allowsvg
                breaks
                .content=${n}
              ></ha-markdown>
            `:""}
      `},renderCreateEntryDescription(e,t){const n=e.localize(`component.${t.handler}.config.create_entry.${t.description||"default"}`,t.description_placeholders);return o.dy`
        ${n?o.dy`
              <ha-markdown
                allowsvg
                breaks
                .content=${n}
              ></ha-markdown>
            `:""}
        <p>
          ${e.localize("ui.panel.config.integrations.config_flow.created_config","name",t.title)}
        </p>
      `},renderShowFormProgressHeader:(e,t)=>e.localize(`component.${t.handler}.config.step.${t.step_id}.title`)||e.localize(`component.${t.handler}.title`),renderShowFormProgressDescription(e,t){const n=e.localize(`component.${t.handler}.config.progress.${t.progress_action}`,t.description_placeholders);return n?o.dy`
            <ha-markdown allowsvg breaks .content=${n}></ha-markdown>
          `:""},renderMenuHeader:(e,t)=>e.localize(`component.${t.handler}.config.step.${t.step_id}.title`)||e.localize(`component.${t.handler}.title`),renderMenuDescription(e,t){const n=e.localize(`component.${t.handler}.config.step.${t.step_id}.description`,t.description_placeholders);return n?o.dy`
            <ha-markdown allowsvg breaks .content=${n}></ha-markdown>
          `:""},renderMenuOption:(e,t,n)=>e.localize(`component.${t.handler}.config.step.${t.step_id}.menu_options.${n}`,t.description_placeholders),renderLoadingDescription(e,t,n,o){if("loading_flow"!==t&&"loading_step"!==t)return"";const i=(null==o?void 0:o.handler)||n;return e.localize(`ui.panel.config.integrations.config_flow.loading.${t}`,{integration:i?(0,r.Lh)(e.localize,i):e.localize("ui.panel.config.integrations.config_flow.loading.fallback_title")})}})},52871:(e,t,n)=>{n.d(t,{w:()=>r});var o=n(47181);const i=()=>Promise.all([n.e(29563),n.e(24103),n.e(31338),n.e(86251),n.e(59799),n.e(6294),n.e(88278),n.e(41985),n.e(85084),n.e(51882),n.e(45507),n.e(51644),n.e(68200),n.e(49842),n.e(1548),n.e(49075),n.e(35435),n.e(77576),n.e(29925),n.e(12545),n.e(26272),n.e(67681),n.e(4940),n.e(68101),n.e(48194),n.e(34553)]).then(n.bind(n,93990)),r=(e,t,n)=>{(0,o.B)(e,"show-dialog",{dialogTag:"dialog-data-entry-flow",dialogImport:i,dialogParams:{...t,flowConfig:n,dialogParentElement:e}})}},33137:(e,t,n)=>{n.r(t);n(53268),n(12730),n(60010),n(38353),n(63081);var o=n(37500),i=n(36924),r=n(2852),a=n(47181),s=n(11654);function l(){l=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(n){t.forEach((function(t){t.kind===n&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var n=e.prototype;["method","field"].forEach((function(o){t.forEach((function(t){var i=t.placement;if(t.kind===o&&("static"===i||"prototype"===i)){var r="static"===i?e:n;this.defineClassElement(r,t)}}),this)}),this)},defineClassElement:function(e,t){var n=t.descriptor;if("field"===t.kind){var o=t.initializer;n={enumerable:n.enumerable,writable:n.writable,configurable:n.configurable,value:void 0===o?void 0:o.call(e)}}Object.defineProperty(e,t.key,n)},decorateClass:function(e,t){var n=[],o=[],i={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,i)}),this),e.forEach((function(e){if(!p(e))return n.push(e);var t=this.decorateElement(e,i);n.push(t.element),n.push.apply(n,t.extras),o.push.apply(o,t.finishers)}),this),!t)return{elements:n,finishers:o};var r=this.decorateConstructor(n,t);return o.push.apply(o,r.finishers),r.finishers=o,r},addElementPlacement:function(e,t,n){var o=t[e.placement];if(!n&&-1!==o.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");o.push(e.key)},decorateElement:function(e,t){for(var n=[],o=[],i=e.decorators,r=i.length-1;r>=0;r--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,i[r])(s)||s);e=l.element,this.addElementPlacement(e,t),l.finisher&&o.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);n.push.apply(n,c)}}return{element:e,finishers:o,extras:n}},decorateConstructor:function(e,t){for(var n=[],o=t.length-1;o>=0;o--){var i=this.fromClassDescriptor(e),r=this.toClassDescriptor((0,t[o])(i)||i);if(void 0!==r.finisher&&n.push(r.finisher),void 0!==r.elements){e=r.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:n}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return m(e,t);var n=Object.prototype.toString.call(e).slice(8,-1);return"Object"===n&&e.constructor&&(n=e.constructor.name),"Map"===n||"Set"===n?Array.from(e):"Arguments"===n||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)?m(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var n=u(e.key),o=String(e.placement);if("static"!==o&&"prototype"!==o&&"own"!==o)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+o+'"');var i=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var r={kind:t,key:n,placement:o,descriptor:Object.assign({},i)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(i,"get","The property descriptor of a field descriptor"),this.disallowProperty(i,"set","The property descriptor of a field descriptor"),this.disallowProperty(i,"value","The property descriptor of a field descriptor"),r.initializer=e.initializer),r},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:f(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var n=f(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:n}},runClassFinishers:function(e,t){for(var n=0;n<t.length;n++){var o=(0,t[n])(e);if(void 0!==o){if("function"!=typeof o)throw new TypeError("Finishers must return a constructor.");e=o}}return e},disallowProperty:function(e,t,n){if(void 0!==e[t])throw new TypeError(n+" can't have a ."+t+" property.")}};return e}function c(e){var t,n=u(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var o={kind:"field"===e.kind?"field":"method",key:n,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(o.decorators=e.decorators),"field"===e.kind&&(o.initializer=e.value),o}function d(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function p(e){return e.decorators&&e.decorators.length}function h(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function f(e,t){var n=e[t];if(void 0!==n&&"function"!=typeof n)throw new TypeError("Expected '"+t+"' to be a function");return n}function u(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var n=e[Symbol.toPrimitive];if(void 0!==n){var o=n.call(e,t||"default");if("object"!=typeof o)return o;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function m(e,t){(null==t||t>e.length)&&(t=e.length);for(var n=0,o=new Array(t);n<t;n++)o[n]=e[n];return o}!function(e,t,n,o){var i=l();if(o)for(var r=0;r<o.length;r++)i=o[r](i);var a=t((function(e){i.initializeInstanceElements(e,s.elements)}),n),s=i.decorateClass(function(e){for(var t=[],n=function(e){return"method"===e.kind&&e.key===r.key&&e.placement===r.placement},o=0;o<e.length;o++){var i,r=e[o];if("method"===r.kind&&(i=t.find(n)))if(h(r.descriptor)||h(i.descriptor)){if(p(r)||p(i))throw new ReferenceError("Duplicated methods ("+r.key+") can't be decorated.");i.descriptor=r.descriptor}else{if(p(r)){if(p(i))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+r.key+").");i.decorators=r.decorators}d(r,i)}else t.push(r)}return t}(a.d.map(c)),e);i.initializeClassElements(a.F,s.elements),i.runClassFinishers(a.F,s.finishers)}([(0,i.Mo)("ha-config-ais-dom-config-wifi")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,i.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,i.Cb)({type:Boolean})],key:"isWide",value:()=>!0},{kind:"field",decorators:[(0,i.Cb)({type:Boolean})],key:"narrow",value:()=>!1},{kind:"method",key:"firstUpdated",value:async function(){}},{kind:"method",key:"render",value:function(){return this.hass?o.dy`
      <hass-subpage header="Konfiguracja bramki AIS dom">
        <div .narrow=${this.narrow}>
          <ha-config-section .isWide=${this.isWide}>
            <span slot="header">Połączenie WiFi</span>
            <span slot="introduction"
              >Możesz sprawdzić lub skonfigurować parametry połączenia
              WiFi</span
            >
            <ha-card header="Parametry sieci">
              <div class="card-content" style="display: flex;">
                <div style="text-align: center;">
                  <div class="aisInfoRow">Lokalna nazwa hosta</div>
                  <div class="aisInfoRow">
                    <mwc-button
                      >${this.hass.states["sensor.local_host_name"].state}
                      <ha-icon
                        class="user-button"
                        icon="hass:cog"
                        @click=${this.createFlowHostName}
                      ></ha-icon>
                    </mwc-button>
                  </div>
                </div>
                <div style="text-align: center;" @click=${this.showLocalIpInfo}>
                  <div class="aisInfoRow">Lokalny adres IP</div>
                  <div class="aisInfoRow">
                    <mwc-button
                      >${this.hass.states["sensor.internal_ip_address"].state}</mwc-button
                    >
                  </div>
                </div>
                <div
                  @click=${this.showWiFiSpeedInfo}
                  style="text-align: center;"
                >
                  <div class="aisInfoRow">Prędkość połączenia WiFi</div>
                  <div class="aisInfoRow">
                    <mwc-button
                      >${this.hass.states["sensor.ais_wifi_service_current_network_info"].state}</mwc-button
                    >
                  </div>
                </div>
              </div>
              <div class="card-actions">
                <ha-icon
                  class="user-button"
                  icon="hass:wifi"
                  @click=${this.showWiFiGroup}
                ></ha-icon
                ><mwc-button @click=${this.createFlowWifi}
                  >Konfigurator połączenia z siecą WiFi</mwc-button
                >
              </div>
            </ha-card>
          </ha-config-section>
        </div>
      </hass-subpage>
    `:o.dy``}},{kind:"get",static:!0,key:"styles",value:function(){return[s.Qx,o.iv`
        .content {
          padding-bottom: 32px;
        }
        .border {
          margin: 32px auto 0;
          border-bottom: 1px solid rgba(0, 0, 0, 0.12);
          max-width: 1040px;
        }
        .narrow .border {
          max-width: 640px;
        }
        div.aisInfoRow {
          display: inline-block;
        }
        .center-container {
          @apply --layout-vertical;
          @apply --layout-center-center;
          height: 70px;
        }
        div.card-actions {
          text-align: center;
        }
      `]}},{kind:"method",key:"showWiFiGroup",value:function(){(0,a.B)(this,"hass-more-info",{entityId:"group.internet_status"})}},{kind:"method",key:"showWiFiSpeedInfo",value:function(){(0,a.B)(this,"hass-more-info",{entityId:"sensor.ais_wifi_service_current_network_info"})}},{kind:"method",key:"showLocalIpInfo",value:function(){(0,a.B)(this,"hass-more-info",{entityId:"sensor.internal_ip_address"})}},{kind:"method",key:"_continueFlow",value:function(e){(0,r.t)(this,{continueFlowId:e,dialogClosedCallback:()=>{console.log("OK")}})}},{kind:"method",key:"createFlowHostName",value:function(){this.hass.callApi("POST","config/config_entries/flow",{handler:"ais_host"}).then((e=>{this._continueFlow(e.flow_id)}))}},{kind:"method",key:"createFlowWifi",value:function(){this.hass.callApi("POST","config/config_entries/flow",{handler:"ais_wifi_service"}).then((e=>{console.log(e),this._continueFlow(e.flow_id)}))}}]}}),o.oi)}}]);
//# sourceMappingURL=42580d3a.js.map