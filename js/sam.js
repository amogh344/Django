// // function f2()
// // {
// //     document.write("hi, you selected button 2")
// // }
// // function f3()
// // {
// //     document.getElementById('i1').innerHTML = '<input placeholder="Comment">'
// // }
// // function f4()
// // {
// //     console.log("Hello, you clicked button 4")
// // }
// // function f5()
// // {
// //     document.getElementsByClassName('btn')[2].innerText='Comment'
// // }

// // var a = 10

// // function abc()
// // {
// //     var a=20;
// //     console.log(a)
// // }
// // abc()

// // function efg()
// // {
// //     let a=20;
// //     a=10;
// //     console.log(a);
// // }
// // efg()

// // function hij()
// // {
    
// //     const a=10;

// //     console.log(a);
// // }
// // hij()

// // function add(a,b)
// // {
// //     let c=a+b;
// //     console.log(c);
// //     return 50;
// // }
// // console.log(add(20,50))

// let a=function(){
//     return "hi";
// };

// console.log


// function f1()
// {
//     console.log("General Function Declaration")
// }

// function f2(a,b)
// {
//     console.log("Functions declaration with parameters")
// }

// function f3()
// {
//     console.log("function declaration with return type without parameters")
//     return "hi";

// }
// function f4(a,b)
// {
//     console.log("function declaration with return type with parameters")
//     return a+b;
// }

// function f5(a,b)
// {
//         return a===b;
// }

// console.log(f5(20,"20"))

// let f6=()=>
// {
//     console.log("Neutron is wow")
// }
// f6()

// let f7=(a,b)=>
// {
//     return a == b
// }
// console.log(f7(true,false))

// let f8=(a,b)=>{
//     return (a<<b);
// }
// console.log(f8(10,1))



// let ar2=new Array();

// let ar3 = new Array(10,20,30,40,50);

// ar1.pop()
// ar1.push(60)
// ar1.shift()
// ar1.unshift(70)
// console.log(ar1)
// console.log(ar1.findIndex(val => val > 20));
let ar1 = [10,20,30,40,50]

ar1.map((val) =>
{
    console.log(val);

})


console.log(ar1.every((val)=> val%3===0))
console.log(ar1.some((val)=> val%3===0))
console.log(ar1.filter((val)=> val%4===0))

