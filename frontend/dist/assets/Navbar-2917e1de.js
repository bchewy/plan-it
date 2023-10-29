import{_ as Ve,l as We,r as he,o as k,c as D,a as p,b as N,h as C,k as v,m as Ke,t as Ge,w as Xe,q as Ze,F as Ye,u as Qe,e as Z,A as et,p as tt,j as nt}from"./index-751a66e8.js";function Ae(e,t){return function(){return e.apply(t,arguments)}}const{toString:rt}=Object.prototype,{getPrototypeOf:ae}=Object,V=(e=>t=>{const n=rt.call(t);return e[n]||(e[n]=n.slice(8,-1).toLowerCase())})(Object.create(null)),O=e=>(e=e.toLowerCase(),t=>V(t)===e),W=e=>t=>typeof t===e,{isArray:B}=Array,L=W("undefined");function st(e){return e!==null&&!L(e)&&e.constructor!==null&&!L(e.constructor)&&S(e.constructor.isBuffer)&&e.constructor.isBuffer(e)}const Te=O("ArrayBuffer");function ot(e){let t;return typeof ArrayBuffer<"u"&&ArrayBuffer.isView?t=ArrayBuffer.isView(e):t=e&&e.buffer&&Te(e.buffer),t}const it=W("string"),S=W("function"),xe=W("number"),K=e=>e!==null&&typeof e=="object",at=e=>e===!0||e===!1,M=e=>{if(V(e)!=="object")return!1;const t=ae(e);return(t===null||t===Object.prototype||Object.getPrototypeOf(t)===null)&&!(Symbol.toStringTag in e)&&!(Symbol.iterator in e)},lt=O("Date"),ct=O("File"),ut=O("Blob"),dt=O("FileList"),ft=e=>K(e)&&S(e.pipe),ht=e=>{let t;return e&&(typeof FormData=="function"&&e instanceof FormData||S(e.append)&&((t=V(e))==="formdata"||t==="object"&&S(e.toString)&&e.toString()==="[object FormData]"))},pt=O("URLSearchParams"),mt=e=>e.trim?e.trim():e.replace(/^[\s\uFEFF\xA0]+|[\s\uFEFF\xA0]+$/g,"");function j(e,t,{allOwnKeys:n=!1}={}){if(e===null||typeof e>"u")return;let r,s;if(typeof e!="object"&&(e=[e]),B(e))for(r=0,s=e.length;r<s;r++)t.call(null,e[r],r,e);else{const o=n?Object.getOwnPropertyNames(e):Object.keys(e),i=o.length;let c;for(r=0;r<i;r++)c=o[r],t.call(null,e[c],c,e)}}function Ne(e,t){t=t.toLowerCase();const n=Object.keys(e);let r=n.length,s;for(;r-- >0;)if(s=n[r],t===s.toLowerCase())return s;return null}const Ce=(()=>typeof globalThis<"u"?globalThis:typeof self<"u"?self:typeof window<"u"?window:global)(),Pe=e=>!L(e)&&e!==Ce;function ne(){const{caseless:e}=Pe(this)&&this||{},t={},n=(r,s)=>{const o=e&&Ne(t,s)||s;M(t[o])&&M(r)?t[o]=ne(t[o],r):M(r)?t[o]=ne({},r):B(r)?t[o]=r.slice():t[o]=r};for(let r=0,s=arguments.length;r<s;r++)arguments[r]&&j(arguments[r],n);return t}const yt=(e,t,n,{allOwnKeys:r}={})=>(j(t,(s,o)=>{n&&S(s)?e[o]=Ae(s,n):e[o]=s},{allOwnKeys:r}),e),bt=e=>(e.charCodeAt(0)===65279&&(e=e.slice(1)),e),wt=(e,t,n,r)=>{e.prototype=Object.create(t.prototype,r),e.prototype.constructor=e,Object.defineProperty(e,"super",{value:t.prototype}),n&&Object.assign(e.prototype,n)},gt=(e,t,n,r)=>{let s,o,i;const c={};if(t=t||{},e==null)return t;do{for(s=Object.getOwnPropertyNames(e),o=s.length;o-- >0;)i=s[o],(!r||r(i,e,t))&&!c[i]&&(t[i]=e[i],c[i]=!0);e=n!==!1&&ae(e)}while(e&&(!n||n(e,t))&&e!==Object.prototype);return t},Et=(e,t,n)=>{e=String(e),(n===void 0||n>e.length)&&(n=e.length),n-=t.length;const r=e.indexOf(t,n);return r!==-1&&r===n},St=e=>{if(!e)return null;if(B(e))return e;let t=e.length;if(!xe(t))return null;const n=new Array(t);for(;t-- >0;)n[t]=e[t];return n},_t=(e=>t=>e&&t instanceof e)(typeof Uint8Array<"u"&&ae(Uint8Array)),Rt=(e,t)=>{const r=(e&&e[Symbol.iterator]).call(e);let s;for(;(s=r.next())&&!s.done;){const o=s.value;t.call(e,o[0],o[1])}},Ot=(e,t)=>{let n;const r=[];for(;(n=e.exec(t))!==null;)r.push(n);return r},At=O("HTMLFormElement"),Tt=e=>e.toLowerCase().replace(/[-_\s]([a-z\d])(\w*)/g,function(n,r,s){return r.toUpperCase()+s}),pe=(({hasOwnProperty:e})=>(t,n)=>e.call(t,n))(Object.prototype),xt=O("RegExp"),ve=(e,t)=>{const n=Object.getOwnPropertyDescriptors(e),r={};j(n,(s,o)=>{let i;(i=t(s,o,e))!==!1&&(r[o]=i||s)}),Object.defineProperties(e,r)},Nt=e=>{ve(e,(t,n)=>{if(S(e)&&["arguments","caller","callee"].indexOf(n)!==-1)return!1;const r=e[n];if(S(r)){if(t.enumerable=!1,"writable"in t){t.writable=!1;return}t.set||(t.set=()=>{throw Error("Can not rewrite read-only method '"+n+"'")})}})},Ct=(e,t)=>{const n={},r=s=>{s.forEach(o=>{n[o]=!0})};return B(e)?r(e):r(String(e).split(t)),n},Pt=()=>{},vt=(e,t)=>(e=+e,Number.isFinite(e)?e:t),Y="abcdefghijklmnopqrstuvwxyz",me="0123456789",Fe={DIGIT:me,ALPHA:Y,ALPHA_DIGIT:Y+Y.toUpperCase()+me},Ft=(e=16,t=Fe.ALPHA_DIGIT)=>{let n="";const{length:r}=t;for(;e--;)n+=t[Math.random()*r|0];return n};function Bt(e){return!!(e&&S(e.append)&&e[Symbol.toStringTag]==="FormData"&&e[Symbol.iterator])}const kt=e=>{const t=new Array(10),n=(r,s)=>{if(K(r)){if(t.indexOf(r)>=0)return;if(!("toJSON"in r)){t[s]=r;const o=B(r)?[]:{};return j(r,(i,c)=>{const d=n(i,s+1);!L(d)&&(o[c]=d)}),t[s]=void 0,o}}return r};return n(e,0)},Dt=O("AsyncFunction"),Ut=e=>e&&(K(e)||S(e))&&S(e.then)&&S(e.catch),a={isArray:B,isArrayBuffer:Te,isBuffer:st,isFormData:ht,isArrayBufferView:ot,isString:it,isNumber:xe,isBoolean:at,isObject:K,isPlainObject:M,isUndefined:L,isDate:lt,isFile:ct,isBlob:ut,isRegExp:xt,isFunction:S,isStream:ft,isURLSearchParams:pt,isTypedArray:_t,isFileList:dt,forEach:j,merge:ne,extend:yt,trim:mt,stripBOM:bt,inherits:wt,toFlatObject:gt,kindOf:V,kindOfTest:O,endsWith:Et,toArray:St,forEachEntry:Rt,matchAll:Ot,isHTMLForm:At,hasOwnProperty:pe,hasOwnProp:pe,reduceDescriptors:ve,freezeMethods:Nt,toObjectSet:Ct,toCamelCase:Tt,noop:Pt,toFiniteNumber:vt,findKey:Ne,global:Ce,isContextDefined:Pe,ALPHABET:Fe,generateString:Ft,isSpecCompliantForm:Bt,toJSONObject:kt,isAsyncFn:Dt,isThenable:Ut};function y(e,t,n,r,s){Error.call(this),Error.captureStackTrace?Error.captureStackTrace(this,this.constructor):this.stack=new Error().stack,this.message=e,this.name="AxiosError",t&&(this.code=t),n&&(this.config=n),r&&(this.request=r),s&&(this.response=s)}a.inherits(y,Error,{toJSON:function(){return{message:this.message,name:this.name,description:this.description,number:this.number,fileName:this.fileName,lineNumber:this.lineNumber,columnNumber:this.columnNumber,stack:this.stack,config:a.toJSONObject(this.config),code:this.code,status:this.response&&this.response.status?this.response.status:null}}});const Be=y.prototype,ke={};["ERR_BAD_OPTION_VALUE","ERR_BAD_OPTION","ECONNABORTED","ETIMEDOUT","ERR_NETWORK","ERR_FR_TOO_MANY_REDIRECTS","ERR_DEPRECATED","ERR_BAD_RESPONSE","ERR_BAD_REQUEST","ERR_CANCELED","ERR_NOT_SUPPORT","ERR_INVALID_URL"].forEach(e=>{ke[e]={value:e}});Object.defineProperties(y,ke);Object.defineProperty(Be,"isAxiosError",{value:!0});y.from=(e,t,n,r,s,o)=>{const i=Object.create(Be);return a.toFlatObject(e,i,function(d){return d!==Error.prototype},c=>c!=="isAxiosError"),y.call(i,e.message,t,n,r,s),i.cause=e,i.name=e.name,o&&Object.assign(i,o),i};const Lt=null;function re(e){return a.isPlainObject(e)||a.isArray(e)}function De(e){return a.endsWith(e,"[]")?e.slice(0,-2):e}function ye(e,t,n){return e?e.concat(t).map(function(s,o){return s=De(s),!n&&o?"["+s+"]":s}).join(n?".":""):t}function jt(e){return a.isArray(e)&&!e.some(re)}const It=a.toFlatObject(a,{},null,function(t){return/^is[A-Z]/.test(t)});function G(e,t,n){if(!a.isObject(e))throw new TypeError("target must be an object");t=t||new FormData,n=a.toFlatObject(n,{metaTokens:!0,dots:!1,indexes:!1},!1,function(m,E){return!a.isUndefined(E[m])});const r=n.metaTokens,s=n.visitor||l,o=n.dots,i=n.indexes,d=(n.Blob||typeof Blob<"u"&&Blob)&&a.isSpecCompliantForm(t);if(!a.isFunction(s))throw new TypeError("visitor must be a function");function h(u){if(u===null)return"";if(a.isDate(u))return u.toISOString();if(!d&&a.isBlob(u))throw new y("Blob is not supported. Use a Buffer instead.");return a.isArrayBuffer(u)||a.isTypedArray(u)?d&&typeof Blob=="function"?new Blob([u]):Buffer.from(u):u}function l(u,m,E){let T=u;if(u&&!E&&typeof u=="object"){if(a.endsWith(m,"{}"))m=r?m:m.slice(0,-2),u=JSON.stringify(u);else if(a.isArray(u)&&jt(u)||(a.isFileList(u)||a.endsWith(m,"[]"))&&(T=a.toArray(u)))return m=De(m),T.forEach(function(H,Je){!(a.isUndefined(H)||H===null)&&t.append(i===!0?ye([m],Je,o):i===null?m:m+"[]",h(H))}),!1}return re(u)?!0:(t.append(ye(E,m,o),h(u)),!1)}const f=[],b=Object.assign(It,{defaultVisitor:l,convertValue:h,isVisitable:re});function g(u,m){if(!a.isUndefined(u)){if(f.indexOf(u)!==-1)throw Error("Circular reference detected in "+m.join("."));f.push(u),a.forEach(u,function(T,_){(!(a.isUndefined(T)||T===null)&&s.call(t,T,a.isString(_)?_.trim():_,m,b))===!0&&g(T,m?m.concat(_):[_])}),f.pop()}}if(!a.isObject(e))throw new TypeError("data must be an object");return g(e),t}function be(e){const t={"!":"%21","'":"%27","(":"%28",")":"%29","~":"%7E","%20":"+","%00":"\0"};return encodeURIComponent(e).replace(/[!'()~]|%20|%00/g,function(r){return t[r]})}function le(e,t){this._pairs=[],e&&G(e,this,t)}const Ue=le.prototype;Ue.append=function(t,n){this._pairs.push([t,n])};Ue.toString=function(t){const n=t?function(r){return t.call(this,r,be)}:be;return this._pairs.map(function(s){return n(s[0])+"="+n(s[1])},"").join("&")};function Ht(e){return encodeURIComponent(e).replace(/%3A/gi,":").replace(/%24/g,"$").replace(/%2C/gi,",").replace(/%20/g,"+").replace(/%5B/gi,"[").replace(/%5D/gi,"]")}function Le(e,t,n){if(!t)return e;const r=n&&n.encode||Ht,s=n&&n.serialize;let o;if(s?o=s(t,n):o=a.isURLSearchParams(t)?t.toString():new le(t,n).toString(r),o){const i=e.indexOf("#");i!==-1&&(e=e.slice(0,i)),e+=(e.indexOf("?")===-1?"?":"&")+o}return e}class Mt{constructor(){this.handlers=[]}use(t,n,r){return this.handlers.push({fulfilled:t,rejected:n,synchronous:r?r.synchronous:!1,runWhen:r?r.runWhen:null}),this.handlers.length-1}eject(t){this.handlers[t]&&(this.handlers[t]=null)}clear(){this.handlers&&(this.handlers=[])}forEach(t){a.forEach(this.handlers,function(r){r!==null&&t(r)})}}const we=Mt,je={silentJSONParsing:!0,forcedJSONParsing:!0,clarifyTimeoutError:!1},qt=typeof URLSearchParams<"u"?URLSearchParams:le,zt=typeof FormData<"u"?FormData:null,$t=typeof Blob<"u"?Blob:null,Jt=(()=>{let e;return typeof navigator<"u"&&((e=navigator.product)==="ReactNative"||e==="NativeScript"||e==="NS")?!1:typeof window<"u"&&typeof document<"u"})(),Vt=(()=>typeof WorkerGlobalScope<"u"&&self instanceof WorkerGlobalScope&&typeof self.importScripts=="function")(),R={isBrowser:!0,classes:{URLSearchParams:qt,FormData:zt,Blob:$t},isStandardBrowserEnv:Jt,isStandardBrowserWebWorkerEnv:Vt,protocols:["http","https","file","blob","url","data"]};function Wt(e,t){return G(e,new R.classes.URLSearchParams,Object.assign({visitor:function(n,r,s,o){return R.isNode&&a.isBuffer(n)?(this.append(r,n.toString("base64")),!1):o.defaultVisitor.apply(this,arguments)}},t))}function Kt(e){return a.matchAll(/\w+|\[(\w*)]/g,e).map(t=>t[0]==="[]"?"":t[1]||t[0])}function Gt(e){const t={},n=Object.keys(e);let r;const s=n.length;let o;for(r=0;r<s;r++)o=n[r],t[o]=e[o];return t}function Ie(e){function t(n,r,s,o){let i=n[o++];const c=Number.isFinite(+i),d=o>=n.length;return i=!i&&a.isArray(s)?s.length:i,d?(a.hasOwnProp(s,i)?s[i]=[s[i],r]:s[i]=r,!c):((!s[i]||!a.isObject(s[i]))&&(s[i]=[]),t(n,r,s[i],o)&&a.isArray(s[i])&&(s[i]=Gt(s[i])),!c)}if(a.isFormData(e)&&a.isFunction(e.entries)){const n={};return a.forEachEntry(e,(r,s)=>{t(Kt(r),s,n,0)}),n}return null}function Xt(e,t,n){if(a.isString(e))try{return(t||JSON.parse)(e),a.trim(e)}catch(r){if(r.name!=="SyntaxError")throw r}return(n||JSON.stringify)(e)}const ce={transitional:je,adapter:["xhr","http"],transformRequest:[function(t,n){const r=n.getContentType()||"",s=r.indexOf("application/json")>-1,o=a.isObject(t);if(o&&a.isHTMLForm(t)&&(t=new FormData(t)),a.isFormData(t))return s&&s?JSON.stringify(Ie(t)):t;if(a.isArrayBuffer(t)||a.isBuffer(t)||a.isStream(t)||a.isFile(t)||a.isBlob(t))return t;if(a.isArrayBufferView(t))return t.buffer;if(a.isURLSearchParams(t))return n.setContentType("application/x-www-form-urlencoded;charset=utf-8",!1),t.toString();let c;if(o){if(r.indexOf("application/x-www-form-urlencoded")>-1)return Wt(t,this.formSerializer).toString();if((c=a.isFileList(t))||r.indexOf("multipart/form-data")>-1){const d=this.env&&this.env.FormData;return G(c?{"files[]":t}:t,d&&new d,this.formSerializer)}}return o||s?(n.setContentType("application/json",!1),Xt(t)):t}],transformResponse:[function(t){const n=this.transitional||ce.transitional,r=n&&n.forcedJSONParsing,s=this.responseType==="json";if(t&&a.isString(t)&&(r&&!this.responseType||s)){const i=!(n&&n.silentJSONParsing)&&s;try{return JSON.parse(t)}catch(c){if(i)throw c.name==="SyntaxError"?y.from(c,y.ERR_BAD_RESPONSE,this,null,this.response):c}}return t}],timeout:0,xsrfCookieName:"XSRF-TOKEN",xsrfHeaderName:"X-XSRF-TOKEN",maxContentLength:-1,maxBodyLength:-1,env:{FormData:R.classes.FormData,Blob:R.classes.Blob},validateStatus:function(t){return t>=200&&t<300},headers:{common:{Accept:"application/json, text/plain, */*","Content-Type":void 0}}};a.forEach(["delete","get","head","post","put","patch"],e=>{ce.headers[e]={}});const ue=ce,Zt=a.toObjectSet(["age","authorization","content-length","content-type","etag","expires","from","host","if-modified-since","if-unmodified-since","last-modified","location","max-forwards","proxy-authorization","referer","retry-after","user-agent"]),Yt=e=>{const t={};let n,r,s;return e&&e.split(`
`).forEach(function(i){s=i.indexOf(":"),n=i.substring(0,s).trim().toLowerCase(),r=i.substring(s+1).trim(),!(!n||t[n]&&Zt[n])&&(n==="set-cookie"?t[n]?t[n].push(r):t[n]=[r]:t[n]=t[n]?t[n]+", "+r:r)}),t},ge=Symbol("internals");function U(e){return e&&String(e).trim().toLowerCase()}function q(e){return e===!1||e==null?e:a.isArray(e)?e.map(q):String(e)}function Qt(e){const t=Object.create(null),n=/([^\s,;=]+)\s*(?:=\s*([^,;]+))?/g;let r;for(;r=n.exec(e);)t[r[1]]=r[2];return t}const en=e=>/^[-_a-zA-Z0-9^`|~,!#$%&'*+.]+$/.test(e.trim());function Q(e,t,n,r,s){if(a.isFunction(r))return r.call(this,t,n);if(s&&(t=n),!!a.isString(t)){if(a.isString(r))return t.indexOf(r)!==-1;if(a.isRegExp(r))return r.test(t)}}function tn(e){return e.trim().toLowerCase().replace(/([a-z\d])(\w*)/g,(t,n,r)=>n.toUpperCase()+r)}function nn(e,t){const n=a.toCamelCase(" "+t);["get","set","has"].forEach(r=>{Object.defineProperty(e,r+n,{value:function(s,o,i){return this[r].call(this,t,s,o,i)},configurable:!0})})}class X{constructor(t){t&&this.set(t)}set(t,n,r){const s=this;function o(c,d,h){const l=U(d);if(!l)throw new Error("header name must be a non-empty string");const f=a.findKey(s,l);(!f||s[f]===void 0||h===!0||h===void 0&&s[f]!==!1)&&(s[f||d]=q(c))}const i=(c,d)=>a.forEach(c,(h,l)=>o(h,l,d));return a.isPlainObject(t)||t instanceof this.constructor?i(t,n):a.isString(t)&&(t=t.trim())&&!en(t)?i(Yt(t),n):t!=null&&o(n,t,r),this}get(t,n){if(t=U(t),t){const r=a.findKey(this,t);if(r){const s=this[r];if(!n)return s;if(n===!0)return Qt(s);if(a.isFunction(n))return n.call(this,s,r);if(a.isRegExp(n))return n.exec(s);throw new TypeError("parser must be boolean|regexp|function")}}}has(t,n){if(t=U(t),t){const r=a.findKey(this,t);return!!(r&&this[r]!==void 0&&(!n||Q(this,this[r],r,n)))}return!1}delete(t,n){const r=this;let s=!1;function o(i){if(i=U(i),i){const c=a.findKey(r,i);c&&(!n||Q(r,r[c],c,n))&&(delete r[c],s=!0)}}return a.isArray(t)?t.forEach(o):o(t),s}clear(t){const n=Object.keys(this);let r=n.length,s=!1;for(;r--;){const o=n[r];(!t||Q(this,this[o],o,t,!0))&&(delete this[o],s=!0)}return s}normalize(t){const n=this,r={};return a.forEach(this,(s,o)=>{const i=a.findKey(r,o);if(i){n[i]=q(s),delete n[o];return}const c=t?tn(o):String(o).trim();c!==o&&delete n[o],n[c]=q(s),r[c]=!0}),this}concat(...t){return this.constructor.concat(this,...t)}toJSON(t){const n=Object.create(null);return a.forEach(this,(r,s)=>{r!=null&&r!==!1&&(n[s]=t&&a.isArray(r)?r.join(", "):r)}),n}[Symbol.iterator](){return Object.entries(this.toJSON())[Symbol.iterator]()}toString(){return Object.entries(this.toJSON()).map(([t,n])=>t+": "+n).join(`
`)}get[Symbol.toStringTag](){return"AxiosHeaders"}static from(t){return t instanceof this?t:new this(t)}static concat(t,...n){const r=new this(t);return n.forEach(s=>r.set(s)),r}static accessor(t){const r=(this[ge]=this[ge]={accessors:{}}).accessors,s=this.prototype;function o(i){const c=U(i);r[c]||(nn(s,i),r[c]=!0)}return a.isArray(t)?t.forEach(o):o(t),this}}X.accessor(["Content-Type","Content-Length","Accept","Accept-Encoding","User-Agent","Authorization"]);a.reduceDescriptors(X.prototype,({value:e},t)=>{let n=t[0].toUpperCase()+t.slice(1);return{get:()=>e,set(r){this[n]=r}}});a.freezeMethods(X);const x=X;function ee(e,t){const n=this||ue,r=t||n,s=x.from(r.headers);let o=r.data;return a.forEach(e,function(c){o=c.call(n,o,s.normalize(),t?t.status:void 0)}),s.normalize(),o}function He(e){return!!(e&&e.__CANCEL__)}function I(e,t,n){y.call(this,e??"canceled",y.ERR_CANCELED,t,n),this.name="CanceledError"}a.inherits(I,y,{__CANCEL__:!0});function rn(e,t,n){const r=n.config.validateStatus;!n.status||!r||r(n.status)?e(n):t(new y("Request failed with status code "+n.status,[y.ERR_BAD_REQUEST,y.ERR_BAD_RESPONSE][Math.floor(n.status/100)-4],n.config,n.request,n))}const sn=R.isStandardBrowserEnv?function(){return{write:function(n,r,s,o,i,c){const d=[];d.push(n+"="+encodeURIComponent(r)),a.isNumber(s)&&d.push("expires="+new Date(s).toGMTString()),a.isString(o)&&d.push("path="+o),a.isString(i)&&d.push("domain="+i),c===!0&&d.push("secure"),document.cookie=d.join("; ")},read:function(n){const r=document.cookie.match(new RegExp("(^|;\\s*)("+n+")=([^;]*)"));return r?decodeURIComponent(r[3]):null},remove:function(n){this.write(n,"",Date.now()-864e5)}}}():function(){return{write:function(){},read:function(){return null},remove:function(){}}}();function on(e){return/^([a-z][a-z\d+\-.]*:)?\/\//i.test(e)}function an(e,t){return t?e.replace(/\/+$/,"")+"/"+t.replace(/^\/+/,""):e}function Me(e,t){return e&&!on(t)?an(e,t):t}const ln=R.isStandardBrowserEnv?function(){const t=/(msie|trident)/i.test(navigator.userAgent),n=document.createElement("a");let r;function s(o){let i=o;return t&&(n.setAttribute("href",i),i=n.href),n.setAttribute("href",i),{href:n.href,protocol:n.protocol?n.protocol.replace(/:$/,""):"",host:n.host,search:n.search?n.search.replace(/^\?/,""):"",hash:n.hash?n.hash.replace(/^#/,""):"",hostname:n.hostname,port:n.port,pathname:n.pathname.charAt(0)==="/"?n.pathname:"/"+n.pathname}}return r=s(window.location.href),function(i){const c=a.isString(i)?s(i):i;return c.protocol===r.protocol&&c.host===r.host}}():function(){return function(){return!0}}();function cn(e){const t=/^([-+\w]{1,25})(:?\/\/|:)/.exec(e);return t&&t[1]||""}function un(e,t){e=e||10;const n=new Array(e),r=new Array(e);let s=0,o=0,i;return t=t!==void 0?t:1e3,function(d){const h=Date.now(),l=r[o];i||(i=h),n[s]=d,r[s]=h;let f=o,b=0;for(;f!==s;)b+=n[f++],f=f%e;if(s=(s+1)%e,s===o&&(o=(o+1)%e),h-i<t)return;const g=l&&h-l;return g?Math.round(b*1e3/g):void 0}}function Ee(e,t){let n=0;const r=un(50,250);return s=>{const o=s.loaded,i=s.lengthComputable?s.total:void 0,c=o-n,d=r(c),h=o<=i;n=o;const l={loaded:o,total:i,progress:i?o/i:void 0,bytes:c,rate:d||void 0,estimated:d&&i&&h?(i-o)/d:void 0,event:s};l[t?"download":"upload"]=!0,e(l)}}const dn=typeof XMLHttpRequest<"u",fn=dn&&function(e){return new Promise(function(n,r){let s=e.data;const o=x.from(e.headers).normalize(),i=e.responseType;let c;function d(){e.cancelToken&&e.cancelToken.unsubscribe(c),e.signal&&e.signal.removeEventListener("abort",c)}let h;a.isFormData(s)&&(R.isStandardBrowserEnv||R.isStandardBrowserWebWorkerEnv?o.setContentType(!1):o.getContentType(/^\s*multipart\/form-data/)?a.isString(h=o.getContentType())&&o.setContentType(h.replace(/^\s*(multipart\/form-data);+/,"$1")):o.setContentType("multipart/form-data"));let l=new XMLHttpRequest;if(e.auth){const u=e.auth.username||"",m=e.auth.password?unescape(encodeURIComponent(e.auth.password)):"";o.set("Authorization","Basic "+btoa(u+":"+m))}const f=Me(e.baseURL,e.url);l.open(e.method.toUpperCase(),Le(f,e.params,e.paramsSerializer),!0),l.timeout=e.timeout;function b(){if(!l)return;const u=x.from("getAllResponseHeaders"in l&&l.getAllResponseHeaders()),E={data:!i||i==="text"||i==="json"?l.responseText:l.response,status:l.status,statusText:l.statusText,headers:u,config:e,request:l};rn(function(_){n(_),d()},function(_){r(_),d()},E),l=null}if("onloadend"in l?l.onloadend=b:l.onreadystatechange=function(){!l||l.readyState!==4||l.status===0&&!(l.responseURL&&l.responseURL.indexOf("file:")===0)||setTimeout(b)},l.onabort=function(){l&&(r(new y("Request aborted",y.ECONNABORTED,e,l)),l=null)},l.onerror=function(){r(new y("Network Error",y.ERR_NETWORK,e,l)),l=null},l.ontimeout=function(){let m=e.timeout?"timeout of "+e.timeout+"ms exceeded":"timeout exceeded";const E=e.transitional||je;e.timeoutErrorMessage&&(m=e.timeoutErrorMessage),r(new y(m,E.clarifyTimeoutError?y.ETIMEDOUT:y.ECONNABORTED,e,l)),l=null},R.isStandardBrowserEnv){const u=(e.withCredentials||ln(f))&&e.xsrfCookieName&&sn.read(e.xsrfCookieName);u&&o.set(e.xsrfHeaderName,u)}s===void 0&&o.setContentType(null),"setRequestHeader"in l&&a.forEach(o.toJSON(),function(m,E){l.setRequestHeader(E,m)}),a.isUndefined(e.withCredentials)||(l.withCredentials=!!e.withCredentials),i&&i!=="json"&&(l.responseType=e.responseType),typeof e.onDownloadProgress=="function"&&l.addEventListener("progress",Ee(e.onDownloadProgress,!0)),typeof e.onUploadProgress=="function"&&l.upload&&l.upload.addEventListener("progress",Ee(e.onUploadProgress)),(e.cancelToken||e.signal)&&(c=u=>{l&&(r(!u||u.type?new I(null,e,l):u),l.abort(),l=null)},e.cancelToken&&e.cancelToken.subscribe(c),e.signal&&(e.signal.aborted?c():e.signal.addEventListener("abort",c)));const g=cn(f);if(g&&R.protocols.indexOf(g)===-1){r(new y("Unsupported protocol "+g+":",y.ERR_BAD_REQUEST,e));return}l.send(s||null)})},se={http:Lt,xhr:fn};a.forEach(se,(e,t)=>{if(e){try{Object.defineProperty(e,"name",{value:t})}catch{}Object.defineProperty(e,"adapterName",{value:t})}});const Se=e=>`- ${e}`,hn=e=>a.isFunction(e)||e===null||e===!1,qe={getAdapter:e=>{e=a.isArray(e)?e:[e];const{length:t}=e;let n,r;const s={};for(let o=0;o<t;o++){n=e[o];let i;if(r=n,!hn(n)&&(r=se[(i=String(n)).toLowerCase()],r===void 0))throw new y(`Unknown adapter '${i}'`);if(r)break;s[i||"#"+o]=r}if(!r){const o=Object.entries(s).map(([c,d])=>`adapter ${c} `+(d===!1?"is not supported by the environment":"is not available in the build"));let i=t?o.length>1?`since :
`+o.map(Se).join(`
`):" "+Se(o[0]):"as no adapter specified";throw new y("There is no suitable adapter to dispatch the request "+i,"ERR_NOT_SUPPORT")}return r},adapters:se};function te(e){if(e.cancelToken&&e.cancelToken.throwIfRequested(),e.signal&&e.signal.aborted)throw new I(null,e)}function _e(e){return te(e),e.headers=x.from(e.headers),e.data=ee.call(e,e.transformRequest),["post","put","patch"].indexOf(e.method)!==-1&&e.headers.setContentType("application/x-www-form-urlencoded",!1),qe.getAdapter(e.adapter||ue.adapter)(e).then(function(r){return te(e),r.data=ee.call(e,e.transformResponse,r),r.headers=x.from(r.headers),r},function(r){return He(r)||(te(e),r&&r.response&&(r.response.data=ee.call(e,e.transformResponse,r.response),r.response.headers=x.from(r.response.headers))),Promise.reject(r)})}const Re=e=>e instanceof x?e.toJSON():e;function F(e,t){t=t||{};const n={};function r(h,l,f){return a.isPlainObject(h)&&a.isPlainObject(l)?a.merge.call({caseless:f},h,l):a.isPlainObject(l)?a.merge({},l):a.isArray(l)?l.slice():l}function s(h,l,f){if(a.isUndefined(l)){if(!a.isUndefined(h))return r(void 0,h,f)}else return r(h,l,f)}function o(h,l){if(!a.isUndefined(l))return r(void 0,l)}function i(h,l){if(a.isUndefined(l)){if(!a.isUndefined(h))return r(void 0,h)}else return r(void 0,l)}function c(h,l,f){if(f in t)return r(h,l);if(f in e)return r(void 0,h)}const d={url:o,method:o,data:o,baseURL:i,transformRequest:i,transformResponse:i,paramsSerializer:i,timeout:i,timeoutMessage:i,withCredentials:i,adapter:i,responseType:i,xsrfCookieName:i,xsrfHeaderName:i,onUploadProgress:i,onDownloadProgress:i,decompress:i,maxContentLength:i,maxBodyLength:i,beforeRedirect:i,transport:i,httpAgent:i,httpsAgent:i,cancelToken:i,socketPath:i,responseEncoding:i,validateStatus:c,headers:(h,l)=>s(Re(h),Re(l),!0)};return a.forEach(Object.keys(Object.assign({},e,t)),function(l){const f=d[l]||s,b=f(e[l],t[l],l);a.isUndefined(b)&&f!==c||(n[l]=b)}),n}const ze="1.5.1",de={};["object","boolean","number","function","string","symbol"].forEach((e,t)=>{de[e]=function(r){return typeof r===e||"a"+(t<1?"n ":" ")+e}});const Oe={};de.transitional=function(t,n,r){function s(o,i){return"[Axios v"+ze+"] Transitional option '"+o+"'"+i+(r?". "+r:"")}return(o,i,c)=>{if(t===!1)throw new y(s(i," has been removed"+(n?" in "+n:"")),y.ERR_DEPRECATED);return n&&!Oe[i]&&(Oe[i]=!0,console.warn(s(i," has been deprecated since v"+n+" and will be removed in the near future"))),t?t(o,i,c):!0}};function pn(e,t,n){if(typeof e!="object")throw new y("options must be an object",y.ERR_BAD_OPTION_VALUE);const r=Object.keys(e);let s=r.length;for(;s-- >0;){const o=r[s],i=t[o];if(i){const c=e[o],d=c===void 0||i(c,o,e);if(d!==!0)throw new y("option "+o+" must be "+d,y.ERR_BAD_OPTION_VALUE);continue}if(n!==!0)throw new y("Unknown option "+o,y.ERR_BAD_OPTION)}}const oe={assertOptions:pn,validators:de},P=oe.validators;class J{constructor(t){this.defaults=t,this.interceptors={request:new we,response:new we}}request(t,n){typeof t=="string"?(n=n||{},n.url=t):n=t||{},n=F(this.defaults,n);const{transitional:r,paramsSerializer:s,headers:o}=n;r!==void 0&&oe.assertOptions(r,{silentJSONParsing:P.transitional(P.boolean),forcedJSONParsing:P.transitional(P.boolean),clarifyTimeoutError:P.transitional(P.boolean)},!1),s!=null&&(a.isFunction(s)?n.paramsSerializer={serialize:s}:oe.assertOptions(s,{encode:P.function,serialize:P.function},!0)),n.method=(n.method||this.defaults.method||"get").toLowerCase();let i=o&&a.merge(o.common,o[n.method]);o&&a.forEach(["delete","get","head","post","put","patch","common"],u=>{delete o[u]}),n.headers=x.concat(i,o);const c=[];let d=!0;this.interceptors.request.forEach(function(m){typeof m.runWhen=="function"&&m.runWhen(n)===!1||(d=d&&m.synchronous,c.unshift(m.fulfilled,m.rejected))});const h=[];this.interceptors.response.forEach(function(m){h.push(m.fulfilled,m.rejected)});let l,f=0,b;if(!d){const u=[_e.bind(this),void 0];for(u.unshift.apply(u,c),u.push.apply(u,h),b=u.length,l=Promise.resolve(n);f<b;)l=l.then(u[f++],u[f++]);return l}b=c.length;let g=n;for(f=0;f<b;){const u=c[f++],m=c[f++];try{g=u(g)}catch(E){m.call(this,E);break}}try{l=_e.call(this,g)}catch(u){return Promise.reject(u)}for(f=0,b=h.length;f<b;)l=l.then(h[f++],h[f++]);return l}getUri(t){t=F(this.defaults,t);const n=Me(t.baseURL,t.url);return Le(n,t.params,t.paramsSerializer)}}a.forEach(["delete","get","head","options"],function(t){J.prototype[t]=function(n,r){return this.request(F(r||{},{method:t,url:n,data:(r||{}).data}))}});a.forEach(["post","put","patch"],function(t){function n(r){return function(o,i,c){return this.request(F(c||{},{method:t,headers:r?{"Content-Type":"multipart/form-data"}:{},url:o,data:i}))}}J.prototype[t]=n(),J.prototype[t+"Form"]=n(!0)});const z=J;class fe{constructor(t){if(typeof t!="function")throw new TypeError("executor must be a function.");let n;this.promise=new Promise(function(o){n=o});const r=this;this.promise.then(s=>{if(!r._listeners)return;let o=r._listeners.length;for(;o-- >0;)r._listeners[o](s);r._listeners=null}),this.promise.then=s=>{let o;const i=new Promise(c=>{r.subscribe(c),o=c}).then(s);return i.cancel=function(){r.unsubscribe(o)},i},t(function(o,i,c){r.reason||(r.reason=new I(o,i,c),n(r.reason))})}throwIfRequested(){if(this.reason)throw this.reason}subscribe(t){if(this.reason){t(this.reason);return}this._listeners?this._listeners.push(t):this._listeners=[t]}unsubscribe(t){if(!this._listeners)return;const n=this._listeners.indexOf(t);n!==-1&&this._listeners.splice(n,1)}static source(){let t;return{token:new fe(function(s){t=s}),cancel:t}}}const mn=fe;function yn(e){return function(n){return e.apply(null,n)}}function bn(e){return a.isObject(e)&&e.isAxiosError===!0}const ie={Continue:100,SwitchingProtocols:101,Processing:102,EarlyHints:103,Ok:200,Created:201,Accepted:202,NonAuthoritativeInformation:203,NoContent:204,ResetContent:205,PartialContent:206,MultiStatus:207,AlreadyReported:208,ImUsed:226,MultipleChoices:300,MovedPermanently:301,Found:302,SeeOther:303,NotModified:304,UseProxy:305,Unused:306,TemporaryRedirect:307,PermanentRedirect:308,BadRequest:400,Unauthorized:401,PaymentRequired:402,Forbidden:403,NotFound:404,MethodNotAllowed:405,NotAcceptable:406,ProxyAuthenticationRequired:407,RequestTimeout:408,Conflict:409,Gone:410,LengthRequired:411,PreconditionFailed:412,PayloadTooLarge:413,UriTooLong:414,UnsupportedMediaType:415,RangeNotSatisfiable:416,ExpectationFailed:417,ImATeapot:418,MisdirectedRequest:421,UnprocessableEntity:422,Locked:423,FailedDependency:424,TooEarly:425,UpgradeRequired:426,PreconditionRequired:428,TooManyRequests:429,RequestHeaderFieldsTooLarge:431,UnavailableForLegalReasons:451,InternalServerError:500,NotImplemented:501,BadGateway:502,ServiceUnavailable:503,GatewayTimeout:504,HttpVersionNotSupported:505,VariantAlsoNegotiates:506,InsufficientStorage:507,LoopDetected:508,NotExtended:510,NetworkAuthenticationRequired:511};Object.entries(ie).forEach(([e,t])=>{ie[t]=e});const wn=ie;function $e(e){const t=new z(e),n=Ae(z.prototype.request,t);return a.extend(n,z.prototype,t,{allOwnKeys:!0}),a.extend(n,t,null,{allOwnKeys:!0}),n.create=function(s){return $e(F(e,s))},n}const w=$e(ue);w.Axios=z;w.CanceledError=I;w.CancelToken=mn;w.isCancel=He;w.VERSION=ze;w.toFormData=G;w.AxiosError=y;w.Cancel=w.CanceledError;w.all=function(t){return Promise.all(t)};w.spread=yn;w.isAxiosError=bn;w.mergeConfig=F;w.AxiosHeaders=x;w.formToJSON=e=>Ie(a.isHTMLForm(e)?new FormData(e):e);w.getAdapter=qe.getAdapter;w.HttpStatusCode=wn;w.default=w;const gn=w;const En=We({name:"NavBar",setup(){const{loginWithRedirect:e,user:t,isAuthenticated:n,logout:r}=Qe(),s=Z(""),o=Z(!1),i=Z({}),c=()=>{h(),o.value=!o.value};et(t,async l=>{if(l){console.log("new value here",l);try{(await(await fetch(`https://api.bchwy.com/users/handle/${l.nickname}`,{method:"GET",headers:{"x-api-key":"PlanItIsTheBestProjectEverXYZ"}})).json()).message==="User not found."&&(console.log("handle not found"),$("#handleModal").modal("show"))}catch(f){console.error("Failed to check handle:",f)}try{const b=await(await fetch('${"https://api.bchwy.com"}/users',{method:"POST",headers:{"Content-Type":"application/json","x-api-key":"PlanItIsTheBestProjectEverXYZ"},body:JSON.stringify({auth0_user_id:l.sub,email:l.email,handle:l.nickname,pictureurl:l.picture})})).json();console.log("User upserted:",b)}catch(f){console.error("Failed to upsert user:",f)}}});const d=async()=>{t.nickname=s.value,$("#handleModal").modal("hide")},h=async()=>{const l=`https://api.bchwy.com/users/iz/${encodeURIComponent(t.value.email)}`,f={"x-api-key":"PlanItIsTheBestProjectEverXYZ"};try{const b=await gn.get(l,{headers:f});console.log(b.data),i.value=b.data,console.log(i.value.level)}catch(b){console.error("Error fetching user",b)}};return{login:async()=>{try{await e({appState:{targetUrl:window.location.pathname}})}catch(l){console.error("Failed to login:",l)}},logout:()=>{r({logoutParams:{returnTo:window.location.origin}})},user:t,isAuthenticated:n,userHandle:s,saveHandle:d,showGamification:o,toggleGamification:c,fetchUser:h,userMe:i}}}),A=e=>(tt("data-v-2869635e"),e=e(),nt(),e),Sn={class:"navbar navbar-expand-lg navbar-light bg-green"},_n={class:"container"},Rn={class:"navbar-brand text-supergreen",href:"#"},On=A(()=>p("button",{class:"navbar-toggler",type:"button","data-bs-toggle":"collapse","data-bs-target":"#navbarNav","aria-controls":"navbarNav","aria-expanded":"false","aria-label":"Toggle navigation"},[p("span",{class:"navbar-toggler-icon"})],-1)),An={class:"collapse navbar-collapse",id:"navbarNav"},Tn={class:"navbar-nav me-auto"},xn={class:"nav-item"},Nn={class:"nav-item"},Cn={class:"nav-item"},Pn={class:"nav-item"},vn={class:"navbar-nav"},Fn={key:0,class:"nav-item"},Bn={key:1,class:"nav-item dropdown"},kn={class:"nav-link dropdown-toggle text-evenlighter d-flex align-items-center",href:"#",id:"navbarDropdown",role:"button","data-bs-toggle":"dropdown","aria-expanded":"false"},Dn=["src"],Un={class:"text-evenlighter"},Ln={class:"dropdown-menu bg-green2 text-evenlighter","aria-labelledby":"navbarDropdown"},jn={xmlns:"http://www.w3.org/2000/svg",width:"24",height:"24",viewBox:"0 0 24 24",style:{fill:"rgba(255, 255, 255, 1)",transform:""}},In=A(()=>p("path",{d:"M12 2C6.579 2 2 6.579 2 12s4.579 10 10 10 10-4.579 10-10S17.421 2 12 2zm0 5c1.727 0 3 1.272 3 3s-1.273 3-3 3c-1.726 0-3-1.272-3-3s1.274-3 3-3zm-5.106 9.772c.897-1.32 2.393-2.2 4.106-2.2h2c1.714 0 3.209.88 4.106 2.2C15.828 18.14 14.015 19 12 19s-3.828-.86-5.106-2.228z"},null,-1)),Hn=[In],Mn={xmlns:"http://www.w3.org/2000/svg",width:"24",height:"24",viewBox:"0 0 24 24",style:{fill:"rgb(255, 255, 255)",transform:""}},qn=A(()=>p("path",{d:"m2.344 15.271 2 3.46a1 1 0 0 0 1.366.365l1.396-.806c.58.457 1.221.832 1.895 1.112V21a1 1 0 0 0 1 1h4a1 1 0 0 0 1-1v-1.598a8.094 8.094 0 0 0 1.895-1.112l1.396.806c.477.275 1.091.11 1.366-.365l2-3.46a1.004 1.004 0 0 0-.365-1.366l-1.372-.793a7.683 7.683 0 0 0-.002-2.224l1.372-.793c.476-.275.641-.89.365-1.366l-2-3.46a1 1 0 0 0-1.366-.365l-1.396.806A8.034 8.034 0 0 0 15 4.598V3a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v1.598A8.094 8.094 0 0 0 7.105 5.71L5.71 4.904a.999.999 0 0 0-1.366.365l-2 3.46a1.004 1.004 0 0 0 .365 1.366l1.372.793a7.683 7.683 0 0 0 0 2.224l-1.372.793c-.476.275-.641.89-.365 1.366zM12 8c2.206 0 4 1.794 4 4s-1.794 4-4 4-4-1.794-4-4 1.794-4 4-4z"},null,-1)),zn=[qn],$n=A(()=>p("li",null,null,-1)),Jn=A(()=>p("hr",{class:"dropdown-divider"},null,-1)),Vn=A(()=>p("li",null,[p("hr",{class:"dropdown-divider"})],-1)),Wn=A(()=>p("div",{class:"overlay bg-white",style:{height:"20px"}},null,-1)),Kn={class:"modal",tabindex:"-1",role:"dialog",id:"handleModal"},Gn={class:"modal-dialog",role:"document"},Xn={class:"modal-content"},Zn=A(()=>p("div",{class:"modal-header"},[p("h5",{class:"modal-title"},"Enter User Handle"),p("button",{type:"button",class:"close","data-dismiss":"modal","aria-label":"Close"},[p("span",{"aria-hidden":"true"},"×")])],-1)),Yn={class:"modal-body"},Qn=A(()=>p("p",null,"Please enter a handle for your account:",-1)),er={class:"modal-footer"},tr=A(()=>p("button",{type:"button",class:"btn btn-secondary","data-dismiss":"modal"},"Close",-1));function nr(e,t,n,r,s,o){const i=he("font-awesome-icon"),c=he("router-link");return k(),D(Ye,null,[p("nav",Sn,[p("div",_n,[p("a",Rn,[N(i,{icon:"fa-solid fa-car",bounce:"",style:{color:"#a7c957"}}),C(" Plan-It ")]),On,p("div",An,[p("ul",Tn,[p("li",xn,[N(c,{class:"nav-link text-evenlighter",to:"/"},{default:v(()=>[C("Home")]),_:1})]),p("li",Nn,[N(c,{class:"nav-link text-evenlighter",to:"/route"},{default:v(()=>[C("Routing")]),_:1})]),p("li",Cn,[N(c,{class:"nav-link text-evenlighter",to:"/community"},{default:v(()=>[C(" Community ")]),_:1})]),p("li",Pn,[N(c,{class:"nav-link text-evenlighter",to:"/leaderboard"},{default:v(()=>[C(" Leaderboards ")]),_:1})])]),p("ul",vn,[e.isAuthenticated?(k(),D("li",Bn,[p("a",kn,[p("img",{src:e.user.picture,alt:"",class:"rounded-circle me-2",style:{width:"30px",height:"30px"}},null,8,Dn),p("span",Un,"Welcome, "+Ge(e.user.name)+"!",1)]),p("ul",Ln,[p("li",null,[N(c,{class:"dropdown-item text-light",to:"/profile"},{default:v(()=>[(k(),D("svg",jn,Hn)),C(" Profile")]),_:1})]),p("li",null,[N(c,{class:"dropdown-item text-light",to:"/admin"},{default:v(()=>[(k(),D("svg",Mn,zn)),C(" Admin")]),_:1})]),$n,Jn,p("li",null,[p("button",{class:"dropdown-item text-light",onClick:t[1]||(t[1]=(...d)=>e.toggleGamification&&e.toggleGamification(...d))}," Toggle Gamification ")]),Vn,p("li",null,[p("a",{class:"dropdown-item text-light",onClick:t[2]||(t[2]=(...d)=>e.logout&&e.logout(...d))},[C("Logout "),N(i,{icon:"fa-solid fa-arrow-right-from-bracket"})])])])])):(k(),D("li",Fn,[p("a",{class:"nav-link text-evenlighter",onClick:t[0]||(t[0]=Ke((...d)=>e.login&&e.login(...d),["prevent"]))},"Login")]))])])]),Wn]),p("div",Kn,[p("div",Gn,[p("div",Xn,[Zn,p("div",Yn,[Qn,Xe(p("input",{type:"text",class:"form-control","onUpdate:modelValue":t[3]||(t[3]=d=>e.userHandle=d),placeholder:"Enter handle"},null,512),[[Ze,e.userHandle]])]),p("div",er,[p("button",{type:"button",class:"btn btn-primary",onClick:t[4]||(t[4]=(...d)=>e.saveHandle&&e.saveHandle(...d))},"Save changes"),tr])])])])],64)}const sr=Ve(En,[["render",nr],["__scopeId","data-v-2869635e"]]);export{sr as N,gn as a};