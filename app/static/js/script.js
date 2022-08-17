menulist = document.getElementsByClassName('navbar')
show = false
function menu() {
    if (show) {
        menulist[0].style.left='-100vw'
        show = false
    }else{
        menulist[0].style.left='0'
        show = true
    }
}

inputsearch = document.getElementsByClassName('search')
showinput = false
function search() {
    console.log(showinput)
    if (showinput) {
        inputsearch[1].style.width='0px'
        inputsearch[1].style.padding='0px'
        showinput = false
    }else{
        inputsearch[1].style.width='150px'
        inputsearch[1].style.paddingLeft='15px'
        showinput = true
    }
}


var intervalId = window.setInterval(function(){
    profilepic = document.getElementById('input').value
    if (profilepic != '') {
        document.forms['profilepic'].submit()
        clearInterval(intervalId) 
    }
},1000)