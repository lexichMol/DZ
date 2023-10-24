let k = 0
function f(id) {
    k ++;
    let b = document.getElementById(id);
    let m_w = b.parentElement.clientWidth;
    let m_h = b.parentElement.clientHeight;
    b.style.top = Math.floor(Math.random() * (m_h - b.clientHeight)) + 'px';
    b.style.left = Math.floor(Math.random() * (m_w - b.clientWidth)) + 'px';
    if (k % 3 == 0){
        b.style.backgroundColor = "red"
    }
    else if (k % 3 == 1){
        b.style.backgroundColor = "green"
    }
    else if (k % 3 == 2){
        b.style.backgroundColor = "blue"
    }
}