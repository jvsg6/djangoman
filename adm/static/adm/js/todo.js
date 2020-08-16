



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

