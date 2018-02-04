$(document).ready(function(){

function getStudentInfo(){
//preventDefault();

$.ajax({
url:'/static/image/ajax_file.xml',
cache : false,
dataType : "xml",
})

.done(function(xml){
console.log(xml)



$('#male_students').empty();
$('#all_students').empty();
$('#female_students').empty();

$(xml).find('student').each(function(){
 var content = '<li> Name:'+$(this).find('name').text()+ 'Roll: '+$(this).find('roll').text()+'gender:'+$(this).find('gender').text()+'</li>'
if ($(this).find('gender').text()=='M'){
$('#male_students').append(content);
}
else if ($(this).find('gender').text()=='F'){
$('#female_students').append(content);}


else {}
$('#all_students').append(content)





});
});



};




//function startAjax(){
//setTimeout(function(){
//getStudentInfo();
//startAjax();
//},10000)
//}

//getStudentInfo();
//startAjax();


// this is to check if the request the type of request sent throgh browser

// function to test rquest.send() and request.open() in ajax
function getInfo_ajaxbook_way(){

console.log('i am within ajax onreadystatuschange functtion')
console.log('after call back gunction working '+request.readyState)
console.log(request)



xml = request.responseXML;
//console.log('this is xml'+xml)


$('#male_students').empty();
$('#all_students').empty();
$('#female_students').empty();

$(xml).find('student').each(function(){
 var content = '<li> Name:'+$(this).find('name').text()+ 'Roll: '+$(this).find('roll').text()+'gender:'+$(this).find('gender').text()+'</li>'
if ($(this).find('gender').text()=='M'){
$('#male_students').append(content);
}
else if ($(this).find('gender').text()=='F'){
$('#female_students').append(content);}


else {}
$('#all_students').append(content)





});
}


function createRequest() {
try {
    request = new XMLHttpRequest();
    console.log('XMLHttpRequest')
//    alert('XMLHttpRequest')
} catch (tryMS) {
  try {
      request = new ActiveXObject("Msxml2.XMLHTTP");
          console.log('ActiveXObject("Msxml2.XMLHTTP"')
          alert('ActiveXObject("Msxml2.XMLHTTP"')

    } catch (otherMS) {
   try {
    request = new ActiveXObject("Microsoft.XMLHTTP");
    console.log('ActiveXObject("Microsoft.XMLHTTP")')
    alert('ActiveXObject("Microsoft.XMLHTTP")')

      } catch (failed) {
    request = null;
   }
  }
}
return request;
}
$("#request_check_button").click( function() {
request=createRequest();
//request.readyState = 4
console.log('just after request created  '+ request.readyState)
console.log('inside the click function to print the request type')

//url ="{% url 'ajax'%}"
url='/static/image/ajax_file.xml'
request.open('GET',url,true)
console.log('just after open () is called '+request.readyState)

request.onreadystatechange= getInfo_ajaxbook_way
console.log('after callcack funtion provided '+request.readyState)

request.send(null)
console.log(request)


//alert(request)

});

// following is form validation for each field using ajax
//$('#id_name').bind('propertychange change click keyup input paste' ,function(){
$('#register_submit').prop( "disabled", true ); // this disables the submit button
$('#id_name').bind('blur' ,function(){
//               alert('dont do this')
            username = $('#id_name').val()

            console.log("username is   :" +username +" here")
            $.ajax({
             url: 'http://localhost:8000/check_username/'+username,
//             url: "{% 'pangra:check_username' username%}",
            type:'GET',
            success:function(data){
          console.log("inside sucess")
          console.log(data)
            if (data=='okay'){
            $added_p='<p> heelp </p>'
//            $added_p.appendTo('#id_name')'<i class="fa fa-check" aria-hidden="true"></i>'
            $('#id_name').after('<i class="fa fa-check" style="color:green" aria-hidden="true"></i>')


//            alert('its okay')
            }
            }
            })
            });
var $ul_list = document.getElementById('getelementbytagname').getElementsByTagName('a');
//var $ul_list = $(#getelementbytagname.a);
for (i=0; i < $ul_list.length; i++){
current_li = $ul_list[i]
current_li.onclick = function(){console.log('onclick')}
current_li.onmouseover = function(){alert('onmouseover')}
current_li.onmouseout = function(){console.log('mouse is out')
}
}



//event handler
//$('.male').click(function (){alert('danger')})
//$('.male').addEventListener('click',function(){alert('this is due to event handler')},false)
console.log(document.addEventListener) // for opera firebox chrome to handle events
console.log(document.attachEvent) // for internet explorer to eventhandlers  ,undefined in chrome
//alert(document.addEventListener)
//alert(document.attachEvent)

// following is add event handler
function addEventHandler(obj,event,handler){
if (document.attachEvent){
obj.attachEvent(event,handler)
//alert('attachEvent')

 }
 else if (document.addEventListener){

 obj.addEventListener(event,handler)


// alert('addEvent')

 }
}

function addevent_handler_first(){alert('this is for click ,but first one first first ')
this.className='small'}
function addevent_handler_second(){alert('this is for click ,but second second second ')}

link = document.getElementById("addeventlink")
addEventHandler(link,'click',addevent_handler_first)
addEventHandler(link,'click',addevent_handler_second)

document.getElementById("all_text").addEventListener("click", function(){ //addEventListener did not work with jquery selector
    alert("Hello World");
});

console.log(document.documentElement)
//text_node = document.getElementById('#female_students')
text_node = document.getElementById("addeventlink")
//text_node.innerHTML = 'ghjkl;'
console.log(text_node)
console.log(text_node.nodeName)
//console.log(text.nodeName)
console.log(text_node.nodeValue)

node = $('#register_submit')
console.log(node)
console.log(node.nodeName)
console.log(node.nodeValue)

//create element
para= document.createElement('p')
para.innerHTML = 'this p is created by using the createElement tag'
text_node.appendChild(para)

console.log(text_node.parent)

// create textnode
user=document.createTextNode('ramesh')
text_node.appendChild(user)




var $list = document.getElementById('getelementbytagname');
console.log($list)

console.log('this s list 2'+$list[1])
//text_node.insertBefore(para,$list.firstChild) //adding befire or after selected element
//text_node.insertAfter(para,$list[0]) //adding befire or after selected element


console.log($list.firstChild)
console.log($list.lastChild)
console.log($list.lastChild.nodeName)
console.log($list.lastChild.nodeValue)

console.log($list.parent)
console.log(document.getElementById('getelementbytagname').nextSibling)
//console.log('the number of the length of li list'+list.childNodes.length)


// adding ,crreating nodes
var newItem = document.createElement("LI");       // Create a <li> node
var textnode = document.createTextNode("Water");  // Create a text node
newItem.appendChild(textnode);                    // Append the text to <li>
console.log(newItem)




// ajax to work with the json field

$('#evalbutton').click(function(){
//alert('eval()')
request = createRequest()
$.ajax({
url : 'http://localhost:8000/json/',
cache : false,
dataType : 'json',


success: function(data){
console.log('as it is '+data)


console.log(eval('(data)')+'this is eval data')
evaldata = (eval('(data)'))
console.log(evaldata[0].name,evaldata[0].nam,evaldata[0].na,evaldata[1].name,evaldata[1].nam,evaldata[1].na)
console.log(data[0].name,data[0].nam,data[0].na,data[1].name,data[1].nam,data[1].na)
console.log(data)
//alert(data,evaldata)
//evaldata = eval(data)
console.log(eval('2'+'2'))

for (var property in data){
console.log(property)
console.log(data[property].name)

}
// check if the object is array in javascript

console.log(typeof (data) + 'is type of returned object')
if (typeof data == 'object'){
console.log('oh i did it')
cons = typeof data
arrayobject = new Array()
array_data = [1,1,2,,4,6,'fdgdfgdf','fgdfg',565,]
console.log('Arraay data is this: '+array_data.constructor.toString().match(/array/i))
console.log(cons.constructor.toString().match(/string/i))

console.log(arrayobject.constructor.toString().match(/array/i))
evaltype = console.log(typeof (eval('(data)')+' is typeof eval object'))
//json parser
//console.log(JSON.parse(data)+ ' this values are obtained by using JSON.parse')
//alert(JSON.parse(data)); // capital P
}

}



});



});
console.log('after eval test')
// using txt file to store json and calling ajax to return value
function get_json_file(){

request = createRequest()
request.onreadystatechange = function(data){
    console.log('this is json data extracted from the jsonfile.txt'+ data)
    if (this.readyState==4 && this.status == 200){
//    alert('everthing is okay')
//    parsed_data = JSON.parse(data)
    console.log(typeof data)
    data = this.responseText //use this responseText to data if ajax is not used ann direct method id used
    console.log(data)
    }


};
url='/static/image/json_file.txt'
request.open('GET',url,true)
request.send(null);
}
$('#jsonfilebutton').click(get_json_file)

//post ajax example
function postajaxexample(e){
e.preventDefault();

//request = createRequest()
//request.onreadystatechange = function(data){
//postdata = {'firstname':document.getElementById('firstname').value,'lastname':document.getElementById('lastname').value,'csrfmiddlewaretoken':$('input[name="csrfmiddlewaretoken"]').val()}
//
//console.log(postdata)
//console.log(data.responseText+'this is returned from server')
//console.log(data.status+'this is returned from server')
//console.log(data.readyState+'this is returned from server')
//alert(postdata)
//
//
//}
postdata = {'firstname':document.getElementById('firstname').value,
            'lastname':document.getElementById('lastname').value,
            'csrfmiddlewaretoken':$('input[name="csrfmiddlewaretoken"]').val(),
            'first':$("#ajaxcheckform input[id='firstname']").val(),
            'last':$("#ajaxcheckform input[id='lastname']").val(),
            'last_name':$("#ajaxcheckform input[name='last_name']").val()}
//url = 'http://localhost:8000/postajax/'
//request.open("POST",url,true)
////h=request.setRequestHeader('Content-Type','application/x-www-form-urlencoded');
//request.setRequestHeader('Content-Type','application/x-www-form-urlencoded');
////console.log(h+'this is request')
//console.log(postdata)
//request.send(postdata)
postdata={'key1':[1,2,3,4],'key2':'simple string','csrfmiddlewaretoken':$('input[name="csrfmiddlewaretoken"]').val()}
$.ajax({
url:'http://localhost:8000/postajax/',
type:'POST',
data:postdata,
success:function(data){
console.log('actual data from server'+data)
console.log(data['status']+'status from server data')

alert('post is success ful'+data)
stringifydata = JSON.stringify(data)
console.log('data after stingify '+stringifydata)
console.log(stringifydata['status']+'status from stingify data')

alert(stringifydata)

parsed_data = JSON.parse(data)
console.log(parsed_data)
alert('this is json parsed data'+parsed_data)
console.log(parsed_data['status']+'status from json parsed  data')


}



});

}
$('#formsubmit').click(postajaxexample)
});

