import{M as I}from"./MapItem-e4c4c7f6.js";import{A as q}from"./AddFriends-a37c6021.js";import{N as B,a as w}from"./Navbar-2917e1de.js";import{C as T,r as E,F as S,B as V}from"./chartjs-adapter-date-fns.esm-2d0c330f.js";import{_ as z,u as N,e as C,r as _,o as n,c as l,b as m,a as e,n as g,h as d,t as u,i as A,F as f,f as x,d as v,w as k,v as R,p as L,j as D,g as U}from"./index-751a66e8.js";import"./auto-25ed8786.js";T.register(...E);const j={created(){this.fetchData()},watch:{activeTab:{immediate:!0,handler(a,o){a==="routes"&&this.$nextTick(()=>{this.fetchData()})}}},data(){const{user:a,isAuthenticated:o}=N(),i=C(0),c=C(0),t=C(0);return{userExp:i,expToNextLevel:c,userLvl:t,activeTab:"profile",isLoading:!1,currentPage:1,itemsPerPage:3,user:a,isAuthenticated:o,routes:[],friends:[],friendRequests:[],receivedRequests:[],sentRequests:[]}},computed:{paginatedRoutes(){const a=(this.currentPage-1)*this.itemsPerPage,o=a+this.itemsPerPage;return this.routes.slice(a,o)},totalPages(){return Math.ceil(this.routes.length/this.itemsPerPage)}},components:{Navbar:B,MapItem:I,AddFriend:q,FriendRequest:S,Badges:V},methods:{async drawChart(){if(!Array.isArray(this.routes)||this.routes.length===0){console.error("No routes available.");return}this.routes.sort((c,t)=>new Date(c.timestamp)-new Date(t.timestamp));const a=this.routes.map(c=>new Date(c.timestamp).toISOString()),o=this.routes.map(c=>parseFloat(c.carbon_emission.toFixed(1)));if(document.getElementById("carbonFootprintChart")){const c=document.getElementById("carbonFootprintChart").getContext("2d");this.myChart&&this.myChart.destroy();const t=this.routes;this.myChart=new T(c,{type:"bar",data:{labels:a,datasets:[{label:"Carbon Emission",data:o,backgroundColor:"rgba(75, 192, 192, 0.2)",borderColor:"rgba(75, 192, 192, 1)",borderWidth:1}]},options:{responsive:!0,maintainAspectRatio:!0,aspectRatio:1,scales:{x:{barPercentage:.5,categoryPercentage:.5,type:"category",time:{unit:"day",displayFormats:{day:"mmm d"}},bounds:"data",ticks:{source:"data",autoSkip:!0,minUnit:"day"}},y:{min:0,suggestedMax:5,ticks:{stepSize:.5}}},tooltips:{callbacks:{title:function(s,P){const p=t[s[0].index];return`Route: ${p.start_point_name} to ${p.end_point_name}`},label:function(s,P){return`Carbon Emission: ${t[s.index].carbon_emission}`},afterLabel:function(s,P){return`Mode of Transport: ${t[s.index].transport_mode}`}}}}});const F=this.routes.map(s=>s.transport_mode),h={};F.forEach(s=>{h[s]?h[s]++:h[s]=1});const y=Object.keys(h),b=Object.values(h);if(document.getElementById("travelCategoryChart")){const s=document.getElementById("travelCategoryChart").getContext("2d");this.myTravelModeChart&&this.myTravelModeChart.destroy(),this.myTravelModeChart=new T(s,{type:"pie",data:{labels:y,datasets:[{data:b,backgroundColor:["rgba(255, 99, 132, 0.2)","rgba(54, 162, 235, 0.2)","rgba(255, 206, 86, 0.2)","rgba(75, 192, 192, 0.2)","rgba(153, 102, 255, 0.2)","rgba(255, 159, 64, 0.2)"],borderColor:["rgba(255, 99, 132, 1)","rgba(54, 162, 235, 1)","rgba(255, 206, 86, 1)","rgba(75, 192, 192, 1)","rgba(153, 102, 255, 1)","rgba(255, 159, 64, 1)"],borderWidth:1}]},options:{responsive:!0,maintainAspectRatio:!0,aspectRatio:2}})}}},fetchData(){this.fetchRoutes().then(()=>{this.drawChart()}),this.fetchUser(),this.fetchFriendRequests()},async fetchUser(){const a=`https://api.bchwy.com/users/iz/${encodeURIComponent(this.user.email)}`,o={"x-api-key":"PlanItIsTheBestProjectEverXYZ"};try{const i=await w.get(a,{headers:o});this.friends=i.data.friends,this.userLvl=i.data.level,this.userExp=i.data.exp}catch(i){console.error("Error fetching user",i)}},async fetchFriendRequests(){const a=`https://api.bchwy.com/users/${encodeURIComponent(this.user.email)}/friend_requests`,o={"x-api-key":"PlanItIsTheBestProjectEverXYZ"};try{const i=await w.get(a,{headers:o});this.receivedRequests=i.data.received,this.sentRequests=i.data.sent}catch(i){console.error("Error fetching friend requests",i)}},async fetchRoutes(){const a=this.user.email,o=`https://api.bchwy.com/routes/email?email=${encodeURIComponent(a)}`,i={"x-api-key":"PlanItIsTheBestProjectEverXYZ"};try{const c=await w.get(o,{headers:i});this.routes=c.data.reverse()}catch(c){console.error("Error fetching routes:",c)}}}},r=a=>(L("data-v-06b02a6b"),a=a(),D(),a),X={class:"container-fluid pt-3 bg-supergreen"},H={class:"row"},Y={class:"col-md-3"},O={class:"nav flex-column nav-pills",id:"myTabs",role:"tablist"},Z={class:"nav-item"},W={xmlns:"http://www.w3.org/2000/svg",width:"24",height:"24",viewBox:"0 0 24 24",style:{fill:"rgba(236, 227, 206, 1)",transform:"scaleX(-1)",msFilter:"progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1)"}},G=r(()=>e("path",{d:"M12 10c1.151 0 2-.848 2-2s-.849-2-2-2c-1.15 0-2 .848-2 2s.85 2 2 2zm0 1c-2.209 0-4 1.612-4 3.6v.386h8V14.6c0-1.988-1.791-3.6-4-3.6z"},null,-1)),J=r(()=>e("path",{d:"M19 2H5c-1.103 0-2 .897-2 2v13c0 1.103.897 2 2 2h4l3 3 3-3h4c1.103 0 2-.897 2-2V4c0-1.103-.897-2-2-2zm-5 15-2 2-2-2H5V4h14l.002 13H14z"},null,-1)),K=[G,J],Q={class:"nav-item"},$={xmlns:"http://www.w3.org/2000/svg",width:"24",height:"24",viewBox:"0 0 24 24",style:{fill:"rgba(236, 227, 206, 1)",transform:""}},ee=r(()=>e("path",{d:"m21.447 6.105-6-3a1 1 0 0 0-.895 0L9 5.882 3.447 3.105A1 1 0 0 0 2 4v13c0 .379.214.725.553.895l6 3a1 1 0 0 0 .895 0L15 18.118l5.553 2.776a.992.992 0 0 0 .972-.043c.295-.183.475-.504.475-.851V7c0-.379-.214-.725-.553-.895zM10 7.618l4-2v10.764l-4 2V7.618zm-6-2 4 2v10.764l-4-2V5.618zm16 12.764-4-2V5.618l4 2v10.764z"},null,-1)),te=[ee],se={class:"nav-item"},oe={xmlns:"http://www.w3.org/2000/svg",width:"24",height:"24",viewBox:"0 0 24 24",style:{fill:"rgba(236, 227, 206, 1)",transform:""}},ae=r(()=>e("path",{d:"M4.035 15.479A3.976 3.976 0 0 0 4 16c0 2.378 2.138 4.284 4.521 3.964C9.214 21.198 10.534 22 12 22s2.786-.802 3.479-2.036C17.857 20.284 20 18.378 20 16c0-.173-.012-.347-.035-.521C21.198 14.786 22 13.465 22 12s-.802-2.786-2.035-3.479C19.988 8.347 20 8.173 20 8c0-2.378-2.143-4.288-4.521-3.964C14.786 2.802 13.466 2 12 2s-2.786.802-3.479 2.036C6.138 3.712 4 5.622 4 8c0 .173.012.347.035.521C2.802 9.214 2 10.535 2 12s.802 2.786 2.035 3.479zm1.442-5.403 1.102-.293-.434-1.053A1.932 1.932 0 0 1 6 8c0-1.103.897-2 2-2 .247 0 .499.05.73.145l1.054.434.293-1.102a1.99 1.99 0 0 1 3.846 0l.293 1.102 1.054-.434C15.501 6.05 15.753 6 16 6c1.103 0 2 .897 2 2 0 .247-.05.5-.145.73l-.434 1.053 1.102.293a1.993 1.993 0 0 1 0 3.848l-1.102.293.434 1.053c.095.23.145.483.145.73 0 1.103-.897 2-2 2-.247 0-.499-.05-.73-.145l-1.054-.434-.293 1.102a1.99 1.99 0 0 1-3.846 0l-.293-1.102-1.054.434A1.935 1.935 0 0 1 8 18c-1.103 0-2-.897-2-2 0-.247.05-.5.145-.73l.434-1.053-1.102-.293a1.993 1.993 0 0 1 0-3.848z"},null,-1)),re=r(()=>e("path",{d:"m15.742 10.71-1.408-1.42-3.331 3.299-1.296-1.296-1.414 1.414 2.704 2.704z"},null,-1)),ie=[ae,re],ne={class:"nav-item"},le={xmlns:"http://www.w3.org/2000/svg",width:"24",height:"24",viewBox:"0 0 24 24",style:{fill:"rgba(236, 227, 206, 1)",transform:""}},ce=r(()=>e("path",{d:"m2.344 15.271 2 3.46a1 1 0 0 0 1.366.365l1.396-.806c.58.457 1.221.832 1.895 1.112V21a1 1 0 0 0 1 1h4a1 1 0 0 0 1-1v-1.598a8.094 8.094 0 0 0 1.895-1.112l1.396.806c.477.275 1.091.11 1.366-.365l2-3.46a1.004 1.004 0 0 0-.365-1.366l-1.372-.793a7.683 7.683 0 0 0-.002-2.224l1.372-.793c.476-.275.641-.89.365-1.366l-2-3.46a1 1 0 0 0-1.366-.365l-1.396.806A8.034 8.034 0 0 0 15 4.598V3a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v1.598A8.094 8.094 0 0 0 7.105 5.71L5.71 4.904a.999.999 0 0 0-1.366.365l-2 3.46a1.004 1.004 0 0 0 .365 1.366l1.372.793a7.683 7.683 0 0 0 0 2.224l-1.372.793c-.476.275-.641.89-.365 1.366zM12 8c2.206 0 4 1.794 4 4s-1.794 4-4 4-4-1.794-4-4 1.794-4 4-4z"},null,-1)),de=[ce],he={class:"col-md-9 my-4"},ue={key:0,class:"tab-pane show active"},me={class:"profile-container bg-light p-3 rounded d-flex flex-column flex-md-row mb-4"},ve={class:"pb-3 pb-md-0"},be=["src"],pe={class:"pl-md-4"},_e={class:"mb-2 glowing-text"},ge={class:"mb-2"},fe=r(()=>e("b",null,"Level:",-1)),ye={class:"progress stylish-progress-bar mb-4"},we={class:"mb-2"},Ce=r(()=>e("b",null,"Handle:",-1)),xe={class:"mb-2"},ke=r(()=>e("b",null,"Email:",-1)),Re={class:"bg-white rounded-3 shadow-sm p-3"},Te=r(()=>e("h3",{class:"mb-0"},"Friends",-1)),Fe={class:"mt-3"},Me={class:"m-0"},Pe={class:"bg-white rounded shadow-sm p-3 mt-4 mb-4"},Ie=r(()=>e("h3",{class:"mb-0"},"Friend Requests",-1)),qe={class:"mt-3"},Be=r(()=>e("h4",{class:"mt-2"},"Received Requests",-1)),Ee=r(()=>e("h4",{class:"mt-2"},"Sent Requests",-1)),Se={key:1,class:"tab-pane"},Ve=U('<div class="bg-light p-3 rounded d-flex flex-column flex-md-row mb-2" data-v-06b02a6b><div class="pr-4 pb-3 pb-md-0" data-v-06b02a6b><h3 class="mb-2" data-v-06b02a6b>Your Routes</h3><div class="chart-container" data-v-06b02a6b><h4 class="mb-2" data-v-06b02a6b>Carbon emissions</h4><canvas id="carbonFootprintChart" data-v-06b02a6b></canvas></div><div class="chart-container mt-4" data-v-06b02a6b><h4 class="mb-2" data-v-06b02a6b>Travel modes</h4><canvas id="travelCategoryChart" data-v-06b02a6b></canvas></div></div></div>',1),ze=[Ve],Ne={key:2,class:"tab-pane"},Ae={class:"card mt-4 mb-4"},Le=r(()=>e("div",{class:"card-header"},[e("h3",{class:"mb-0"},"Game Stats")],-1)),De={key:3,class:"tab-pane"},Ue={class:"card mt-4 mb-4"},je=r(()=>e("div",{class:"card-header"},[e("h3",{class:"mb-0"},"Settings")],-1)),Xe={class:"container m-2"},He=r(()=>e("div",{class:"row"},[e("div",{class:"col-12 mt-5"},[e("h1",null,"Notification Settings")])],-1)),Ye={key:0,class:"alert alert-info",role:"alert"},Oe={class:"control-group col-12 mt-5"},Ze={class:"controls"},We=r(()=>e("br",null,null,-1)),Ge=r(()=>e("br",null,null,-1));function Je(a,o,i,c,t,F){const h=_("Navbar"),y=_("AddFriend"),b=_("FriendRequest"),M=_("Badges");return n(),l(f,null,[m(h),e("div",X,[e("div",H,[e("div",Y,[e("ul",O,[e("li",Z,[e("a",{class:g(["nav-link",{active:t.activeTab==="profile"}]),onClick:o[0]||(o[0]=s=>t.activeTab="profile"),href:"#",role:"tab"},[(n(),l("svg",W,K)),d(" My Profile")],2)]),e("li",Q,[e("a",{class:g(["nav-link",{active:t.activeTab==="routes"}]),onClick:o[1]||(o[1]=s=>t.activeTab="routes"),href:"#",role:"tab"},[(n(),l("svg",$,te)),d(" My Routes")],2)]),e("li",se,[e("a",{class:g(["nav-link",{active:t.activeTab==="progress"}]),onClick:o[2]||(o[2]=s=>t.activeTab="progress"),href:"#",role:"tab"},[(n(),l("svg",oe,ie)),d(" My Badges")],2)]),e("li",ne,[e("a",{class:g(["nav-link",{active:t.activeTab==="settings"}]),onClick:o[3]||(o[3]=s=>t.activeTab="settings"),href:"#",role:"tab"},[(n(),l("svg",le,de)),d(" Settings")],2)])])]),e("div",he,[t.activeTab==="profile"?(n(),l("div",ue,[e("div",me,[e("div",ve,[e("img",{src:t.user.picture,class:"img-fluid px-3",alt:"User profile picture"},null,8,be)]),e("div",pe,[e("h3",_e,u(t.user.name),1),e("p",ge,[fe,d(" "+u(t.userLvl),1)]),e("div",ye,[e("div",{class:"progress-bar bg-supergreen",role:"progressbar",style:A({width:`${t.userExp.toFixed(2)}%`}),"aria-valuenow":"","aria-valuemin":"0","aria-valuemax":"100"},u(t.userExp.toFixed(2))+"%",5)]),e("p",we,[Ce,d(" @"+u(t.user.nickname),1)]),e("p",xe,[ke,d(" "+u(t.user.email),1)])])]),e("div",Re,[Te,e("div",Fe,[(n(!0),l(f,null,x(t.friends,s=>(n(),l("div",{key:s,class:"mb-3 p-2 bg-light rounded"},[e("h5",Me,u(s),1)]))),128))])]),e("div",Pe,[Ie,e("div",qe,[m(y,{user:t.user},null,8,["user"]),Be,(n(!0),l(f,null,x(t.receivedRequests,s=>(n(),l("div",{key:s,class:"mb-2 p-2 bg-light rounded"},[m(b,{friend:s,user:t.user,receivedRequests:t.receivedRequests,type:"received"},null,8,["friend","user","receivedRequests"])]))),128)),Ee,(n(!0),l(f,null,x(t.sentRequests,s=>(n(),l("div",{key:s,class:"mb-2 p-2 bg-light rounded"},[m(b,{friend:s,user:t.user,sentRequests:t.sentRequests,type:"sent"},null,8,["friend","user","sentRequests"])]))),128))])])])):v("",!0),t.activeTab==="routes"?(n(),l("div",Se,ze)):v("",!0),t.activeTab==="progress"?(n(),l("div",Ne,[e("div",Ae,[Le,m(M)])])):v("",!0),t.activeTab==="settings"?(n(),l("div",De,[e("div",Ue,[je,e("div",Xe,[He,this.isSubmitted?(n(),l("div",Ye," Settings saved! ")):v("",!0),e("div",Oe,[e("div",Ze,[e("label",null,[k(e("input",{type:"checkbox","onUpdate:modelValue":o[4]||(o[4]=s=>a.newFriends=s)},null,512),[[R,a.newFriends]]),d("Notify me about new friends who signed up with my friend code ")]),We,e("label",null,[k(e("input",{type:"checkbox","onUpdate:modelValue":o[5]||(o[5]=s=>a.newFeatures=s)},null,512),[[R,a.newFeatures]]),d("Nofity me about new features of PlanIt! ")]),Ge,e("label",null,[k(e("input",{type:"checkbox","onUpdate:modelValue":o[6]||(o[6]=s=>a.lostPlace=s)},null,512),[[R,a.lostPlace]]),d("Notify me if I lose my place in the leaderboard")])]),e("button",{class:"btn btn-light",onClick:o[7]||(o[7]=s=>a.reset())},"Reset"),e("button",{class:"btn btn-success",onClick:o[8]||(o[8]=s=>a.submit())},"Save")])])])])):v("",!0)])])])],64)}const ot=z(j,[["render",Je],["__scopeId","data-v-06b02a6b"]]);export{ot as default};