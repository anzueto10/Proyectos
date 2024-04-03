"use strict";

const dom = () =>{
    //Diferenciación de ventana
    
    //Declaración de objetos al DOM
    const enviarButton = document.getElementById("send-message");
    const mensajeTextoInput = document.getElementById("mensaje");
    const mensajesCotenendor = document.getElementById("mensajes-contenedor");
    const user = document.getElementById("nombreUser");
    const imgInput = document.getElementById("inputImg");

    function generateUniqueId() {
        return Date.now() + Math.random().toString(36).substr(2, 9);
    }
    
    const uniqueId = generateUniqueId();
    user.innerHTML = uniqueId;

    //Registrar SW
    const registrarSW = () => {
        if (navigator.serviceWorker) {
            navigator.serviceWorker.register("sw.js");
        };
    };

    //------ENVIAR MENSAJES

    //Envía el mensaje al SW
    
    const enviarMensajeAlSW = msg =>{
        const msgId = {
            origen: uniqueId,
            mensaje: msg,
        };    
        navigator.serviceWorker.ready.then(res => res.active.postMessage(msgId));
        borrarTextArea();
        crearMensajePropio(msgId.mensaje);
    };

    //Extraer Mensaje
    const extreaerMensajeDelTextoInput = () =>{
        if(mensajeTextoInput.value != ""){
            const mensajeTexto = mensajeTextoInput.value;
            return mensajeTexto;
        } else return false;
    };

    //Extraer Imágenes

    const leerImg  = ar =>{
        for (let i = 0; i < ar.length; i++) {
            const reader = new FileReader();
            reader.readAsDataURL(ar[i]);
            reader.addEventListener("load", e =>{
                const creado = document.createElement("IMG");
                creado.id = "imgEnviada";
                creado.setAttribute("src", `${e.currentTarget.result}`);
                const imgEnviar = creado.outerHTML;
                enviarMensajeAlSW(imgEnviar);
            });
        };
    };

    const extraerImágenes = () =>{
        imgInput.addEventListener("change", () =>{
            leerImg(imgInput.files);
        });
    };

    //Limpiar el text area
    const borrarTextArea = () =>{
        mensajeTextoInput.textContent = "";
        mensajeTextoInput.value = "";
    };

    //Enviar mensajes al click
    const buttonEnviarClick = () =>{
        enviarButton.addEventListener("click", e =>{
            if(extreaerMensajeDelTextoInput() !== false){
                enviarMensajeAlSW(extreaerMensajeDelTextoInput());
            };
        });
        addEventListener("keypress", e =>{
            if(e.key == "Enter"){
                e.preventDefault();
                if(extreaerMensajeDelTextoInput() !== false){
                    enviarMensajeAlSW(extreaerMensajeDelTextoInput());
                };
            }
        })
    };

    //-----RECIBIR MENSAJES

    //Recibir mensaje con un evento

    const recibirMensaje = () =>{
        navigator.serviceWorker.addEventListener("message", e =>{
            if(e.data.origen !== user.innerHTML) crearMensajeEntrante(e.data.mensaje);
        });
    };

    //--------CONVERTIR ELEMENTOS DOM

    const crearElementosParaElCard = (tdemsg, typealign, colorBG,msg) =>{
        const divContenedor = document.createElement("DIV");
        divContenedor.id = "divContenedorMensajeCard"
        divContenedor.classList.add("flex-grow-0", "text-light", "fs-6", typealign, "card", tdemsg, colorBG);
        const divCardBody = document.createElement("DIV");
        divCardBody.classList.add("card-body");
        divCardBody.innerHTML = msg;
        divContenedor.appendChild(divCardBody);
        return [divContenedor, divCardBody];
    };

    const añadirCardMensajeAlContenedorMensaje = msgCard =>{
        mensajesCotenendor.appendChild(msgCard)
    };
    

    //Crear el mensaje ENTRANTE
    const crearMensajeEntrante = msg =>{
        const divCardMSG = crearElementosParaElCard("rounded-mensaje-entrante", "align-self-start", "bg-gris-mensaje-entrante", msg)[0];
        añadirCardMensajeAlContenedorMensaje(divCardMSG);
    };


    //Crear el mensaje PROPIO
    const crearMensajePropio = msg =>{
        const divCardMSG = crearElementosParaElCard("rounded-mensaje-propio", "align-self-end", "bg-azul-oscuro",msg)[0];
        añadirCardMensajeAlContenedorMensaje(divCardMSG);
    };

    //----CARGAR FUNCIONES

    addEventListener("DOMContentLoaded", () => {
        registrarSW();
        buttonEnviarClick();
        recibirMensaje();
        extraerImágenes();
    });
};

dom();