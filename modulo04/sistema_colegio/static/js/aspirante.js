// HACIENDO INSERT AL UPDATE /app/api/estudiante

const form_create = document.querySelector('#form_create');
form_create.onsubmit = () => {
const data = new FormData(form_create);
const map = new Map(data.entries());
let obj = {
    'nombre': map.get('nombre'),
    'apellido': map.get('apellido'),
    'genero': map.get('genero'),
};
create_estudiante(obj);
return false;
};

async function create_estudiante(data){
    let url = '/app/api/estudiante/';
    const response = await fetch(url, {
        method: "POST",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then((res) => {list_estudiante();form_create.reset();});
};

// HACIENDO SELECT AL API /app/api/estudiante

async function list_estudiante(){
    let url = '/app/api/estudiante/';
    const response = await fetch(url, {method: "GET"})
    .then(res => res.json())
    .then((res) => {
        let table = document.getElementById('tabla_estudiante').getElementsByTagName('tbody')[0];
        table.innerHTML = "";
        for (let i = 0; i < res.length; i++){
            table.insertRow().innerHTML = "<tr><td>"+res[i].nombre+"</td><td>"+res[i].apellido+"</td><td>"+res[i].genero+"</td><td><button class='btn btn-xs btn-warning' onclick='openmodal_estudiante("+JSON.stringify(res[i])+")'><i class='fa fa-edit'></i></button> <button class='btn btn-xs btn-danger' onclick='delete_estudiante("+res[i].id+")'><i class='fa fa-trash'></i></button></td></tr>";
        }
    });
};
list_estudiante();


// HACIENDO SELECT AL UPDATE /app/api/estudiante
function openmodal_estudiante(data){
    document.getElementById("e_id").value = data['id']
    document.getElementById("e_nombre").value = data['nombre']
    document.getElementById("e_apellido").value = data['apellido']
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
    'genero': map.get('e_genero'),
};
let id = map.get('e_id');
update_estudiante(id, e_obj);
return false;
};

async function update_estudiante(id, data){
    let url = '/app/api/estudiante/'+id+'/';
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
        list_estudiante();
        form_edit.reset();
    });
};

async function delete_estudiante(id){
    if (confirm("¿Desea eliminar el registro?")){
        let url = '/app/api/estudiante/'+id+'/';
        const response = await fetch(url, {
            method: "DELETE"
        })
        .then(res => list_estudiante());
    };
};