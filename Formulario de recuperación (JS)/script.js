const documento = () => {
    const carrera = document.querySelector(".botonCarrera");
    const elegir = document.querySelector(".car");
    const articulo = document.querySelector(".artcarrera")
    const atras = document.querySelector(".back")
    const inputs = document.querySelectorAll(".inputnombre");
    const nombre = document.querySelector(".nombre");
    const apellido = document.querySelector(".apellido")
    const mail = document.querySelector(".mail")
    const form = document.querySelector(".formularioPrincipal");
    const claseAElegir = document.querySelectorAll(".claseElegida");
    const inputt = document.querySelectorAll(".input")
    const labelNombre = document.querySelector(".labelNombre");
    const labelApellido = document.querySelector(".labelApellido");
    const labelMail = document.querySelector(".labelMail")
    const validar = document.querySelector(".validad");
    const icono = document.querySelector(".loading");
    const cargar = document.querySelector(".cargar");
    const enviado = document.querySelector(".cargarr")
    let valuado;
    let validacion = false;
    let eventoActivo = false;

    carrera.addEventListener("click",()=>{
        elegir.classList.replace("car", "eleccion");
    })

    atras.addEventListener("click",() =>{
        elegir.classList.replace("eleccion","car");
    })

    window.addEventListener('popstate',() =>{
        elegir.classList.replace("eleccion","car");
    });
    
    document.addEventListener("keydown", () =>{
        if (event.code === "Escape") {
            elegir.classList.replace("eleccion","car");
        }
      });
      

    atras.addEventListener("mouseover",()=>{
        atras.classList.add("backAnimation")
    })

    atras.addEventListener('animationend', () => {
        atras.classList.remove("backAnimation");
    });


    inputs.forEach((input) =>{
        input.addEventListener("keydown",(e) =>{
            let noletras = /[^a-zA-Z\s]/gi;
            if (e.key.match(noletras) && input.value != "" ){
                e.preventDefault();
            } else if(e.key.match(noletras) && input.value === "" ) {
                input.value = null;
                e.preventDefault();
            }
        });
    });
 
    const subirLabel = (input, label) =>{
        input.addEventListener("focus", (e) =>{
            label.classList.add("subir")
        })
    }


    const bajarLabel =(input,label) =>{
        input.addEventListener("blur", (e) =>{
                if(input.value === ""){
                    label.classList.remove("subir")
                }
        })
    }

    const elegirCarrera  = () =>{
        claseAElegir.forEach(elemento => {
            const img = elemento.querySelector("img");
            img.addEventListener("click", () => {
            valuado = elemento.querySelector("h3").innerHTML;
            carrera.innerHTML = valuado;
            elegir.classList.replace("eleccion","car");
            validacion = true;
            });
        });
    }

    const primerTemporizador = () =>{
        setTimeout(() =>{
            icono.classList.replace("loading", "cargars");
            enviado.classList.replace("cargarr", "aparece");
        }, 4000);

    }

    const segundoTemporizador = () =>{
        setTimeout(() =>{
            form.submit();
        }, 3500);
    }

    const carreraValidacion = () =>{
        form.addEventListener("submit", (event) =>{
            if(validacion === false){
                alert("Por favor, eliga una carrera")
                event.preventDefault();
            } else {
                event.preventDefault();
                cargar.classList.replace("cargar", "cargando");
                primerTemporizador();
                setTimeout(() =>{
                    segundoTemporizador();
                },4000);
            } 
        });
    }


    elegirCarrera();

    subirLabel(nombre, labelNombre);
    subirLabel(apellido, labelApellido);
    subirLabel(mail, labelMail);
    bajarLabel(nombre, labelNombre);
    bajarLabel(apellido, labelApellido);
    bajarLabel(mail, labelMail);
    
    carreraValidacion();
    
}

documento();