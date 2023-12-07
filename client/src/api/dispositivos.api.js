import axios from 'axios';

const baseURL = 'http://localhost:8000/BackOffice/Dispositivosv1/';

export const getAllDispositivosv1 = () => {
  return axios.get(baseURL);
};

export const getDispositivov1 = (idDispositivo) => {
  return axios.get(`${baseURL}${idDispositivo}/`);
};

export const createDispositivov1 = (dispositivo) => {
  return axios.post(baseURL, dispositivo);
};

export const deleteDispositivov1 = (idDispositivo) => {
  return axios.delete(`${baseURL}${idDispositivo}`);
};

export const updateDispositivov1 = (idDispositivo, dispositivo) => {
  return axios.put(`${baseURL}${idDispositivo}/`, dispositivo);
};

// Funciones para obtener información relacionada con los dispositivos (puedes ajustarlas según tu estructura)
export const getTipoDispositivos = () => {
  return axios.get('http://localhost:8000/BackOffice/tipoDispositivos/');
};

export const getSectores = () => {
  return axios.get('http://localhost:8000/BackOffice/sectores/');
};

export const getDetallesDispo = () => {
  return axios.get('http://localhost:8000/BackOffice/detallesDispo/');
};

export const getAllUsers = () => {
    return axios.get('http://localhost:8000/BackOffice/usuarios/')
}

export const getTiposDispositivo = () => {
    return axios.get('http://localhost:8000/BackOffice/tipoDispositivos/')
      .then(response => response.data)
      .catch(error => {
        console.error("Error obteniendo tipos de dispositivo:", error);
        throw error; // Puedes manejar el error según tus necesidades
      });
  };
  
  export const getIdsTiposDispositivo = () => {
    return axios.get('http://localhost:8000/BackOffice/tipoDispositivos/')
      .then(response => response.data.map(tipo => tipo.idTipoDispositivo))
      .catch(error => {
        console.error("Error obteniendo IDs de tipos de dispositivo:", error);
        throw error; // Puedes manejar el error según tus necesidades
      });
  };
