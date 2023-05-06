// HACIENDO INSERT AL APPI /app/admisionapi/postulante/

const form_create = document.querySelector('#form_create');
form_create.onsubmit = () => {
const data = new FormData(form_create);
const map = new Map(data.entries());
let obj = {
    'nombre': map.get('nombre'),
    'apellido': map.get('apellido'),
    'tipo_documento': map.get('tipo_documento'),
    'documento': map.get('documento'),
    'genero': map.get('genero'),
};
create_postulante(obj);
return false;
};

async function create_postulante(data){
    let url = '/app/admisionapi/postulante/';
    const response = await fetch(url, {
        method: "POST",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then((res) => {list_postulante();form_create.reset();});
};

// HACIENDO SELECT AL API /app/admisionapi/postulante/

async function list_postulante(){
    let url = '/app/admisionapi/postulante/';
    const response = await fetch(url, {method: "GET"})
    .then(res => res.json())
    .then((res) => {
        let table = document.getElementById('tabla_postulante').getElementsByTagName('tbody')[0];
        table.innerHTML = "";
        for (let i = 0; i < res.length; i++){
            console.log(res[i])
            table.insertRow().innerHTML = "<tr><td>"+res[i].nombre+"</td><td>"+res[i].apellido+"</td><td>"+res[i].tipo_documento+"</td><td>"+res[i].documento+"</td><td>"+res[i].genero+"</td><td><button class='btn btn-xs btn-warning' onclick='openmodal_postulante("+JSON.stringify(res[i])+")'><i class='fa fa-edit'></i></button> <button class='btn btn-xs btn-danger' onclick='delete_postulante("+res[i].id+")'><i class='fa fa-trash'></i></button></td></tr>";
        }
    });
};
list_postulante();


// HACIENDO SELECT AL UPDATE /app/admisionapi/postulante/
function openmodal_postulante(data){
    //console.log(data)
    document.getElementById("e_id").value = data['id']
    document.getElementById("e_nombre").value = data['nombre']
    document.getElementById("e_apellido").value = data['apellido']
    document.getElementById("e_tdocumento").value = data['tipo_documento']
    document.getElementById("e_documento").value = data['documento']
    document.getElementById("e_genero").value = data['genero']
    $('#modal-edit').modal();
};

const form_edit = document.querySelector('#form_edit');
form_edit.onsubmit = () => {
const data = new FormData(form_edit);
const map = new Map(data.entries());
let e_obj = {
    'nombre': map.get('e_nombre'),
    'apellido': map.get('e_apellido'),
    'tipo_documento': map.get('e_tdocumento'),
    'documento': map.get('e_documento'),
    'genero': map.get('e_genero'),
};
let id = map.get('e_id');
update_postulante(id, e_obj);
return false;
};

async function update_postulante(id, data){
    //console.log(id, data)
    let url = '/app/admisionapi/postulante/'+id+'/';
    const response = await fetch(url, {
        method: "PUT",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
            },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then((res) => {
        $('#modal-edit').modal('hide');
        list_postulante();
        form_edit.reset();
    });
};

async function delete_postulante(id){
    if (confirm("¿Desea eliminar el registro?")){
        let url = '/app/admisionapi/postulante/'+id+'/';
        const response = await fetch(url, {
            method: "DELETE"
        })
        .then(res => list_postulante());
    };
};


