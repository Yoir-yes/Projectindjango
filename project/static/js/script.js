
            var element = document.getElementById('name');
            var tekst = element.innerText;
            if(tekst == "very important"){
                document.getElementById('colo').style.backgroundColor = '#A50021'
            }
            else if(tekst == "important"){
                document.getElementById('colo').style.backgroundColor = '#FFD300'
            }
            else if(tekst == "not as important"){
                document.getElementById('colo').style.backgroundColor = '#acff5e'
            }
            else{
                document.getElementById('colo').style.backgroundColor = '#47ff47'
            }