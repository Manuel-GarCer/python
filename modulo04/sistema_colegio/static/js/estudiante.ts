async function list_estudiante() {
    let url = '/app/api/estudiante/';
    await fetch(url, {
        method: "GET"
    })
    .then(res => res.json())
    .then((res) => {
        let table = document.getElementById('tabla_estudiante').getElementsByTagName('tbody')[0];
        table.innerHTML = ""
        for(let i=0; i < res.length; i++){
            // console.log(res[i])
            table.insertRow().innerHTML = "<tr><td>"+res[i].nombre+"</td><td>"+res[i].apellido+"</td><td>"+res[i].genero+"</td><td></td></tr>"
        }
    });
};
list_estudiante();