import axios from 'axios'


export const getAllUsers = () => {
    return axios.get('http://localhost:8000/BackOffice/usuarios/')
}

export const getUser = (idUsuario) => {
    return axios.get(`http://localhost:8000/BackOffice/usuarios/${idUsuario}/`)
}

export const createUsers = (user) => {
    return axios.post('http://localhost:8000/BackOffice/usuarios/', user)
}

export const deleteUsers = (idUsuario) => {
    return axios.delete(`http://localhost:8000/BackOffice/usuarios/${idUsuario}`)
}

export const updateUsers = (idUsuario, user) => {
    return axios.put(`http://localhost:8000/BackOffice/usuarios/${idUsuario}/`, user)
}

