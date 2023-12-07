// En configurations.api.js
import axios from 'axios';

export const getConfigDetails = (idConfigUsuario) => {
  return axios.get(`http://localhost:8000/BackOffice/usuarioConfig/${idConfigUsuario}`);
};