import{N as m}from"./Navbar-2917e1de.js";import{_ as h,u as b,r as f,o as u,c,b as p,a as e,d as v,w as o,v as l,h as a,F as w}from"./index-751a66e8.js";const _={created(){this.fetchData()},mounted(){this.fetchData()},watch:{isAuthenticated:{immediate:!0,handler(){this.fetchData()}},user:{immediate:!0,handler(){this.fetchData()}}},data(){const{user:i,isAuthenticated:t}=b();return{isLoading:!1,currentPage:1,itemsPerPage:3,user:i,isAuthenticated:t,routes:[],friends:[],isSubmitted:!1,newFriends:!0,newFeatures:!0,lostPlace:!0}},computed:{},components:{Navbar:m},methods:{submit(){this.isSubmitted=!0},reset(){this.newFriends=!0,this.newFeatures=!0,this.lostPlace=!0}}},N={class:"container"},g=e("div",{class:"row"},[e("div",{class:"col-12 mt-5"},[e("h1",null,"Notification Settings")])],-1),F={key:0,class:"alert alert-info",role:"alert"},k={class:"control-group col-12 mt-5"},y={class:"controls"},x=e("br",null,null,-1),P=e("br",null,null,-1);function S(i,t,V,C,n,r){const d=f("Navbar");return u(),c(w,null,[p(d),e("div",N,[g,this.isSubmitted?(u(),c("div",F," Settings saved! ")):v("",!0),e("div",k,[e("div",y,[e("label",null,[o(e("input",{type:"checkbox","onUpdate:modelValue":t[0]||(t[0]=s=>n.newFriends=s)},null,512),[[l,n.newFriends]]),a("Notify me about new friends who signed up with my friend code ")]),x,e("label",null,[o(e("input",{type:"checkbox","onUpdate:modelValue":t[1]||(t[1]=s=>n.newFeatures=s)},null,512),[[l,n.newFeatures]]),a("Nofity me about new features of PlanIt! ")]),P,e("label",null,[o(e("input",{type:"checkbox","onUpdate:modelValue":t[2]||(t[2]=s=>n.lostPlace=s)},null,512),[[l,n.lostPlace]]),a("Notify me if I lose my place in the leaderboard")])]),e("button",{class:"btn btn-light",onClick:t[3]||(t[3]=s=>r.reset())},"Reset"),e("button",{class:"btn btn-success",onClick:t[4]||(t[4]=s=>r.submit())},"Save")])])],64)}const U=h(_,[["render",S]]);export{U as default};
