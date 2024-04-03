self.addEventListener("message", e => {
    const msg = e.data.mensaje;
    self.clients.matchAll().then(clients => {
        clients.forEach(client => {
            client.postMessage({
                mensaje: msg,
                origen: e.data.origen
            });
        });
    });
});




