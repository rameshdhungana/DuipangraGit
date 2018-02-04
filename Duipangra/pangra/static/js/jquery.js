jQuery(document).ready(function() {
      $("#move_up").click( function() {
        $("#change_me").animate({top:30},200);
      });//end move_up
      $("#move_down").click( function() {
        $("#change_me").animate({top:500},2000);
      });//end move_down
      $("#color").click( function() {
        $("#change_me").css("color", "purple");
      });//end color
      $("#disappear").click( function() {
        $("#change_me").toggle("slow");
      });//end disappear

       $('#bike-img').click(function(){
       $('#bike-img').hide()
       });//end of bike-img
        $('#scoty-img').click(function(){
       $(this).fadeOut(100)
       });//end of bike-img
       $('#bike-img2').slideToggle();
       $('#bike-img3').slideDown();
       $('#bike-img4').slideUp();
//       $('#scoty-img2').fadeOut(10000).fadeIn(500);

       $('#para').append('this is after append() works');
       $('#remove').click(function(){
            $('#para').detach()
            $('#remove').remove()
            $('#para').show() // since remove completely removes the
       })
       setInterval(lightening,1000);

       function lightening(t){
//       $('#scoty-img2').show('slow').hide('slow');
       $('#scoty-img2').fadeIn(1000).fadeOut(1000);


       }

       $('#bike-img5').click(function(){
//       $(this).innerHTML='you got 1000000 as lottery cash'
//        offer=document.getElementById('offer')
//        offer.innerHTML = 'you got 200000 cash'
//        print(offer.innerHTML)
        alert('you will get the discount now')

        $(this).unbind('click') //unbing the events so that it further cant be done

//        $(this).slideUp()

       });
//        $('#bike-img5').unbind('click'); //unbing the events so that it further cant be done,if done here it will disable in first attempt ie first one also dont woirk

       $('.home-img').click(function(){  // this fucntion() inside click is an anonymous function so we cant call it from any where else,duplicating is
                                        // done to reuse such anonymous function
        alert('this is loop in  jquery')

        $(this).unbind('click')
//        $(this).slideToggle('10');

        });
        $('#discount').hide();
        // generating discount display
       function show_discount(){
        $(this).hide()
         $('#discount').append(' 9 %')
         $('#discount').addClass('redcolor')

         $('#discount').show(1000)
        }

//        $('#discount-info').click(show_discount);


        //the following codes are for car_and_truck.html
        $('#small_button').click(function(){

//              $parent = $('.big').parent().parent().detach()
//              $parent = $('.big').parent().detach()
            $big = $('.big').detach()
            $medium = $('.medium').detach()
//             $('.big').replaceWith('<li class="small""> big ones are replaced small ones</li>')
            $('.small').before('<li> this is before small ones</li>')
            $('.small').after('<li> this is before small ones</li>')

            $(this).unbind('click')




        });
         $('#medium_button').click(function(){

            $big = $('.big').detach()
            $small = $('.small').detach()



        });
         $('#big_button').click(function(){

            $small = $('.small').detach()
            $medium = $('.medium').detach()



        });
         $('#all_button').click(function(){

            $small = $('.small').detach()
            $medium = $('.medium').detach()
            $big = $('.big').detach()



        });

        //animation starts here

        $('#animating').click(function(){
//        alert('animation')
                $(this).animate({'height':'300px','width':'1200px','marginLeft':'100px'},'slow')
                h= $(this).css('height')
//                alert(h)
                if  (h == '300px'){
                 $('#animating').click(function(){
                 $(this).animate({'height':'120px','width':'120px','marginLeft':'0px'},'slow')

                 });
                 }

         });
        // game section starts here
        card_object={
         totalscore:0,
         score:0
            };

         $('.cardbox').hide();
         $('#result').hide();

         function endgame(){
            $('#play').toggle()
            $('#cardimage').empty()
            $('#cardimage').toggle()
            $('.addition').toggle()
            $('.addition').empty()


               card_object.totalscore=0;
               card_object.score= 0;
               }

        function appendresults(){
        tscore=card_object.totalscore
        if (card_object.score<=5){
                card_object.totalscore +=card_object.score
                console.log(card_object.totalscore)
                $added_image = $('<img>').appendTo("#cardimage").attr('src','static/image/car_m.jpg')
                $added_text = $('<b>').html(card_object.totalscore)

                $added_image.appendTo(".addition")
                $added_text.appendTo(".addition")


            }
            if (card_object.score<=10 && card_object.score >5){
               card_object.totalscore +=card_object.score
              console.log(card_object.totalscore)
                            $added_image = $('<img>').appendTo("#cardimage").attr('src','static/image/car_b.jpg')
                              $added_text = $('<b>').html(card_object.totalscore)


                $added_image.appendTo(".addition")
                $added_text.appendTo(".addition")




            }
             if (card_object.score<=15 && card_object.score >10){
                      card_object.totalscore +=card_object.score
                      console.log(card_object.totalscore)
                                     $added_image = $('<img>').appendTo("#cardimage").attr('src','static/image/truck_m.jpg')
                             $added_text = $('<b>').html(card_object.totalscore)


                $added_image.appendTo(".addition")
                $added_text.appendTo(".addition")



            }
             if (card_object.score<=20 && card_object.score >15){

                    card_object.totalscore +=card_object.score
                    console.log(card_object.totalscore)
                                   $added_image = $('<img>').appendTo("#cardimage").attr('src','static/image/truck_b.jpg')
                                $added_text = $('<b>').html(card_object.totalscore)



                $added_image.appendTo(".addition")
                $added_text.appendTo(".addition")



            }
            if (card_object.totalscore >100){

            $('#result').append( card_object.totalscore+'...Multiple of 5 .Game won!!');
             $('#result').show()
             $('#reset').toggle().trigger('click')



             }
         }

        function generatescore(){
            var num = Math.random()
            score = Math.floor(num*20)
            card_object.score=score
            console.log(card_object.score)

            appendresults()



            };

         function startgame(){

         $('.cardbox').show()

         $('#cardimage').click(generatescore)
         }







         $('#play').click(startgame);
         $('#reset').click(endgame)

        window.onfocus=function(){
        console.log('you have opened the tab now')}

        window.onblur=function(){
        console.log('you have left the tab now ')}


    });//end doc ready

//fucntion loopjquery(){
