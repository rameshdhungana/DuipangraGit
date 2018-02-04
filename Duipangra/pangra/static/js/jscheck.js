

setTimeout(wakeUpUser,30)
       arrayexample(['1','2','3','4'])
       function wakeUpUser()
           {
                alert ("Are you going to stare at this boring page")
           }

//       setTimeout(check,30)

       function check()
       {
            var age;
            age =prompt('Enter the number:')
            console.log(age)

            num = Math.random()
            console.log('ramdom number ='+num)

            if (age>14){
            alert('okay,you are adult')
            <!--document.write('this is adult speaking')-->
            console.log('let him have what he wants')
            console.log('let her have what he wants')
            console.log('let them have what he wants')}
            else{
            alert('you are child')}



        }


       function arrayexample(list)
        {   console.log('list length is'+list.length)

            list.push('push_is_used_to_add new list value')
            console.log('list length is'+list.length)





        }
//       this is testing of object its property and behaviour in javascript
        function objectexample(testobject){

        console.log(testobject.name,testobject.surname);
        m=testobject.test();
        console.log(m);


        }
        testobject={};
        testobject.name='ramesh';
          testobject.surname='dhungana';


        testobject=
        { name:'ramesh',
          surname:'dhungana',
           test:function()
                {
                   return this.name +' is genius'}
                    }



        objectexample(testobject);

        para=document.getElementById("para");

        content=para.innerHTML;
        para.innerHTML='this is changed one'

        attvalue=para.getAttribute('class')

        console.log(attvalue)
        if (attvalue=='text'){
            para.setAttribute('class','body-text')
            newatt=para.getAttribute('class')

            console.log(newatt)
            }

        console.log(typeof attvalue);
        console.log(typeof attva);
        console.log(typeof 0/0);
        console.log(typeof 110/0);

        sub='hello sir how are you';
        console.log(sub.indexOf('e'));
        console.log(sub.charAt(4))

//        substr=substring(5,10);
        console.log(sub);

        function displayblogcontent(){
        blog=document.getElementById('id_tagline')
        total=blog.value
        console.log(blog.innerHTML)
        }

        button=document.getElementById('button')
        button.onclick=displayblogcontent

        function keypresshandler(e){
            if (e.KeyCode==13){
            console.log('pressing enter key worked')}

            }
        name=document.getElementById('id_name');
//        name.onkeypress=keypresshandler;
        console.log('pressing enter key not  worked')


        function  imfine(eventobj){
//        alert('i am okay')
            console.log(eventobj.target + '  '+eventobj.type)

        }
        window.onload=imfine
        function imageclick(eventobj){
          img=document.getElementById('bike-img')
//        img.setAttribute('src',"{% static 'image/download.jpg'%}")
          console.log('image is clicked');
          var imag = eventobj.target
          console.log(imag.id + ".jpg")
          console.log(imag.src)

          console.log(imag.type)
          console.log(imag.timestamp)
          console.log(imag.KeyCode)
          console.log(imag.clientX)
          console.log(imag.clientY)
          console.log(imag.touches)
          console.log(imag)



        }
        img=document.getElementById('bike-img')
        img.onclick=imageclick

        function mousemovehandler(eventobj){
            alert(eventobj.clientX + "  "  + eventobj.clientY+'   '+
            eventobj.screenX + "  "  + eventobj.screenY+'  '+
            eventobj.pageX + "  "  + eventobj.pageY)
        }
        img.onmousemove=mousemovehandler

        function setintervalhanlder(){
        console.log('set interval')}
//        setInterval(setintervalhanlder,50)
        clearInterval(5000)

        function mouseoverhandler(eventobj){
            console.log('mouse is over me')
        }
        img.onmousemover=mouseoverhandler

        function mouseouthandler(eventobj){
            console.log('mouse isout of me')
        }
        img.onmouseout=mouseoverhandler

         function windowresize(eventobj){
            alert('window  resizing sure?')
        }
       window.onresize=windowresize

//    constructor in javascript
       function Construct(name,roll){
       this.name=name,
       this.roll=roll}

       test=new Construct('ramesh','1')
       test.status='okay'

       console.log('constructor workded'+test.name,test.roll,test.status)
       console.log(test instanceof Construct)

//       #inheritance in javascript
        Construct.prototype.surname='dhungana';
        cannie=new Construct('kl','jkljsdklj','jkklsjklf')
        cannie.surname='regmi'

        console.log('protype :: '+ cannie.surname)
        console.log('ramesh')

//        #hasOwnProperty
        console.log(cannie.hasOwnProperty('surname'))

        $(document).ready( function(){
    $('#bike-img').click(function(){
//    $('#bike').hide('slow');
    alert('be careful')
    });

    });

    $(document).ready(function(){
  $("#bike-img").click(function(){
  $("#bike-img").hide("slow");

  });
});

$("p").html(" using jquery is easy")

//
//

//       paraclass=document.getElementByTagName('p')
//       paraclass.innerHTML='this is class changed'
//        console.log(para.innerHTML);



