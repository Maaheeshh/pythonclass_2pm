< !DOCTYPE html >
    <
    html lang = "en" >
    <
    head >
    <
    meta charset = "UTF-8" >
    <
    meta http - equiv = "X-UA-Compatible"
content = "IE=Edge" >
    <
    meta name = "viewport"
content = "width=device-width, initial-scale=1" >
    <
    title > Calculator HTML, CSS and JavaScript < /title> <
style >
    body {
        background: white;
        <!-- mahesh paudel -->
    } * {
        box - sizing: border - box; -
        webkit - box - sizing: border - box; -
        moz - box - sizing: border - box;
    }
    .wrap {
        width: 300 px;
        margin: auto;
        height: 400 px;
        background: #E466F2;
        border: 3 px solid black;
        padding: 10 px;
        border - radius: 20 px;
    }
input[type = text] {
    background - color: lightsteelblue;
    width: 100 % ;
    padding - top: 5 px;
    padding - bottom: 5 px;
    font - size: 22 px;
    font - height: bold;
    margin - top: 20 px;
    border - radius: 5 px;
    border - color: black;
    text - align: right;
    padding - right: 10 px;
}
input[type = button] {
    background - color: #A4F266;
    color: #000;















width:63px;















padding:5px;















font-size:22px;















font-height:bold;















border-radius: 50px;















border-color: # A4F266;
}#
del {
    width: 48 % ;
}
input: hover {
        background - color: #FF0000;
        color: #fff;
        border - color: #FF0000;
    }
    .box {
        background - color: gray;
        color: #000;















}















.box:hover {















  background-color: lightsteelblue;















  color: # 000;
    } <
    /style> < /
head > <
    br / >
    <
    div class = "wrap" >
    <
    form name = "cal" >
    <
    input type = "text"
class = "box"
name = "display"
disabled >
    <
    br > < br >
    <
    input type = "button"
value = "7"
onclick = "cal.display.value+='7'" >
    <
    input type = "button"
value = "8"
onclick = "cal.display.value+='8'" >
    <!-- ma -->
    <
    input type = "button"
value = "9"
onclick = "cal.display.value+='9'" >
    <
    input type = "button"
value = "+"
onclick = "cal.display.value+='+'" >
    <
    br > < br >
    <
    input type = "button"
value = "4"
onclick = "cal.display.value+='4'" >
    <
    input type = "button"
value = "5"
onclick = "cal.display.value+='5'" >
    <
    input type = "button"
value = "6"
onclick = "cal.display.value+='6'" >
    <
    input type = "button"
value = "-"
onclick = "cal.display.value+='-'" >
    <
    br > < br >
    <
    input type = "button"
value = "1"
onclick = "cal.display.value+='1'" >
    <
    input type = "button"
value = "2"
onclick = "cal.display.value+='2'" >
    <
    input type = "button"
value = "3"
onclick = "cal.display.value+='3'" >
    <
    input type = "button"
value = "×"
onclick = "cal.display.value+='*'" >
    <
    br > < br >
    <
    input type = "button"
value = "0"
onclick = "cal.display.value+='0'" >
    <
    input type = "button"
value = " √ "
onclick = "sq()" >
    <
    input type = "button"
value = "%"
onclick = "cal.display.value+='%'" >
    <
    input type = "button"
value = "÷"
onclick = "cal.display.value+='/'" >
    <
    br > < br >
    <
    input type = "button"
value = "="
onclick = "cal.display.value =eval(cal.display.value)"
id = "del" >
    <
    input type = "button"
value = "DEL"
onclick = "cal.display.value=''" >
    <
    input type = "button"
value = "."
onclick = "cal.display.value+='.'" >
    <
    /form> <
script >
    j

function sq() {
    cal.display.value = Math.sqrt(cal.display.value);
} <
/script> <
br / > < br / > < br / > < center >
    <
    b > Developed by < font color = "red" > mahesh paudel < /font></b >
    <
    /center> <
br / >
    <
    center >
    <
    b > E - mail: < font color = "red" > gr568836 @gmail.com < /font></b >
    <
    /center> <
br / >
    <
    body >
    <
    /body> < /
html >