const button =document.querySelector("button")
button.addEventListener('click', function(e){  
    try{
        if (e.currentTarget===this){
            const input = document.getElementById("encryptInput")
            console.log(input.value);
         }
    }catch(error){
        console.log(error);
    }
})
const python = require('python');
const pythonFuctionEncrypt = python.import('utilities/encrypt.py');
const result = pythonFuctionEncrypt("hieu")

console.log(result);