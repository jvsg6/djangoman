$(document).ready(function(){
    $("#WindOroFormBtn").click(function(){
       var serializedData = $("#WindOroForm").serialize();
       console.log(serializedData);
       var endpoint = $("#WindOroForm").attr("data-url");
       $.ajax({
            url: '/edit/29/',
            data: serializedData,
            type: 'post',
        success: function(response) {
            $("#windOroPhaseListTable > tbody").append('<tr>'+
            '<td>' + response.newWindOroPhase.meteoPhaseStart +'</td>'+
            '<td>' + response.newWindOroPhase.windConst +'</td>'+
            '<td>' + response.newWindOroPhase.precipitationsRate +'</td>'+
            '<td>' + response.newWindOroPhase.precipitationType +'</td>'+
            '<td>' + response.newWindOroPhase.stab +'</td>'+
            '<td>' + response.newWindOroPhase.roughness +'</td>'+
            '<td><button type="button" class="btn btn-danger"><i class="fa fa-trash mr-2"></button></td>'+
            '</tr>'
                )
        }
       })
    });
});


function show_hide_password(target){
  var input = document.getElementById('id_password');
  if (input.getAttribute('type') == 'password') {
    target.classList.add('view');
    input.setAttribute('type', 'text');
  } else {
    target.classList.remove('view');
    input.setAttribute('type', 'password');
  }
  return false;
}



let timer; // пока пустая переменная
let x =10; // стартовое значение обратного отсчета
function countdown(){  // функция обратного отсчета
    document.getElementById('rocket').innerHTML = x;
    x--; // уменьшаем число на единицу
    if (x<0){
        clearTimeout(timer); // таймер остановится на нуле
    
    }
    else {
        timer = setTimeout(countdown, 1000);
    }
}

