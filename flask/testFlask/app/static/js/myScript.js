document.write("<h1>This is a heading!</h1>");
document.write("<p>This is a paragraph.</p>");
/*get the url link*/
urlinfo=window.location.href;
// array test
/*var arr = [1, 2, 3, "fang"];
alert(arr);
var narr = new Array(1, 2, 3);
alert(narr);
alert(`${narr} length is ${narr.length}`);
*/

// template string
/*var name = "xiaoming";
var age = "18";
var message = `"hello " + ${name} + ', ' + 'You are ' + ${age} + ' year old!'`;
alert(message);*/

// for .. in
/*
var arr = []
var obj = {name:"fang", age:665};
var val;
var s = '';
for(val in obj){
    //alert(obj[val]);
    arr.push(obj[val]);
}
alert(arr.join(','));
*/
// map
/*var m = new Map();
m.set("math", 88);
alert(m.get("math"));
*/
// set
/*var s = new Set();
s.add(2);
s.add(1);
alert(s.size);
*/

//iterator
/*var s = new Set(['a', 'b', 'c']);
s.forEach(function (element, sameElement, set){
    alert(element);
});


//如果对某些参数不感兴趣，由于JavaScript的函数调用不要求参数必须一致，
//因此可以忽略它们。例如，只需要获得Array的element：
var a = ['A', 'B', 'C']
a.forEach(function (element){
    alert(element);
});*/

// function
/*function abs(){
    if (arguments.length === 0){
        alert('please input arguments for abs function!');
        return 0;
    }
    for (var x of arguments){
        alert(x);
    }
}
abs();
abs(1, 2, 3);*/

// global object window
/*var gv = "fanghaiqun";
alert(window.gv);*/

// object function
/*var xiaoming = {
    name: "xiaoming", 
    birth: 1990,
    age: function(){
        var y = new Date().getFullYear();
        return y-this.birth;
    }
};
alert(xiaoming.age);// function definition
alert(xiaoming.age());// age
*/
// map/reduce
// 由于map()方法定义在JavaScript的Array中，
// 我们调用Array的map()方法，传入我们自己的函数，
// 就得到了一个新的Array作为结果
/*function pow(x){
    return x*x;
}
var arr = [1, 2, 3, 4, 5];
var narr = arr.map(pow);
alert(narr);*/
//再看reduce的用法。Array的reduce()把一个函数作用
//在这个Array的[x1, x2, x3...]上，这个函数必须接收两个参数，
//reduce()把结果继续和序列的下一个元素做累积计算，其效果就是：
//[x1, x2, x3, x4].reduce(f) = f(f(f(x1, x2), x3), x4)
/*var arr = [1, 2, 3, 4, 5];
function f(x, y){
    return x+y;
}
alert(arr.reduce(f));*/
/*function string2int(s){
// s: string
    s = s.split('');
    var ns = s.map(function(x){return x-'0';});
    var nnumber =  ns.reduce(function(x, y){ return x*10+y;});
    alert(nnumber);
}
string2int("123");*/

//请把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
//输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
/*function normalize(arr) {
    var narr = arr.map(function(s){
        s = s.toLowerCase();
        s = s[0].toUpperCase() + s.substring(1, s.length);
        return s;});
    alert(narr);
    return narr;
}
normalize(['adam', 'LISA', 'barT'])*/

// filter
/*function get_primes(arr){
    var narr = arr.filter(function(x){
        if(x <= 1){
            return false;
        }
        var mid = Math.sqrt(x);
        var i = 2
        while(i <= mid){
            if(x%i === 0){
                return false;
            }
            i = i + 1;
        }
        return true;
    });
    return narr;
}
var arr = [];
var x = 1;
for(var x = 1; x<100; x++)
{
    arr.push(x);
}
alert(get_primes(arr));*/

    
flag = true;
function myFunction()
{
  //window.location.reload();
  if(flag)
  {
    x=document.getElementById("demo");
    x.innerHTML = "hello javaScript!";
    flag=false;
  }
  else{
    x=document.getElementById("demo");
    x.innerHTML = "JavaScript 能改变html元素的内容。";
    flag=true;
    
  }
}
/*ff = function(){
alert("hatcher");
}
ff();
*/
