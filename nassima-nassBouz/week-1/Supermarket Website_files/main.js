var cereals = ['cherios', 'crunch' , 'fruit loops','puffs', 'raisin bran'];
var botonEvn = [".button1", ".button2", ".button3",".button4",".button5"];
var bootton = [];
var itemsInCart = 0;
var listOfProducts = [];
for(let i = 0 ; i < botonEvn.length; i++){
  bootton[i] = document.querySelector(botonEvn[i]);
   let temp = cereals[i];
   bootton[i].addEventListener('click', function(i){
   var t = document.createElement('li');
   var m = document.createTextNode(temp);
   t.appendChild(m);
   document.querySelector('.shoppingCartList').appendChild(t);
   itemsInCart +=1;
});
   listOfProducts[i] = temp;
}




// function showMess(k){
//   // for(let i = 0 ; i < botonEvn.length; i++){
//   //   if (i == k){

//     // }else {
//     //   alert("error!!!");
//     // }
//   }

// var bootton = document.querySelector('.button2');
// bootton.addEventListener('click', showMess);





/// second solution
// var cereals = [{name:"cherios", price: 2.99}, {name:"crunch", price:1.99},
// {name:"puffs", price:3.45}];


// var bootton = document.querySelector('.button1');
// bootton.addEventListener('click', showMess);

// function showMess(){
//   var t = document.createElement('li');
//  var m = document.createTextNode("cheriosssitaa");
//   t.appendChild(m);
//   document.querySelector('.shoppingCartList').appendChild(t);
//   }

// var bootton = document.querySelector('.button2');
// bootton.addEventListener('click', showMess);


